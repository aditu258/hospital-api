from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()

# Use environment variable - do NOT hardcode secrets
RAPIDAPI_KEY = os.getenv("rapidapi-key", "")

@app.get("/")
def home():
    return {"message": "Hospital API Working!"}

@app.post("/hospital")
def hospital_info(payload: dict):
    name = payload.get("hospital_name", "")
    city = payload.get("city", "")
    host = "indian-hospitals.p.rapidapi.com"
    url = f"https://{host}/getByName"

    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": host
    }
    params = {}
    if name:
        params["name"] = name
    if city:
        params["city"] = city

    resp = requests.get(url, headers=headers, params=params, timeout=10)
    try:
        data = resp.json()
    except Exception:
        data = {"error": "Upstream returned non-json", "status": resp.status_code, "text": resp.text}
    return {"source": "rapidapi", "status": resp.status_code, "data": data}


# Optional: run locally with uvicorn (useful for local testing)
if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", "80"))  # Azure expects port 80 by default
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
