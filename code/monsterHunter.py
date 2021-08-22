#輸入Discord用的函式庫
import discord
from discord.ext import commands
from sympy import limit, Symbol, sin, oo
import random
import os
import json
import time
#This is use vanilla command.

with open('url.json', 'r', encoding = 'utf8') as jfile:
    data = json.load(jfile)

class monsterHunter(Commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def MH(self, ctx, s: str):
        await ctx.send("牠弱散彈啦")
def setup(bot):
    bot.add_cog(cmds(bot))
