from fastapi import FastAPI
from pydantic import BaseModel
from ddgs import DDGS

app = FastAPI()


class PlateRequest(BaseModel):
    plate: str


@app.get("/")
def home():
    return {"status": "ok"}


@app.post("/lookup-vehicle")
def lookup_vehicle(request: PlateRequest):

    plate = request.plate.upper().replace(" ", "")

    results = []

    try:
        with DDGS() as ddgs:
            search_results = ddgs.text(
                f'"{plate}" matrícula vehículo',
                max_results=5
            )

            for item in search_results:
                results.append({
                    "title": item.get("title"),
                    "url": item.get("href"),
                    "snippet": item.get("body")
                })

    except Exception as e:
        return {
            "plate": plate,
            "status": "error",
            "message": str(e)
        }

    return {
        "plate": plate,
        "source": "web_search",
        "confidence": "low",
        "results_found": len(results),
        "results": results
    }
