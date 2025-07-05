from pydantic import BaseModel
from typing import List

class MyBag(BaseModel):
    id: int
    name: str
    description: str
    items: List[str]
