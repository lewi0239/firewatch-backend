from fastapi import APIRouter
from typing import List

from app.crud.item import get_fire_data
from app.schemas.item import FireData

router = APIRouter()

@router.get("/fires", response_model=List[FireData])
def read_fires(country: str = "USA", day_range: int = 1):
    """
    Retrieve fire data from NASA FIRMS API.

    - **country**: 3-letter country code (e.g., USA, CAN, MEX).
    - **day_range**: Number of days of data to retrieve (1-10).
    """
    fire_data = get_fire_data(country=country, day_range=day_range)
    return fire_data
