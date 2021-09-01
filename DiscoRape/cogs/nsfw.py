import discord
import asyncio
from discord.ext import commands
import nekos
import random


class nsfw(commands.Cog):
    """nfsw messages"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def neko(self, ctx, message):
        """Shows hentai"""
        await ctx.delete()
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        msg = message
        embed = discord.Embed(
            title=":flushed:", description="", colour=discord.Colour.from_rgb(r, g, b),
        )
        url = nekos.img(msg)
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    @commands.command()
    async def nekoalt(self, ctx):
        """Shows all options for neko"""
        await ctx.delete()
        possible = [
            "**Feet** | **Yuri** | **Trap** | **Futanri** | **Hololewd** | **Lewdkemo** | **Solo** | **Feet** | **Cum** | **Erokemo** | **Les** | **Wallpaper** | **Lewd** | **Feed** | **Gecg** | **Femdom** | **Eroyuri** | **Eron** | **Blowjob** | **Kemonomimi** | **Gasm** | **Anal** | **Erok** | **Boobs** | **Smallboobs** | **Spank** | **Hentai** | **Holo** | **Keta** | **Pussy** | **Tits** | **Classic** | **Kuni** | **Waifu** | **Pat** | **Poke** | **Neko** | **Cuddle** | **Kiss** | **Baka** | **Smug**",
        ]

        list = ""
        for item in possible:
            list += f"{item}\n"
        r = random.randint(50, 255)
        g = random.randint(50, 255)
        b = random.randint(50, 255)
        embed = discord.Embed(
            title=":flushed: options:", description=f"{list}", colour=discord.Colour.from_rgb(r, g, b),
        )
        await ctx.send(embed=embed)


### Add cog lmao
def setup(bot):
    bot.add_cog(nsfw(bot))
