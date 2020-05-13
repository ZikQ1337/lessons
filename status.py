from discord import Activity, ActivityType

@Bot.event
async def on_ready():
    print("Бот запустился")
    await Bot.change_presence(status=discord.Status.idle,activity=Activity(name="Наблюдает за коронавирусом",type=ActivityType.watching))
