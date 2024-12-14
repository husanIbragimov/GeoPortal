import json
from typing import List, Dict, Any

from bson import ObjectId
from app.schemas.documents import Region, District
from fastapi import APIRouter, HTTPException

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
