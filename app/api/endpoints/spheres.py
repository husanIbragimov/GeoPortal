from typing import List, Annotated
import polars as pl
import requests
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session, joinedload

from app.core.config import settings
from app.models.sphere import Sphere
from app.schemas.spheres import SphereCreateSchema, SphereSchema
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


@router.post("/sphere/", response_model=SphereCreateSchema)
def create_sphere(sphere: SphereCreateSchema, db: Session = Depends(get_db)):
    db_sphere = Sphere(
        title=sphere.title,
        icon=sphere.icon,
        is_active=sphere.is_active,
        parent_id=sphere.parent_id
    )
    db.add(db_sphere)
    db.commit()
    db.refresh(db_sphere)
    return db_sphere


@router.get("/all_spheres", response_model=List[SphereSchema])
def read_all_spheres(db: Session = Depends(get_db)):
    spheres = db.query(Sphere).filter(Sphere.parent_id == None).order_by(Sphere.id).all()
    return spheres


@router.get("/columns/{pk}/")
def get_columns(pk: int):
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



    return


@router.get("/report_field/{pk}/meta-data")
def get_report_field_meta_data(pk: int, query: Annotated[str | None, Query(max_length=50)] = None):
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

    COLOR_MAP = ["#FFA500", "#FFFF00", "#008000", "#00FFFF", "#0000FF"]

    def get_color(value, min_value, max_value):
        norm = (value - min_value) / (max_value - min_value)  # Normalization
        index = int(norm * (len(COLOR_MAP) - 1))  # Calculate color index
        print(COLOR_MAP[index])
        return COLOR_MAP[index]

    years = data_df.columns[4:]

    for year in years:
        max_value = data_df[year].max()
        min_value = data_df[year].min()
        data_df = data_df.with_columns(
            pl.col(year).map_elements(lambda x: {'value': x, 'color': get_color(x, min_value, max_value)},
                                      return_dtype=pl.Object).alias(year)
        )

    return data_df.to_dicts()


