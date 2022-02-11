import discord
from discord.ext import commands
import os
import json
import random

with open('url.json', 'r', encoding = 'utf8') as jfile:
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
#        printDetail(message) #開發階段用來確認內部資訊
        authorName = getName(message.author) #取得暱稱nick(沒有則取得名稱name)

        if ("autoDeleteTest" in message.content):
            await message.channel.send("This message delete after 10 sec", delete_after=10.0)
        elif ("test" in message.content):
            await message.channel.send("a")

        #if (message.author.bot == True and message.author.discriminator != "1854"):
        #    await message.channel.send(f"{message.author.name} hi")

        if ( not isBot(message.author) ): #如果該訊息不是bot發出的
            if ( "上個香" in message.content or "上香" in message.content):
                #await message.channel.send(randomRIP)
                await message.channel.send(randomRipGif())

            elif ( "民進黨" in message.content):
                await message.channel.send(data['DPP'])

            elif (("mac" in message.content) or ("macbook" in message.content) or ("iphone" in message.content)):
                await message.channel.send(f'{authorName}同志想換美帝國主義的計算機? 判勞改10年\n', delete_after=90.0)

            elif (("喉嚨癢" in message.content) or ("咳" in message.content) or ("確診" in message.content)):
                await message.channel.send(PepeCough)

            elif ( "我們" in message.content):
                pass

            elif ( "我" in message.content):
                await message.channel.send(f"{authorName}同志。不單只是我，是「我們」\n", delete_after=90.0)

            elif ( "盤" in message.content):
                await message.channel.send(f"{authorName}同志。『Pan』此字乃是資本主義的糜爛奢華之象徵，必須由共產人民團結一致共同打倒！\n", delete_after=90.0)

            elif ( "好耶" in message.content):
                await message.channel.send(AmeGood, delete_after=90.0)

            elif ( "共產主義書單" in message.content):
                await message.channel.send(data['Marxist'], delete_after=90.0)

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

def isBot(author):
    return author.bot

def printDetail(message):
    #print(message)
    channel = message.channel
    mType = message.type
    user = message.author
    server = message.author.guild
    flags = message.flags
    print("\nmessage:")
    print(f"author say: {message.content}")
    print(f"ID: {message.id}")
    print(f"channel: {channel.name}, id: {channel.id}")
    print(f"author(realName): {user.nick}({user.name})\nauthorID: {user.id}, author is bot: {user.bot}")
    print(f"server(guild): {server.name}, id: {server.id}, memberCount: {server.member_count}")

def getName(author):
    name = author.name
    if (author.nick != None):
        name = author.nick
    return name


















