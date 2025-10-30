# sena-fastapi-actividad3

API que demuestre el uso de:
- Rutas básicas (`/`)
- Parámetros de ruta (`/item/{item_id}`, `/saludo/{nombre}`)
- Parámetros de consulta (query params como `?q=valor`, `?modo=dev`)

La API debe validar su comportamiento desde el navegador y desde la documentación automática disponible en `/docs`.

Clonar el repositorio
git clone https://github.com/<tu-usuario>/sena-fastapi-actividad3.git
cd sena-fastapi-actividad3

2️⃣ Crear y activar entorno virtual (opcional pero recomendado)
python -m venv fastapi-venv
En Windows:
fastapi-venv\Scripts\activate

En Mac/Linux:
source fastapi-venv/bin/activate

3️⃣ Instalar dependencias
pip install fastapi uvicorn

Método	Ruta	Descripción	Ejemplo de respuesta
GET	/	Ruta raíz que muestra mensaje de bienvenida	{"mensaje": "Bienvenido..."}
GET	/item/{item_id}	Devuelve información del item. Acepta parámetros de consulta opcionales (q, activo)	{"item_id": 42, "q": null, "activo": true}
GET	/item/{item_id}?q=busqueda&activo=false	Ejemplo con parámetros de consulta	{"item_id": 10, "q": "busqueda", "activo": false}
GET	/saludo/{nombre}	Devuelve un saludo personalizado	{"saludo": "¡Hola, María!"}
GET	/config?modo=dev&version=2.5	Devuelve configuración recibida	{"modo": "dev", "version": 2.5}
GET	/config	Usa valores por defecto cuando no se pasan parámetros	{"modo": "produccion", "version": 1.0}
GET	/config?modo=test&version=abc	Ejemplo de error de tipo en versión	422 Unprocessable Entity
