import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from discord import Activity, ActivityType
import datetime
import random
import json
#0x4c12f5
Bot = commands.Bot(command_prefix="$")
queue = []

@Bot.command()
async def timely(ctx):
    with open('economy.json','r') as f:
        money = json.load(f)
    if not str(ctx.author.id) in money:
        money[str(ctx.author.id)] = {}
        money[str(ctx.author.id)]['Money'] = 0

    if not str(ctx.author.id) in queue:
        emb = discord.Embed(description=f'**{ctx.author}** Вы получили свои 1250 монет')
        await ctx.send(embed= emb)
        money[str(ctx.author.id)]['Money'] += 1250
        queue.append(str(ctx.author.id))
        with open('economy.json','w') as f:
            json.dump(money,f)
        await asyncio.sleep(12*60)
        queue.remove(str(ctx.author.id))
    if str(ctx.author.id) in queue:
        emb = discord.Embed(description=f'**{ctx.author}** Вы уже получили свою награду')
        await ctx.send(embed= emb)
@Bot.command()
async def balance(ctx,member:discord.Member = None):
    if member == ctx.author or member == None:
        with open('economy.json','r') as f:
            money = json.load(f)
        emb = discord.Embed(description=f'У **{ctx.author}** {money[str(ctx.author.id)]["Money"]} монет')
        await ctx.send(embed= emb)
    else:
        with open('economy.json','r') as f:
            money = json.load(f)
        emb = discord.Embed(description=f'У **{member}** {money[str(member.id)]["Money"]} монет')
        await ctx.send(embed= emb)
@Bot.command()
async def addshop(ctx,role:discord.Role,cost:int):
    with open('economy.json','r') as f:
        money = json.load(f)
    if str(role.id) in money['shop']:
        await ctx.send("Эта роль уже есть в магазине")
    if not str(role.id) in money['shop']:
        money['shop'][str(role.id)] ={}
        money['shop'][str(role.id)]['Cost'] = cost
        await ctx.send('Роль добавлена в магазин')
    with open('economy.json','w') as f:
        json.dump(money,f)
@Bot.command()
async def shop(ctx):
    with open('economy.json','r') as f:
        money = json.load(f)
    emb = discord.Embed(title="Магазин")
    for role in money['shop']:
        emb.add_field(name=f'Цена: {money["shop"][role]["Cost"]}',value=f'<@&{role}>',inline=False)
    await ctx.send(embed=emb)
@Bot.command()
async def removeshop(ctx,role:discord.Role):
    with open('economy.json','r') as f:
        money = json.load(f)
    if not str(role.id) in money['shop']:
        await ctx.send("Этой роли нет в магазине")
    if str(role.id) in money['shop']:
        await ctx.send('Роль удалена из магазина')
        del money['shop'][str(role.id)]
    with open('economy.json','w') as f:
        json.dump(money,f)
@Bot.command()
async def buy(ctx,role:discord.Role):
    with open('economy.json','r') as f:
        money = json.load(f)
    if str(role.id) in money['shop']:
        if money['shop'][str(role.id)]['Cost'] <= money[str(ctx.author.id)]['Money']:
            if not role in ctx.author.roles:
                await ctx.send('Вы купили роль!')
                for i in money['shop']:
                    if i == str(role.id):
                        buy = discord.utils.get(ctx.guild.roles,id = int(i))
                        await ctx.author.add_roles(buy)
                        money[str(ctx.author.id)]['Money'] -= money['shop'][str(role.id)]['Cost']
            else:
                await ctx.send('У вас уже есть эта роль!')
    with open('economy.json','w') as f:
        json.dump(money,f)

@Bot.command()
async def give(ctx,member:discord.Member,arg:int):
    with open('economy.json','r') as f:
        money = json.load(f)
    if money[str(ctx.author.id)]['Money'] >= arg:
        emb = discord.Embed(description=f'**{ctx.author}** подарил **{member}** **{arg}** монет')
        money[str(ctx.author.id)]['Money'] -= arg
        money[str(member.id)]['Money'] += arg
        await ctx.send(embed = emb)
    else:
        await ctx.send('У вас недостаточно денег')
    with open('economy.json','w') as f:
        json.dump(money,f)
Bot.run('NjcwNjI1MjU0MzIxODE1NTkz.Xwcelw.Qqb-eYhPIutmZE8KGCvx_xotyts')