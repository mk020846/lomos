from discord.ext import commands

class test_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pong")

def setup(bot):
    bot.add_cog(test_cog(bot))
