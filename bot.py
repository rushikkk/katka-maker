import discord
import logging
import aiohttp
from discord.ext import commands
import xml.etree.ElementTree
import secrets
import random
# import rio

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - \
    %(message)s', level=logging.INFO)

BOT_PREFIX = ("-", "!")
description = '''NARUTA ETA KRUTA!!!!!111!'''
bot = commands.Bot(command_prefix=BOT_PREFIX, description=description)
client = discord.Client()


@bot.event
async def on_ready():
    # await bot.change_presence(game=discord.Game(name="with humans"))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for you"))
    print('------')
    print("Logged in as " + bot.user.name)
    print('------')


@bot.command()
async def naruto(ctx):
    """Send naruto pic in chat."""
    url = "https://qtv.ua/wp-content/uploads/2016/12/1453876472-30f41751775300d9860d749c94fb5d5b-640x480.jpg"
    await ctx.send(url)


@bot.command()
async def anime(ctx):
    page = random.randint(1, 864)
    """Link a picture with a dog in chat."""
    async with aiohttp.ClientSession() as session:
        async with session.get('https://wall.alphacoders.com/api2.0/get.php?auth={}&method=category&id=3&page={}'
                               .format(secrets.ANIME_KEY, page)) as r:
            if r.status == 200:
                js = await r.json()
                await ctx.send(js['wallpapers'][random.randint(0, 29)]['url_image'])
            else:
                await ctx.send("Аниме афк 8'(")


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
        async with session.get('http://api.thedogapi.co.uk/v2/dog.php?limit=1') as r:
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


affixes_dict = {
        "Тиранический, Взрывной, Упрямый, Зараженный": "http://bot-static.m-gaming.tk/tyr-burs-skitt-inf.jpg"
        }

@bot.command()
async def affix(ctx):
    """Current week affixes"""
    async with aiohttp.ClientSession() as session:
        async with session.get('https://raider.io/api/v1/mythic-plus/affixes?region=eu&locale=ru') as r:
            if r.status == 200:
                js = await r.json()
                # embed = discord.Embed(title="**Аффиксы на этой неделе**", colour=random.randint(0, 0xFFFFFF))
                embed = discord.Embed(colour=random.randint(0, 0xFFFFFF))
                embed.set_thumbnail(url=affixes_dict[js['title']])
                embed.set_author(name="Аффиксы на этой неделе", icon_url="http://bot-static.m-gaming.tk/wow-48px.png")
                embed.add_field(name=js['affix_details'][0]['name'], value="```" + js['affix_details'][0]['description'] + "```")
                embed.add_field(name=js['affix_details'][1]['name'], value="```" + js['affix_details'][1]['description'] + "```")
                embed.add_field(name=js['affix_details'][2]['name'], value="```" + js['affix_details'][2]['description'] + "```")
                embed.add_field(name=js['affix_details'][3]['name'], value="```" + js['affix_details'][3]['description'] + "```")
                await ctx.send(embed=embed)
            else:
                await ctx.send("Something wrong ;[")

@bot.command()
async def affixnext(ctx):
    """Current week affixes"""
    # embed = discord.Embed(title="**Аффиксы на этой неделе**", colour=random.randint(0, 0xFFFFFF))
    embed = discord.Embed(colour=random.randint(0, 0xFFFFFF))
    embed.set_thumbnail(url=affixes_dict[js['title']])
    embed.set_author(name="Аффиксы на этой неделе", icon_url="http://bot-static.m-gaming.tk/wow-48px.png")
    embed.add_field(name=js['affix_details'][0]['name'], value="```" + js['affix_details'][0]['description'] + "```")
    await ctx.send(embed=embed)




bot.run(secrets.TOKEN)
