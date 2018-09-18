import discord
import logging
import aiohttp
from discord.ext import commands

async def affixes(ctx):
    """Current week affixes"""
    async with aiohttp.ClientSession() as session:
        async with session.get('https://raider.io/api/v1/mythic-plus/affixes?region=eu&locale=ru') as r:
            if r.status == 200:
                js = await r.json()
                await ctx.send(js['title'])
            else:
                await ctx.send("lohpidr")
