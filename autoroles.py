@Bot.event
async def on_member_join(member):
    channel = Bot.get_channel(ВашАйди)
    for guild in Bot.guilds:
        role = discord.utils.get(guild.roles,id=ВашАйди)
    await member.add_roles(role)
    await channel.send(f"{member.mention} Добро пожаловать на сервер!")
@Bot.event
async def on_member_remove(member):
    channel = Bot.get_channel(ВашАйд)
    await channel.send(f"{member} Покинул нас!")