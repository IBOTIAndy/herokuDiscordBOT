#輸入Discord用的函式庫
import discord
from discord.ext import commands
from bs4 import BeautifulSoup
from lxml import etree
import os
import json
import requests
import re

with open('set.json', 'r', encoding = 'utf8') as jfile:
    data = json.load(jfile)

class fastcar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def NTUT(self, ctx, *, arg):
        url = data['NTUT']
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "lxml")

        inputstring = arg
        x = inputstring.split()
        await ctx.send(x)
    
        if x[0] == "id":
            html = soup.find(id = x[1]).text
            await ctx.send(len(html))
            if len(html) > 2000:
                await ctx.send("This html is too long that can't output.\n")
            else:
                await ctx.send(html)

        elif x[0] == "class":
            html = soup.find(class_ = x[1]).text
            if len(html) > 2000:
                await ctx.send("This html is too long that can't output.\n")
            else:
                await ctx.send(html)

    @commands.command()
    async def Car(self, ctx, arg):
        if arg.isdigit():
            if len(arg) == 8:
                output = data['Pixiv'] + arg
                if LDOApixiv(output):
                    await ctx.send('||' + output + '||')
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

