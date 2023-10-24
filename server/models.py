from datetime import datetime
from db import Base
from sqlalchemy.orm import Mapped, mapped_column
'''
class School:
    id int
    name str
    date_created datetime
'''
class School(Base):
    __tablename__ = "school"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(nullable=False)
    date_created: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Note {self.title} at {self.date_created}>"
    