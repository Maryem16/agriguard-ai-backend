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

@router.post("/register/")
def register_farm(farm: schemas.FarmCreate, db: Session = Depends(get_db)):
    farm_model = models.Farm(**farm.dict())
    db.add(farm_model)
    db.commit()
    return {"message": "Farm registered", "farm_id": farm_model.id}
