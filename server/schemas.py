from pydantic import BaseModel, ConfigDict
from datetime import datetime

class SchoolModel(BaseModel):
    id: int
    title: str
    date_created: datetime

class SchoolCreateModel(BaseModel):
    title: str

    # model_config = ConfigDict(
    #     from_attributes = True
    # )

