from typing import Optional # Optional дает возможность не заполнять данные в параметре, по умолчанию None
from pydantic import BaseModel, ConfigDict # для описание данных, валидация (устанавливается вместе в fastapi)


class STaskAdd(BaseModel): # класс от которого наследуются все наши модели
    name: str
    description: Optional[str] = None



class STask(STaskAdd): # наследование параметров из класса STaskAdd(BaseModel)
    id: int

    model_config = ConfigDict(from_attributes=True) # парсит не только как словарь данный объект, а еще как экземпляр класса и из атрибутов его достаёт все свойства



class STaskId(BaseModel):
    ok: bool = True
    task_id: int


