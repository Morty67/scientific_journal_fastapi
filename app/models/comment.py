from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from uuid import uuid4
from app.core.database import Base


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    uuid = Column(String, default=str(uuid4()), nullable=False)
    article_id = Column(Integer, ForeignKey("articles.id"), nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)
    body = Column(String, nullable=False)
    created_ad = Column(DateTime(timezone=True), server_default=func.now())
    conclusion = Column(String, nullable=False)

    article = relationship("Article", back_populates="comments")
    author = relationship("Author", back_populates="comments")
