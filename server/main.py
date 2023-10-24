import uuid
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from crud import CRUD
from sqlalchemy.ext.asyncio import async_sessionmaker
from db import engine
from schemas import SchoolModel, SchoolCreateModel
from typing import List
from models import School

app = FastAPI(
    title="Learning Management System API",
    description="",
    docs_url="/"
)


origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

session = async_sessionmaker(
    bind = engine,
    expire_on_commit = False
)

db = CRUD()

@app.get('/')
async def hello():
    return {"message": "hello world"}

@app.get('/schools', response_model=List[SchoolModel])
async def get_all_schools():
    schools = await db.get_all(session)
    return schools

@app.post('/schools')
async def create_school(school_data: SchoolCreateModel):
    new_school = School(
        title = school_data.title,
    )
    school = await db.add(session, new_school)
    return school

@app.get('/school/{school_id}')
async def get_school_by_id(school_id):
    school = await db.get_by_id(session, school_id)
    return school

@app.patch('/school/{school_id}')
async def update_school(school_id, data: SchoolCreateModel):
    school = db.update(session, school_id, data={
        'title': data.title
    })
    return school

@app.delete('/school/{school_id}')
async def delete_school(school_id):
    school = await db.get_by_id(session, school_id)
    result = await db.delete(session, school)
    return result


