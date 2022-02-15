from telnetlib import GA
from tokenize import String


from lightbulb import BotApp
import lightbulb
from hikari import PermissionOverwrite, PermissionOverwriteType, Permissions, GatewayGuild, PartialRole, GuildChannel

async def create_channel(ctx) -> GuildChannel:
    guild: GatewayGuild = ctx.interaction.get_guild()
    everyoneRole= (await guild.fetch_roles())[0]
    overwrite = [PermissionOverwrite(
    id=everyoneRole,
    type=PermissionOverwriteType.ROLE,
    deny=(
        Permissions.VIEW_CHANNEL
        | Permissions.READ_MESSAGE_HISTORY
        | Permissions.SEND_MESSAGES
    ),
    )]
    created_channel = await guild.create_text_channel('secret', permission_overwrites=overwrite)
    return created_channel