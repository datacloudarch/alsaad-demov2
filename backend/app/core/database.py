from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .config import settings


# For Azure SQL, prefer an ODBC connection string in DATABASE_URL
# Example: mssql+pyodbc:///?odbc_connect=DRIVER%3D%7BODBC+Driver+18+for+SQL+Server%7D%3B...
engine = create_engine(
    settings.database_url,
    pool_pre_ping=True,
    pool_recycle=300,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


