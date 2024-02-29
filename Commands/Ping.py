import Main as main
@main.commands.command(
    aliases = [
        'latency'
    ],
    enabled = True
)
async def ping(
    context
):
    latency = round(
        context.bot.latency * 1000000
    )
    embed = main.embed(
        context,
        names = {
            'Latency': 'I am currently responding to commands {:,}'.format(
                latency
            ) + ' microseconds after they are sent.'
        }
    )
    await main.deletable(
        context,
        embed,
        deletable = True
    )
def setup(
    mm
):
    mm.add_command(
        ping
    )