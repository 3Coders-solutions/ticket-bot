from bot.bot import Bot
from decouple import config
if __name__ == "__main__":
    Bot(config("TOKEN")).run()