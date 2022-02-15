import hikari
from decouple import config

rest = hikari.RESTApp()
async def get_guild_count() -> int:
    async with rest.acquire(config('TOKEN'), token_type=hikari.TokenType.BOT) as client:
        return len(client.fetch_guild())

async def get_guild_ids():
    async with rest.acquire(config('TOKEN'), token_type=hikari.TokenType.BOT) as client:

        return client.fetch_my_guilds()