import bson

from flask import g ,current_app
from werkzeug.local import LocalProxy
from pymongo.errors import DuplicateKeyError, OperationFailure
from bson.objectid import ObjectId
from bson.errors import InvalidId
from pymongo import MongoClient

def get_db():
    """
    Configuration method to return db instance
    """
    if "db" not in g:
        mongo_uri = current_app.config['MONGO_URI']
        client = MongoClient(mongo_uri)
        g.db = client["data"]

    return g.db

db = LocalProxy(get_db)