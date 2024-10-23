from pymongo import MongoClient
import json

client = MongoClient('localhost', 27017)
db = client['gis']
document = db.get_collection('gis').find_one()

with open("geo.json", "w") as f:
    f.write(json.dumps(document, default=str))

client.close()