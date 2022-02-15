import hikari
import lightbulb
from lightbulb.app import BotApp

plugin = lightbulb.Plugin("Example", "Example command.")


@plugin.command()
@lightbulb.option("champ", "Champ3 you want stats")
@lightbulb.option("champ2", "Champ3 you want stats")
@lightbulb.command(name="examplee", description="Example command")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def example(ctx: lightbulb.SlashContext) -> None:
    await ctx.respond('hola')
    
@example.child
@lightbulb.command("bar", "test subgroup")
@lightbulb.implements(lightbulb.SlashSubGroup)
async def bar(ctx: lightbulb.Context) -> None:
    await ctx.respond("invoked foo bar")

def load(bot: BotApp) -> None:
    bot.add_plugin(plugin)


def unload(bot: BotApp) -> None:
    bot.remove_plugin(plugin)