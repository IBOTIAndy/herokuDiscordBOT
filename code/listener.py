import discord
from discord.ext import commands
import os
import json
import random

with open('set.json', 'r', encoding = 'utf8') as jfile:
    data = json.load(jfile)

UBIimg = 0
RIPdata = []
RIPdata.append(data["shark_RIP"])
RIPdata.append(data["gura_RIP"])
randomRIP = random.choice([data["shark_RIP"], data["gura_RIP"]])
AmeGood = data["AmeGood"]
PepeCough = data["PepeCough"]

class listener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if (message.author != "上個香" in message.content or "上香" in message.content):
            #await message.channel.send(randomRIP)
            await message.channel.send(randomRipGif())

        elif message.author != "IBOTIBOT#1854" and "民進黨" in message.content:
            await message.channel.send(data['DPP'])

        elif ("mac" in message.content) or ("macbook" in message.content) or ("iphone" in message.content):
            await message.channel.send('{0.author}同志想換美帝國主義的計算機? 判勞改10年\n'.format(message, ))

        elif ("喉嚨癢" in message.content) or ("咳" in message.content) or ("確診" in message.content):
            await message.channel.send(PepeCough)

        #elif message.content == "test":
        #    await message.channel.send('Message from {0.author}: {0.content}\n'.format(message))

        elif message.author != "IBOTIBOT#1854" and "我們" in message.content:
            pass

        elif message.author != "IBOTIBOT#1854" and "我" in message.content:
            await message.channel.send("{0.author}同志。不單只是我，是「我們」\n".format(message))

        elif message.author != "Наш робот Discord#8637" and "盤" in message.content:
            await message.channel.send("{0.author}同志。『Pan』此字乃是資本主義的糜爛奢華之象徵，必須由共產人民團結一致共同打倒！\n".format(message))
        #elif (message.author != "上個香" in message.content or "上香" in message.content):
            #await message.channel.send(randomRIP)
            #await message.channel.send(randomRipGif())

        elif message.author != "好耶" in message.content:
            await message.channel.send(AmeGood)

        elif message.author != "共產主義書單" in message.content:
            await message.channel.send(data['Marxist'])

def setup(bot):
    bot.add_cog(listener(bot))

def randomRipGif():
    randomNum = random.randint(0, 2)
    print(randomNum)
    if randomNum == 0:
        return data["shark_RIP"]
    elif randomNum == 1:
        return data["gura_RIP"]
    else:
        return data["shark_BigRIP"]



















