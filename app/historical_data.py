import json
from pymongo import MongoClient 
 
 
# Making Connection
try:
    myclient = MongoClient("mongodb://localhost:27017/") 
    
    # database 
    db = myclient["estimation_db"]
    Collection = db["historical_data"]


    with open('historical_data.json') as file:
        data = json.load(file)

    Collection.insert_many(data)
    
except Exception as e:
    print(e)

