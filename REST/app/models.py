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
    
class PublisherCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=40)


class PublisherUpdate(BaseModel):
    name: str = Field(..., min_length=1, max_length=40)


class Publisher(BaseModel):
    id: int
    name: str

class BookCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    author_id: int
    publisher_id: int
    publishing_year: int = Field(..., ge=1900)


class BookUpdate(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    author_id: int
    publisher_id: int
    publishing_year: int = Field(..., ge=1900)


class Book(BaseModel):
    id: int
    title: str
    author_id: int
    publisher_id: int
    publishing_year: int
