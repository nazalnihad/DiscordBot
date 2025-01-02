import discord
from discord.ext import commands
from discord import app_commands
from db.database import get_db_connection

class RoleSelect(discord.ui.Select):
    def __init__(self, roles):
        options = [
            discord.SelectOption(
                label=role.name,
                value=str(role.id),
                description=f"Select to get {role.name} role"
            ) for role in roles
        ]
        super().__init__(
            placeholder="Choose your role...",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):
        try:
            print("RoleSelect callback triggered.")
            # Get the selected role
            role_id = int(self.values[0])
            print(f"Selected role_id: {role_id}")
            role = interaction.guild.get_role(role_id)
            
            if not role:
                await interaction.response.send_message("Error: Role not found!", ephemeral=True)
                return

            # Store in database
            conn = get_db_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO user_role (discord_id, role_id)
                VALUES (%s, %s)
                ON DUPLICATE KEY UPDATE role_id = %s
            ''', (interaction.user.id, role_id, role_id))
            
            conn.commit()
            cursor.close()
            conn.close()

            # Add role to user
            await interaction.user.add_roles(role)
            print(f"Assigned role to {interaction.user.name}")
            await interaction.response.send_message(
                f"Successfully assigned you the {role.name} role!", 
                ephemeral=True
            )

        except Exception as e:
            print(f"Error in role selection: {str(e)}")
            await interaction.response.send_message(
                "An error occurred while assigning the role. Please try again later.",
                ephemeral=True
            )

class RoleView(discord.ui.View):
    def __init__(self, roles):
        super().__init__(timeout=None)
        self.add_item(RoleSelect(roles))

class Roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="select-role", description="Select your role from the available options")
    async def select_role(self, interaction: discord.Interaction):
        try:
            print("select_role command invoked.")
            # Get assignable roles (excluding admin/mod roles)
            available_roles = [
                role for role in interaction.guild.roles 
                if role.name.lower() in ['developer', 'gamer', 'lurker']
            ]

            print(f"Available roles: {[r.name for r in available_roles]}")

            if not available_roles:
                await interaction.response.send_message(
                    "No roles are currently available for selection.",
                    ephemeral=True
                )
                return

            view = RoleView(available_roles)
            await interaction.response.send_message(
                "Please select a role from the menu below:",
                view=view,
                ephemeral=True
            )

        except Exception as e:
            print(f"Error in select_role command: {str(e)}")
            await interaction.response.send_message(
                "An error occurred while setting up the role selection.",
                ephemeral=True
            )

async def setup(bot):
    await bot.add_cog(Roles(bot))
