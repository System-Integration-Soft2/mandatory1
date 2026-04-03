from fastapi import APIRouter, Query, status
from app.models import Book, BookCreate, BookUpdate
from app.services import book_service

router = APIRouter(prefix="/books", tags=["books"])


@router.post("", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(body: BookCreate):
    return book_service.create(body)


@router.get("/{id}", response_model=Book)
def get_book(id: int):
    return book_service.get_by_id(id)


@router.get("", response_model=list[Book])
def list_books(
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
):
    return book_service.get_all(limit, offset)


@router.put("/{id}", response_model=Book)
def update_book(id: int, body: BookUpdate):
    return book_service.update(id, body)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(id: int):
    book_service.delete(id)
