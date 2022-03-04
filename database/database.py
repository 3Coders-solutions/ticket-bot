from pymongo import errors
from pymodm import connect
from pymodm.queryset import QuerySet
from decouple import config
from .models.Ticket import Ticket
from .models.Category import Category
from pymongo import errors
def initialize():
    try:
        connect(config('MONGO_URI'))
        print('Successfully connected to DB.')
    except errors.ConnectionFailure:
        print('ERROR ON CONNECTION')

async def create_ticket(channel_id: int,
                        guild_id: int,
                        ticket_id: int,
                        author_id: int,
                        closed: bool = False) -> Ticket:
    ticket = Ticket().save()


def fetch_categories(guild_id: int):
    categories:QuerySet = Category.objects.raw({'guild_id': guild_id})
    return categories

