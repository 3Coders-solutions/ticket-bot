import hikari
import lightbulb
from lightbulb.app import BotApp

plugin = lightbulb.Plugin("Example", "Example command.")


@plugin.command()
@lightbulb.option("champ", "Champ you want stats")
@lightbulb.command(name="example", description="Example command.")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def command_stats(ctx: lightbulb.SlashContext) -> None:
    await ctx.respond('hola')
    


def load(bot: BotApp) -> None:
    bot.add_plugin(plugin)


def unload(bot: BotApp) -> None:
    bot.remove_plugin(plugin)