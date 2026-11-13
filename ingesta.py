"""
ingesta.py - Descarga datos de la FreeToGame API y los guarda CRUDOS en MongoDB.

Base de datos: taller3_db | Colección: raw_data
El _id de cada documento es el id que entrega la API, así que ejecutar el
script varias veces NO duplica datos (upsert).
"""
from dotenv import load_dotenv
import os
import requests
from pymongo import MongoClient, ReplaceOne

load_dotenv()

API_URL = "https://www.freetogame.com/api/games"
MONGO_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")  # o tu URI de Atlas
DB_NAME = "taller3_db"
COLLECTION = "raw_data"


def descargar():
    """Descarga todos los juegos (un solo endpoint, ~400 registros)."""
    resp = requests.get(API_URL, headers={"User-Agent": "taller3-bd/1.0"}, timeout=30)
    resp.raise_for_status()
    return resp.json()


def guardar(registros):
    """Inserta/actualiza cada registro usando el id de la API como _id."""
    col = MongoClient(MONGO_URI)[DB_NAME][COLLECTION]
    ops = []
    for r in registros:
        doc = dict(r)          # JSON tal cual llega, sin modificar campos
        doc["_id"] = r["id"]   # id de la API -> _id (evita duplicados)
        ops.append(ReplaceOne({"_id": doc["_id"]}, doc, upsert=True))
    col.bulk_write(ops)
    return col.count_documents({})


if __name__ == "__main__":
    data = descargar()
    print(f"Descargados desde la API: {len(data)} registros")
    total = guardar(data)
    print(f"Documentos en {DB_NAME}.{COLLECTION}: {total}")
