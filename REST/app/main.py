from fastapi import FastAPI
from app.routers import authors

app = FastAPI(title="Library API", version="1.0.0")

app.include_router(authors.router)


@app.get("/")
def read_root():
  return {"message": "THIS BE REST YO"}