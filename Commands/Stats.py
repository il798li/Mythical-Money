import Main
@ Main.commands.command(
	name = 'stats',
	aliases = [
		'statistics'
	]
)
async def stats(
	context
) :
	await Main.deletable(
		context ,
		Main.embed(
			context,
			[
				'Guilds',
				'Users',
				'Birthday',
				'Latency'
			],
			[
				f'''Including **{
					context.guild.name
				}**, I am currently participating in {
					len(
						await Main.mm.fetch_guilds(
							limit = None
						).flatten()
					)
				} guilds.''',
				f'''Including bots, I am currently used by {
					'{:,}'.format(
						len(
						    Main.mm.users
					    ) - 1
					)
				} total Discord users.''',
				'I was created <t:1600780399:R> at <t:1600780399:T> of <t:1600780399:D>.',
				f'''I am currently responding to commands approximately {
					'{:,}'.format(
						round(
							Main.mm.latency * 1000000,
							3
						)
					)
				} microseconds after they are sent.'''
			]
		),
		deletable = True
	)
def setup(
	mm
):
	mm.add_command(
		stats
	)