import Main
@Main.commands.command(
	name = 'usage',
	description = 'Usage Reference',
	aliases = [
		'recipes'
	]
)
async def recipes(
	context,
	item = ''
):
	if item not in Main.storage.shop:
		return await Main.deletable(
			context,
			Main.embed(
				context,
				{
					'Usage Reference Error': 'You need to provide a valid item to view the recipes for!'
				}
			)
		)
	prefix = Main.discord.utils.escape_markdown(
		context.prefix
	)
	names = []
	values = []
	for craftable in Main.storage.craftables:
		craftable_ = Main.storage.craftables[
			craftable
		].copy()
		if item in craftable_[
			'recipe'
		]:
			names.append(
				prefix + ' craft ' + craftable + '\n' + prefix + ' make ' + craftable
			)
			values.append(
				f'''This will let you craft a {
					craftable_[
						'name'
					]
				} for {
					'{:,}'.format(
						craftable_[
							'recipe'
						][
							item
						]
					)
				} {
					Main.storage.shop[
						item
					][
						'plural'
					]
				}. Type \'__{
					prefix
				}recipe {
					craftable.lower()
				}__\' to view the full recipe for this item.'''
			)
	if names != []:
		return await Main.deletable(
			context,
			Main.embed(
				context,
				names,
				values
			)
		)
	await Main.deletable(
		context,
		Main.embed(
			context,
			'Usage Reference Error',
			f'''So far, none of my craftable items require any amount of {
				Main.storage.shop[
					item
				][
					'plural'
				]
			}. This item will later have some recipes.'''
		)
	)
def setup(
	mm
):
	mm.add_command(
		recipes
	)