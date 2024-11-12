import pandas as pd
import json
from db import db
from pymongo import MongoClient

def mongoimport(csv_path, coll_name):
    """Imports a CSV file at path csv_name to a MongoDB collection.
    Returns: count of the documents in the new collection.
    """
    mongo_uri = "mongoUri"
    client = MongoClient(mongo_uri)
    db = client["data"]
    
    coll = db[coll_name]
    data = pd.read_csv(csv_path)
    payload = json.loads(data.to_json(orient='records'))
    coll.delete_many({})
    coll.insert_many(payload)
    return coll.count_documents({})

if __name__ == "__main__":
    csv_path = './dataset/DisasterDataset.csv'
    collection_name = 'disaster'
    print(f"Number of documents in {collection_name}: {mongoimport(csv_path, collection_name)}")
