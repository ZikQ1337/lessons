import json

@Bot.event
async def on_message(message):
    with open('ВашПуть','r') as f:
        users = json.load(f)
    async def update_data(users,user):
        if not user in users:
            users[user] = {}
            users[user]['exp'] = 0
            users[user]['lvl'] = 1
    async def add_exp(users,user,exp):
        users[user]['exp'] += exp
    async def add_lvl(users,user):
        exp = users[user]['exp']
        lvl = users[user]['lvl']
        if exp > lvl:
            await message.channel.send(f'{message.author.mention} повысил свой уровень!')
            users[user]['exp'] = 0
            users[user]['lvl'] = lvl + 1
    await update_data(users,str(message.author.id))
    await add_exp(users,str(message.author.id),0.1)
    await add_lvl(users,str(message.author.id))
    with open('ВашПуть','w') as f:
        json.dump(users,f)