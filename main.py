import discord
from discord.ext import commands

bot = commands.Bot(command_preFix = '[')

@bot.event
async def on_ready():
    print("Bot works successfully!")

bot.run('NzAzMDc0ODg3NjQ3ODg3NDYx.XqJTog.do9Z6VgFEun_7u0KNhL7Uc933x0')