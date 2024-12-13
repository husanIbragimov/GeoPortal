from sqlalchemy import Column, String, Boolean, TIMESTAMP
from sqlalchemy.sql.expression import text
from app.db.session import Base


class User(Base):
    __tablename__ = "users"

    GENDER = (
        ("Male", "Male"),
        ("Female", "Female"),
    )

    id = Column(String(255), primary_key=True, index=True)
    username = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    
    full_name = Column(String(255), nullable=False)
    gender = Column(String(10), nullable=False, default="male")
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP, server_default=text("now()"))
    updated_at = Column(TIMESTAMP, server_default=text("now()"), onupdate=text("now()"))

    def __str__(self):
        return self.username