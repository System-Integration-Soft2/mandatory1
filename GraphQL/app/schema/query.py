import strawberry
from app.schema.types import Book, Author, Publisher
from app.services import author_service, publisher_service, book_service


@strawberry.type
class Query:
    @strawberry.field
    def book(self, id: int) -> Book | None:
        return book_service.get_by_id(id)

    @strawberry.field
    def authors(self) -> list[Author]:
        return author_service.get_all()

    @strawberry.field
    def publishers(self) -> list[Publisher]:
        return publisher_service.get_all()
