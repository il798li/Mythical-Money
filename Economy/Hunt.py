import Main as main, Storage as storage
@main.commands.command(
	name = 'hunt',
	description = 'Hunting',
	help = 'This will let you hunt some monsters. You must have a weapon to do this.'
)
@main.commands.cooldown(
	1,
	15,
	main.commands.BucketType.user
)
async def hunt(
	context
):
	profiles = main.storage.load(
		'json/profiles.json'
	)
	profile = profiles[
		str(
			context.author.id
		)
	]
	weapon = profile[
		'tools'
	][
		'weapon'
	]
	chances = weapon[
		'chances'
	]
	mobsDictionary = {
		'zombie': 0,
		'ghost': 0,
		'vampire': 0,
		'blazer': 0
	}
	mobsList = []
	for mob in chances:
		for loop in range(
			chances[
				mob
			]
		):
			mobsList.append(mob)
	for loop in range(
		weapon[
			'entities'
		]
	):
		mobsDictionary[
			main.random.choice(
				mobsList
			)
		] += 1
	profile = profiles[
		str(
			context.author.id
		)
	]
	for mob in mobsDictionary:
		mob_ = main.storage.mobs[
			mob
		]
		profile[
			'inventory'
		][
			mob_[
				'drops'
			]
		] += 1
		profile[
			'coins'
		] += mob_[
			'coins'
		]
	main.storage.dump(
		profiles,
		'json/profiles.json'
	)
	values = []
	for mob in mobsDictionary:
		mob_ = mobsDictionary[
			mob
		]
		suffix = 'plural' if mob_ != 1 else 'single'
		suffix_ = 's' if suffix == 'plural' else ''
		values.append(
			'You killed ' + '{:,}'.format(
				mob_
			) + ' ' + mob.title() + suffix_ + ' and received ' + str(
				mob_
			) + ' ' + storage.shop[
				storage.mobs[
					mob
				][
					'drops'
				]
			][
				suffix
			] + '!'
		)
	await main.deletable(
		context,
		main.embed(
			context.message,
			[
				'Zombies' ,
				'Ghosts' ,
				'Vampires' ,
				'Blazers'
			],
			values
		),
        deletable = True
	)
def setup(
	mm
):
	mm.add_command(
		hunt
	)