from typing import Optional
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker #ext-расширения, asyncio-асинхронный, create_async_engine - создание асинхронного движка для работы с бд
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


engine = create_async_engine(
    "sqlite+aiosqlite:///tasks.db" #aiosqlite драйвер, ///tasks.db - база данных внутри файла в проекте
)
new_session = async_sessionmaker(engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass


class TaskTable(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


