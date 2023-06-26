from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Enum as EnumType,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from enum import Enum
from uuid import uuid4

from app.core.database import Base
from app.utils.generate_content import generate_content


class ResearchFieldEnum(Enum):
    physics = "physics"
    chemistry = "chemistry"
    economics = "economics"
    computer_science = "computer_science"
    astronomy = "astronomy"


class StatusEnum(Enum):
    rejected = "rejected"
    self_check = "self_check"
    preprint = "preprint"
    peer_review = "peer_review"
    ready_to_publish = "ready_to_publish"
    published = "published"


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    uuid = Column(String, default=str(uuid4()), nullable=False)
    research_field = Column(String(50), nullable=False)
    summary = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    title = Column(String(100), nullable=False)
    content = Column(String, nullable=False, default=generate_content)
    status = Column(EnumType(StatusEnum), default=StatusEnum.self_check,
                    nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)
    author = relationship("Author", back_populates="articles", lazy="select")
    comments = relationship("Comment", back_populates="article")
