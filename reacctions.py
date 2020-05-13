@Bot.event
async def on_raw_reaction_add(payload):
    if payload.message_id == ВашАйди and payload.emoji.name == ВашЭмоджи:
        for guild in Bot.guilds:
            role = discord.utils.get(guild.roles, id = ВашАйди)
            await payload.member.add_roles(role)
