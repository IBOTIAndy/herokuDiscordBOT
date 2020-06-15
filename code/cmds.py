#輸入Discord用的函式庫
import discord
from discord.ext import commands
import random
import os
import json
import time

with open('set.json', 'r', encoding = 'utf8') as jfile:
    data = json.load(jfile)

class cmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add(self, ctx, a: int, b: int):
        await ctx.send(a + b)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Товарищ! водка!!")

    @commands.command()
    async def pan(self, ctx):
        await ctx.send("你這是資本主義的反動行為 該去古拉格「共產」一下")

    @commands.command()
    async def USSR(self, ctx):
        await ctx.send("這是「我們」的國歌\n")
        await ctx.send(data['USSR'])

    @commands.command()
    async def USSRExtreme(self, ctx):
        await ctx.send("Это наш национальный гимн\n")
        await ctx.send(data['USSRExtreme'])

    @commands.command()
    async def PS5(self, ctx):
        await ctx.send("這是空氣清淨機\n")

def setup(bot):
    bot.add_cog(cmds(bot))
