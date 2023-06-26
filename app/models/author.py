from sqlalchemy import Column, Integer, String, DateTime, Enum as EnumType
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base
from uuid import uuid4
from enum import Enum


class FieldEnum(str, Enum):
    physics = "physics"
    chemistry = "chemistry"
    economics = "economics"
    computer_science = "computer_science"
    astronomy = "astronomy"


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String, default=str(uuid4()), nullable=False)
    name = Column(String, nullable=False)
    middle_name = Column(String)
    surname = Column(String, nullable=False)
    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    field = Column(EnumType(FieldEnum), nullable=False)
    comments = relationship("Comment", back_populates="author", lazy="select")
