# Backend Data - Python Flask

Servicio de datos que se conecta a MongoDB.

## Desarrollo Local

```bash
pip install -r requirements.txt
export MONGO_URI=mongodb://localhost:27017/
python app.py
```

## Build Local

```bash
docker build -t comments-backend-data:local .
docker run -p 3001:3001 -e MONGO_URI=mongodb://host.docker.internal:27017/ comments-backend-data:local
```

## Endpoints

- GET /data/comments - Lista comentarios desde MongoDB
- POST /data/comments - Crea comentario en MongoDB
- GET /health - Health check
