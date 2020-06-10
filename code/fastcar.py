#輸入Discord用的函式庫
import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import os
import json

with open('set.json', 'r', encoding = 'utf8') as jfile:
    data = json.load(jfile)

class fastcar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def NTUT(ctx, arg):
        soup = BeautifulSoup(open('NTUT'))
        await ctx.send(arg)

        
def setup(bot):
    bot.add_cog(fastcar(bot))
    bot.add_command(NTUT)
    

