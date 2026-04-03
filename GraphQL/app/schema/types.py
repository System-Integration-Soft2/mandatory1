import strawberry

@strawberry.type
class Book:
    id: int
    title: str
    author_id: int
    publisher_id: int
    publishing_year: int


@strawberry.type
class Author:
    id: int
    name: str
    surname: str


@strawberry.type
class Publisher:
    id: int
    name: str

@strawberry.input
class CreateBookInput:
    title: str
    author_id: int
    publisher_id: int
    publishing_year: int


@strawberry.input
class UpdateBookInput:
    title: str
    author_id: int
    publisher_id: int
    publishing_year: int


@strawberry.input
class CreateAuthorInput:
    name: str
    surname: str


@strawberry.input
class UpdateAuthorInput:
    name: str
    surname: str


@strawberry.input
class CreatePublisherInput:
    name: str


@strawberry.input
class UpdatePublisherInput:
    name: str
