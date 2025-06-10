from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# CORS (herkese açık)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# JSON dosyasını yükle
with open("akademics.json", "r", encoding="utf-8") as f:
    akademisyenler = json.load(f)

@app.get("/akademisyenler")
def get_akademisyenler():
    return akademisyenler

@app.get("/akademisyen/{eposta}")
def get_akademisyen(eposta: str):
    for akademisyen in akademisyenler:
        if akademisyen["eposta"] == eposta:
            return akademisyen
    return {"error": "Akademisyen bulunamadı"} 
