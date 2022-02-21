
from time import sleep
import hikari
import lightbulb
import asyncio
from ..helpers import components
from hikari import ComponentInteraction, MessageFlag, events
from lightbulb.app import BotApp
plugin = lightbulb.Plugin("Message Components",
                          "Message component event handler.")


@plugin.listener(hikari.InteractionCreateEvent, bind=True)
async def message_components(plugin: lightbulb.Plugin, event: hikari.InteractionCreateEvent) -> None:
    if event.interaction.type != hikari.InteractionType.MESSAGE_COMPONENT:
        return
    interaction: hikari.ComponentInteraction = event.interaction
    if(interaction.custom_id.startswith("ticket_")):
        return await ticket_handler(interaction, plugin.bot)
    return

async def ticket_handler(interaction: hikari.ComponentInteraction, bot: hikari.GatewayBot):
    if(interaction.custom_id == "ticket_close"):
        return await confirm_menu(interaction, bot)

async def confirm_menu(interaction: hikari.ComponentInteraction, bot: hikari.GatewayBot):
    row = components.confirmation_menu()
    await interaction.create_initial_response(
      hikari.ResponseType.MESSAGE_CREATE, 
      flags=MessageFlag.EPHEMERAL,
      content="Confirm ticket close.", 
      components=[row])
    stream = bot.stream(events.InteractionCreateEvent, timeout=30).filter(("interaction.user.id", interaction.user.id))
    stream.open()
    async for event in stream:
        if event.interaction.custom_id.startswith("ticket_confirmation"):
            stream.close()
            return await handle_ticket_close(interaction, bot, event.interaction.custom_id == "ticket_confirmation_true")
    stream.close()
    await interaction.edit_initial_response("Timed out ", components=[])

async def handle_ticket_close(interaction: ComponentInteraction, bot: hikari.GatewayBot, confirm: bool):
    if confirm: 
      await interaction.edit_initial_response("Ticket will be closed in 5 seconds.", components=[])
      sleep(5)
      return await interaction.get_channel().delete()
    return await interaction.edit_initial_response("Ticket close canceled.", components=[])



def load(bot: BotApp) -> None:
    bot.add_plugin(plugin)


def unload(bot: BotApp) -> None:
    bot.remove_plugin(
        plugin)@plugin.listener(hikari.InteractionCreateEvent, bind=True)
