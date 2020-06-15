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
    async def Car(self, ctx, arg):
        if arg.isdigit():
            if len(arg) == 8:
                output = data['Pixiv'] + arg
                if LDOApixiv(output):
                    await ctx.send('||' + output + '||\n')
                    await ctx.send("可能會有太香的東西 慎點\n")
                else:
                    await ctx.send("404 not found. 發車到P網的同志翻車了\n")
            if len(arg) == 6:
                output = data['nhentai'] + arg
                await ctx.send('||' + output + '||')
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
    return 1
        
def setup(bot):
    bot.add_cog(fastcar(bot))

