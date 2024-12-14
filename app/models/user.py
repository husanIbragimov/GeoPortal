import enum

from sqlalchemy import Column, String, Boolean, TIMESTAMP, Enum, Integer
from sqlalchemy.sql.expression import text

from app.core.utils import hash_password
from app.db.session import Base


class GenderEnum(str, enum.Enum):
    male = "male"
    female = "female"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)

    full_name = Column(String(255), nullable=False)
    gender = Column(Enum(GenderEnum, name='genderenum'), nullable=False, default=GenderEnum.male)
    is_active = Column(Boolean, default=True)
    is_staff = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, server_default=text("now()"))
    updated_at = Column(TIMESTAMP, server_default=text("now()"), onupdate=text("now()"))

    def __str__(self):
        return self.username

    def __init__(self, username, email, full_name, gender, password=hash_password("Pass!123"), **kwargs):
        super().__init__(**kwargs)
        self.username = username
        self.email = email
        self.full_name = full_name
        self.gender = gender
        self.password = password
