from datetime import datetime
from typing import List, Any, Dict

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

    years = (
        {
            "year": year,
        } for year in columns
    )

    return years


# Ranglar gradienti uchun doimiy o'zgaruvchi
COLOR_MAP = ["#FFA500", "#FFFF00", "#008000", "#00FFFF", "#0000FF"]


# --- Ranglarni konvertatsiya va interpolatsiya qilish funksiyalari ---

def hex_to_rgb(hex_color: str) -> tuple:
    """Hex rangni (masalan, "#FFA500") RGB tuple ga o‘zgartiradi."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb: tuple) -> str:
    """RGB tuple ni hex rangga (masalan, "#FFA500") o‘zgartiradi."""
    return '#{:02X}{:02X}{:02X}'.format(*rgb)


def interpolate_color(color1: str, color2: str, t: float) -> str:
    """
    Ikkita hex rang orasida chiziqli interpolatsiya qiladi.

    :param color1: Boshlang'ich rang (hex)
    :param color2: Tugash rang (hex)
    :param t: Interpolatsiya progressi (0 dan 1 gacha)
    :return: Interpolatsiyalangan rang (hex)
    """
    r1, g1, b1 = hex_to_rgb(color1)
    r2, g2, b2 = hex_to_rgb(color2)
    r = int(r1 + (r2 - r1) * t)
    g = int(g1 + (g2 - g1) * t)
    b = int(b1 + (b2 - b1) * t)
    return rgb_to_hex((r, g, b))


def get_gradient_color(normalized_value: float, color_map: List[str]) -> str:
    """
    Normalizatsiyalangan qiymat asosida rang gradientini aniqlaydi.

    :param normalized_value: 0 va 1 oraligʻidagi qiymat
    :param color_map: Ranglar roʻyxati (hex formatda)
    :return: Mos keluvchi rang (hex)
    """
    n = len(color_map)
    if normalized_value <= 0:
        return color_map[0]
    if normalized_value >= 1:
        return color_map[-1]

    segment_length = 1 / (n - 1)
    segment_index = int(normalized_value / segment_length)

    # Agar normalized_value oxirgi segmentga to'g'ri kelsa
    if segment_index >= n - 1:
        return color_map[-1]

    segment_start = segment_index * segment_length
    t = (normalized_value - segment_start) / segment_length
    return interpolate_color(color_map[segment_index], color_map[segment_index + 1], t)


def calculate_color_mapping(values: List[float], color_map: List[str]) -> List[str]:
    """
    Berilgan qiymatlar uchun minimal va maksimal qiymatlar asosida normalizatsiya
    va gradient ranglarni hisoblaydi.

    :param values: Qiymatlar roʻyxati
    :param color_map: Ranglar roʻyxati (hex formatda)
    :return: Har bir qiymatga mos ranglar roʻyxati (hex formatda)
    """
    if not values:
        return []

    min_value = min(values)
    max_value = max(values)

    # Agar barcha qiymatlar teng bo'lsa, oxirgi rangni qaytaramiz
    if max_value == min_value:
        return [color_map[-1]] * len(values)

    mapped_colors = []
    for value in values:
        normalized = (value - min_value) / (max_value - min_value)
        mapped_colors.append(get_gradient_color(normalized, color_map))
    return mapped_colors


# --- API endpoint ---
@router.get("/report_field/{pk}/meta-data")
def get_report_field_meta_data(
        pk: int,
        year: int = Query(default=datetime.now().year, le=datetime.now().year)
) -> List[Dict[str, Any]]:
    response = requests.get(f"{settings.SIAT_URI}/media/uploads/sdmx/sdmx_data_{pk}.json")
    print(response.status_code)
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

    data_df = data_df.filter(data_df["Code"] != "1700")

    try:
        year_values = data_df[year_column].to_list()
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"{e}")

    colors = calculate_color_mapping(year_values, COLOR_MAP)

    sub_data = (
        {
            row.get("Code"): {
                "soato": row.get("Code"),
                "value": row.get(year_column),
                "year": year_column,
                "color": color,
                "Klassifikator": row.get("Klassifikator"),
                "Klassifikator_ru": row.get("Klassifikator_ru"),
                "Klassifikator_en": row.get("Klassifikator_en")
            }
        } for row, color in zip(data_df.to_dicts(), colors)
    )

    return [{
        "metadata": data[0]["metadata"],
        "data": sub_data
    }]
