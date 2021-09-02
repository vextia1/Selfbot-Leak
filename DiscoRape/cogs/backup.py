import discord
import requests
import random
import time
import sys
import os
from discord.ext import commands
import json
from colorama import Fore, init
import datetime


with open("./data/config.json") as f:
    config = json.load(f)

token = config.get("TOKEN")
headers = {"authorization": token}
connect = requests.get(
    "https://canary.discordapp.com/api/v6/users/@me", headers=headers
)


class backup(commands.Cog):
    """Uhhh it backs up your acocunt kinda but offbrand"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def backupfriends(self, ctx):
        """Backups your friendslist"""
        print(
            f"{Fore.GREEN}[-] BACKUP_FRIENDS >{Fore.RESET} Attempting to to remove old backup to prevent multiplication issues"
        )
        try:
            os.remove("Discord Friends.txt")
            print(
                f"{Fore.GREEN}[-] BACKUP_FRIENDS >{Fore.RESET} Successfully removed old backup"
            )
        except Exception as e:
            print(
                f"{Fore.GREEN}[-] BACKUP_FRIENDS >{Fore.RESET} Couldn't remove old backup because there is none"
            )
        start = datetime.datetime.now()
        saved_friends = 0

        friends = requests.get(
            "https://discord.com/api/v6/users/@me/relationships", headers=headers
        )
        for friend in friends.json():
            if friend["type"] == 1:
                name = friend["user"]["username"]
                dsc = friend["user"]["discriminator"]
                username = "Username: %s#%s | User ID: %s\n" % (
                    friend["user"]["username"],
                    friend["user"]["discriminator"],
                    friend["id"],
                )
                print(
                    f"{Fore.GREEN}[-] BACKUP_FRIENDS >{Fore.RESET} Saved friend: {name}#{dsc}"
                )
                with open("Discord Friends.txt", "a", encoding="UTF-8") as f:
                    f.write(username)
                saved_friends += 1

        with open("Discord Friends.txt", "r", encoding="UTF-8") as f:
            fixed = f.read()[:-1]
        with open("Discord Friends.txt", "w", encoding="UTF-8") as f:
            f.write(fixed)
        elapsed = datetime.datetime.now() - start
        elapsed = f"{elapsed.seconds}.{elapsed.microseconds}"

        print(
            f"\n> Successfully saved {saved_friends} friend(s) in {elapsed} second(s)"
        )

    # NOTE: Shameless copy paste for both of these commands got the src from a friend

    @commands.command()
    async def backupservers(self, ctx):
        """Backups all your servers where you can create an invite"""
        print(
            f"{Fore.GREEN}[-] BACKUP_SERVERS >{Fore.RESET} Attempting to to remove old backup to prevent multiplication issues"
        )
        try:
            os.remove("Discord Servers.txt")
            print(
                f"{Fore.GREEN}[-] BACKUP_SERVERS >{Fore.RESET} Successfully removed old backup"
            )
        except Exception as e:
            print(
                f"{Fore.GREEN}[-] BACKUP_SERVERS >{Fore.RESET} Couldn't remove old backup because there is none"
            )

        start = datetime.datetime.now()

        saved_servers = 0
        attempts = 0
        server_info_all = ""

        servers = requests.get(
            "https://discordapp.com/api/v6/users/@me/guilds", headers=headers
        )
        for server in servers.json():
            server_info_all += "%s|||%s\n" % (server["id"], server["name"])

        payload = {"max_age": "0", "max_uses": "0", "temporary": False}
        for server_info in server_info_all.splitlines():
            server_id = server_info.split("|||")[0]
            server_name = server_info.split("|||")[1]

            channels = requests.get(
                "https://discord.com/api/v6/guilds/%s/channels" % (server_id),
                headers=headers,
            )
            for channel in channels.json():
                if channel["type"] == 0:
                    channel_id = channel["id"]
                    invite = requests.post(
                        "https://discord.com/api/v6/channels/%s/invites" % (channel_id),
                        json=payload,
                        headers=headers,
                    )

                    if invite.status_code == 403:
                        attempts += 1
                        print(
                            f"{Fore.RED}[-] BACKUP_SERVERS >{Fore.RESET} Unable to make invite for: {server_name} | Channel ID: {channel_id} | Retrying . . ."
                        )
                        if attempts == 4:
                            print(
                                f"{Fore.RED}[-] BACKUP_SERVERS >{Fore.RESET} Unable to make invite for {server_name} assuming it has a Vanity URL"
                            )
                            with open(
                                "Discord Servers.txt", "a", encoding="UTF-8"
                            ) as f:
                                f.write(
                                    "Discord Server: %s | Vanity URL\n" % (server_name)
                                )
                            saved_servers += 1
                            attempts = 0
                            break
                        else:
                            pass

                    elif invite.status_code == 429:
                        print(
                            f"{Fore.RED}[-] BACKUP_SERVERS >{Fore.RESET} Rate limited. | Taking 10 second break to avoid rate limit"
                        )
                        time.sleep(9)

                    else:
                        invite_url = "https://discord.gg/%s" % (
                            str(invite.json()["code"])
                        )
                        print(
                            f"{Fore.GREEN}[-] BACKUP_SERVERS >{Fore.RESET} Saved server: {server_name} | Invite Link: {invite_url}"
                        )
                        with open("Discord Servers.txt", "a", encoding="UTF-8") as f:
                            f.write(
                                "Discord Server: %s | Channel ID: %s | Invite Link: %s\n"
                                % (server_name, channel_id, invite_url)
                            )
                        saved_servers += 1
                        break
        elapsed = datetime.datetime.now() - start
        elapsed = f"{elapsed.seconds}.{elapsed.microseconds}"
        print(
            f">{Fore.GREEN}[-] BACKUP_SERVERS >{Fore.RESET} Successfully saved {saved_servers} server(s) in {elapsed} second(s)"
        )

    # This was a bitch to do but it should work just fine
    @commands.command()
    async def recoverservers(self, ctx):
        """Joins back all the servers from a previous backup if it exists"""
        joined_servers = 0

        if os.path.exists("Discord Servers.txt"):
            with open("Discord Servers.txt", "r", encoding="UTF-8") as f:
                for line in f.readlines():
                    while True:
                        try:
                            line = line.replace("\n", "")
                            if "Vanity URL" in line:
                                server_name = line.split("Discord Server: ")[1].split(
                                    " | Vanity URL"
                                )[0]
                                print(
                                    f"{Fore.RED}[-] RECOVERY_SERVERS >{Fore.RESET} {server_name} Server has a Vanity URL."
                                )
                                break
                            else:
                                invite_code = line.split("https://discord.gg/")[1]
                                server_name = line.split("Discord Server: ")[1].split(
                                    " | Channel ID"
                                )[0]
                        except IndexError:
                            print(f"{Fore.RED}Invalid syntax at line: {line}")
                            break

                        join = requests.post(
                            "https://discord.com/api/v6/invites/%s" % (invite_code),
                            headers=headers,
                        )
                        if join.status_code == 429:
                            print(
                                f"{Fore.GREEN}[-] RECOVERY_SERVERS >{Fore.RESET} Rate limited | Timeout for 10 seconds"
                            )
                            time.sleep(10)
                        elif join.status_code == 200:
                            print(
                                f"{Fore.GREEN}[-] RECOVERY_SERVERS >{Fore.RESET} Successfully joined {server_name}"
                            )
                            joined_servers += 1
                            break
                        elif join.status_code == 403:
                            print(
                                f"{Fore.RED}[-] RECOVERY_SERVERS >{Fore.RESET} Verify your Discord account."
                            )
                            break
                        else:
                            print(
                                f"{Fore.RED}[-] RECOVERY_SERVERS >{Fore.RESET} Error: {join.text}"
                            )
                            break

            print(
                f"{Fore.GREEN}[-] RECOVERY_SERVERS >{Fore.RESET} Successfully joined {joined_servers} Discord Servers... "
            )

        else:
            print(
                f"{Fore.RED}[-] RECOVERY_SERVERS >{Fore.RESET} You have not saved any servers."
            )

    @commands.command()
    async def recoverfriends(self, ctx):
        """Adds all your friends back from a previous friendslist backup"""
        added_friends = 0

        if os.path.exists("Discord Friends.txt"):
            with open("Discord Friends.txt", "r", encoding="UTF-8") as f:
                for line in f.readlines():
                    while True:
                        try:
                            line = line.replace("\n", "")
                            user_id = line.split("User ID: ")[1]
                            user_name = line.split(" |")[0]
                        except IndexError:
                            print(
                                f"{Fore.RED}[-] RECOVERY_FRIENDS >{Fore.RESET} Invalid syntax at line: {line}"
                            )

                        add = requests.put(
                            "https://discord.com/api/v6/users/@me/relationships/%s"
                            % (user_id),
                            json={},
                            headers=headers,
                        )
                        if add.status_code == 429:
                            print(
                                f"{Fore.RED}[-] RECOVERY_FRIENDS >{Fore.RESET} Rate limited 10 second break to avoid rate limit"
                            )
                            time.sleep(10)
                        elif add.status_code == 204:
                            print(
                                f"{Fore.GREEN}[-] RECOVERY_FRIENDS >{Fore.RESET} Sent friend request to: {user_name}"
                            )
                            added_friends += 1
                            break
                        elif add.status_code == 400:
                            print(
                                f"{Fore.RED}[-] RECOVERY_FRIENDS >{Fore.RESET} User has disabled friend requests: {user_name}"
                            )
                            break
                        elif add.status_code == 403:
                            print(
                                f"{Fore.RED}[-] RECOVERY_FRIENDS >{Fore.RESET} Verify your Discord account"
                            )
                            break
                        else:
                            print(
                                f"{Fore.RED}[-] RECOVERY_FRIENDS >{Fore.RESET} Error: {add.text}"
                            )

    @commands.command()
    async def recoverall(self, ctx):
        """Recovers friends and servers from previous backups"""
        added_friends = 0

        if os.path.exists("Discord Friends.txt"):
            with open("Discord Friends.txt", "r", encoding="UTF-8") as f:
                for line in f.readlines():
                    while True:
                        try:
                            line = line.replace("\n", "")
                            user_id = line.split("User ID: ")[1]
                            user_name = line.split(" |")[0]
                        except IndexError:
                            print(
                                f"{Fore.RED}[-] RECOVERY_FRIENDS >{Fore.RESET} Invalid syntax at line: {line}"
                            )

                        add = requests.put(
                            "https://discord.com/api/v6/users/@me/relationships/%s"
                            % (user_id),
                            json={},
                            headers=headers,
                        )
                        if add.status_code == 429:
                            print(
                                f"{Fore.RED}[-] RECOVERY_FRIENDS >{Fore.RESET} Rate limited 10 second break to avoid rate limit"
                            )
                            time.sleep(10)
                        elif add.status_code == 204:
                            print(
                                f"{Fore.GREEN}[-] RECOVERY_FRIENDS >{Fore.RESET} Sent friend request to: {user_name}"
                            )
                            added_friends += 1
                            break
                        elif add.status_code == 400:
                            print(
                                f"{Fore.RED}[-] RECOVERY_FRIENDS >{Fore.RESET} User has disabled friend requests: {user_name}"
                            )
                            break
                        elif add.status_code == 403:
                            print(
                                f"{Fore.RED}[-] RECOVERY_FRIENDS >{Fore.RESET} Verify your Discord account"
                            )
                            break
                        else:
                            print(
                                f"{Fore.RED}[-] RECOVERY_FRIENDS >{Fore.RESET} Error: {add.text}"
                            )
        else:
            print(
                f"{Fore.RED}[-] RECOVERY_FRIENDS >{Fore.RESET} You have not saved any friends."
            )
        joined_servers = 0

        if os.path.exists("Discord Servers.txt"):
            with open("Discord Servers.txt", "r", encoding="UTF-8") as f:
                for line in f.readlines():
                    while True:
                        try:
                            line = line.replace("\n", "")
                            if "Vanity URL" in line:
                                server_name = line.split("Discord Server: ")[1].split(
                                    " | Vanity URL"
                                )[0]
                                print(
                                    f"{Fore.RED}[-] RECOVERY_SERVERS >{Fore.RESET} {server_name} Server has a Vanity URL."
                                )
                                break
                            else:
                                invite_code = line.split("https://discord.gg/")[1]
                                server_name = line.split("Discord Server: ")[1].split(
                                    " | Channel ID"
                                )[0]
                        except IndexError:
                            print(f"{Fore.RED}Invalid syntax at line: {line}")
                            break

                        join = requests.post(
                            "https://discord.com/api/v6/invites/%s" % (invite_code),
                            headers=headers,
                        )
                        if join.status_code == 429:
                            print(
                                f"{Fore.GREEN}[-] RECOVERY_SERVERS >{Fore.RESET} Rate limited | Timeout for 10 seconds"
                            )
                            time.sleep(10)
                        elif join.status_code == 200:
                            print(
                                f"{Fore.GREEN}[-] RECOVERY_SERVERS >{Fore.RESET} Successfully joined {server_name}"
                            )
                            joined_servers += 1
                            break
                        elif join.status_code == 403:
                            print(
                                f"{Fore.RED}[-] RECOVERY_SERVERS >{Fore.RESET} Verify your Discord account."
                            )
                            break
                        else:
                            print(
                                f"{Fore.RED}[-] RECOVERY_SERVERS >{Fore.RESET} Error: {join.text}"
                            )
                            break

            print(
                f"{Fore.GREEN}[-] RECOVERY_SERVERS >{Fore.RESET} Successfully joined {joined_servers} Discord Servers... "
            )

        else:
            print(
                f"{Fore.RED}[-] RECOVERY_SERVERS >{Fore.RESET} You have not saved any servers."
            )

    @commands.command()
    async def backupall(self, ctx):

        # Backup for friends
        # I could prolly fix this by writing over but for now this is a decent solution
        # Might wanna make a feature where it renames the old one but I'm not sure
        print(
            f"{Fore.GREEN}[-] BACKUP_FRIENDS >{Fore.RESET} Attempting to to remove old backup to prevent multiplication issues"
        )
        try:
            os.remove("Discord Friends.txt")
            print(
                f"{Fore.GREEN}[-] BACKUP_FRIENDS >{Fore.RESET} Successfully removed old backup"
            )
        except Exception as e:
            print(
                f"{Fore.GREEN}[-] BACKUP_FRIENDS >{Fore.RESET} Couldn't remove old backup because there is none"
            )
        saved_friends = 0

        friends = requests.get(
            "https://discord.com/api/v6/users/@me/relationships", headers=headers
        )
        for friend in friends.json():
            if friend["type"] == 1:
                name = friend["user"]["username"]
                dsc = friend["user"]["discriminator"]
                username = "Username: %s#%s | User ID: %s\n" % (
                    friend["user"]["username"],
                    friend["user"]["discriminator"],
                    friend["id"],
                )
                print(
                    f"{Fore.GREEN}[-] BACKUP_FRIENDS >{Fore.RESET} Saved friend: {name}#{dsc}"
                )
                with open("Discord Friends.txt", "a", encoding="UTF-8") as f:
                    f.write(username)
                saved_friends += 1

        with open("Discord Friends.txt", "r", encoding="UTF-8") as f:
            fixed = f.read()[:-1]
        with open("Discord Friends.txt", "w", encoding="UTF-8") as f:
            f.write(fixed)

        print(f"\n> Successfully saved {saved_friends} friend(s)")

        # Backup for servers
        # I could prolly fix this by writing over but for now this is a decent solution
        # Might wanna make a feature where it renames the old one
        print(
            f"{Fore.GREEN}[-] BACKUP_SERVERS >{Fore.RESET} Attempting to to remove old backup to prevent multiplication issues"
        )
        try:
            os.remove("Discord Servers.txt")
            print(
                f"{Fore.GREEN}[-] BACKUP_SERVERS >{Fore.RESET} Successfully removed old backup"
            )
        except Exception as e:
            print(
                f"{Fore.GREEN}[-] BACKUP_SERVERS >{Fore.RESET} Couldn't remove old backup because there is none"
            )
        saved_servers = 0
        attempts = 0
        server_info_all = ""

        servers = requests.get(
            "https://discordapp.com/api/v6/users/@me/guilds", headers=headers
        )
        for server in servers.json():
            server_info_all += "%s|||%s\n" % (server["id"], server["name"])

        payload = {"max_age": "0", "max_uses": "0", "temporary": False}

        for server_info in server_info_all.splitlines():
            server_id = server_info.split("|||")[0]
            server_name = server_info.split("|||")[1]

            channels = requests.get(
                "https://discord.com/api/v6/guilds/%s/channels" % (server_id),
                headers=headers,
            )
            for channel in channels.json():
                if channel["type"] == 0:
                    channel_id = channel["id"]
                    invite = requests.post(
                        "https://discord.com/api/v6/channels/%s/invites" % (channel_id),
                        json=payload,
                        headers=headers,
                    )

                    if invite.status_code == 403:
                        attempts += 1
                        print(
                            f"{Fore.RED}[-] BACKUP_SERVERS >{Fore.RESET} Unable to make invite for: {server_name} | Channel ID: {channel_id} | Retrying . . ."
                        )
                        if attempts == 4:
                            print(
                                f"{Fore.RED}[-] BACKUP_SERVERS >{Fore.RESET} Unable to make invite for {server_name} assuming it has a Vanity URL"
                            )
                            with open(
                                "Discord Servers.txt", "a", encoding="UTF-8"
                            ) as f:
                                f.write(
                                    "Discord Server: %s | Vanity URL\n" % (server_name)
                                )
                            saved_servers += 1
                            attempts = 0
                            break
                        else:
                            pass
                        time.sleep(2)

                    elif invite.status_code == 429:
                        print(
                            f"{Fore.RED}[-] BACKUP_SERVERS >{Fore.RESET} Rate limited. brb lol"
                        )
                        time.sleep(10)

                    else:
                        invite_url = "https://discord.gg/%s" % (
                            str(invite.json()["code"])
                        )
                        print(
                            f"{Fore.GREEN}[-] BACKUP_SERVERS >{Fore.RESET} Saved server: {server_name} | Invite Link: {invite_url}"
                        )
                        with open("Discord Servers.txt", "a", encoding="UTF-8") as f:
                            f.write(
                                "Discord Server: %s | Channel ID: %s | Invite Link: %s\n"
                                % (server_name, channel_id, invite_url)
                            )
                        saved_servers += 1
                        break

        print(
            f"{Fore.GREEN}[-] BACKUP_SERVERS >{Fore.RESET} Successfully saved {saved_servers} server(s))"
        )


### Add cog lmao
def setup(bot):
    bot.add_cog(backup(bot))
