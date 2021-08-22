#輸入Discord用的函式庫
import discord
from discord.ext import commands
from bs4 import BeautifulSoup
from lxml import etree
import os
import json
import requests
import re
import random

with open('url.json', 'r', encoding = 'utf8') as jfile:
    data = json.load(jfile)

class fastcar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

#    @commands.command()
#    async def Car(self, ctx, html):
#        if (html == "p") or (html == "P") or (html == "pixiv") or (html == "Pixiv"):
#            output = data['Pixiv'] + (random(10000000, 99999999) 
#            if LDOApixiv(output):
#                await ctx.send('||' + output + '||\n')
#                await ctx.send("可能會有太香的東西 慎點\n")
#            else:
#                await ctx.send("404 not found. 發車到P網的同志翻車了\n")
#        elif (html == "n") or (html == "nhentai"):
#            output = data['nhentai'] + (random(100000, 999999) 
#            await ctx.send('||' + output + '||')
#        else:
#           await ctx.send("plz enter \'!Car p\' or \'!Car n\'\n to use randomCar")
       
    @commands.command()
    async def RandomCar(self, ctx, arg):
        if (arg == "p") or (arg == "P") or (arg == "pixiv") or (arg == "Pixiv"):
            i=0
            while(True):
                output = data['Pixiv'] + str(random.randint(10000000, 99999999))
                if LDOApixiv(output):
                    if i != 0:
                        await ctx.send("司機同志總共翻車了 " + str(i) + " 次")
                    else:
                        await ctx.send("太神拉 沒有翻車")
                    await ctx.send('||' + output + '||' + "\n可能會有太香的東西 慎點")
                    break
                else:
                    i = i + 1
        elif (arg == "n") or (arg == "nhentai"):
            i=0
            while(True):
                output = data['nhentai'] + str(random.randint(100000, 999999))
                if LDOAnhentai(output):
                    if i != 0:
                        await ctx.send("司機同志總共翻車了 " + str(i) + " 次")
                    else:
                        await ctx.send("太神拉 沒有翻車")
                    await ctx.send('||' + output + '||' + "\n三思而後行，前方連結極高概率讓您社會性死亡")
                    break
                else:
                    i = i + 1

    @commands.command()
    async def Car(self, ctx, *args):
        if len(args) != 0:
            #print("good\n")
            arg = str(args[0])
            #print(arg + '\n')
            if arg.isdigit():
                if len(arg) == 8:
                    output = data['Pixiv'] + arg
                    if LDOApixiv(output):
                        await ctx.send('以下連結飄出了來自P網的香氣\n' + '||' + output + '||')
                    else:
                        await ctx.send("404 not found. 發車到P網的同志翻車了\n")
                if len(arg) == 6:
                    output = data['nhentai'] + arg
                    if LDOAnhentai(output):
                        await ctx.send("以下連結內容基本母湯，不建議在公開場合點擊\n")
                        await ctx.send('||' + output + '||')
                    else:
                        await ctx.send("404 not found. 發車到n網的同志翻車了\n")
            else:
                await ctx.send("Please input Num!")
        else:
            await ctx.send("input cannot be NULL!")

def LDOApixiv(output):
    r = requests.get(output)
    soup = BeautifulSoup(r.text, "lxml")
    try:
        html = soup.find(class_ = "error-title").text
        if html == 'エラーが発生しました':
            return 0        
    except AttributeError:
            return 1
    else:
        print("I don't know what happen. Check Log first.\n")

def LDOAnhentai(output):
    r = requests.get(output)
    soup = BeautifulSoup(r.text, "lxml")
    try:
        html = soup.find('h1').text
        #print(html)
        if html == '404 – Not Found':
            return 0
        else:
            return 1
    except AttributeError:
        return 1
    else:
        #print(html + '\n')
        print("I don't know what happen. Check Log first.\n")
        
def setup(bot):
    bot.add_cog(fastcar(bot))

