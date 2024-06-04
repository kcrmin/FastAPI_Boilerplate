# SQLAlchemy2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# psycopg3
import psycopg
from psycopg_pool import ConnectionPool
from functools import lru_cache

# config
from .config import settings

# SQLAlchemy2 Connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

SQLALCHEMY_DATABASE_URL = f'postgresql+psycopg://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Psycopg3 Connection
def get_conn():
     return psycopg.connect(conninfo=conninfo)

@lru_cache()
def get_pool():
	return ConnectionPool(conninfo=conninfo)

conninfo = f"user={settings.database_username} password={settings.database_password} host={settings.database_hostname} dbname={settings.database_name}"
