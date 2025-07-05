from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.my_family import MyFamily
from app.crud import crud_my_family

router = APIRouter()

@router.get("/myfamily", response_model=List[MyFamily])
def get_myfamily():
    return crud_my_family.get_myfamily()

@router.post("/myfamily", response_model=MyFamily)
def create_myfamily(family: MyFamily):
    return crud_my_family.create_myfamily(family)

@router.get("/myfamily/{family_id}", response_model=MyFamily)
def get_myfamily_by_id(family_id: int):
    return crud_my_family.get_myfamily_by_id(family_id)

@router.put("/myfamily/{family_id}", response_model=MyFamily)
def update_myfamily(family_id: int, updated: MyFamily):
    return crud_my_family.update_myfamily(family_id, updated)

@router.delete("/myfamily/{family_id}")
def delete_myfamily(family_id: int):
    return crud_my_family.delete_myfamily(family_id)
