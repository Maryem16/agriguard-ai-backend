# AgriGuard.AI Backend 

This is the FastAPI backend for AgriGuard.AI — a predictive carbon farming platform aligned with Net Zero and SDG 13.

## Features

-  Register farm plots by location
-  Upload soil sensor data (carbon %, pH, moisture)
-  Predict CO₂ sequestration (tons/hectare/year)
-  Recommend sustainable practices (e.g. no-till, compost)

## Tech Stack

- FastAPI, SQLAlchemy, Uvicorn
- SQLite (dev) or Supabase (prod)
- scikit-learn for ML (dummy model for now)

## API Endpoints

- `POST /register/` → Add farm info
- `POST /upload-soil/` → Upload soil sensor data
- `GET /predict/` → Get carbon prediction + recommendations

## Author

👩‍💻 Maryem Jebari — Backend Lead + ML Wizard
