#輸入Discord用的函式庫
import discord
from discord.ext import commands
#from core.classes import Cog_Extension
import random
import os
import json

with open('set.json', 'r', encoding = 'utf8') as jfile:
    data = json.load(jfile)
#from core.classes import Cog_Extension   
class showPicGif(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rdrrN(self, ctx):
        pic = discord.File('./pic/rdrr01.png')
        await ctx.send(file = pic)

    @commands.command()
    async def LUL(self, ctx):
        pic = discord.File('./pic/lul.png')
        await ctx.send(file = pic)

    @commands.command()
    async def rdrrNWeb(self, ctx):
        random_pic = random.choice(data['Url_Pic'])
        #pic = ['Url_Pic']
        await ctx.send(random_pic)

    @commands.command()
    async def KoLianNa(self, ctx):
        pic = data['KoLianNa']
        await ctx.send(pic)

def setup(bot):
    bot.add_cog(showPicGif(bot))
