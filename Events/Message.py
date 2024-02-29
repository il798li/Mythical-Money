import Main
@Main.commands.Cog.listener()
async def on_message(
	message
):
	Main.storage.register(
		message.author
	)
	command_prefix = Main.command_prefix(
		Main.mm,
		message
	)
	if message.guild == None:
		prefix = 'mm'
	else:
		if message.content in command_prefix:
			prefix = message.content
		for item in command_prefix:
			if message.content in [
				item + 'mm',
				item + 'money'
			]:
				prefix = item
		if message.content == '<@758058370271019059>' or message.content == '<@!758058370271019059>':
			prefix = Main.storage.load(
				'JSON/Settings.json'
			)[
				str(
					message.guild.id
				)
			][
				'prefix'
			]
	try:
		prefix = Main.discord.utils.escape_markdown(
			prefix
		) + ' '
	except Exception:
		return
	await Main.deletable(
		message,
		Main.embed(
			message,
			{
				prefix + 'shop\n' + prefix + 'store': 'The above command will show you all the things you can buy from my shop as well as their cost and exact command to buy them.',
				prefix + 'buy <item> [amount]\n' + prefix + 'purchase <item> [amount]': 'The above command will make you buy an item for the specified amount.',
				prefix + 'inventory': 'The above command will show you how many of each base item you have in your inventory.',
				prefix + 'craft <item>\n' + prefix + 'make <item>\n' + prefix + 'build <item>': 'The above commands will let your combine items in your inventory to build tools and/or armor. Old items will be overridden, meaning that a Starter Helmet can be replaced (without confirmation) with a Ghost Helmet.',
				prefix + 'recipe <item>': 'This will let you view an item\'s recipe. It must be a valid craftable item!',
				prefix + 'recipes <item>\n' + prefix + 'usage <item>': 'The above command will show you all craftables items that require at least 1 of your specifed item.',
				prefix + 'donate <member> <coins>\n' + prefix + 'give <member> <coins>': 'The above commands will let you show your kindness by giving your coins away to someone else __without a confirmation message__. No taxes will be issued on this command.',
				prefix + 'gamble <amount>\n' + prefix + 'bet <amount>': 'The above commands will let your gamble some of your coins to either lose or gain more. Your chances of victory and loss are equal, and you will either gain or lose your specifed amount in coins.',
				prefix + 'giveaway <amount> <time>\n' + prefix + 'raffle <amount> <time>': 'The above command will let you giveaway some coins to a random winner. You can customize the time by suffixing it with \'__s__\', \'__m__\', \'__h__\', \'__d__\', or \'__y__\' for seconds, minutes, hours, days, or years respecitively. The amount is the number of coins given from you to the winner at the end. Please make sure you really want to do this as the coins will automatically be given.',
				prefix + 'hunt': 'The above command lets you hunt monsters for extra coins and money.',
				prefix + 'chop': 'The above command will let you use your axe to chop wood and gain money.',
				prefix + 'math': 'The above command gives you a math problem to solve. If you give the right answer within 15 seconds, you will receive and random amount of coins between 500 and 1,500.',
				prefix + 'duel <member>\n' + prefix + '1v1 <member>\n' + prefix + 'battle <member>\n' + prefix + 'fight <member>': 'The above command will let you duel an opponent for fun. Better stats will increase your chance of victory. These fights will only be for fun, and not be recorded anywhere.'
			}
		),
		deletable = True
	)
def setup(
	mm
):
	mm.add_listener(
		on_message
	)