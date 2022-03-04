# Import the command handler
import lightbulb
from decouple import config
# Instantiate a Bot instance


class Bot(lightbulb.BotApp):
    def __init__(self, token, *args, **kwargs):
        super().__init__(
            token=token,
            default_enabled_guilds=(config('ENABLED_GUILDS').split(",")),
            *args,
            **kwargs,
        )
        self.load_extensions_from("bot/cogs")
        self.load_extensions_from("bot/events")



if __name__ == "__main__":
    Bot = Bot()