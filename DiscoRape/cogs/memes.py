import discord
import asyncio
from discord.ext import commands
import random


class memes(commands.Cog):
    """m e m e s but make them black like my slaves"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ghostping(self, ctx):
        """Ghostpings people"""
        await ctx.delete()

    @commands.command()
    async def floyd(self, ctx):
        """I can't breathe"""
        await ctx.message.delete()
        await ctx.send("https://i.imgur.com/mn3EslL.png")


### Add cog again
def setup(bot):
    bot.add_cog(memes(bot))
