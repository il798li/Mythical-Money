import Storage, Main
@Main.commands.Cog.listener()
async def on_guild_add(
	guild
):
	settings = Storage.load(
		'JSON/Settings.json'
	)
	settings[
		str(
			guild.id
		)
	] = {
		'prefix': 'mm',
		'compact': False
	}
	Storage.dump(
		settings,
		'JSON/Settings.json'
	)
	for user in guild.users:
		Storage.register(
			user
		)
	await Main.refresh.refresh(
		Main.mm
	)
def setup(
	mm
):
	mm.add_listener(
		on_guild_add
	)