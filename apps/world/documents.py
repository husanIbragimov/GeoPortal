from mongo_db import db


class Document:
    def __init__(self, document):
        self.document = document

    def save(self):
        db.documents.insert_one(self.document)

    @staticmethod
    def get_all():
        return db.documents.find()

    @staticmethod
    def get_by_parent_code(parent_code):
        return db.documents.find_one({"properties": {"parent_code": parent_code}})

    @staticmethod
    def update(parent_code, document):
        db.documents.update_one({"properties": {"parent_code": parent_code}}, {"$set": document})

    @staticmethod
    def delete(parent_code):
        db.documents.delete_one({"properties": {"parent_code": parent_code}})

    @staticmethod
    def delete_all():
        db.documents.delete_many({})

    @staticmethod
    def search(query):
        return db.documents.find({"properties": {"$regex": query}})

    @staticmethod
    def get_parents():
        return db.documents.find({"properties": {"parent_code": None}})
