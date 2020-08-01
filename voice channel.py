@Bot.event
async def on_voice_state_update(member,before,after):
    if after.channel.id == ВашАйди:
        mainCategory = discord.utils.get(after.channel.guild.categories, id=ВашАйди)
        channel2 = await after.guild.create_voice_channel(name=f"Комната {member.display_name}",category=mainCategory)
        await member.move_to(channel2)
        await channel2.set_permissions(member,mute_members=True,move_members=True,manage_channels=True)
        def check(a,b,c):
            return len(channel2.members) == 0
        await Bot.wait_for('voice_state_update', check=check)
        await channel2.delete()
