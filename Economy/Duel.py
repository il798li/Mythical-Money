import Main
@Main.commands.command(
	name = 'duel',
	aliases = [
		'1v1',
		'fight',
		'battle',
	],
	description = 'Battling'
)
async def duel(
	context,
	member: Main.discord.Member = None
):
	Main.storage.register(
		context.author
	)
	if member == None:
		return await Main.deletable(
			context,
			Main.embed(
				context,
				'Battling Error',
				'You must specify a valid member to battle!'
			)
		)
	if member.bot:
		return await Main.deletable(
			context,
			Main.embed(
				context,
				'Battling Error',
				'You cannot battle against Discord bots!'
			)
		)
	Main.storage.register(
		member
	)
	profiles = Main.storage.load(
		'json/profiles.json'
	)
	home = profiles[
		str(
			context.author.id
		)
	].copy()
	guest = profiles[
		str(
			member.id
		)
	].copy()
	if member.id == context.author.id:
		return await Main.deletable(
			context,
			Main.embed(
				context,
				'Battling Error',
				'You can\'t battle yourself, it would be unnecessarily painful!'
			)
		)
	message = await Main.deletable(
		context,
		Main.embed(
			context,
			'Battling Confirmation',
			member.mention + ', would you like to duel ' + context.author.mention + ' for fun? No coins or other rewards will be given to the winner of this battle.'
		)
	)
	for emoji in '✅❌':
		await message.add_reaction(
			emoji
		)
	def check(
		reaction,
		user
	):
		return emoji in '✅❌' and user == member and reaction.message == message
	reaction, user = await Main.mm.wait_for(
		'reaction_add',
		check = check
	)
	if reaction.emoji == '❌':
		return await Main.deletable(
			message,
			Main.embed(
				context,
				'Battling Declination',
				'This battle request was declined. You may redo this command with a different user if you wish.'
			)
		)
	preperation = await Main.deletable(
		message,
		Main.embed(
			context,
			'Battling Preparation',
			'Please take the time to read the instructions while I prepare the battle: Both battlers must send messages to hit the other player. The message\'s text doesn\'t matter.'
		)
	)
	home_armor = home[
		'armor'
	]
	guest_armor = guest[
		'armor'
	]
	guest_weapon = guest[
		'tools'
	][
		'weapon'
	]
	home_health = 0
	for item in home_armor:
		home_health += home_armor[
			item
		][
			'health'
		]
	guest_health = 0
	for item in guest_armor:
		guest_health += guest_armor[
			item
		][
			'health'
		]
	home_defense = 1
	for item in home_armor:
		home_defense *= home_armor[
			item
		][
			'defense'
		]
	guest_defense = 1
	for item in guest_armor:
		guest_defense *= guest_armor[
			item
		][
			'defense'
		]
	guest_defense *= 100
	home_defense *= 100
	try:
		home_defense = int(
			home_defense
		)
	except Exception:
		pass
	try:
		home_defense = int(
			home_defense
		)
	except Exception:
		pass
	home_weapon = home[
		'tools'
	][
		'weapon'
	]
	home_damage = home_weapon[
		'damage'
	]
	guest_damage = guest_weapon[
		'damage'
	]
	guest_defense = 100 - round(
		guest_defense,
		6
	)
	home_defense = 100 - round(
		home_defense,
		6
	)
	print(
		home_defense
	)
	print(
		guest_defense,
		home_defense
	)
	def embed(
		home_health: float,
		home_defense: float,
		home_damage: float,
		guest_health: float,
		guest_defense: float,
		guest_damage: float
	):
		return Main.embed(
			context,
			[
				'Battling Arena',
				'@' + str(
					context.author
				) + '\'s Info',
				'@' + str(
					member
				) + '\'s Info'
			],
			[
				'Start sending random messages to hit the other player! All hits will go through their target\'s Damage Reduction before inflicting on the target.',
				context.author.mention + f''' has {
					home_health
				} Health, {
					home_defense
				}% Damage Reduction, and {
					home_damage
				} damage per hit.''',
				member.mention + f''' has {
					guest_health
				} Health, {
					home_defense
				}% Damage Reduction, and {
					guest_damage
				} damage per hit.'''
			]
		)
	try:
		battle = await preperation.reply(
			embed = embed(
				home_health,
				home_defense,
				home_damage,
				guest_health,
				guest_defense,
				guest_damage
			)
		)
	except Exception:
		battle = await preperation.channel.send(
			embed = embed(
				home_health,
				home_defense,
				home_damage,
				guest_health,
				guest_defense,
				guest_damage
			)
		)
	def check(
		message
	):
		return message.author.id in [
			context.author.id,
			member.id
		] and message.channel == context.channel
	while True:
		hit = await Main.mm.wait_for(
			'message',
			check = check
		)
		if hit.author == context.author:
			damage = home_damage
			factor = guest_defense / 100
			factor = 1 - factor
			guest_health -= damage * factor
		elif hit.author == member:
			damage = guest_damage
			factor = home_defense / 100
			factor = 1 - factor
			home_health -= damage * factor
		if guest_health <= 0 or home_health <= 0:
			break
		await battle.edit(
			embed = embed(
				home_health,
				home_defense,
				home_damage,
				guest_health,
				guest_defense,
				guest_damage
			)
		)
		try:
			await hit.delete()
		except Exception:
			pass
	if guest_health == 0:
		description = 'Congratulations to ' + member.mention + ' for winning this duel!'
	elif home_health == 0:
		description = 'Congratulations to ' + context.author.mention + ' for winning this duel!'
	await battle.reply(
		embed = Main.embed(
			hit,
			'Battling Victory',
			description
		)
	)
def setup(
	mm
):
	mm.add_command(
		duel
	)