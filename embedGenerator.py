import discord

def XKCDEmbed(response):
    num = response['num']
    d, m, y = response['day'], response['month'], response['year']
    embd = discord.Embed(title=response['title'],url=f'https://xkcd.com/{num}',description=response['alt'])
    embd.set_author(name='Randall Munroe')
    embd.set_image(url=response['img'])
    embd.set_footer(text=f'XKCD {num} - {d}/{m}/{y}')
    return embd