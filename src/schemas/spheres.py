from typing import Optional, List

from pydantic import BaseModel, ValidationError


class SubSphereSchema(BaseModel):
    id: int
    title: str
    is_active: bool

    class Config:
        from_attributes = True


class SphereSchema(BaseModel):
    id: int
    title: str
    icon: Optional[str] = None
    icon_light: Optional[str] = None
    is_active: bool
    children: Optional[List[SubSphereSchema]] = []

    class Config:
        from_attributes = True


class SphereCreateSchema(BaseModel):
    title: str
    icon: Optional[str] = None
    icon_light: Optional[str] = None
    is_active: bool = True
    parent_id: Optional[int] = None

    class Config:
        from_attributes = True
