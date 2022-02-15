from functools import cache
import sqlite3

from lightbulb.app import BotApp
from lightbulb.context import Context

from hikari.messages import Message
from hikari.events import GuildMessageDeleteEvent, GuildBulkMessageDeleteEvent

from typing import Union


def initialise_databases() -> None:
    """CREATING THE DATABASE FILES AND TABLES IN CASE THEY DONT EXIST ALREADY"""
    conn = sqlite3.connect("database/guilds.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS prefixes
        ( guild_id TEXT , prefix TEXT )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS colors
        (guild_id TEXT , color TEXT )
        """
    )
    conn.commit()
    conn.close()
