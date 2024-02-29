import Main as main, Refresh
@main.commands.slash_command(
    name = 'refresh',
    guild_ids = [
        834113328459677747
    ],
    description = 'Refreshes Mythical Money and resets any cached data.'
)
async def refresh(
    context,
    register: bool = False
):
    await context.defer(
        ephemeral = True
    )
    await Refresh.refresh(
        main.mm,
        register
    )
    await context.respond(
        '_ _',
        ephemeral = True
    )
def setup(
    mm
):
    mm.add_application_command(
        refresh
    )