import Main as main
@main.commands.slash_command(
	name = 'blacklist',
	guild_ids = [
		834113328459677747
	],
	description = 'Blacklists a user from using Mythical Money.'
)
async def blacklist(
	context,
	identification: str
):
	print(context, '\n', type(context))
	user = main.mm.get_user(
		int(
			identification
		)
	)
	if user == None and context.author.id != 751533372890677398 and context.author.id != 655263219459293210:
		return await main.deletable(
			context,
			main.embed(
				context,
				'Blacklisting Error',
				'You must specify a valid user to blacklist!'
			)
		)
	if context.author.id != 751533372890677398 and context.author.id != 655263219459293210:
		return await main.deletable(
			context,
			main.embed(
				context,
				'Blacklisting Error',
				'Only <@655263219459293210> can blacklist users from Mythical Money! Please report ' + user.mention + ' if you feel they are breaking any of my rules.'
			)
		)
	if user == None:
		return await main.deletable(
			context,
			main.embed(
				context,
				'Blacklisting Error',
				'You must specify a valid member to blacklist.'
			)
		)
	blacklisted = main.storage.load(
		'JSON/Blacklisted.json'
	)
	blacklisted[
		'blacklisted'
	].append(
		identification
	)
	main.storage.dump(
		blacklisted,
		'JSON/Blacklisted.json'
	)
	await main.deletable(
		context,
		main.embed(
			context,
			'Successful User Blacklist',
			user.mention + ' was blacklisted from Mythical Money. Until whitelisted, they will be unable to run any commands.'
		)
	)
def setup(
	mm
):
	mm.add_application_command(
		blacklist
	)