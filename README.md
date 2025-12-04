# 🚀 SENA FastAPI - Actividad 3

API REST desarrollada con FastAPI para la gestión de artículos y demostración de diferentes tipos de endpoints.

## 📋 Descripción

Este proyecto es una API REST construida con FastAPI que implementa varios endpoints para demostrar el uso de:
- Parámetros de ruta (path parameters)
- Parámetros de consulta (query parameters)
- Operaciones CRUD básicas
- Gestión de CORS
- Respuestas JSON personalizadas

## ✨ Características

- ✅ API RESTful con FastAPI
- ✅ Gestión de artículos (CRUD básico)
- ✅ Endpoints con parámetros de ruta y consulta
- ✅ Configuración CORS habilitada
- ✅ Documentación automática con Swagger UI
- ✅ Validación de tipos con Pydantic
- ✅ Servidor Uvicorn integrado

## 🛠️ Tecnologías Utilizadas

- **Python**: Lenguaje de programación
- **FastAPI**: Framework web moderno y rápido
- **Uvicorn**: Servidor ASGI de alto rendimiento
- **Pydantic**: Validación de datos
- **Starlette**: Framework base de FastAPI

## 📦 Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/heiderrevelo333/sena-fastapi-actividad3.git
cd sena-fastapi-actividad3
```

### 2. Crear entorno virtual

```bash
# Windows
python -m venv fastapi-env
fastapi-env\Scripts\activate

# Linux/Mac
python3 -m venv fastapi-env
source fastapi-env/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## ▶️ Ejecución

### Ejecutar el servidor

```bash
# Opción 1: Usando Python directamente
python src/main.py

# Opción 2: Usando Uvicorn
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

El servidor estará disponible en: `http://localhost:8000`

## 📚 Documentación de la API

Una vez iniciado el servidor, puedes acceder a la documentación interactiva en:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🔌 Endpoints Disponibles

### 1. Raíz
```http
GET /
```
**Descripción**: Mensaje de bienvenida a la API

**Respuesta**:
```json
{
  "mensaje": "¡Bienvenido a mi API con FastAPI!"
}
```

---

### 2. Bienvenida
```http
GET /bienvenida
```
**Descripción**: Endpoint de bienvenida alternativo

**Respuesta**:
```json
{
  "mensaje": "¡Bienvenido a la API de FastAPI"
}
```

---

### 3. Listar Artículos
```http
GET /articulos
```
**Descripción**: Obtiene la lista completa de artículos

**Respuesta**:
```json
{
  "articulos": [
    {
      "id": 10,
      "titulo": "Primer Artículo",
      "contenido": "Contenido del primer artículo."
    },
    ...
  ]
}
```

---

### 4. Obtener Artículo por ID
```http
GET /articulos/{articulo_id}
```
**Descripción**: Obtiene un artículo específico por su ID

**Parámetros de ruta**:
- `articulo_id` (int): ID del artículo a buscar

**Ejemplo**:
```bash
GET /articulos/10
```

**Respuesta exitosa**:
```json
{
  "articulo": {
    "id": 10,
    "titulo": "Primer Artículo",
    "contenido": "Contenido del primer artículo."
  }
}
```

**Respuesta error**:
```json
{
  "error": "Artículo con ID 99 no encontrado"
}
```

---

### 5. Obtener Item
```http
GET /item/{item_id}?q={query}&activo={boolean}
```
**Descripción**: Endpoint con parámetros de ruta y consulta

**Parámetros**:
- `item_id` (int): ID del item (obligatorio)
- `q` (str): Parámetro de búsqueda (opcional, default: "")
- `activo` (bool): Estado del item (opcional, default: true)

**Ejemplo**:
```bash
GET /item/42?q=busqueda&activo=true
```

**Respuesta**:
```json
{
  "item_id": 42,
  "q": "busqueda",
  "activo": true
}
```

---

### 6. Saludo Personalizado
```http
GET /saludo/{nombre}
```
**Descripción**: Genera un saludo personalizado

**Parámetros de ruta**:
- `nombre` (str): Nombre de la persona

**Ejemplo**:
```bash
GET /saludo/Juan
```

**Respuesta**:
```json
{
  "saludo": "¡Hola, Juan!"
}
```

---

### 7. Configuración
```http
GET /config?modo={modo}&version={version}
```
**Descripción**: Obtiene configuración con parámetros obligatorios

**Parámetros de consulta**:
- `modo` (str): Modo de operación (obligatorio)
- `version` (float): Versión de la configuración (obligatorio)

**Ejemplo**:
```bash
GET /config?modo=produccion&version=1.5
```

**Respuesta**:
```json
{
  "modo": "produccion",
  "version": 1.5
}
```

## 📁 Estructura del Proyecto

```
sena-fastapi-actividad3/
│
├── src/
│   └── main.py              # Archivo principal de la aplicación
│
├── fastapi-env/             # Entorno virtual (no incluido en git)
│
├── requirements.txt         # Dependencias del proyecto
├── README.md               # Documentación del proyecto
└── .git/                   # Control de versiones
```

## 🧪 Pruebas

### Usando cURL

```bash
# Obtener todos los artículos
curl http://localhost:8000/articulos

# Obtener un artículo específico
curl http://localhost:8000/articulos/10

# Saludo personalizado
curl http://localhost:8000/saludo/Maria

# Item con parámetros
curl "http://localhost:8000/item/5?q=prueba&activo=false"

# Configuración
curl "http://localhost:8000/config?modo=desarrollo&version=2.0"
```

### Usando Python

```python
import requests

# Obtener todos los artículos
response = requests.get("http://localhost:8000/articulos")
print(response.json())

# Obtener un artículo específico
response = requests.get("http://localhost:8000/articulos/10")
print(response.json())
```

## 🔧 Configuración

### CORS
La API está configurada para aceptar solicitudes desde cualquier origen. Para producción, se recomienda especificar los orígenes permitidos:

```python
allow_origins=["http://localhost:3000", "https://tudominio.com"]
```

### Puerto
El servidor por defecto corre en el puerto 8000. Para cambiar el puerto, modifica el archivo `main.py`:

```python
uvicorn.run(app, host="0.0.0.0", port=TU_PUERTO)
```

## 📝 Dependencias

```
annotated-doc==0.0.3
annotated-types==0.7.0
anyio==4.11.0
click==8.3.0
colorama==0.4.6
fastapi==0.120.1
h11==0.16.0
idna==3.11
pydantic==2.12.3
pydantic_core==2.41.4
sniffio==1.3.1
starlette==0.48.0
typing-inspection==0.4.2
typing_extensions==4.15.0
uvicorn==0.38.0
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu característica (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto fue desarrollado como parte de una actividad del SENA (Servicio Nacional de Aprendizaje).

## 👤 Autor

**Heider Revelo**
- GitHub: [@heiderrevelo333](https://github.com/heiderrevelo333)

## 📞 Soporte

Si tienes alguna pregunta o problema, por favor abre un issue en el repositorio.

---

⭐️ Si este proyecto te fue útil, no olvides darle una estrella!