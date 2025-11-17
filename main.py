from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hospital API Working!"}

@app.get("/nearby-hospitals")
def hospitals(city: str):
    url = f"https://api.api-ninjas.com/v1/hospitals?city={city}"
    headers = {"X-Api-Key": "2807d5d08cmshbbbb52e3952b043p139574jsnb06bb02fc550"}
    res = requests.get(url, headers=headers)
    return res.json()
