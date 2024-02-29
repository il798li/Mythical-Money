import Main
@Main.commands.command(
	name = 'credits'
)
async def credits(
	context
):
	await Main.deletable(
		context,
		Main.embed(
			context,
			{
				'Developer': 'I was created and programmed by @il798li#3336.',
				'Teachers': '@{}, @{}, and @{} were the 3 people that taught my creator how to program Discord bots.'.format(
					Main.mm.get_user(
						697535361315766322
					),
					Main.mm.get_user(
						697913907528073296
					),
					Main.mm.get_user(
						475315771086602241
					)
				)
			}
		),
		deletable = True
	)
def setup(
	mm
):
	mm.add_command(
		credits
	)