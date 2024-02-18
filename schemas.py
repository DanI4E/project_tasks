from typing import Optional # Optional дает возможность не заполнять данные в параметре, по умолчанию None
from pydantic import BaseModel # для описание данных, валидация (устанавливается вместе в fastapi)


class STaskAdd(BaseModel): # класс от которого наследуются все наши модели
    name: str
    description: Optional[str] = None



class STask(STaskAdd): # наследование параметров из класса STaskAdd(BaseModel)
    id: int



class STaskId(BaseModel):
    ok: bool = True
    task_id: int


