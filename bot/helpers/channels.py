import lightbulb
import hikari
from . import components
from hikari.impl.special_endpoints import ActionRowBuilder
from hikari import ButtonStyle, PartialComponent, PermissionOverwrite, PermissionOverwriteType, Permissions, GatewayGuild, PartialRole, GuildTextChannel, embeds, ButtonComponent, ActionRowComponent, ComponentType


async def create_channel(ctx: lightbulb.Context) -> GuildTextChannel:
    guild: GatewayGuild = ctx.interaction.get_guild()

    everyoneRole = (await guild.fetch_roles())[0]
    overwrite = [PermissionOverwrite(
        id=everyoneRole,
        type=PermissionOverwriteType.ROLE,
        deny=(
            Permissions.VIEW_CHANNEL
            | Permissions.READ_MESSAGE_HISTORY
            | Permissions.SEND_MESSAGES
        )
    ),
        PermissionOverwrite(
        id=ctx.author.id,
        type=PermissionOverwriteType.MEMBER,
        allow=(
            Permissions.VIEW_CHANNEL
            | Permissions.READ_MESSAGE_HISTORY
            | Permissions.SEND_MESSAGES
        )
    )]
    created_channel: GuildTextChannel = await guild.create_text_channel(ctx.options.category, permission_overwrites=overwrite)
    return created_channel


async def send_ticket_message(ctx: lightbulb.Context, created_channel: GuildTextChannel) -> None:
    row = components.ticket_close_button()
    embed = embeds.Embed(title="New ticket", description="This is a new ticket")
    await created_channel.send(embed=embed, components=[row])
    return
