import discord
import logging

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
# bot = commands.Bot(command_prefix='!', description=description)
bot = discord.Client()

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - \
    %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.event
async def on_message(message):
    print(message.id)
    print(message.content)
    print(message.channel)
    print(message.channel.id)
    print(message.author)
    print(message.type)


bot.run('token')
