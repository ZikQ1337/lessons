import discord
from discord.ext import commands
from discord.ext.commands import Bot
import time
import asyncio
from discord import utils
from discord import Activity, ActivityType
import datetime
import random
import nekos
Bot = commands.Bot(command_prefix="!")
Arguments = ['feet', 'yuri', 'trap', 'futanari', 'hololewd', 'lewdkemo', 'solog', 'feetg', 'cum', 'erokemo', 'les', 'wallpaper', 'lewdk', 'ngif', 'tickle', 'lewd', 'feed', 'gecg', 'eroyuri', 'eron', 'cum_jpg', 'bj', 'nsfw_neko_gif', 'solo', 'kemonomimi', 'nsfw_avatar', 'gasm', 'poke', 'anal', 'slap', 'hentai', 'avatar', 'erofeet', 'holo', 'keta', 'blowjob', 'pussy', 'tits', 'holoero', 'lizard', 'pussy_jpg', 'pwankg', 'classic', 'kuni', 'waifu', 'pat', '8ball', 'kiss', 'femdom', 'neko', 'spank', 'cuddle', 'erok', 'fox_girl', 'boobs', 'random_hentai_gif', 'smallboobs', 'hug', 'ero', 'smug', 'goose', 'baka', 'woof']
def is_nsfw():
    async def predicate(ctx):
        return ctx.channel.is_nsfw()
    return commands.check(predicate)

@Bot.command()
@is_nsfw()
async def cum(ctx):
    emb = discord.Embed(color=0xebebeb)
    emb.set_image(url=nekos.img('cum'))
    await ctx.send(embed=emb)

@Bot.event
async def on_ready():
    print('Бот запустился')