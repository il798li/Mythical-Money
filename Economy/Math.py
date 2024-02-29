import Main as main
@main.commands.command(
	name = 'math' ,
	description = 'Math' ,
	help = 'This will give you a random math problem to solve. If you solve it in 15 seconds, you wil a random amount of coins in between 50 and 150 inclusive.' ,
)
@main.commands.cooldown(
	1,
	15,
	main.commands.BucketType.user
)
async def math(
	context
):
	main.storage.register(
		context.author
	)
	profiles = main.storage.load(
		'JSON/Profiles.json'
	)
	class multiplication:
		name = 'Multiplication'
		string = 'multiplied by'
	class addition:
		name = 'Addition'
		string = 'plus'
	class subtraction:
		name = 'Subtraction'
		string = 'minus'
	operations = [
		multiplication,
		addition,
		subtraction,
	]
	operation = main.random.choice(
		operations
	)
	if operation == subtraction or operation == addition:
		number1 = main.random.randint(
			0,
			5000
		)
		number2 = main.random.randint(
			0,
			5000
		)
		answer = number1 - number2
		if operation == addition:
			answer += number2 * 2
	elif operation == multiplication:
		number1 = main.random.randint(
			0,
			25
		)
		number2 = main.random.randint(
			0,
			25
		)
		answer = number1 * number2
	embed = main.embed(
		context,
		operation.name,
		f'''What is {
			number1
		} ''' + operation.string + f''' {
			number2
		}? You have 15 seconds to answer this question.'''
	)
	try:
		message = await context.reply(
			embed = embed
		)
	except Exception:
		message = await context.send(
			embed = embed
		)
	messages = [
		context.message,
		message
	]
	def check(
		message
	):
		int_ = True
		try:
			content = int(
				message.content
			)
		except ValueError:
			int_ = False
		return message.author == context.author and message.channel == context.channel and int_ == True
	try:
		message_ = await main.mm.wait_for(
			'message',
			check = check,
			timeout = 15
		)
		if message_.content == str(
			answer
		):
			messages.append(
				message_
			)
			coins = main.random.randint(
				500,
				1500
			)
			profiles = main.storage.load(
				'JSON/Profiles.json'
			)
			profiles[
				str(
					context.author.id
				)
			][
				'coins'
			] += coins
			main.storage.dump(
				profiles,
				'JSON/Profiles.json'
			)
			await message_.reply(
				embed = main.embed(
					context,
					'Correct Answer',
					f'''Congratulations for answering the question correctly! You received {
						'{:,}' . format(coins)
					} coins!'''
				)
			)
		elif message_.content != str(
			answer
		):
			await message_.reply(
				embed = main.embed(
					context,
					'Incorrect Answer',
					f'Sorry, ' + context.author.mention + ', but that is not the answer. Better luck next time!'
				)
			)
	except main.asyncio.TimeoutError:
		messages.append(
			await context.reply(
				embed = main.embed(
					context,
					'Math Timeout',
					f'Sorry, ' + context.author.mention + ', but you didn\'t answer the question in time. Try again later.'
				)
			)
		)
def setup(
	mm
):
    mm.add_command(
        math
    )