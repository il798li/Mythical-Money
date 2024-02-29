import Main as main
@main.commands.Cog.listener()
async def on_command(
	context
):
	if context.guild == None:
		location = 'direct messages.'
	else:
		location = context.channel.mention + '/#' + context.channel.name + ' of **' + context.guild.name + '**.' 
	await main.mm.get_channel(
		838936689635491910
	).send(
		embed = main.embed(
			context,
			{
                main.discord.utils.escape_markdown(
                    context.message.content
                ): 'The above command was sent by ' + context.author.mention + '/@' + main.discord.utils.escape_markdown(
			        context.author.name
		        ) + '#' + context.author.discriminator + ' in ' + location,
                'Message Link': context.message.jump_url
            }
		)
	)
def setup(
	mm
):
	mm.add_listener(
		on_command
	)