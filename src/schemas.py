from pydantic import BaseModel
from bson import ObjectId


class RegionSchema(BaseModel):
    _id: ObjectId
    type: str
    properties: dict


class DistrictSchema(BaseModel):
    _id: ObjectId
    type: str
    properties: dict
    geometry: dict
