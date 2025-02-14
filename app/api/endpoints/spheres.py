from typing import List
import matplotlib.pyplot as plt
import polars as pl
import requests
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload

from app.core.config import settings
from app.models.sphere import Sphere
from app.schemas.spheres import SphereCreateSchema, SphereSchema
from . import get_db
from ...models import ColorEnum

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


@router.get("/number_of_births")
def get_number_of_births(db: Session = Depends(get_db)):
    response = requests.get(settings.STAT_URI).json()
    return response


@router.get("/report_field/{pk}/meta-data")
def get_report_field_meta_data(pk: int):
    response = requests.get(f"{settings.SIAT_URI}/media/uploads/sdmx/sdmx_data_{pk}.json")
    print(response.status_code)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch data")

    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Invalid JSON response")

    if not data:
        raise HTTPException(status_code=404, detail="No data found")
    df = pl.DataFrame(response[0]["data"])

    COLOR_MAP = [ColorEnum.ORANGE, ColorEnum.YELLOW, ColorEnum.GREEN, ColorEnum.CYAN, ColorEnum.BLUE]

    years = [col for col in df.columns if col.isdigit()]
    values = df.select(years).to_numpy().flatten()

    min_val = values.min()
    max_val = values.max()

    def get_color(value):
        norm = (value - min_val) / (max_val - min_val)  # Normalizatsiya
        index = int(norm * (len(COLOR_MAP) - 1))  # Rang indeksini hisoblash
        return COLOR_MAP[index].value

    updated_data = []
    for index, row in df.iter_rows():
        new_row = row.copy()
        for year in years:
            new_row[year] = {"value": row[year], "color": get_color(row[year])}
        updated_data.append(new_row)

    print(updated_data)



