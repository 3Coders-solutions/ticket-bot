# Import the command handler
import lightbulb
from decouple import config
from discord.ext import ipc
from .helpers import db_handler
# Instantiate a Bot instance


class Bot(lightbulb.BotApp):
    def __init__(self, token, *args, **kwargs):
        super().__init__(
            token=token,
            default_enabled_guilds=(871537631807283241,),
            *args,
            **kwargs,
            )
        db_handler.initialise_databases()
        self.load_extensions_from("bot/cogs")



if __name__ == "__main__":

    Bot = Bot()