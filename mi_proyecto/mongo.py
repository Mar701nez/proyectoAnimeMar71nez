import os
from pymongo import MongoClient

MONGO_URI = os.environ.get('MONGO_URI')

def obtener_db_mongo():
    if not MONGO_URI:
        return None
    cliente = MongoClient(MONGO_URI)
    return cliente['anime_db']  # Nombre de tu base de datos en Mongo