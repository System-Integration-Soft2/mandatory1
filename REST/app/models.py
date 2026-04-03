from pydantic import BaseModel, Field

class AuthorCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=40)
    surname: str = Field(..., max_length=60)


class AuthorUpdate(BaseModel):
    name: str = Field(..., min_length=1, max_length=40)
    surname: str = Field(..., max_length=60)


class Author(BaseModel):
    id: int
    name: str
    surname: str