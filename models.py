from sqlalchemy import Column, Integer, String, Float
from database import Base

class Farm(Base):
    __tablename__ = "farms"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)

class SoilData(Base):
    __tablename__ = "soil_data"
    id = Column(Integer, primary_key=True, index=True)
    farm_id = Column(Integer)
    carbon = Column(Float)
    ph = Column(Float)
    moisture = Column(Float)
