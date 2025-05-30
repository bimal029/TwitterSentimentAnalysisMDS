from pymongo import MongoClient

def load_to_mongo(df):
    client = MongoClient("mongodb://localhost:27017/")
    db = client['sentiment140']
    collection = db['tweets']
    collection.insert_many(df.to_dict(orient='records'))
