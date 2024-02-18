from sqlalchemy import select
from database import TaskTable, new_session
from schemas import STask, STaskAdd


class TaskRepository: #нет экземпляра репозитория, паттерн unit of work
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session: #открываем контекстный менеджер который отдает объект session
            task_dict = data.model_dump() #task приводим к виду словаря с помощью функции model_dump

            task  = TaskTable(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id


    @classmethod
    async def find_all(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskTable)
            result = await session.execute(query)
            task_models = result.scalars().all() #объекты alchemy, вернутся все объекты
            task_schemas = [STask.model_validate(task_model) for task_model in task_models] #чтобы конвертировать к pydantic схемам
            return task_schemas


