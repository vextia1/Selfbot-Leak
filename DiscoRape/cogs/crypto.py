import discord
import asyncio
from discord.ext import commands
import requests
from colorama import Fore, init

# you're defining shit here


class crypto(commands.Cog):
    """Cryptocurrency stuff"""

    def __init__(self, bot):
        self.bot = bot

    #define shit here

    @commands.command()
    async def daily(self, ctx):
        await ctx.message.delete()
        await ctx.send("Getting BTC/ETH info...")
        # BTC info
        r = requests.get(
            "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR,GBP"
        )
        r = r.json()
        usd = r["USD"]
        eur = r["EUR"]
        gbp = r["GBP"]
        em = discord.Embed(
            description=f"USD: `{str(usd)}$`\n\nEUR: `{str(eur)}€`\n\nGBP: `{str(gbp)}£`"
        )
        em.set_author(
            name="Bitcoin",
            icon_url="https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png",
        )
        await ctx.send(embed=em)

        # ETH info
        r = requests.get(
            "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR,GBP"
        )
        r = r.json()
        usd = r["USD"]
        eur = r["EUR"]
        gbp = r["GBP"]
        em = discord.Embed(
            description=f"USD: `{str(usd)}$`\nEUR: `{str(eur)}€`\n\nGBP: `{str(gbp)}£`"
        )
        em.set_author(
            name="Ethereum",
            icon_url="https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png",
        )
        await ctx.send(embed=em)

    @commands.command(aliases=["bitcoin"])
    async def btc(self, ctx):
        """Gets the current Bitcoin Price"""
        await ctx.message.delete()
        r = requests.get(
            "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR,GBP"
        )
        r = r.json()
        usd = r["USD"]
        eur = r["EUR"]
        gbp = r["GBP"]
        em = discord.Embed(
            description=f"USD: `{str(usd)}$`\n\nEUR: `{str(eur)}€`\n\nGBP: `{str(gbp)}£`"
        )
        em.set_author(
            name="Bitcoin",
            icon_url="https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png",
        )
        await ctx.send(embed=em)
        ### I hope this code is so horrible I'm never allowed to code embeds again

    @commands.command(aliases=["ethereum"])
    async def eth(self, ctx):
        """Gets the current Etherium price"""
        await ctx.message.delete()
        r = requests.get(
            "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR,GBP"
        )
        r = r.json()
        usd = r["USD"]
        eur = r["EUR"]
        gbp = r["GBP"]
        em = discord.Embed(
            description=f"USD: `{str(usd)}$`\nEUR: `{str(eur)}€`\n\nGBP: `{str(gbp)}£`"
        )
        em.set_author(
            name="Ethereum",
            icon_url="https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png",
        )
        await ctx.send(embed=em)

    @commands.command(aliases=["usdtobtc", "usd2btc"])
    async def usdbtc(self, ctx, message):
        """Converts USD to BTC

        Parameters
        • USD - Amount of USD you want in BTC (NOTE: NEEDS TO BE WHOLE NUMBER)
        """
        await ctx.message.delete()
        r = requests.get(
            "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD"
        )

        r = r.json()
        usd = r["USD"]
        index = 1 / usd
        amount = int(message)
        converted = amount * index
        em = discord.Embed(description=f"**{amount}$** = **{converted} BTC**")
        em.set_author(
            name="USD to Bitcoin",
            icon_url="https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png",
        )
        await ctx.send(embed=em)

    @commands.command(aliases=["usdtoeth", "usd2eth"])
    async def usdeth(self, ctx, message):
        """Converts USD to ETH

        Parameters
        • USD - Amount of USD you want in ETH (NOTE: NEEDS TO BE WHOLE NUMBER)
        """
        await ctx.message.delete()
        r = requests.get(
            "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD"
        )

        r = r.json()
        usd = r["USD"]
        index = 1 / usd
        amount = int(message)
        converted = amount * index
        em = discord.Embed(description=f"**{amount}$** = **{converted} ETH**")
        em.set_author(
            name="USD to ETH",
            icon_url="https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png",
        )
        await ctx.send(embed=em)


### Add cog lmao
def setup(bot):
    bot.add_cog(crypto(bot))
