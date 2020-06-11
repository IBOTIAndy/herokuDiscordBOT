#輸入Discord用的函式庫
from discord.ext import commands
from bs4 import BeautifulSoup
from lxml import etree
import os
import json
import requests
with open('set.json', 'r', encoding = 'utf8') as jfile:
    data = json.load(jfile)

bot = commands.Bot(command_prefix='!')

bot.load_extension('code.cmds')     #不明原因錯誤: 程式檔放入資料夾內便無法load
bot.load_extension('code.showPicGif')
bot.load_extension('code.listener')
#bot.load_extension('code.fastcar')
#bot.load_extension('cmds')
#bot.load_extension('showPicGif')

#當bot成功上線時輸出成功訊息
@bot.event
async def on_ready():
    print(bot.user, 'is ready.')
    #print("Bot works successfully!")
    for pyFile in os.listdir('./code'):
        print(pyFile)

#當新成員加入伺服器時輸出訊息
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(data['IN_SERVER & OUT_SERVER'])
    await channel.send(f'{member} join the server OwO!')
    #print("f'{member}' join in the server!")

#當新成員離開伺服器時輸出訊息
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(data['IN_SERVER & OUT_SERVER'])
    await channel.send(f'{member} leave the server Q^Q!')
    #print(f'{member} leave the server Q^Q!')

#catch the webside of NTUT
@bot.command()
async def NTUT(ctx, *, arg):
    url = "https://www.ntut.edu.tw/"
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

#catch the webside of PIXIV
@bot.command()
async def Pixiv(ctx, arg):
    url = "https://www.pixiv.net/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")

if __name__ == "__main__":
    bot.run(data['DISCORD_TOKEN'])
