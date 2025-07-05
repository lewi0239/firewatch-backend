from fastapi import HTTPException
from typing import List
from app.schemas.my_family import MyFamily

# In-memory data store (for demo purposes)
family_list: List[MyFamily] = []  # Renamed from 'myfamily'

def get_myfamily() -> List[MyFamily]:
    return family_list

def create_myfamily(family: MyFamily) -> MyFamily:
    for m in family_list:
        if m.id == family.id:
            raise HTTPException(status_code=400, detail="ID already exists")
    family_list.append(family)
    return family

def get_myfamily_by_id(family_id: int) -> MyFamily:
    for family in family_list:
        if family.id == family_id:
            return family
    raise HTTPException(status_code=404, detail="Family not found")

def update_myfamily(family_id: int, updated: MyFamily) -> MyFamily:
    for i, family in enumerate(family_list):
        if family.id == family_id:
            family_list[i] = updated
            return updated
    raise HTTPException(status_code=404, detail="Family not found")

def delete_myfamily(family_id: int):
    for i, family in enumerate(family_list):
        if family.id == family_id:
            del family_list[i]
            return {"detail": "Deleted"}
    raise HTTPException(status_code=404, detail="Family not found")
