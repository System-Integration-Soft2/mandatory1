from fastapi import FastAPI
from app.routers import authors, publishers, books

app = FastAPI(title="Library API", version="1.0.0")

app.include_router(authors.router)
app.include_router(publishers.router)
app.include_router(books.router)


@app.get("/")
def read_root():
  return {"message": "THIS BE REST YO"}