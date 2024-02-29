import Main as main
@main.commands.command(
	name = 'help',
	aliases = [
		'intro',
	],
	description = 'Help'
)
async def help(
	context
):
	prefix = main.discord.utils.escape_markdown(
		context.prefix
	)
	await main.deletable(
		context,
		main.embed(
			context,
			{
				prefix + 'extra': 'The above command will let you view my miscellaneuous commands that don\'t involve my money system.',
				prefix + 'money\n' + prefix + 'mm\n' + prefix: 'The above commands will let you view all my commands that involve interacting with your profile in my money system.'
			}
		),
		deletable = True
	)
def setup(
	mm
):
	mm.add_command(
		help
	)