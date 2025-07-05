from pydantic import BaseModel

class FireData(BaseModel):
    latitude: float
    longitude: float
    bright_ti4: float
    scan: float
    track: float
    acq_date: str
    acq_time: str
    satellite: str
    confidence: str
    version: str
    bright_ti5: float
    frp: float
    daynight: str
