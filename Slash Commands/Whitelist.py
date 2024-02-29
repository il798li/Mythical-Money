import Main
@Main.discord.commands.slash_command(
	name = 'whitelist',
	guild_ids = [
		834113328459677747
	],
	description = 'Whitelists a user to allow them to continue using Mythical Money'
)
async def whitelist(
	context,
	identification
):
	properUser = True
	try:
		user = Main.mm.get_user(
			int(
				identification
			)
		)
		properUser = user != None
	except Exception:
		properUser = user = False
	if context.author.id != 751533372890677398 and context.author.id != 655263219459293210:
		return await Main.deletable(
			context,
			Main.embed(
				context,
				'Whitelisting Error',
				'Only my owner can whitelist users from Mythical Money! Please report this if you feel that ' + user.mention + ' does not deserve to be blacklisted'
			)
		)
	if properUser == False:
		return await Main.deletable(
			context,
			Main.embed(
				context,
				'Whitelisting Error',
				'You must specify a valid user identification to whitelist them!'
			)
		)
	blacklisted = Main.storage.load(
		'json/blacklisted.json'
	)
	blacklisted_ = blacklisted[
		'blacklisted'
	]
	if blacklisted_ != []:
		for index in range(
			len(
				blacklisted
			)
		):
			if blacklisted_[
				index - 1
			] == identification:
				try:
					blacklisted_.remove(
						index - 1
					)
				except Exception:
					blacklisted_.remove(
						identification
					)
		Main.storage.dump(
			blacklisted,
			'json/blacklisted.json'
		)
	await Main.deletable(
		context,
		Main.embed(
			context,
			'Successful User Whitelist',
			user.mention + ' was whitelisted from Mythical Money. They will be able to use commands like normal.'
		)
	)
def setup(
	mm
):
	mm.add_application_command(
		whitelist
	)