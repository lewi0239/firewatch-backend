from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.my_bag import MyBag
from app.crud import crud_my_bag

router = APIRouter()

@router.get("/mybags", response_model=List[MyBag])
def get_mybags():
    return crud_my_bag.get_mybags()

@router.post("/mybags", response_model=MyBag)
def create_mybag(mybag: MyBag):
    return crud_my_bag.create_mybag(mybag)

@router.get("/mybags/{bag_id}", response_model=MyBag)
def get_mybag(bag_id: int):
    return crud_my_bag.get_mybag(bag_id)

@router.put("/mybags/{bag_id}", response_model=MyBag)
def update_mybag(bag_id: int, updated: MyBag):
    return crud_my_bag.update_mybag(bag_id, updated)

@router.delete("/mybags/{bag_id}")
def delete_mybag(bag_id: int):
    return crud_my_bag.delete_mybag(bag_id)
