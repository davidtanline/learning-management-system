from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_async_engine(
    url = f"postgresql+asyncpg://postgres:{os.getenv('DB_PASS')}@localhost/lms_db",
    echo = True
)

SessionLocal = sessionmaker(autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass
