from sqlalchemy.orm import Session

from app.models.sphere import Sphere
from app.schemas.spheres import SphereCreateSchema


def create_sphere(db: Session, sphere: SphereCreateSchema):
    db_sphere = Sphere(
        title=sphere.title,
        parent_id=sphere.parent_id
    )
    db.add(db_sphere)
    db.commit()
    db.refresh(db_sphere)

    # If the sphere has a parent, add it to the parent's children
    if db_sphere.parent_id:
        parent_sphere = db.query(Sphere).filter(Sphere.id == db_sphere.parent_id).first()
        if parent_sphere:
            parent_sphere.children.append(db_sphere)
            db.commit()

    return db_sphere


def get_sphere(db: Session, sphere_id: int):
    sphere = db.query(Sphere).filter(Sphere.id == sphere_id).first()
    return sphere


def get_all_spheres(db: Session):
    return db.query(Sphere).all()
