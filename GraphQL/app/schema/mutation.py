import strawberry
from app.schema.types import (
    Book, Author, Publisher,
    CreateBookInput, UpdateBookInput,
    CreateAuthorInput, UpdateAuthorInput,
    CreatePublisherInput, UpdatePublisherInput,
)
from app.services import author_service, publisher_service, book_service


@strawberry.type
class Mutation:

# BOOKS
    @strawberry.mutation
    def create_book(self, input: CreateBookInput) -> Book:
        return book_service.create(input)

    @strawberry.mutation
    def update_book(self, id: int, input: UpdateBookInput) -> Book | None:
        return book_service.update(id, input)

    @strawberry.mutation
    def delete_book(self, id: int) -> bool:
        return book_service.delete(id)


# Authors
    @strawberry.mutation
    def create_author(self, input: CreateAuthorInput) -> Author:
        return author_service.create(input)

    @strawberry.mutation
    def update_author(self, id: int, input: UpdateAuthorInput) -> Author | None:
        return author_service.update(id, input)

    @strawberry.mutation
    def delete_author(self, id: int) -> bool:
        return author_service.delete(id)


# Publishers

    @strawberry.mutation
    def create_publisher(self, input: CreatePublisherInput) -> Publisher:
        return publisher_service.create(input)

    @strawberry.mutation
    def update_publisher(self, id: int, input: UpdatePublisherInput) -> Publisher | None:
        return publisher_service.update(id, input)

    @strawberry.mutation
    def delete_publisher(self, id: int) -> bool:
        return publisher_service.delete(id)
