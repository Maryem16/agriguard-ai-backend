from fastapi import FastAPI
import register_route, soil_route, predict_route
from database import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AgriGuard.AI")

app.include_router(register_route.router)
app.include_router(soil_route.router)
app.include_router(predict_route.router)
