from models import School
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import select

class CRUD:
    async def get_all(self, async_session: async_sessionmaker[AsyncSession]):
        async with async_session() as session:
            statement = select(School).order_by(School.id)
            result = await session.execute(statement)
            return result.scalars()
    
    async def get_by_id(self, async_session: async_sessionmaker[AsyncSession], school_id: str):
        async with async_session() as session:
            statement = select(School).filter(School.id == school_id)
            result = await session.execute(statement)
            return result.scalars().one()
        
    async def add(self, async_session: async_sessionmaker[AsyncSession], school: School):
        async with async_session() as session:
            session.add(school)
            await session.commit()
    
    
    async def update(self, async_session: async_sessionmaker[AsyncSession], school_id: str, data):
        async with async_session() as session:
            # school = await self.get_by_id(session, school_id)
            statement = select(School).filter(School.id == school_id)
            result = await session.execute(statement)
            school = result.scalars().one()
            school.title = data['title']
            await session.commit()
            return school

    async def delete(self, async_session: async_sessionmaker[AsyncSession], school: School):
        async with async_session() as session:
            session.delete(school)
            await session.commit()
