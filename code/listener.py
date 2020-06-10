import discord
from discord.ext import commands
import os
import json

with open('set.json', 'r', encoding = 'utf8') as jfile:
    data = json.load(jfile)

UBIimg = 0

class listener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == "test":
            await message.channel.send('Message from {0.author}: {0.content}\n'.format(message))

    @commands.Cog.listener()
    async def on_message(self, message):
        if "macbook" in message.content:
            await message.channel.send('{0.author} 還想換蘋果筆電啊 owO?\n'.format(message))

    """@commands.Cog.listener()
    async def on_message(self, message):
        if (("ubi" or "UBI") and "伺服器") in message.content:
            pic = data['UBIPotato']
            await message.channel.send('跟 {0.author} 說個祕密, UBI的伺服器就是\n'.format(message))
            UBIimg = 1
            ubi()"""

    #def ubi():
       #pic = data['KoLianNa']
       #channel.send(pic)

"""class showPic(commands.Cog):
    async def sentImg():
        if UBIimg == 1:
            print("UBIimg is true!\n")
            UBIimg = 0"""

def setup(bot):
    bot.add_cog(listener(bot))
    #bot.add_cog(showPic(bot))




















