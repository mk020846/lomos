import discord
from discord.ext import commands
from config import config
import asyncio
import os
import tracemalloc
tracemalloc.start()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=config.PREFIX, intents=intents)

async def load_cogs():
    for cog in os.listdir('./bot/cogs'):
        if cog.endswith('.py'):
            try:
                cog_name = os.path.splitext(cog)[0]  # Get the filename without the extension
                await bot.load_extension(f'bot.cogs.{cog_name}')
                print(f"Loaded extension: {cog_name}")
            except Exception as e:
                print(f"Failed to load extension: {cog_name}\n{type(e).__name__}: {e}")


            
@bot.event
async def on_ready():
    print(f"logged in as {bot.user}")
    await load_cogs()

bot.run(config.TOKEN)
