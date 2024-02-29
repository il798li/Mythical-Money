import Main as main
@main.commands.command(
    name = 'inventory',
    description = 'Inventory Viewer'
)
async def inventory(
    context,
    member: main.discord.Member = None
):
    if member != None:
        if member.id == context.author.id:
            member = None
    prefix = 'You have ' if member == None else member.mention + ' has '
    member = main.storage.load(
        'json/profiles.json'
    )[
        str(
            member.id if member != None else context.author.id
        )
    ]
    inventory = member[
        'inventory'
    ]
    fields = {
        'Coins': prefix + '{:,}'.format(
            member[
                'coins'
            ]
        ) + ' coins.'
    }
    for item in main.storage.shop:
        if 'candy' in item.lower():
            continue
        amount = inventory[
            item
        ]
        fields[
            main.storage.shop[
                item
            ][
                'plural'
            ].title()
        ] = prefix + '{:,}'.format(
            amount
        ) + ' ' + main.storage.shop[
            item
        ][
            'plural' if amount != 1 else 'single'
        ] + '.'
    await main.deletable(
        context,
        main.embed(
            context,
            fields
        ),
        deletable = True
    )        
def setup(
    mm
):
    mm.add_command(
        inventory
    )