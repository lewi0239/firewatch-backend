from pydantic import BaseModel

class FireReport(BaseModel):
    id: int
    location: str
    description: str
    status: str  # e.g., "active", "contained", "resolved"
