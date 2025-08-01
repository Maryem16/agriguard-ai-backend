from pydantic import BaseModel

class FarmCreate(BaseModel):
    name: str
    latitude: float
    longitude: float

class SoilDataCreate(BaseModel):
    farm_id: int
    carbon: float
    ph: float
    moisture: float
