from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  
import uvicorn

app = FastAPI()

# Configura CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

@app.get("/bienvenida")
def bienvenida():
    return {"mensaje": "¡Bienvenido a la API de FastAPI"}

articulo_db = [
    {"id": 10, "titulo": "Primer Artículo", "contenido": "Contenido del primer artículo."},
    {"id": 42, "titulo": "Segundo Artículo", "contenido": "Contenido del segundo artículo."},
    {"id": 43, "titulo": "Tercer Artículo", "contenido": "Contenido del tercer artículo."},
    {"id": 44, "titulo": "Cuarto Artículo", "contenido": "Contenido del cuarto artículo."},

]

# Rutas GET
@app.get("/")
def root():
    return {"mensaje": "¡Bienvenido a mi API con FastAPI!"}

@app.get("/articulos")
def obtener_articulos():
    return {"articulos": articulo_db}

@app.get("/articulos/{articulo_id}")
def obtener_articulo(articulo_id: int):
    for articulo in articulo_db:
        if articulo["id"] == articulo_id:
            return {"articulo": articulo}
    return {"error": f"Artículo con ID {articulo_id} no encontrado"}



# Ejecutar la aplicación
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
