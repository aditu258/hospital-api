# main.py
from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()

RAPIDAPI_KEY ="2807d5d08cmshbbbb52e3952b043p139574jsnb06bb02fc550"

@app.get("/")
def home():
    return {"message": "Hospital API Working!"}

@app.post("/hospital")
def hospital_info(payload: dict):
    # expected payload: {"hospital_name": "AIIMS", "city": "Delhi"}
    name = payload.get("hospital_name", "")
    city = payload.get("city", "")
    host = "indian-hospitals.p.rapidapi.com"
    url = f"https://{host}/getByName"  # replace if provider path differs
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
    return {"source":"rapidapi", "status": resp.status_code, "data": data}
