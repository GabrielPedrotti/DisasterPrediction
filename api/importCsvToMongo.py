import pandas as pd
from pymongo import MongoClient
import json
from db import db

def mongoimport(csv_path, coll_name):
    """ Imports a csv file at path csv_name to a mongo colection
    returns: count of the documants in the new collection
    """
    coll = db[coll_name]
    data = pd.read_csv(csv_path)
    payload = json.loads(data.to_json(orient='records'))
    coll.remove()
    coll.insert(payload)
    return coll.count()


mongoimport('data.csv', 'disaster')