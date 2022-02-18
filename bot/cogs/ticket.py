import hikari
import lightbulb
from lightbulb.app import BotApp
from ..helpers import channels
plugin = lightbulb.Plugin("Ticket", "Main ticket command.")

#Example choices
choices=("Assistance", "Support")
@plugin.command()
@lightbulb.command("ticket", "Ticket Commands")
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def ticket(ctx: lightbulb.Context) -> None:
    await ctx.respond("Invoked ticket? What, how.")
    return


@ticket.child
@lightbulb.option(name="category", choices=choices, required=True, description="Choose the category to make the ticket")
@lightbulb.command("new", "Create a new ticket")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def bar(ctx: lightbulb.Context) -> None:
    created_channel = await channels.create_channel(ctx)
    await ctx.respond(f'Succesfully created ticket! <#{created_channel.id}>', flags=hikari.MessageFlag.EPHEMERAL)
    return

def load(bot: BotApp) -> None:
    bot.add_plugin(plugin)


def unload(bot: BotApp) -> None:
    bot.remove_plugin(plugin)