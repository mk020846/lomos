import requirements.py
import discord
from discord.ext import commands
from config import config

intents = discord.Intents.defaults()
intents.members = True

bot = commands.Bot(command_prefix=config.PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f"logged in as {bot.user.name}")

if __name__ = '__main__':
    for extension in config.EXTENSIONS:
        bot.load_extension(extension)
    bot.run(config.TOKEN)
