from fastapi import APIRouter
from ml_model import predict_carbon
from ml_recommend import recommend_practices

router = APIRouter()

@router.get("/predict/")
def predict():
    carbon = predict_carbon()
    recommendations = recommend_practices(carbon)
    return {
        "predicted_carbon_storage": carbon,
        "unit": "tCO2e/hectare/year",
        "recommended_practices": recommendations
    }
