from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship, aliased
from sqlalchemy.orm import Session

from app.db.session import Base


class Sphere(Base):
    __tablename__ = "spheres"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=True)
    parent_id = Column(Integer, ForeignKey('spheres.id'), nullable=True)
    icon = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    section_id = Column(Integer, nullable=True, index=True)

    # Define a self-referential relationship
    parent = relationship('Sphere', remote_side=[id], backref='children')

    def __str__(self):
        return self.title
