import hikari
import lightbulb
from lightbulb.app import BotApp
plugin = lightbulb.Plugin("Message Components",
                          "Message component event handler.")


@plugin.listener(hikari.InteractionCreateEvent, bind=True)
async def message_components(plugin: lightbulb.Plugin, event: hikari.InteractionCreateEvent) -> None:
    if event.interaction.type != hikari.InteractionType.MESSAGE_COMPONENT:
        return
    interaction: hikari.ComponentInteraction = event.interaction
    return

def load(bot: BotApp) -> None:
    bot.add_plugin(plugin)


def unload(bot: BotApp) -> None:
    bot.remove_plugin(
        plugin)@plugin.listener(hikari.InteractionCreateEvent, bind=True)
