from fastapi import FastAPI
from app.routers import authors, publishing_companies

app = FastAPI()

app.include_router(authors.router)
app.include_router(publishing_companies.router)


@app.get("/")
def read_root():
  return {"message": "THIS BE REST YO"}