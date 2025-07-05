from fastapi import HTTPException
from typing import List
from app.schemas.my_bag import MyBag

# In-memory data store (for demo purposes)
mybags: List[MyBag] = []

def get_mybags() -> List[MyBag]:
    return mybags

def create_mybag(mybag: MyBag) -> MyBag:
    for m in mybags:
        if m.id == mybag.id:
            raise HTTPException(status_code=400, detail="ID already exists")
    mybags.append(mybag)
    return mybag

def get_mybag(bag_id: int) -> MyBag:
    for bag in mybags:
        if bag.id == bag_id:
            return bag
    raise HTTPException(status_code=404, detail="Bag not found")

def update_mybag(bag_id: int, updated: MyBag) -> MyBag:
    for i, bag in enumerate(mybags):
        if bag.id == bag_id:
            mybags[i] = updated
            return updated
    raise HTTPException(status_code=404, detail="Bag not found")

def delete_mybag(bag_id: int):
    for i, bag in enumerate(mybags):
        if bag.id == bag_id:
            del mybags[i]
            return {"detail": "Deleted"}
    raise HTTPException(status_code=404, detail="Bag not found")
