import discord
from discord.ext import commands
from config.config import DISCORD_TOKEN
from db.database import setup_database

# intents
intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await load_cogs()
    await bot.tree.sync()  

async def load_cogs():
    await bot.load_extension('cogs.welcome')
    await bot.load_extension('cogs.word_counter')
    await bot.load_extension('cogs.roles')

setup_database()

# Run the bot
bot.run(DISCORD_TOKEN)
