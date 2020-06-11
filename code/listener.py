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
        if "macbook" in message.content:
            await message.channel.send('{0.author} 想換美帝國主義的電腦? 該受到人民正義的法槌的制裁了(拿起AK47\n'.format(message))

        elif message.content == "test":
            await message.channel.send('Message from {0.author}: {0.content}\n'.format(message))

def setup(bot):
    bot.add_cog(listener(bot))
    #bot.add_cog(showPic(bot))




















