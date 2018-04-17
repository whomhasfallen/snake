from contextBot.CommandHandler import CommandHandler
import asyncio
import traceback

cmds = CommandHandler()

@cmds.cmd("ping")
async def cmd_ping(ctx):
    """
    Usage:
        {prefix}ping
    Description:
        Pings the bot.
    """
    await ctx.reply("Pong!")

@cmds.cmd("eval")
async def cmd_eval(ctx):
    """
    Usage:
        {prefix}eval <code>
    Description:
        Runs <code> in current environment using eval() and prints the output or error.
    """
    if not ctx.authid in ctx.bot.objects["exec_whitelist"]:
        return
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

@cmds.cmd("kick")
async def cmd_kick(ctx):
    """
    Usage:
        {prefix}kick [@member|ID] [type your reason or say 'None' for no reason]
    Description:
        Kicks a member.
    """
    await ctx.reply("If you're reading this, the kick command is a work in progress and will be finished soon.")

@cmds.cmd("ban")
async def cmd_ban(ctx):
    """
    Usage:
        {prefix}ban [@member|ID] [type your reason or say 'None' for no reason]
    Description:
        Bans a member.
    """
    await ctx.reply("If you're reading this, the ban command is a work in progress and will be finished soon.")

async def _eval(ctx):
    output = None
    try:
        output = eval(ctx.arg_str)
    except Exception:
        await ctx.bot.log(str(traceback.format_exc()))
        return (str(traceback.format_exc()), 1)
    if asyncio.iscoroutine(output):
        output = await output
    return (output, 0)
