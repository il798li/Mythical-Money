if __name__ == '__main__':
    print(
        'Mythical Money is loading...'
    )
import discord, os, json, random, asyncio, datetime, math, time, Storage as storage
from discord.ext import commands, tasks
class toClass:
    def __init__(
        self,
        dictionary: dict
    ):
        print(
            type(
                self
            )
        )
        for key in dictionary:
            setattr(
                self,
                key,
                dictionary[
                    key
                ]
            )
def command_prefix(
    mm,
    message: discord.Message
) -> list:
    settings = storage.load(
        'JSON/Settings.json'
    )
    try :
        prefix = settings[
            str(
                message.guild.id
            )
        ][
            'prefix'
        ] if message.guild != None else 'mm'
    except KeyError:
        settings[
            str(
                message.guild.id
            )
        ] = {
            'prefix': 'mm',
            'compact': False
        }
        prefix = 'mm'
        storage.dump(
            settings,
            'JSON/Settings.json'
        )
    prefixes_ = [
        'mm ',
        prefix + ' ',
        prefix,
        'mm'
    ]
    prefixes = prefixes_.copy()
    for prefix in prefixes:
        if message.content.lower().startswith(
            prefix
        ) :
            prefixes_.append(
                message.content[
                    0:len(
                        prefix
                    )
                ]
            )
    return prefixes_
mm = commands.Bot(
    command_prefix = command_prefix,
    help_command = None,
    description = 'Welcome to Mythical Money, Discord\'s most advanced economy bot ever! Type \'mm help\' to view all commands.',
    intents = discord.Intents.all(),
    case_insensitive = True,
    owner_id = 655263219459293210
)
async def before_invoke(
    context
) :
    if type(
        context.command
    ) != discord.commands.core.SlashCommand:
        await context.channel.trigger_typing()
    storage.register(
        context.author
    )
@mm.before_invoke(
    before_invoke
)
async def before_invoke(
    context
):
    await before_invoke(
        context
    )
def embed(
    message,
    names,
    values = '',
    description: str = None,
):
    type_ = type(
        names
    )
    if type_ == str:
        names = [
            names
        ]
        values = [
            values
        ]
    elif type_ == dict:
        values = list(
            names.values()
        )
        names = list(
            names.keys()
        )
    try:
        compact = storage.load(
            'JSON/settings.json'
        )[
            str(
                message.guild.id
            )
        ][
            'compact'
        ]
    except Exception:
        compact = False
    type_ = type(
        message
    )
    if description == None:
        ending = 'direct messages.\n' if message.channel.type == discord.ChannelType.private or message.channel.type == discord.ChannelType.group else message.channel.mention + ' of **' + discord.utils.escape_markdown(
            message.guild.name
        ) + '**.\n'
        description = '_ _' if compact else 'This embed was requested by ' + message.author.mention + ' in ' + ending
        description = '' if compact == True else description
    for index in range(
        len(
            names
        )
    ):
        description += '\n**' + names[
            index
        ] + '**\n' + values[
            index
        ] + '\n'
    now = datetime.datetime.now(
        datetime.timezone(
            datetime.timedelta(
                hours = - 7
            )
        )
    )
    timestamp = round(
        now.timestamp()
    )
    if compact == False:
        description += '\nThis embed was sent <t:{}:R> on <t:{}:T> of <t:{}:D>.'.format(
            timestamp,
            timestamp,
            timestamp
        )
    embed = discord.Embed()
    embed.title = None if compact else '**Mythical Money**'
    embed .color = 0x5865f2
    embed.description = description
    return embed
for folder in [
    'Commands',  
    'Economy',
    'Events',
    'Slash Commands'
]:
    for file in os.listdir(
        './' + folder
    ):
        if file.endswith(
            '.py'
        ):
            mm.load_extension(
                folder + '.' + file[
                    0 : -3
                ]
            )
            print(
                'Mythical Money has loaded ' + folder + '/' + file + '...'
            )
def check(
    context
) -> bool:
    
    return context.author.id not in json.load(
        open(
            'JSON/blacklisted.json'
        )
    )[
        'blacklisted'
    ]
for command in mm.walk_commands():
    command.update(
        enabled = True
    )
async def deletable(
    context,
    embed: discord.Embed,
    hidden: bool = True,
    content: str = '',
    deletable: bool = False,
    components: list = [],
    extra = []
) -> discord.Message:
    extra = extra.copy()
    contextMessage = context.message if type(
        context
    ) == commands.Context else context if type(
        context
    ) == discord.Message else None
    if context.author.bot:
        return
    extra = [
        extra
    ] if type(
        extra
    ) != list else extra
    extra.append(
        context if type(
            context
        ) == discord.Message else context.message
    )
    components = components.copy()
    view = discord.ui.View()
    for component_ in components:
        view.add_item(
            component_
        )
    if deletable:
        view.add_item(
            discord.ui.Button(
                style = discord.ButtonStyle.primary,
                label = 'Delete',
                custom_id = 'delete'
            )
        )
    if 'slash' in str(
        type(
            context
        )
    ).lower():
        return await context.respond(
            content,
            embed = embed
        )
    try:
        message = await context.reply(
            content,
            embed = embed,
            view = view
        )
    except Exception:
        try:
            message = await context.channel.send(
                content,
                embed = embed,
                view = view
            )
        except Exception:
            message = await context.author.send(
                content,
                embed = embed,
                view = view
            )
    if deletable == False:
        return message
    deletables = storage.load(
        'JSON/Deletables.json'
    )
    extra_ = []
    for message_ in extra:
        if str(
            message.id
        ) not in open(
            'JSON/Deletables.json'
        ).read():
            extra_.append(
                message_.id
            )
    deletables[
        str(
            message.id
        )
    ] = extra_
    return storage.dump(
        deletables,
        'JSON/Deletables.json'
    )
async def confirm(
    context: commands.Context
):
    if context.author.bot:
        return
    def components(
        disabled: bool = False
    ):
        components = [
            discord.ui.Button(
                label = 'Confirm',
                style = ButtonStyle.blue,
                custom_id = '',
                disabled = disabled
            ),
            discord.ui.Button(
                label = 'Cancel',
                style = ButtonStyle.blue,
                custom_id = '',
                disabled = disabled
            )
        ]
        if disabled:
            return ActionRow(
                components
            )
        return components
    embed_ = embed(
        context,
        context.command.description + ' Confirmation',
        'Are you sure you want to complete this operation? Click on a button below to register a decision.'
    )
    confirmation = await deletable(
        context,
        embed_,
        components = components()
    )
    try:
        confirmation = confirmation
    except Exception:
        return 'error'
    while True:
        interaction = await mm.wait_for(
            'button_click',
        )
        if interaction.user.id == context.author.id:
            await confirmation.edit(
                embed = embed_,
                components = components(
                    True
                )
            )
            class data:
                component = interaction.component.label
                message = confirmation
            return data
def numberSuffix(
    number: int
) -> str:
    number = str(
        number
    )
    last = number[
        -1
    ]
    last_ = number[
        -2
    ] if len(
        number
    ) > 1 else None
    return number + 'th' if last in '0456789' or last_ == '1' else number + 'st' if last == '1' else number + 'nd' if last == '2' else number + 'rd'
mm.run(
    open(
        'Token.txt'
    ).read()
)