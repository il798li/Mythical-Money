import Main as main
@main.commands.Cog.listener()
async def on_command_error(
	context,
	error
):
	if isinstance(
		error,
		main.commands.CheckFailure
	):
		await main.deletable(
			context,
			main.embed(
				context,
				'Command Error',
				'You are blacklisted from using Mythical Money! Please contact my owner at https://top.gg/servers/834113328459677747 if you believe this is a mistake.'
			)
		)
	elif isinstance(
		error,
		main.commands.CommandNotFound
	):
		if context.message.content in main.command_prefix(
			main.mm,
			context.message
		):
			return
		try:
			await context.message.add_reaction(
				'❌'
			)
			def check (
				reaction: main.discord.Reaction,
				user: main.discord.User
			) -> bool :
				return reaction.emoji == '❌' and user.id == context.author.id and reaction.message.id == context.message.id
			await main.mm.wait_for(
				'reaction_add',
				check = check
			)
			await context.message.remove_reaction(
				'❌',
				main.mm.user
			)
			await context.message.remove_reaction(
				'❌',
				context.author
			)
			return
		except Exception:
			return
	if isinstance(
		error,
		main.commands.MissingRequiredArgument
	):
		await main.deletable(
			context,
			main.embed(
				context,
				context.command.description + ' Error',
				'You are missing a required argument!'
			)
		)
	elif isinstance(
		error,
		main.commands.CommandOnCooldown
	):
		await main.deletable(
			context ,
			main.embed(
				context ,
				context . command.description + ' Error',
				f'Sorry, ' + context.author.mention + ', but you did this too recently. Try again in ' + '{:,}'.format(
					round(
						error.retry_after,
						3
					)
				) + ' seconds.'
			),
			deletable = True
		)
	elif isinstance(
		error,
		main.commands.MemberNotFound
	):
		await main.deletable(
			context,
			main.embed(
				context,
				context.command.description + ' Error',
				'I could not find this member in this server! Please try again.'
			)
		)
	elif isinstance (
		error,
		(
			main.commands.BotMissingPermissions,
			main.commands.DisabledCommand
		)
	):
		return
	else :
		await main.deletable(
			context,
			main.embed(
				context ,
				[
					'Unknown Error' ,
					'Error Value'
				] ,
				[
					f'An unknown error occured and it has been reported to my owner. If it doesn\'t get resolved soon, please contact him via my support server at https://www.mythical-mohey.tk/server/. Thanks for using Mythical Money!',
					'```console\n' + str(
						error
					) + '```'
				]
			),
			deletable = True
		)
		print(error,dir(error))
		raise error
		if context.author.id != 655263219459293210:
			embed = main.embed(
				context,
				[
					'Unexpected Error'
				],
				[
					'```console\n' + str(
						error
					) + '```'
				]
			)
			for identification in main.mm.owner_ids:
				user = main.mm.get_user(
					identification
				)
				await user.send(
					embed = embed
				)
		raise error
def setup(
	mm
):
	mm.add_listener(
		on_command_error
	)