import asyncpraw
import discord
from discord.ext import commands
from utils import config

class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reddit = asyncpraw.Reddit(client_id=config.REDDIT_CLIENT_ID,
                                       client_secret=config.REDDIT_CLIENT_SECRET,
                                       user_agent=config.REDDIT_USER_AGENT)

    @commands.command()
    async def memes(self, ctx):
        subreddit = await self.reddit.subreddit("memes")
        post = await subreddit.random()
        embed = discord.Embed(title=post.title, color=discord.Color.random())
        embed.set_image(url=post.url)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(MemesCog(bot))

