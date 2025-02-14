from enum import Enum

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.db.session import Base


class ColorEnum(Enum):
    ORANGE = 0, 'orange'
    YELLOW = 1, 'yellow'
    GREEN = 2, 'green'
    CYAN = 3, 'cyan'
    BLUE = 4, 'blue'

    @classmethod
    def get_color(cls, value):
        return next(color.value[1] for color in cls if color.value[0] == value)


class Sphere(Base):
    __tablename__ = "spheres"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=True)
    parent_id = Column(Integer, ForeignKey('spheres.id'), nullable=True)
    icon = Column(String, nullable=True)
    icon_light = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    section_id = Column(Integer, nullable=True, index=True)

    # Define a self-referential relationship
    parent = relationship('Sphere', remote_side=[id], backref='children')

    def __str__(self):
        return self.title
