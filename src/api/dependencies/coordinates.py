import json
from typing import List, Dict, Any

import polars as pl
from bson import ObjectId
from fastapi import APIRouter, HTTPException

from schemas.documents import Region, District

router = APIRouter(
    tags=["coordinates"],
    responses={404: {"description": "Not found"}},
)


class MongoEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


@router.get("/regions")
async def get_regions() -> List[Dict[str, Any]]:
    region = Region(document={})  # Provide an empty document
    data = await region.get_all()
    return json.loads(json.dumps(data, cls=MongoEncoder))


@router.get("/districts")
async def get_districts() -> List[Dict[str, Any]]:
    district = District(document={})
    data = await district.get_all()
    return json.loads(json.dumps(data, cls=MongoEncoder))


@router.get("/district/{parent_code}/")
async def get_district(parent_code: int) -> List[Dict[str, Any]]:
    district = District(document={})
    data = await district.get(parent_code)
    if not data:
        raise HTTPException(status_code=404, detail="District not found")
    return json.loads(json.dumps(data, cls=MongoEncoder))


@router.get("/uzbekistan")
async def get_uzbekistan() -> Dict[str, Any]:
    data_df = pl.read_csv("data/uz_coordinates.csv")

    return {
        "type": "Feature",
        "properties": {
            "region_name_en": "Uzbekistan",
            "region_name_ru": "Узбекистан",
            "region_name": "O'zbekiston",
            "parent_code": 1700,
        },
        "geometry": {
            "type": "GeometryCollection",
            "geometries": {
                "type": "MultiPolygon",
                "coordinates": tuple(zip(data_df["long"], data_df["lat"])),
            }
        },
    }
