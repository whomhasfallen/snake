from contextBot.CommandHandler import CommandHandler

cmds = CommandHandler()

@cmds.cmd("ping")
async def cmd_ping(ctx):
    await ctx.reply('Pong!')
