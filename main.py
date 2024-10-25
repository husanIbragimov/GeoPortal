from typing import List, Dict, Any

from fastapi import FastAPI

from gis.documents import Region, District


app = FastAPI(
    title="GIS API",
    version="0.1.0",
    docs_url="/docs",
    debug=True,
)


@app.get("/")
async def get_regions() -> List[Dict[str, Any]]:
    region = Region(document={})  # Provide an empty document
    return await region.get_all()


@app.get("/districts")
async def get_districts() -> List[Dict[str, Any]]:
    district = District(document={})
    return await district.get_all()


@app.get("/district/{parent_code}")
async def get_district(parent_code: int) -> List[Dict[str, Any]]:
    district = District(document={})
    return await district.get(parent_code)
