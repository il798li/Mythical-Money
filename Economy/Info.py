import Main, Storage
@Main.commands.command(
    description = 'Item Info',
    help = 'This command will show you all information about an item to help you decide what you need to advance in Mythical Money.'
)
async def info(
    context,
    *,
    item: str = None
):
    if item == None:
        return await Main.deletable(
            context,
            Main.embed(
                context.message,
                {
                    'Item Info Error': 'You must specify a valid item to view its info!'
                }
            ),
            deletable = True
        )
    try:
        item = Storage.craftables[
            item.lower()
        ]
    except:
        return await Main.deletable(
            context,
            Main.embed(
                context.message,
                {
                    'Item Info Error': 'There are no craftable items that are named __' + item + '__!'
                }
            )
        )
    item = Main.toClass(
        item
    )
    try:
        chances = item.chances
        print(chances)
        itemType = 'tool'
    except:
        itemType = 'armor'
    
    if itemType == 'tool':
        fields = {
            'Damage': 'The ' + item.name + ' deals ' + str(
                item.damage
            ) + ' damage per hit during duels.',
            'Recipe': 'The ' + item.name + ' can be crafted from ' + str(
                item.recipe[
                    list(
                        item.recipe.keys()
                    )[
                        0
                    ]
                ]
            ) + ' ' + Storage.shop[
                list(
                    item.recipe.keys()
                )[
                    0
                ]
            ][
                'plural'
            ] + '.'
        }
    await Main.deletable(
        context,
        Main.embed(
            context,
            names = fields,
        ),
        deletable = True
    )
    
def setup(
    mm
):
    mm.add_command(
        info
    )