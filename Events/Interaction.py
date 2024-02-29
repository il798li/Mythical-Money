import Main as main
@main.commands.Cog.listener()
async def on_interaction(
    interaction
):
    if interaction.type != main.discord.InteractionType.component or interaction.message.author.id != main.mm.user.id or interaction.custom_id != 'delete':
        return
    try:
        await interaction.response.send_message()
    except:
        pass
    deletables = main.storage.load(
        'JSON/Deletables.json'
    )
    try:
        messages = deletables[
            str(
                interaction.message.id
            )
        ]
    except KeyError:
        return
    message = await interaction.message.channel.fetch_message(
        messages[
            -1
        ]
    )
    if message.author.id == interaction.user.id:
        await interaction.message.delete()
        for id in deletables[
            str(
                interaction.message.id
            )
        ]:
            message = await interaction.message.channel.fetch_message(
                id
            )
            try:
                await message.delete()
            except:
                pass
    del deletables[
        str(
            interaction.message.id
        )
    ]
    main.storage.dump(
        deletables , 
        'JSON/Deletables.json'
    )
def setup(
    mm
):
    mm.add_listener(
        on_interaction
    )