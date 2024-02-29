import Main
@ Main . commands . command (
	name = 'extra'
)
async def extra (
	ctx
) -> None :
	prefix = Main . discord . utils . escape_markdown (
		ctx . prefix
	)
	await Main . deletable (
		ctx ,
		Main . embed (
			ctx ,
			{
                prefix + 'credits' : 'This will let you view all people who aided in my creation.',
                prefix + 'stats\n' + prefix + 'statistics': 'The above command will let you view my statistics, ergo, my guilds, users, birthday, and latency.',
				prefix + 'settings view' : 'The above command will let you view my custom prefix for this server as well as whether compact mode is turned on.' ,
                prefix + 'settings prefix <prefix>\n' + prefix + 'set prefix <prefix>': "The above command will let only this server's owner edit my prefix for the server. My default ones will continue to work.",
                prefix + 'settings compact <true/false/on/off>\n' + prefix + 'set compact <true/false/on/off>': 'The above command will turn compact mode on or off depending on whichever option out of the above you chose. Compact mode reduces embed sizes by removing the exact timing and context on which they are sent.'
            }
		) ,
		deletable = True
	)
def setup (
	mm
) :
	mm . add_command (
		extra
	) 