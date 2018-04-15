import discord

from contextBot.Context import Context
from contextBot.Bot import Bot

from botconf import Conf

# Global constants/ environment variables

CONF_FILE = "pytest.conf"

# Initialise

conf = Conf(CONF_FILE)

PREFIX = conf.get("PREFIX")

bot = Bot(data=None,
          bot_conf=conf,
          prefix=PREFIX)

bot.DEBUG = 1


# Loading and initial objects

bot.load("commands", ignore=["__pycache__"])

# ----Discord event handling----


@bot.event
async def on_ready():
    bot.sync_log("Logged in as")
    bot.sync_log(bot.user.name)
    bot.sync_log(bot.user.id)
    bot.sync_log("Logged into {} servers".format(len(bot.servers)))

# ----Event loops----
# ----End event loops----

# ----Everything is defined, start the bot!----
bot.run(conf.get("TOKEN"))
