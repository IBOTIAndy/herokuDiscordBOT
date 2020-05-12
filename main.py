#輸入Discord用的函式庫
from discord.ext import commands
import os
import json
with open('set.json', 'r', encoding = 'utf8') as jfile:
    data = json.load(jfile)

bot = commands.Bot(command_prefix='!')

#bot.load_extension('code.cmds')     #不明原因錯誤: 程式檔放入資料夾內便無法load
#bot.load_extension('code.showPicGif')

bot.load_extension('cmds')
bot.load_extension('showPicGif')

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

#for pyFile in os.listdir('./cmd'):
#    if pyFile.endswith('.py'):
#        bot.load_extension(f'cmd.{pyFile[:-3]}')
#讓bot在Discord伺服器上啟動(需要密鑰)
#if os.environ.get('DISCORD_TOKEN'):
#    bot.run(os.environ.get('DISCORD_TOKEN'))

if __name__ == "__main__":
    bot.run(data['DISCORD_TOKEN'])