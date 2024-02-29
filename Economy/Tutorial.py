import Main
@Main.commands.command(
    name = 'tutorial',
)
async def tutorial(
    context
):
    await Main.deletable(
        context,
        Main.embed(
            context.message,
            {
                'Tutorial': 'Welcome to the Mythical Money tutorial! Here, you will learn how to use all available tools to maximize your wealth.'
            }
        ),
        deletable = False,
        components = [
            Main.discord.ui.Button(
                style = Main.discord.ButtonStyle.primary,
                label = 'Abort',
                custom_id = 'Abort'
            )
        ]
    )
def setup(
    mm
):
    mm.add_command(
        tutorial
    )