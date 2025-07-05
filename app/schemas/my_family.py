from pydantic import BaseModel
from typing import List

class MyFamily(BaseModel):
    id: int
    name: str
    description: str
    members: List[str]
