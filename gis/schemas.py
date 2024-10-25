from pydantic import BaseModel


class RegionSchema(BaseModel):
    _id: str
    type: str
    properties: dict


class DistrictSchema(BaseModel):
    _id: str
    type: str
    properties: dict
    geometry: dict
