import discord
import logging
from discord.ext import commands


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - \
    %(message)s', level=logging.INFO)

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='!', description=description)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
	

@bot.command()
async def anime():
    """Adds two numbers together."""
    url = "https://qtv.ua/wp-content/uploads/2016/12/1453876472-30f41751775300d9860d749c94fb5d5b-640x480.jpg"
    await bot.say(url)
	
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
	

	
@bot.command()
async def kirill():
    """Adds two numbers together."""
    url = "https://sun9-7.userapi.com/c840436/v840436288/16475/sL1tuA7X5-Y.jpg"
    await bot.say(url)
	

## @bot.event
## async def on_message(message):
##    print(message.id)
##    print(message.content)
##    print(message.channel)
##    print(message.channel.id)
##    print(message.author)
##    print(message.type)


bot.run('token')
