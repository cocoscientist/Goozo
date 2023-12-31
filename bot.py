import os

import discord
from discord.ext import commands
from serviceCaller import *
import embedGenerator
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='heygz ',intents=intents)

@bot.command(name='egs', help='Returns games currently available for free on the Epic Games Store')
async def getFreeEpicGames(ctx, page:int=1):
    response = fetchEpicGames.currentGameData(page)
    embd = embedGenerator.egsEmbed(response)
    await ctx.send(embed=embd)

@bot.command(name='xkcd', help='Returns an XKCD comic strip')
async def getXKCD(ctx, edition:int=None):
    response = None
    if edition is None:
        response = fetchxkcd.fetchLatest()
    else:
        response = fetchxkcd.fetchByNum(edition)
    embd = embedGenerator.XKCDEmbed(response)
    await ctx.send(embed=embd)

@bot.command(name='uselessfact', help='A random useless fact (with source)')
async def getUselessFact(ctx):
    response = fetchUselessFact.getRandomFact()
    embd = embedGenerator.uselessFactEmbed(response)
    await ctx.send(embed=embd)

@bot.command(name='coffee', help='A random coffee image')
async def deliverCoffee(ctx):
    curUser = ctx.message.author
    response = fetchCoffee.getCoffee()
    embd = embedGenerator.coffeeEmbed(response, curUser)
    await ctx.send(embed=embd)
    await ctx.send(curUser.mention)

bot.run(TOKEN)