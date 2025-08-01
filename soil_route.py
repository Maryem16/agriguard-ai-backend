from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/upload-soil/")
def upload_soil(data: schemas.SoilDataCreate, db: Session = Depends(get_db)):
    soil_model = models.SoilData(**data.dict())
    db.add(soil_model)
    db.commit()
    return {"message": "Soil data uploaded"}
