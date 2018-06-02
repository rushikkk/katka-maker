import discord
import logging
import aiohttp
from discord.ext import commands
import xml.etree.ElementTree
import secrets

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - \
    %(message)s', level=logging.INFO)

BOT_PREFIX = ("-", "!")
description = '''NARUTA ETA KRUTA!!!!!111!'''
bot = commands.Bot(command_prefix=BOT_PREFIX, description=description)
client = discord.Client()


@bot.event
async def on_ready():
    # await bot.change_presence(game=discord.Game(name="with humans"))
    await bot.change_presence(activity=discord.Game(name="ANIME"))
    print('------')
    print("Logged in as " + bot.user.name)
    print('------')


@bot.command()
async def anime(ctx):
    """Send Naruto in chat."""
    url = "https://qtv.ua/wp-content/uploads/2016/12/1453876472-30f41751775300d9860d749c94fb5d5b-640x480.jpg"
    await ctx.send(url)


@bot.command()
async def cat(ctx):
    """Link a picture with a cat in chat."""
    async with aiohttp.ClientSession() as session:
        async with session.get('http://thecatapi.com/api/images/get?api_key={}&format=xml&type=gif,png,jpg'
                               .format(secrets.CAT_API_TOKEN)) as r:
            if r.status == 200:
                e = xml.etree.ElementTree.fromstring(await r.text())
                for child in e.iter('url'):
                    await ctx.send(child.text)
            else:
                await ctx.send("Котики афк :'(")


@bot.command()
async def dog(ctx):
    """Link a picture with a dog in chat."""
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.thedogapi.co.uk/v2/dog.php?limit=1') as r:
            if r.status == 200:
                js = await r.json()
                await ctx.send(js['data'][0]['url'])
            else:
                await ctx.send("Пёсики афк :'(")


@bot.command()
async def anus(ctx):
    """Personal command for Gleb."""
    url = "https://2ch.hk//mo/src/177945/14774709849140.jpg"
    await ctx.send(url)


@bot.command()
async def brsm(ctx):
    """Personal command for Gleb #2."""
    url = "https://pp.userapi.com/c323617/v323617351/3348/1baGYjXTp-c.jpg"
    await ctx.send(url)


bot.run(secrets.TOKEN)
