import Main as main
@main.commands.command(
	aliases = [
		'set'
	],
	description = 'Server Settings'
)
async def settings(
	context,
	setting: str = '',
	value: str = ''
):
	if 'guild' not in context.__dir__():
		return await main.deletable(
			context,
			main.embed(
				'Server Settings Error',
				'Settings can only be viewed or edited in Discord servers!'
			)
		)
	setting = setting.lower()
	value = value.lower()
	prefix = value
	value_ = value
	settings = main.storage.load(
		'json/settings.json'
	)
	settings_ = settings[
		str(
			context.guild.id
		)
	].copy()
	if setting == 'prefix':
		if context.guild.owner_id != context.author.id and context.invoked_with != 'settings' and setting != 'view' and value != '':
			return await main.deletable(
				context,
				main.embed(
					context,
					'Prefix Management Error',
					'Only the owner of a server can edit my prefix. Please ask ' + context.guild.owner.mention + ' to change the prefix.'
				)
			)
		if prefix == None:
			return await main.deletable(
				context,
				main.embed(
					context,
					'Prefix Management Error',
					'You need to specify a valid prefix of at least 1 character!'
				)
			)
		if len(
			prefix
		) > 15:
			return await main.deletable(
				context,
				main.embed(
					context,
					'Prefix Management Error',
					'You cannot have a prefix that\'s over 15 characters.'
				)
			)
		value = value.lower()
		prefix_ = main.discord.utils.escape_markdown(
			value
		)
		if prefix.lower() == 'mm':
			name = 'Reset'
			value_ = 'I successfully reset my prefix for this server! Type \'__' + context.prefix + 'prefix <prefix>__\' to make a new one!'
		else:
			value_ = 'I successfully edited my prefix for this server! Type \'__' + prefix_ + ' settings prefix mm__\' to reset it!'
			name = 'Edition'
		await main.deletable(
			context,
			main.embed(
				context,
				'Successful Prefix ' + name,
				value_
			)
		)
	elif setting == 'compact':
		value = value.split()
		value = str(
			value[
				0
			]
		).lower()
		choices = {
			'on': True,
			'off': False,
			'true': True,
			'false': False
		}
		description = 'You cannot enable to disable compact mode for this server as you are not the owner!' if context.author.id != context.guild.owner_id and context.author.id not in main.mm.owner_ids else 'You must specify a valid value for enabling/disabling compact mode! You can choose from \'__true__,\' \'__false__,\' \'__on__,\' or \'__off__,\'' if value not in choices else ''
		if description != '':
			return await main.deletable(
				context,
				main.embed(
					context,
					'Compact Mode Error',
					description
				)
			)
		choice = choices[
			value
		]
		description = 'Compact mode has successfully been '
		description += 'activated!' if choice else 'deactivated!'
		description += ' Exact timings and contexts will be '
		description += 'shown' if choice else 'hidden'
		description += ' from now on.'
		await main.deletable(
			context,
			main.embed(
				context,
				'Compact Mode Activation' if choice else 'Compact Mode Deactivation',
				'Compact mode has been activated! Exact timings and contexts will be hidden from now on.' if choice else 'Compact mode has been deactivated! Exact timings and contexts will be shown from now on.'
			)
		)
		value = choice
	else:
		if context.invoked_with == 'settings' and setting == 'view' and value == '':
			return await main.deletable(
				context,
				main.embed(
					context,
					[
						'Compact Mode',
						'Command Prefix'
					],
					[
						'Compact mode is currently disabled. Type \'__' + main . discord.utils.escape_markdown(
							context.prefix
						) + ' settings compact true__\' to enable it.' if settings_ [
							'compact'
						] == False else ' Compact mode is currently enabled. Type \'__' + context.prefix + ' settings compact false__\' to disable it.',
						'My current prefix for this guild is \'__' + main.discord.utils.escape_markdown(
							settings_[
								'prefix'
							]
						) + '__.\' Type \'__' + main.discord.utils.escape_markdown(
							context.prefix
						) + context.invoked_with + ' prefix <prefix>__\' to change it.'
					]
				)
			)
		return await main.deletable(
			context,
			main.embed(
				context,
				'Settings Edition Error',
				'You must specify a valid setting to edit! You can pick from \'__compact\'__ for compact mode, or \'__prefix__\' to edit my command prefix.'
			)
		)
	settings[
		str(
			context.guild.id
		)
	][
		setting
	] = value
	main.storage.dump(
		settings,
		'json/settings.json'
	)
def setup(
	mm
):
	mm.add_command(
		settings
	)