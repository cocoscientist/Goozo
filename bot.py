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

@bot.command(name='xkcd', help='Returns an XKCD comic strip')
async def getXKCD(ctx, edition:int=None):
    response = None
    if edition is None:
        response = fetchxkcd.fetchLatest()
    else:
        response = fetchxkcd.fetchByNum(edition)
    embd = embedGenerator.XKCDEmbed(response)
    await ctx.send(embed=embd)

bot.run(TOKEN)