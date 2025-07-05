from fastapi import APIRouter
from typing import List

from app.crud.item import get_fire_data
from app.schemas.item import FireData

router = APIRouter()

@router.get("/fires", response_model=List[FireData])
def read_fires():
    """
    Endpoint to fetch fire data from the NASA FIRMS API.
    """
    return get_fire_data()
