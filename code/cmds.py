#輸入Discord用的函式庫
import discord
from discord.ext import commands
from sympy import limit, Symbol, sin, oo
import random
import os
import json
import time
#This is use vanilla command.

with open('set.json', 'r', encoding = 'utf8') as jfile:
    data = json.load(jfile)

class cmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
#ctx = discord bot
#await = ?
    @commands.command()
    async def helps(self, ctx):
        await ctx.send("we own these order:\n!add [number1] [number2]\n!sub [number1] [number2]\n!ping\n!pan\n!USSR\n!USSRExtreme\n!PS5")
#        await ctx.send("we own these order:\n")
#        await ctx.send("!add [number1] [number2]")
#        await ctx.send("!sub [number1] [number2]")
#        await ctx.send("!ping")
#        await ctx.send("!pan")
#        await ctx.send("!USSR")
#        await ctx.send("!USSRExtreme")
#        await ctx.send("!PS5")

    @commands.command()
    async def HTC(self, ctx):
        await ctx.send("Never want to FULL COMBO.\nFuck you HTC touch screen.")

    x = Symbol('x')

#    try:
        #inputstr = format(message)

        #@commands.command()
        #async def limit(self, *, arg):
   
    @commands.command()
    async def add(self, ctx, a: int, b: int):
        await ctx.send(a + b)
    
    @commands.command()
    async def sub(self, ctx, a: int, b: int):
        await ctx.send(a - b)

    @commands.command()
    async def mul(self, ctx, a: int, b: int):
        await ctx.send(a * b)
    
    @commands.command()
    async def div(self, ctx, a: int, b: int):
        if b == 0:
            await ctx.send("don't / 0 Plz.")
        else:
            await ctx.send(a / b)
    
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
    
    @commands.command()
    async def MH(self, ctx, s: str):
        await ctx.send("牠弱散彈啦\n")

    @commands.command()
    async def HowYa(self, ctx):
        await ctx.send(data['AmeGood'])

    @commands.command()
    async def Marxist(self, ctx):
        await ctx.send("立即學習馬克思主義，成為社會主義好青年!\n")
        await ctx.send(data['Marxist'])
   

#    except:
#        print("請輸入可用指令。詳細資訊請輸入!help或!helps\n")
#        async def exception(self, ctx):
#            await ctx.send("請輸入可用指令。詳細資訊請輸入!help或!helps")

def setup(bot):
    bot.add_cog(cmds(bot))
