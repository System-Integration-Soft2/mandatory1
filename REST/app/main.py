from fastapi import FastAPI
from app.routers import authors, publishing_companies, books

app = FastAPI()

app.include_router(authors.router)
app.include_router(publishing_companies.router)
app.include_router(books.router)


@app.get("/")
def read_root():
  return {"message": "THIS BE REST YO"}