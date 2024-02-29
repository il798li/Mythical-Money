import Main as main, json, Storage as storage
@main.commands.command(
	name = 'buy',
	description = 'Purchasing',
	aliases = [
		'purchase',
	]
)
async def buy(
	context,
	item = None,
	amount = '1'
):
	suffix = 'single' if amount == 1 or amount == 1.0 else 'plural'
	profiles = storage.load(
		'json/profiles.json'
	)
	prefix = main.discord.utils.escape_markdown(
		context.prefix
	)
	if item not in main.storage.shop:
		return await main.deletable(
			context,
			main.embed(
				context,
				'Purchasing Error',
				'You must specify a valid item to buy from my shop! Type \'__' + prefix + 'shop__\' to view it.'
			),
			deletable = True
		)
	if main.datetime.datetime.now(
		main.datetime.timezone(
			main.datetime.timedelta(
				hours = -7
			)
		)
	).month != 10 and item.lower() == 'candy':
		return await main.deletable(
			ctx,
			main.embed(
				ctx,
				'Purchasing Error',
				'You can only buy Candy Bags during the month of October!'
			),
			deletable = True
		)
	validAmount = amount.isnumeric()
	try:
		amount = int(
			amount
		)
		validAmount = amount >= 1
	except ValueError: 
		validAmount = False
	if validAmount == False:
		return await main.deletable(
			context,
			main.embed(
				context,
				'Purchasing Error',
				'You need to specify a valid positive numeric amount of this item to buy!'
			),
			deletable = True
		)
	item_ = main.storage.shop[
		item
	]
	buy = item_[
		'buy'
	]
	profile = profiles[
		str(
			context.author.id
		)
	]
	if profile['coins'] < buy * amount:
		return await main.deletable(
			context,
			main.embed(
				context,
				'Purchasing Error',
				'You need more coins to buy {} '.format(
					amount
				) + item_[
					suffix
				] + '!'
			),
			deletable = True
		)
	confirm = await main.confirm(
		context
	)
	if confirm.component == 'Cancel':
		return await main.deletable(
			context,
			main.embed(
				context,
				'Purchasing Cancellation',
				'You cancelled your purchase. You can always buy this item again if you want to.'
			),
			deletable = True,
			extra = confirm . message
		)
	profile[
		'inventory'
	][
		item
	] += amount
	profile[
		'coins'
	] -= buy * amount	
	storage.dump(
		profiles,
		'json/profiles.json',
	)
	await main.deletable(
		context,
		main.embed(
			context,
			'Successful Purchase',
			f'''You successfully bought {
				amount
			} {
				item_[
					suffix
				]
			} for {
				'{:,}'.format(
					amount * buy
				)
			} total coins!'''
		),
		deletable = True,
		extra = confirm.message
	)
def setup(
	mm
):
	mm.add_command(
		buy
	)