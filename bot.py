import discord
import logging
import aiohttp
from discord.ext import commands
import xml.etree.ElementTree
import secrets
import random
import affixes
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


@bot.command()
async def affix(ctx, week: str = '0'):
    """Current week affixes"""
    if week == 'next':
        week = '1'
    if week.isdigit() and int(week) >= 0:
        # await ctx.send(":/ Циферки больше 0 вводи после !affixnext")
        # embed = discord.Embed(title="**Аффиксы на этой неделе**", colour=random.randint(0, 0xFFFFFF))
        week = int(week)
        n_affx = affixes.get_affixes(week)
        aff_rot = affixes.affixes_rotation[n_affx]
        embed = discord.Embed(colour=random.randint(0, 0xFFFFFF))
        embed.set_thumbnail(url=aff_rot[4])
        if week == 0:
            embed.set_author(name="Аффиксы на этой неделе", icon_url="http://bot-static.m-gaming.tk/wow-48px.png")
        else:
            embed.set_author(name=f"Аффиксы через {week} нед.", icon_url="http://bot-static.m-gaming.tk/wow-48px.png")
        embed.add_field(name=affixes.affixes_ru[aff_rot[0]][0], value="```" + affixes.affixes_ru[aff_rot[0]][1] + "```")
        embed.add_field(name=affixes.affixes_ru[aff_rot[1]][0], value="```" + affixes.affixes_ru[aff_rot[1]][1] + "```")
        embed.add_field(name=affixes.affixes_ru[aff_rot[2]][0], value="```" + affixes.affixes_ru[aff_rot[2]][1] + "```")
        embed.add_field(name=affixes.affixes_ru[aff_rot[3]][0], value="```" + affixes.affixes_ru[aff_rot[3]][1] + "```")
        await ctx.send(embed=embed)
    else:
        await ctx.send(":/ Циферки больше 0 вводи после !affix")


@bot.command()
async def rank(ctx, name: str, realm: str = 'howling-fjord', region: str = 'eu'):
    """rank by raider.io"""
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://raider.io/api/v1/characters/profile?region={region}&realm={realm}&name={name}\
        &fields=gear,mythic_plus_scores,mythic_plus_ranks') as r:
            if r.status == 200:
                js = await r.json()
                embed = discord.Embed(colour=random.randint(0, 0xFFFFFF))
                embed.set_thumbnail(url=js['thumbnail_url'])
                embed.set_author(name=js['name'], url=js['profile_url'],
                                 icon_url="http://bot-static.m-gaming.tk/wow-48px.png")
                embed.add_field(name="iLVL (max):", value="```" + str(js['gear']['item_level_equipped']) + " (" +
                                                          str(js['gear']['item_level_total']) + ")```", inline=True)
                embed.add_field(name='M+ очки:', value="```" + str(js['mythic_plus_scores']['all']) + "```",
                                inline=True)
                await ctx.send(embed=embed)
            else:
                await ctx.send("Неверно введена команда! \nФормат команды: \
                ```\n!rank character_name [realm='howling-fjord' [region='eu']]```\
                Пример команды:\
                ```\n!rank руфлезс howling-fjord eu\n!rank руфлезс```")

bot.run(secrets.TOKEN)
