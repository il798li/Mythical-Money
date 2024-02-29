import Storage as storage, discord, threading
from discord.ext import commands, tasks
def numberSuffix(
	number: int
):
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
	return number + 'th' if last in '0456789' or last_ == '1' else number + 'st' if last == '1' else number +  'nd' if last == '2' else number + 'rd'
async def refresh(
	mm: commands.Bot,
	register: bool = False
):
	print(
		'@' + mm.user.name + '#' + mm.user.discriminator + ' is loading...'
	)
	guilds = await mm.fetch_guilds(
		limit = None
	).flatten()
	guilds_ = len(
		guilds
	)
	string = f'''\'mm help\' in {
		guilds_
	} servers with ''' + '{:,}'.format(
		round(
			mm.latency * 1000000,
			3
		)
	) + ' microseconds of latency...'
	await mm.change_presence(
		activity = discord.Activity(
			type = discord.ActivityType.listening,
			name = string
		)
	)
	storage.dump(
		{
			'guilds': str(
				guilds_
			),
			'latency': '{:,}'.format(
				round(
					mm.latency * 1000000,
					3
				)
			),
			'user': mm.user.name + '#' + mm.user.discriminator,
			'users': '{:,}'.format(
					len(
					mm.users
				)
			)
		},
		'JSON/Stats.json'
	)
	settings = storage.load(
		'json/settings.json'
	)
	for guild in guilds:
		guild_id = str(
			guild.id
		)
		if guild_id in settings:
			continue
		settings[
			guild_id
		] = {
			'prefix': 'mm',
			'compact': False
		}
	storage.dump(
		settings,
		'json/settings.json'
	)
	if register:
		for user in mm.users:
			if storage.register(
				user
			) == 'Registered user!':
				print(
					'@' + mm.user.name + '#' + mm.user.discriminator + ' has registered @' + user.name + '#' + user.discriminator + '.'
				)
	print(
		'@' + mm.user.name + '#' + mm.user.discriminator + ' is listening to ' + string
	)