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
    response = requests.get(f"{settings.SIAT_URI}/media/uploads/sdmx/sdmx_data_{pk}.json").json()
    data_df = pl.DataFrame(response[0]["data"])

    # Polars DataFrame yaratish
    df = pl.DataFrame(response[0]["data"])

    years = [col for col in data_df.columns if col.isdigit()]
    values = []
    for year in years:
        values.extend(df[year].to_list())

    # Sort the values
    sorted_values = sorted(values)

    # Define a color map
    color_map = ["orange", "cyan", "green", "yellow", "blue", "red", "purple", "pink"]

    # Assign colors based on the sorted order
    color_dict = {value: color_map[i % len(color_map)] for i, value in enumerate(sorted_values)}

    # Prepare data for plotting
    plot_data = []
    plot_colors = []
    for year in years:
        for value in df[year].to_list():
            plot_data.append((year, value))
            plot_colors.append(color_dict[value])

    # Create the bar chart
    fig, ax = plt.subplots()
    for i, (year, value) in enumerate(plot_data):
        ax.bar(f"{year}-{i}", value, color=plot_colors[i])

    # Set labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Value')
    ax.set_title('Yearly Data Visualization')

    # Show the plot
    plt.xticks(rotation=90)
    plt.show()

    return response
