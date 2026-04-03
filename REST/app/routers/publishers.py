from fastapi import APIRouter, status
from app.models import Publisher, PublisherCreate, PublisherUpdate
from app.services import publisher_service

router = APIRouter(prefix="/publishers", tags=["publishers"])


@router.post("", response_model=Publisher, status_code=status.HTTP_201_CREATED)
def create_publisher(body: PublisherCreate):
    return publisher_service.create(body)


@router.get("/{publisher_id}", response_model=Publisher)
def get_publisher(publisher_id: int):
    return publisher_service.get_by_id(publisher_id)


@router.get("", response_model=list[Publisher])
def list_publishers():
    return publisher_service.get_all()


@router.put("/{publisher_id}", response_model=Publisher)
def update_publisher(publisher_id: int, body: PublisherUpdate):
    return publisher_service.update(publisher_id, body)


@router.delete("/{publisher_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_publisher(publisher_id: int):
    publisher_service.delete(publisher_id)
