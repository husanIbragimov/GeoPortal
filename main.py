import json
from typing import List, Dict, Any
from urllib.error import HTTPError

from bson import ObjectId
from fastapi import FastAPI, HTTPException

from gis.documents import Region, District


class MongoEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


app = FastAPI(
    title="GIS API",
    version="0.1.0",
    docs_url="/docs",
    debug=True,
)


@app.get("/regions")
async def get_regions() -> List[Dict[str, Any]]:
    region = Region(document={})  # Provide an empty document
    data = await region.get_all()
    return json.loads(json.dumps(data, cls=MongoEncoder))


@app.get("/districts")
async def get_districts() -> List[Dict[str, Any]]:
    district = District(document={})
    data = await district.get_all()
    return json.loads(json.dumps(data, cls=MongoEncoder))


@app.get("/district/{parent_code}")
async def get_district(parent_code: int) -> List[Dict[str, Any]]:
    district = District(document={})
    print(district)
    data = await district.get(parent_code)
    if not data:
        raise HTTPException(status_code=404, detail="District not found")
    return json.loads(json.dumps(data, cls=MongoEncoder))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
