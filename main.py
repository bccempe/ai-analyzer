from fastapi import FastAPI

# 1. Creamos la instancia de la aplicación
app = FastAPI()

# 2. Definimos una ruta (endpoint)
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}