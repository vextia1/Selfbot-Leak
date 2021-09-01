import discord
from discord.ext.commands import DefaultHelpCommand


class helpformatter(DefaultHelpCommand):
    def get_ending_note(self):
        return "The shittest selfbot in existence by Daddie#1337\n\nWebsite > https://gobyebye.github.io"
