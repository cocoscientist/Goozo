import discord

def XKCDEmbed(response):
    num = response['num']
    d, m, y = response['day'], response['month'], response['year']
    embd = discord.Embed(title=response['title'],url=f'https://xkcd.com/{num}',description=response['alt'])
    embd.set_author(name='Randall Munroe')
    embd.set_image(url=response['img'])
    embd.set_footer(text=f'XKCD {num} - {d}/{m}/{y}')
    return embd

def uselessFactEmbed(response):
    embd = discord.Embed(title='Random Useless Fact',url=response['source_url'],description=response['text'])
    return embd

def coffeeEmbed(response, curUser):
    embd = discord.Embed(title="Here's your coffee!", description=f'Fresh coffee served for {curUser}!')
    embd.set_image(url=response['file'])
    return embd

def egsEmbed(response):
    embd = discord.Embed(title=response['title'],url=response['url'],description=response['desc'])
    embd.set_author(name=response['publisher'])
    embd.set_image(url=response['image'])
    embd.add_field(name="Start Date", value=response['startDate'], inline=True)
    embd.add_field(name="End Date", value=response['endDate'], inline=True)
    embd.set_footer(text=response['footer'])
    return embd