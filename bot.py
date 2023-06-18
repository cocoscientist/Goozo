import os

import discord
from discord.ext import commands
from fetchxkcd import fetchLatest
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='heygz ',intents=intents)

@bot.command(name='xkcd', help='Returns an XKCD comic strip')
async def getXKCD(ctx):
    response = fetchLatest()
    await ctx.send(response['num'])

bot.run(TOKEN)