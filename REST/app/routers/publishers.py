from fastapi import APIRouter, status
from app.models import Publisher, PublisherCreate, PublisherUpdate
from app.services import publisher_service

router = APIRouter(prefix="/publishers", tags=["publishers"])


@router.post("", response_model=Publisher, status_code=status.HTTP_201_CREATED)
def create_publisher(body: PublisherCreate):
    return publisher_service.create(body)


@router.get("/{id}", response_model=Publisher)
def get_publisher(id: int):
    return publisher_service.get_by_id(id)


@router.get("", response_model=list[Publisher])
def list_publishers():
    return publisher_service.get_all()


@router.put("/{id}", response_model=Publisher)
def update_publisher(id: int, body: PublisherUpdate):
    return publisher_service.update(id, body)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_publisher(id: int):
    publisher_service.delete(id)
