from typing import List, Dict, Any

from pymongo import MongoClient


class MongoDB:
    def __init__(self, collection_name):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client["gis"]
        self.collection = self.db[collection_name]

    def insert(self, data):
        self.collection.insert_one(data)

    def find(self, query) -> List[Dict[str, Any]]:
        return self.collection.find(query).to_list()

    def find_all(self) -> List[Dict[str, Any]]:
        return self.collection.find().to_list()

    def delete(self, query):
        self.collection.delete_one(query)

    def update(self, query, data):
        self.collection.update_one(query, data)

    def delete_all(self) -> None:
        self.collection.delete_many({})

    def close(self) -> None:
        self.client.close()
