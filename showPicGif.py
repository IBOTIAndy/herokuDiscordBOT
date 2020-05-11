import discord
from discord.ext import commands
import functools
import psutil

class showPicGif(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @command.Cog()
    async def rdrrN(ctx):
        pic = discord.File('C:\\pythonwork\\Try_Bot\\pic\\rdrr01.png')
        await ctx.send(file = pic)

    @command()
    async def LUL(ctx):
        pic = discord.File('C:\\pythonwork\\Try_Bot\\pic\\lul.png')
        await ctx.send(file = pic)
   