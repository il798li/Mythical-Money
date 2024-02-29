import Main as main
@main.commands.command(
	name = 'shop',
	aliases = [
		'store'
	],
	description = 'Shop Viewer',
	help = 'The above command will show you all the things you can buy from my shop as well as their cost and exact command to buy them.'
)
async def shop(
	context
):
	names = [
		context.prefix + 'buy ' + item + ' [amount]\n' + context.prefix + 'purchase ' + item + ' [amount]' for item in main.storage.shop
	]
	values = []
	for item in main.storage.shop:
		buyable = main.storage.shop[
			item
		]
		values.append(
			f'''This will let you buy some {
				buyable[
					'plural'
				]
			} for {
				'{:,}'.format(
					buyable[
						'buy'
					]
				)
			} coins each.'''
		)
	await main.deletable(
		context,
		main.embed(
			context,
			names,
			values
		)
	)
def setup(
	mm
):
	mm.add_command(
		shop
	)