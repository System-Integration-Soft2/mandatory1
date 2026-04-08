# Library GraphQL API

## Running the project

```bash
poetry install
poetry run uvicorn app.main:app --port 8001 --reload
```

## Queries

```graphql
book(id: Int!): Book
authors: [Author]
publishers: [Publisher]
```

## Mutations

```graphql
# Books
createBook(input: CreateBookInput!): Book
updateBook(id: Int!, input: UpdateBookInput!): Book
deleteBook(id: Int!): Boolean

# Authors
createAuthor(input: CreateAuthorInput!): Author
updateAuthor(id: Int!, input: UpdateAuthorInput!): Author
deleteAuthor(id: Int!): Boolean

# Publishers
createPublisher(input: CreatePublisherInput!): Publisher
updatePublisher(id: Int!, input: UpdatePublisherInput!): Publisher
deletePublisher(id: Int!): Boolean
```

---

## Types

```graphql
type Book {
  id: Int!
  title: String!
  authorId: Int!
  publisherId: Int!
  publishingYear: Int!
}

type Author {
  id: Int!
  name: String!
  surname: String!
}

type Publisher {
  id: Int!
  name: String!
}

input CreateBookInput {
  title: String!
  authorId: Int!
  publisherId: Int!
  publishingYear: Int!
}

input UpdateBookInput {
  title: String!
  authorId: Int!
  publisherId: Int!
  publishingYear: Int!
}

input CreateAuthorInput {
  name: String!
  surname: String!
}

input UpdateAuthorInput {
  name: String!
  surname: String!
}

input CreatePublisherInput {
  name: String!
}

input UpdatePublisherInput {
  name: String!
}
```
