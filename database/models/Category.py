from typing import final
from pymodm import  fields, MongoModel
from pymongo.operations import IndexModel
import pymongo
class Category(MongoModel):
    guild_id = fields.BigIntegerField()
    name = fields.CharField(required=True)
    emoji = fields.CharField()
    class Meta:
      # Text index on content can be used for text search.
      indexes = [IndexModel([('guild_id', pymongo.TEXT)])]
      final = True

