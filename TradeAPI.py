from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from database import async_session_maker
from models import Trade

app = FastAPI()

# dependency to get a DB session per request
async def get_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session

@app.get("/trades")
async def get_all_trades(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Trade))
    trades = result.scalars().all()
    return [{"id": t.id, "user_id": t.user_id} for t in trades]
