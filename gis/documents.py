from typing import Dict, Any, List

from mongo_db import MongoDB


class Document:
    def __init__(self, document: Dict[str, Any], table: str = "regions"):
        self.document = document
        self.table = table
        self.db = MongoDB(self.table)

    async def create(self) -> None:
        self.db.insert(self.document)

    async def get(self, parent_code: int) -> List[Dict[str, Any]]:
        return self.db.find({"properties.parent_code": parent_code})

    async def get_all(self) -> List[Dict[str, Any]]:
        return self.db.find_all()

    async def update(self, parent_code: int, document: Dict[str, Any]) -> List[Dict[str, Any]]:
        self.db.update({"properties.parent_code": parent_code}, document)
        return self.db.find({"properties.parent_code": parent_code})

    async def delete(self, parent_code: int) -> None:
        self.db.delete({"properties.parent_code": parent_code})

    async def delete_all(self) -> None:
        self.db.delete_all()

    async def search(self, query: Dict[str, Any]) -> List[Dict[str, Any]]:
        return self.db.find(query)

    async def get_parents(self) -> List[Dict[str, Any]]:
        return self.db.find({"properties.type": "parent"})


class Region(Document):
    def __init__(self, document: Dict[str, Any]):
        super().__init__(document, table="regions")


class District(Document):
    def __init__(self, document: Dict[str, Any]):
        super().__init__(document, table="districts")


class RegionDocument(Document):
    def __init__(self, document: Dict[str, Any]):
        super().__init__(document, table="regions1")
