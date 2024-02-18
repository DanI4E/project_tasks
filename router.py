from typing import Annotated
from fastapi import APIRouter, Depends #APIRouter конструкция, которая позволяет переносить набор эндпоинтов в один файл, а потом перемещать в файлик main через одну строчку
from repository import TaskRepository

from schemas import STaskAdd, STask, STaskId

router = APIRouter(
    prefix="/tasks",
    tags=["Таски"],
) #router - экземпляр класса APIrouter



@router.post("")  # fastapi может конвертировать pydantic модели JSON  
async def add_task(
        task: Annotated[STaskAdd, Depends()],
) -> STaskId:     
    task_id = await TaskRepository.add_one(task)
    return {'ok': True, "task_id": task_id}



@router.get("")# fastapi может конвертировать pydantic модели JSON  
async def get_task() -> list[STask]: #возвращаю данные STask (аннотации типов)
    tasks = await TaskRepository.find_all()
    return tasks