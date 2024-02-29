import Main as main, Storage as storage
@main.commands.command(
	name = 'craft',
	description = 'Crafting',
	aliases = [
		'make',
		'build'
	]
)
async def craft(
	ctx,
	*,
	item = ''
):
	item = item.lower()
	main.storage.register(
		ctx.author
	)
	profiles = storage.load(
		'json/profiles.json'
	)
	try:
		item_ = main.storage.craftables[
			item
		]
	except KeyError:
		return await main.deletable(
			ctx,
			main.embed(
				ctx,
				'Crafting Error',
				'You must specify a valid item to craft.'
			)
		)
	properIngredients = True
	recipe = item_[
		'recipe'
	]
	profile = profiles[
		str(
			ctx.author.id
		)
	]
	inventory = profile[
		'inventory'
	]
	for item__ in recipe:
		if recipe[
			item__
		] > inventory[
			item__
		]:
			properIngredients = False
	if properIngredients == False:
		return await main.deletable(
			ctx,
			main.embed(
				ctx,
				'Crafting Error',
				'You do not have the required materials to craft this item!'
			)
		)
	destination = item_[
		'destination'
	]
	for item__ in recipe:
		inventory[
			item__
		] -= recipe[
			item__
		]
	destination_0_ = destination[
		0
	]
	destination_1_ = destination[
		1
	]
	if destination_0_ == 'armor':
		profile[
			destination_0_
		][
			destination_1_
		] = {
			'name': item_[
				'name'
			],
			'health': item_[
				'health'
			],
			'defense': item_[
				'defense'
			]
		}
	elif destination_0_ == 'tools':
		profile[
			destination_0_
		][
			destination[
				1
			]
		] = {
			'name': item_[
				'name'
			],
			'chances': item_[
				'chances'
			],
			'entities': item_[
				'entities'
			]
		}
		if destination_1_ == 'weapon':
			profile[
				destination_0_
			][
				'weapon'
			][
				'damage'
			] = item_[
				'damage'
			]
	storage.dump(
		profiles,
		'json/profiles.json'
	)
	await main.deletable(
		ctx,
		main.embed(
			ctx,
			'Crafting Success',
			'You successfully crafted and equipped a ' + item_[
				'name'
			] + '!'
		)
	)
def setup(
	mm
):
	mm.add_command(
		craft
	)