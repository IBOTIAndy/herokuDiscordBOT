#輸入Discord用的函式庫 
from discord.ext import commands
from bs4 import BeautifulSoup
from lxml import etree
import os
import json
import requests

with open('botToken.json', 'r', encoding = 'utf8') as jfile:
    botTokenJson = json.load(jfile)
jfile.close()

with open('url.json', 'r', encoding = 'utf8') as jfile:
    data = json.load(jfile)

bot = commands.Bot(command_prefix='!')

bot.load_extension('code.cmds') 
bot.load_extension('code.showPicGif')
bot.load_extension('code.listener')
bot.load_extension('code.fastcar')

#當bot成功上線時輸出成功訊息
@bot.event
async def on_ready():
    print(bot.user, 'is ready.')
    for pyFile in os.listdir('./code'):
        print(pyFile)

#當新成員加入伺服器時輸出訊息
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(data['IN_SERVER & OUT_SERVER'])
    await channel.send(f'{member} 同志加入蘇維埃的行列了，讓我們一起團結全世界人民!')

#當新成員離開伺服器時輸出訊息
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(data['IN_SERVER & OUT_SERVER'])
    await channel.send(f'{member} 離開我們了，我們懷念他!')

if __name__ == "__main__":
    bot.run(botTokenJson['DISCORD_TOKEN'])
