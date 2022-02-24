from quart import Quart, render_template, redirect, url_for
from quart_discord import DiscordOAuth2Session, models
from decouple import config
import hikari
import discord

app = Quart(__name__)
rest = hikari.RESTApp()
async def get_guild_ids():
    async with rest.acquire(config('TOKEN'), token_type=hikari.TokenType.BOT) as client:
        return client.fetch_my_guilds()

app.config["SECRET_KEY"] = config('SECRET_KEY')
app.config["DISCORD_CLIENT_ID"] = config('DISCORD_CLIENT_ID')
app.config["DISCORD_CLIENT_SECRET"] = config('DISCORD_CLIENT_SECRET')
app.config["DISCORD_REDIRECT_URI"] = config('DISCORD_REDIRECT_URI')
discord = DiscordOAuth2Session(app)


@app.route("/")
async def home():
    return await render_template("index.html")


@app.route("/login")
async def login():
    return await discord.create_session()


@app.route("/callback")
async def callback():
    try:
        await discord.callback()
    except:
        return redirect(url_for("login"))

    user = await discord.fetch_user()
    # You should return redirect(url_for("dashboard")) here
    return redirect("/dashboard")


@app.route("/dashboard")
async def dashboard():
    guild_count = 4
    guild_ids = [2]
    try:
        user_guilds = await discord.fetch_guilds()
        print(user_guilds)
    except:
        return redirect(url_for("login"))

    same_guilds = []

    for guild in user_guilds:
        if guild.id in guild_ids:
            same_guilds.append(guild)

    return await render_template("dashboard.html", guild_count=guild_count, matching=same_guilds)


@app.route("/guilds")
async def guilds():
    user_guilds: list[models.Guild] = await discord.fetch_guilds()
    guild_ids:list[models.Guild] = list(filter(lambda guild: guild.permissions.can_manage_server == True, user_guilds))
    return await render_template("guilds.html", guild_ids=guild_ids)

if __name__ == "__main__":
    app.run(debug=True)