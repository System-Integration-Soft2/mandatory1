from fastapi import APIRouter, status
from app.models import Author, AuthorCreate, AuthorUpdate
from app.services import author_service

router = APIRouter(prefix="/authors", tags=["authors"])


@router.post("", response_model=Author, status_code=status.HTTP_201_CREATED)
def create_author(body: AuthorCreate):
    return author_service.create(body)


@router.get("/{id}", response_model=Author)
def get_author(id: int):
    return author_service.get_by_id(id)


@router.get("", response_model=list[Author])
def list_authors():
    return author_service.get_all()


@router.put("/{id}", response_model=Author)
def update_author(id: int, body: AuthorUpdate):
    return author_service.update(id, body)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_author(id: int):
    author_service.delete(id)
