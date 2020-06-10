#輸入Discord用的函式庫
import discord
from discord.ext import commands
#from core.classes import Cog_Extension
import random
import os
import json

class cmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add(self, ctx, a: int, b: int):
        await ctx.send(a + b)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("I got a ping!")

    @commands.command()
    async def pan(self, ctx):
        await ctx.send("你好盤")

def setup(bot):
    bot.add_cog(cmds(bot))
