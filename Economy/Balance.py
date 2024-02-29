import Main as main
@main.commands.command(
    aliases = [
        'wallet'
    ],
    description = 'Balance'
)
async def balance(
    context,
    user: main.discord.Member = None
):
    user = context.author if user == None else user
    balanceString = 'You have ' if user == context.author else user.mention + ' has '
    coins = main.storage.load()[
        str(
            user.id
        )
    ][
        'coins'
    ]
    balanceString += '{:,} coin.' if coins == 1 else '{:,} coins.'
    balanceTitle = 'Your Balance' if user == context.author else context.author.mention + '\'{} Balance'.format(
        '' if user.name.endswith(
            's'
        ) else 's'
    )
    await main.deletable(
        context,
        main.embed(
            context,
            {
                
            }
        )
    )
def setup(f):
    return