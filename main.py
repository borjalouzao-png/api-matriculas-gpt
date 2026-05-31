from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PlateRequest(BaseModel):
    plate: str

@app.get("/")
def home():
    return {"status": "ok"}

@app.post("/lookup-vehicle")
def lookup_vehicle(request: PlateRequest):

    plate = request.plate.upper().replace(" ", "")

    return {
        "plate": plate,
        "brand": "Mercedes-Benz",
        "model": "Clase C",
        "first_registration_date": "2019-05-14",
        "confidence": "demo"
    }
