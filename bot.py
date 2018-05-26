import discord
import logging
import requests
from discord import Game
from discord.ext import commands
import xml.etree.ElementTree
import secrets

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - \
    %(message)s', level=logging.INFO)

BOT_PREFIX = ("?", "!")
description = '''NARUTA ETA KRUTA!!!!!111!'''
bot = commands.Bot(command_prefix=BOT_PREFIX, description=description)
client = discord.Client()


@bot.event
async def on_ready():
    await bot.change_presence(game=Game(name="with humans"))
    print('------')
    print("Logged in as " + bot.user.name)
    print('------')


@bot.command()
async def anime():
    """Send Naruto in chat."""
    url = "https://qtv.ua/wp-content/uploads/2016/12/1453876472-30f41751775300d9860d749c94fb5d5b-640x480.jpg"
    await bot.say(url)


@bot.command()
async def cat():
    """Link a picture with a cat in chat."""
    r = requests.get('http://thecatapi.com/api/images/get?api_key={}&format=xml&type=gif,png,jpg'
                     .format(secrets.CAT_API_TOKEN))
    if r.status_code == 200:
        e = xml.etree.ElementTree.fromstring(r.content)
        for child in e.iter('url'):
            await bot.say(child.text)
    else:
        await bot.say("Котики афк :'(")


@bot.command()
async def dog():
    """Link a picture with a dog in chat."""
    r = requests.get('https://api.thedogapi.co.uk/v2/dog.php?limit=1')
    if r.status_code == 200:
        js = r.json()
        await bot.say(js['data'][0]['url'])
    else:
        await bot.say("Пёсики афк :'(")


# @bot.command(pass_context=True)
# async def anime2(ctx):
#     print(dir(ctx.message))


@bot.command()
async def anus():
    """Personal command for Gleb."""
    url = "https://2ch.hk//mo/src/177945/14774709849140.jpg"
    await bot.say(url)


@bot.command()
async def brsm():
    """Personal command for Gleb #2."""
    url = "https://pp.userapi.com/c323617/v323617351/3348/1baGYjXTp-c.jpg"
    await bot.say(url)


bot.run(secrets.TOKEN)
