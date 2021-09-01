import discord
from discord.ext import commands
import inspect


class source(commands.Cog):
    def __init__(self, bot):
        """Legit only has one command and that is to show the source of another command"""
        self.bot = bot

    @commands.command()
    async def source(self, ctx, *, command: str):
        """shows source code of a command
        Parameters
        • command - the name of the command
        """
        a = "`" * 3
        source_thing = inspect.getsource(self.bot.get_command(command).callback)
        await ctx.send(f"{a}py\n{source_thing}{a}")


def setup(bot):
    bot.add_cog(source(bot))
