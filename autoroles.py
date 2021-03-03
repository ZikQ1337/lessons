@Bot.event
async def on_member_join(member):
    channel = Bot.get_channel(ВашАйди)
    role = member.guild.get_role(ВашАйди)
    await member.add_roles(role)
    await channel.send(f"{member.mention} Добро пожаловать на сервер!")
@Bot.event
async def on_member_remove(member):
    channel = Bot.get_channel(ВашАйд)
    await channel.send(f"{member} Покинул нас!")
