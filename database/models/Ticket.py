from pymodm import  fields, MongoModel
from pymongo.operations import IndexModel
from . import Category
import pymongo
class Ticket(MongoModel):
    channel_id = fields.BigIntegerField()
    guild_id = fields.BigIntegerField(required=True)
    ticket_id = fields.BigIntegerField(required=True)
    author_id = fields.BigIntegerField(required=True)
    closed = fields.BooleanField(default=False,required=False)
    category = fields.ReferenceField(Category.Category)
    class Meta:
      # Text index on content can be used for text search.
      indexes = [IndexModel([('guild_id', pymongo.TEXT)])]
      final = True

