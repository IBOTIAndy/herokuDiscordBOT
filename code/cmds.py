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

class cmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
#ctx = discord bot
#await = ?
    @commands.command()
    async def helps(self, ctx):
        await ctx.send("we own these order:\n!add [number1] [number2]\n!sub [number1] [number2]\n!ping\n!pan\n!USSR\n!USSRExtreme\n!PS5", delete_after=60.0)
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
        await ctx.send("你這是資本主義的反動行為 該去古拉格「共產」一下", delete_after=90.0)

    @commands.command()
    async def USSR(self, ctx):
        await ctx.send("這是「我們」的國歌\n", delete_after=600.0)
        await ctx.send(data['USSR'], delete_after=600.0)

    @commands.command()
    async def USSRExtreme(self, ctx):
        await ctx.send("Это наш национальный гимн\n", delete_after=600.0)
        await ctx.send(data['USSRExtreme'], delete_after=600.0)

    @commands.command()
    async def PS5(self, ctx):
        await ctx.send("這是空氣清淨機\n")
    
    @commands.command()
    async def MH(self, ctx, s: str):
        await ctx.send("牠弱散彈啦\n")

    @commands.command()
    async def HowYa(self, ctx):
        await ctx.send(data['AmeGood'], delete_after=180.0)

    @commands.command()
    async def Marxist(self, ctx):
        await ctx.send("立即學習馬克思主義，成為社會主義好青年!\n", delete_after=600.0)
        await ctx.send(data['Marxist'], delete_after=600.0)

    @commands.command()
    async def COVID(self, ctx):
        await ctx.send("若有症狀發生(發燒, 上呼吸道不適, 呼吸急促, 味覺喪失等)請撥打防疫專線1922")

    @commands.command()
    async def DPP(self, ctx):
        await ctx.send("台灣不缺電, 只是會跳電, 我們一起人與人連結, 用愛發電。\n")
        await ctx.send("這就是台灣價值啦,不然你要投國民黨? 不喜歡台灣就滾去對岸啦!\n")
        await ctx.send("看好了世界，台灣只示範一次，在兩週內沒水沒電沒疫苗，只剩確診滿街跑。\n", delete_after=600.0)
        await ctx.send(data['Eletricity'], delete_after=600.0)

    @commands.command()
    async def NationalQuality(self, ctx):
        await ctx.send("這就是台灣最美麗的「風景」, 美到不忍直視。\n", delete_after=600.0)
        await ctx.send(data['InOutInOut'], delete_after=600.0)
   

#    except:
#        print("請輸入可用指令。詳細資訊請輸入!help或!helps\n")
#        async def exception(self, ctx):
#            await ctx.send("請輸入可用指令。詳細資訊請輸入!help或!helps")

def setup(bot):
    bot.add_cog(cmds(bot))
