from typing import Any

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./scientific_db.db"

# For async queries
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True, future=True)

# noinspection PyTypeChecker
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)
Base: Any = declarative_base()
