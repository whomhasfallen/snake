import discord

from contextBot.Context import Context
from contextBot.Bot import Bot

from botconf import Conf

# Global constants/environment variables

CONF_FILE = "snake.conf"

# Init

conf = Conf(CONF_FILE)

PREFIX = conf.get("PREFIX")

bot = Bot(data=None,
          bot_conf=conf,
          prefix=PREFIX)

bot.objects["exec_whitelist"] = ["300992784020668416", "299175087389802496", "260246864979296256"]

bot.DEBUG = 1


# Loading commands and objects

bot.load("commands", ignore=["__pycache__"])


# Event handling

@bot.event
async def on_ready():
    bot.sync_log("Logged in as")
    bot.sync_log(bot.user.name)
    bot.sync_log(bot.user.id)
    bot.sync_log("Logged into {} servers".format(len(bot.servers)))
    # await client.change_presence(game=discord.Game(name="name", type=0-3))
    await bot.change_presence(game=discord.Game(name="Snaking around 🐍"))

# --- Event loops --- 
# --- End event loops ---

# --- Everything is defined, start the bot! ---
bot.run(conf.get("TOKEN"))
