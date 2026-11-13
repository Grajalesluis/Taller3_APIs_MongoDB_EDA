# Taller 3 - APIs Públicas, MongoDB y EDA

Curso: Bases de Datos para Ciencia de Datos (UdeA).

## Descripción
Flujo completo de ciencia de datos:
1. **Extracción** de datos desde la [FreeToGame API](https://www.freetogame.com/api-doc) (videojuegos gratuitos, sin llave, ~400 registros).
2. **Almacenamiento RAW** en MongoDB (`taller3_db.raw_data`), usando el `id` de la API como `_id`.
3. **EDA** en Jupyter: selección de variables, 5 insights numéricos y 3 gráficos (1 torta + 2 libres).

## Estructura
| Archivo | Descripción |
|---|---|
| `ingesta.py` | Descarga la API y guarda el JSON crudo en MongoDB |
| `analisis.ipynb` | Lectura desde MongoDB, limpieza y EDA |
| `requirements.txt` | Dependencias |

## Cómo ejecutarlo
```bash
git clone <URL_DEL_REPO>
cd <carpeta>
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# MongoDB local corriendo en localhost:27017 (o define MONGO_URI para Atlas)
python ingesta.py
jupyter notebook analisis.ipynb
```
Para Atlas: `export MONGO_URI="mongodb+srv://usuario:clave@cluster.mongodb.net"`.

## Variables analizadas
`id`, `title`, `genre`, `platform`, `publisher`, `developer`, `release_date` (+ `year` derivada).
