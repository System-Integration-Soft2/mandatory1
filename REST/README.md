# Library REST API

## Running the project

```bash
poetry install
poetry run uvicorn app.main:app --port 8000 --reload
```

## Endpoints

### Books

```
POST   /books
GET    /books          ?limit=20&offset=0
GET    /books/{id}
PUT    /books/{id}
DELETE /books/{id}
```

### Authors

```
POST   /authors
GET    /authors
GET    /authors/{id}
PUT    /authors/{id}
DELETE /authors/{id}
```

### Publishers

```
POST   /publishers
GET    /publishers
GET    /publishers/{id}
PUT    /publishers/{id}
DELETE /publishers/{id}
```
