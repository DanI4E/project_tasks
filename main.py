from fastapi import FastAPI # импортируем класс

from contextlib import asynccontextmanager # импорт декоратора который позволяет создавать контекстные менеджеры

from database import create_tables, delete_tables
from router import router as tasks_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('База удалена')
    await create_tables()
    print('База создана')
    yield
    print("Выключение")


app = FastAPI(lifespan=lifespan) # создание экземпляра класса
app.include_router(tasks_router) # чтобы fastapi заметил роутер





