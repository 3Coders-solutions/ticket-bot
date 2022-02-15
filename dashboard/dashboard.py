from quart import Quart, render_template, request, session, redirect, url_for
from quart_discord import DiscordOAuth2Session
from decouple import config

from helpers import utils

app = Quart(__name__)
app.config["SECRET_KEY"] = config('SECRET_KEY')
app.config["DISCORD_CLIENT_ID"] = config('DISCORD_CLIENT_ID')
app.config["DISCORD_CLIENT_SECRET"] =config('DISCORD_CLIENT_SECRET') 
app.config["DISCORD_REDIRECT_URI"] = config('DISCORD_REDIRECT_URI')
discord = DiscordOAuth2Session(app)
utils.a()

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
	return redirect("/dashboard") #You should return redirect(url_for("dashboard")) here

@app.route("/dashboard")
async def dashboard():
	guild_count = 4
	guild_ids = [2]
	try:
		user_guilds = await discord.fetch_guilds()
	except:
		return redirect(url_for("login")) 

	same_guilds = []

	for guild in user_guilds:
		if guild.id in guild_ids:
			same_guilds.append(guild)


	return await render_template("dashboard.html", guild_count = guild_count, matching = same_guilds)

if __name__ == "__main__":
	app.run(debug=True)