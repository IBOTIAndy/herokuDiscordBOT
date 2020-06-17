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
        if ("mac" in message.content) or ("macbook" in message.content) or ("iphone" in message.content):
            await message.channel.send('{0.author}同志想換美帝國主義的計算機? 判勞改10年\n'.format(message, ))

        elif message.content == "test":
            await message.channel.send('Message from {0.author}: {0.content}\n'.format(message))

        elif message.author != "IBOTIAndy#1854" and "我們" in message.content:
            pass

        elif message.author != "IBOTIAndy#1854" and "我" in message.content:
            await message.channel.send("{0.author}同志。不單只是我，是「我們」\n".format(message))

        elif message.author != "Наш робот Discord#8637" and "盤" in message.content:
            await message.channel.send("{0.author}同志。『Pan』此字乃是資本主義的糜爛奢華之象徵，必須由共產人民團結一致共同打倒！\n".format(message))

def setup(bot):
    bot.add_cog(listener(bot))




















