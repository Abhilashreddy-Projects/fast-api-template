from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

# Update with your actual credentials
DATABASE_URL = "postgresql+asyncpg://postgres:<PASSWORD>@localhost:5432/practice"

# Create the async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Create a session factory
async_session_maker = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)
