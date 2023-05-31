from discord.ext import commands

class lomos(commands.bot):
    def __init__(self, command_prefix):
        super().__init__(command_prefix)

bot = lomos(command_prefix='&&')
