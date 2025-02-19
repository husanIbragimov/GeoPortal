from datetime import datetime
from typing import List, Any, Dict

import polars as pl
import requests
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session, joinedload

from app.core.config import settings
from app.core.utils import calculate_color_mapping, COLOR_MAP
from app.models.sphere import Sphere
from app.schemas.spheres import SphereSchema
from . import get_db

router = APIRouter(
    tags=["spheres"],
    responses={404: {"description": "Not found"}},
)


@router.get("/spheres/", response_model=List[SphereSchema])
def read_spheres(db: Session = Depends(get_db)):
    spheres = (
        db.query(Sphere)
        .filter(Sphere.parent_id.is_(None))  # Fetch only top-level spheres
        .options(joinedload(Sphere.children))  # Load children eagerly
        .all()
    )
    return spheres


@router.get("/spheres/{sphere_id}/", response_model=SphereSchema)
def read_category(sphere_id: int, db: Session = Depends(get_db)):
    sphere = db.query(Sphere).filter(Sphere.id == sphere_id).first()
    if sphere is None:
        raise HTTPException(status_code=404, detail="Sphere not found")
    return sphere


@router.get("/all_spheres", response_model=List[SphereSchema])
def read_all_spheres(db: Session = Depends(get_db)):
    spheres = db.query(Sphere).filter(Sphere.parent_id == None).order_by(Sphere.id).all()
    return spheres


@router.get("/columns/{pk}/")
def get_years(pk: int):
    response = requests.get(f"{settings.SIAT_URI}/media/uploads/sdmx/sdmx_data_{pk}.json")

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch data")

    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Invalid JSON response")

    if not data:
        raise HTTPException(status_code=404, detail="No data found")

    data_df = pl.DataFrame(data[0]["data"])

    columns = data_df.columns[4:]

    years = (
        {
            "year": year,
        } for year in columns
    )

    return years


# --- API endpoint ---
@router.get("/report_field/{pk}/meta-data")
def get_report_data_by_provinces(
        pk: int,
        year: int = Query(default=0, description="Year to fetch data")
) -> List[Dict[str, Any]]:

    if year == 0:
        raise HTTPException(status_code=404, detail="Year is required")

    response = requests.get(f"{settings.SIAT_URI}/media/uploads/sdmx/sdmx_data_{pk}.json")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch data")

    try:
        data = response.json()
    except ValueError:
        raise HTTPException(status_code=500, detail="Invalid JSON response")

    if not data:
        raise HTTPException(status_code=404, detail="No data found")

    data_df = pl.DataFrame(data[0]["data"])
    year_column = f"{year}"

    years = data_df.columns
    if year_column not in years:
        year_column = years[-1]

    data_df = data_df.filter(data_df["Code"] != "1700" & data_df["Code"].str.len_chars() == 4)

    provinces = data_df[year_column].to_list()
    if not provinces:
        raise HTTPException(status_code=404, detail="No data found")

    colors = calculate_color_mapping(provinces, COLOR_MAP)

    sub_data = (
        {
            "soato": row.get("Code"),
            "value": row.get(year_column),
            "year": year_column,
            "color": color,
            "Klassifikator": row.get("Klassifikator"),
            "Klassifikator_ru": row.get("Klassifikator_ru"),
            "Klassifikator_en": row.get("Klassifikator_en")
        } for row, color in zip(data_df.to_dicts(), colors)
    )

    return [{
        "metadata": data[0]["metadata"],
        "data": sub_data
    }]


# --- API endpoint ---
@router.get("/report_data/{year}/{pk}/{soato}/district")
def get_report_data_by_district(
        year: int,
        pk: int,
        soato: str
) -> List[Dict[str, Any]]:
    response = requests.get(f"{settings.SIAT_URI}/media/uploads/sdmx/sdmx_data_{pk}.json")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch data")

    try:
        data = response.json()
    except ValueError:
        raise HTTPException(status_code=500, detail="Invalid JSON response")

    if not data:
        raise HTTPException(status_code=404, detail="No data found")

    data_df = pl.DataFrame(data[0]["data"])
    year_column = f"{year}"

    parent_soato = soato[:4]

    data_df = data_df.filter(
        (pl.col("Code").str.starts_with(parent_soato)) & (pl.col("Code").str.len_chars() != 4)
    )

    district = data_df[year_column].to_list()
    if not district:
        raise HTTPException(status_code=404, detail="No data found")

    colors = calculate_color_mapping(district, COLOR_MAP)

    sub_data = (
        {
            "soato": row.get("Code"),
            "value": row.get(year_column),
            "year": year_column,
            "color": color,
            "Klassifikator": row.get("Klassifikator"),
            "Klassifikator_ru": row.get("Klassifikator_ru"),
            "Klassifikator_en": row.get("Klassifikator_en")
        } for row, color in zip(data_df.to_dicts(), colors)
    )


    return [{
        "metadata": data[0]["metadata"],
        "data": sub_data
    }]
