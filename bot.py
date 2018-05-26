import discord
import logging
import aiohttp
import asyncio
from discord import Game
from discord.ext import commands

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
    """Adds two numbers together."""
    url = "https://qtv.ua/wp-content/uploads/2016/12/1453876472-30f41751775300d9860d749c94fb5d5b-640x480.jpg"
    await bot.say(url)


@bot.command()
async def cat():
    """Adds two numbers together."""
    async with aiohttp.ClientSession() as session:
        r = await session.get('http://aws.random.cat/meow')
        if r.status == 200:
            js = await r.json()
            print(js['file'])
            await bot.say(js['file'])
            return
    # await bot.say(url)


@bot.command(pass_context=True)
async def anime2(ctx):
    print(dir(ctx.message))


@bot.command()
async def anus():
    """Adds two numbers together."""
    url = "https://2ch.hk//mo/src/177945/14774709849140.jpg"
    await bot.say(url)


@bot.command()
async def brsm():
    """Adds two numbers together."""
    url = "https://pp.userapi.com/c323617/v323617351/3348/1baGYjXTp-c.jpg"
    await bot.say(url)


# @bot.event
# async def on_message(message):
#    print(message.id)
#    print(message.content)
#    print(message.channel)
#    print(message.channel.id)
#    print(message.author)
#    print(message.type)


bot.run('NDQ5NTEwMTQ2NTgzMDM1OTA1.DelxZg.q6sHJTXf5jyahgzmq2U1wjQ5WmE')
