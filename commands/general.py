from contextBot.CommandHandler import CommandHandler

cmds = CommandHandler()

@cmds.cmd("ping")
async def cmd_ping(ctx):
    """
    Usage:
        {prefix}ping 
    Description:
        Pings the bot.
    """
    await ctx.reply('Pong!')

@cmds.cmd("eval")
async def cmd_eval(ctx):
    """
    Usage:
        {prefix}eval <code>
    Description:
        Runs <code> in current environment using eval() and prints the output or error.
    """
    if ctx.arg_str == "":
        await ctx.reply("You must give me something to run!")
        return
    output, error = await _eval(ctx)
    await ctx.reply("**Eval input:**\
                    \n```py\n{}\n```\
                    \n**Output {}:** \
                    \n```py\n{}\n```".format(ctx.arg_str,
                                             "error" if error else "",
                                             output))
