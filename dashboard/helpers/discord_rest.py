import hikari
from decouple import config

async def get_guild_count(rest) -> int:
    async with rest.acquire(config('TOKEN'), token_type=hikari.TokenType.BOT) as client:
        return len(client.fetch_guild())

async def get_guild_ids(rest):
    async with rest.acquire(config('TOKEN'), token_type=hikari.TokenType.BOT) as client:
        return client.fetch_my_guilds()

# async def otracosa():
#     async with rest.acquire(config('TOKEN'), token_type=hikari.TokenType.BOT) as client:

#         return client.fetch_my_guilds()
