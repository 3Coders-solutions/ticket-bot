from bot.bot import Bot
from decouple import config
from database import database
if __name__ == "__main__":
    database.initialize()
    Bot(config("TOKEN")).run()
    