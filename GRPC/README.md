# gRPC BookService

A Spring Boot gRPC service for managing books. Supports creating books, fetching by ID, and streaming live book updates.

---

## Setup

**Prerequisites:** Java 17+, Maven

```bash
mvn spring-boot:run
```

Server starts on `localhost:9090` (plaintext — no TLS).

> **Postman tip:** Click the lock icon next to the URL and select **Disable TLS** before invoking any method.

---

## Proto Definition

**Package:** `book`  
**Service:** `BookService`

```proto
service BookService {
  rpc GetBookById(GetBookByIdRequest) returns (GetBookByIdResponse);
  rpc CreateBook(CreateBookRequest)   returns (CreateBookResponse);
  rpc WatchBooks(WatchBooksRequest)   returns (stream Book);
}
```

### Message Types

**Book**
| Field | Type | Description |
|---|---|---|
| id | string | UUID generated on creation |
| title | string | Book title |
| author_id | string | Reference to author |
| publisher_id | string | Reference to publisher |
| publishing_year | int32 | Year of publication |

---

## Methods

### CreateBook

Creates a new book and notifies all active `WatchBooks` subscribers.

**Request**
```json
{
  "title": "Den Grimme Ælling",
  "author_id": "author-1",
  "publisher_id": "publisher-1",
  "publishing_year": 1844
}
```

**Response**
```json
{
  "id": "75e67e1c-04f5-4b2d-83b7-63c1f715786b",
  "title": "Den Grimme Ælling",
  "author_id": "author-1",
  "publisher_id": "publisher-1",
  "publishing_year": 1844
}
```

---

### GetBookById

Fetches a single book by its UUID. Returns `NOT_FOUND` if no book matches.

**Request**
```json
{
  "id": "75e67e1c-04f5-4b2d-83b7-63c1f715786b"
}
```

**Response**
```json
{
  "id": "75e67e1c-04f5-4b2d-83b7-63c1f715786b",
  "title": "Den Grimme Ælling",
  "author_id": "author-1",
  "publisher_id": "publisher-1",
  "publishing_year": 1844
}
```

**Errors**
| Status | Description |
|---|---|
| NOT_FOUND | No book with the given ID exists |

---

### WatchBooks (Server Streaming)

Opens a persistent stream. Immediately emits all existing books, then emits each new book as it is created.

**Request**
```json
{}
```

**Response** — stream of `Book` messages, one per book.

> The stream stays open until the client disconnects. New books created via `CreateBook` are pushed to all active subscribers in real time.

---

## Notes

- Books are stored **in-memory** — all data is lost on restart.
- IDs are auto-generated UUIDs; do not supply them on creation.
- The service runs without TLS — connect using plaintext gRPC.