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
    num = response['num']
    d, m, y = response['day'], response['month'], response['year']
    embd = discord.Embed(title=response['title'],url=f'https://xkcd.com/{num}',description=response['alt'])
    embd.set_author(name='Randall Munroe')
    embd.set_image(url=response['img'])
    embd.set_footer(text=f'{d}/{m}/{y}')
    await ctx.send(embed=embd)

bot.run(TOKEN)