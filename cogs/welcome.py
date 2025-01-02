import discord
from discord.ext import commands
from config.config import WELCOME_CHANNEL_ID

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        welcome_channel = self.bot.get_channel(WELCOME_CHANNEL_ID)
        if welcome_channel:
            welcome_msg = f'Welcome {member.mention} to {member.guild.name}! 🎉'
            await welcome_channel.send(welcome_msg)
        
        try:
            dm_msg = f'''Welcome to {member.guild.name}!
We're glad to have you here. 
Feel free to check out our channels !'''
            await member.send(dm_msg)
        except discord.Forbidden:
            print(f"Couldn't send DM to {member.name}")

async def setup(bot):
    await bot.add_cog(Welcome(bot))
