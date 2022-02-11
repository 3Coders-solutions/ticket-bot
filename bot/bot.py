# Import the command handler
import lightbulb
import hikari
import os
# Instantiate a Bot instance

class Bot(lightbulb.BotApp):
    def __init__(self, token,*args, **kwargs):
        super().__init__(
            token=token,
            default_enabled_guilds=(871537631807283241),
            *args,
            **kwargs,
            )
        self.load_extensions_from("bot/cogs")
    async def on_readt(self):
        print("Bot is ready")

if __name__ == "__main__":
    Bot = Bot()