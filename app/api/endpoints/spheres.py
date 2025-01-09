import requests

from . import get_db
from typing import List
from app.core.config import settings
from app.models.sphere import Sphere
from sqlalchemy.orm import Session, joinedload
from fastapi import APIRouter, Depends, HTTPException
from app.schemas.spheres import SphereCreateSchema, SphereSchema


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
    spheres = db.query(Sphere).filter(Sphere.parent_id == None).all()
    return spheres


@router.get("/number_of_births")
def get_number_of_births(db: Session = Depends(get_db)):
    response = requests.get(settings.STAT_URI).json()
    return response


@router.get("/report_field/{pk}/meta-data")
def get_report_field_meta_data(pk: int):
    response = requests.get(f"{settings.SIAT_URI}/media/uploads/sdmx/sdmx_data_{pk}.json").json()
    return response
