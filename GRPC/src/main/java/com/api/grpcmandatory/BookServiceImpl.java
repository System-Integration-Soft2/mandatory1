package com.api.grpcmandatory;

import book.BookServiceGrpc;
import book.Books;
import io.grpc.stub.StreamObserver;
import net.devh.boot.grpc.server.service.GrpcService;
import org.springframework.jdbc.core.JdbcTemplate;

import java.util.List;
import java.util.concurrent.CopyOnWriteArrayList;

@GrpcService
public class BookServiceImpl extends BookServiceGrpc.BookServiceImplBase {

    private final JdbcTemplate jdbc;
    private final List<StreamObserver<Books.Book>> subscribers = new CopyOnWriteArrayList<>();

    public BookServiceImpl(JdbcTemplate jdbc) {
        this.jdbc = jdbc;
    }

    @Override
    public void getBookById(Books.GetBookByIdRequest request, StreamObserver<Books.GetBookByIdResponse> responseObserver) {
        int bookId;
        try {
            bookId = Integer.parseInt(request.getId());
        } catch (NumberFormatException e) {
            responseObserver.onError(
                    io.grpc.Status.INVALID_ARGUMENT
                            .withDescription("Invalid book ID")
                            .asRuntimeException());
            return;
        }

        var rows = jdbc.queryForList(
                "SELECT nBookID, cTitle, nAuthorID, nPublishingCompanyID, nPublishingYear FROM tbook WHERE nBookID = ?",
                bookId);

        if (rows.isEmpty()) {
            responseObserver.onError(
                    io.grpc.Status.NOT_FOUND
                            .withDescription("Book not found")
                            .asRuntimeException());
            return;
        }

        var row = rows.get(0);
        Books.GetBookByIdResponse response = Books.GetBookByIdResponse.newBuilder()
                .setId(String.valueOf(row.get("nBookID")))
                .setTitle((String) row.get("cTitle"))
                .setAuthorId(String.valueOf(row.get("nAuthorID")))
                .setPublisherId(String.valueOf(row.get("nPublishingCompanyID")))
                .setPublishingYear(((Number) row.get("nPublishingYear")).intValue())
                .build();

        responseObserver.onNext(response);
        responseObserver.onCompleted();
    }


    @Override
    public void createBook(Books.CreateBookRequest request, StreamObserver<Books.CreateBookResponse> responseObserver) {
        var keyHolder = new org.springframework.jdbc.support.GeneratedKeyHolder();
        jdbc.update(connection -> {
            var ps = connection.prepareStatement(
                    "INSERT INTO tbook (cTitle, nAuthorID, nPublishingCompanyID, nPublishingYear) VALUES (?, ?, ?, ?)",
                    java.sql.Statement.RETURN_GENERATED_KEYS);
            ps.setString(1, request.getTitle());
            ps.setInt(2, Integer.parseInt(request.getAuthorId()));
            ps.setInt(3, Integer.parseInt(request.getPublisherId()));
            ps.setInt(4, request.getPublishingYear());
            return ps;
        }, keyHolder);

        String generatedId = String.valueOf(keyHolder.getKey());

        Books.CreateBookResponse response = Books.CreateBookResponse.newBuilder()
                .setId(generatedId)
                .setTitle(request.getTitle())
                .setAuthorId(request.getAuthorId())
                .setPublisherId(request.getPublisherId())
                .setPublishingYear(request.getPublishingYear())
                .build();

        // Notify WatchBooks subscribers
        Books.Book newBook = Books.Book.newBuilder()
                .setId(generatedId)
                .setTitle(request.getTitle())
                .setAuthorId(request.getAuthorId())
                .setPublisherId(request.getPublisherId())
                .setPublishingYear(request.getPublishingYear())
                .build();
        for (StreamObserver<Books.Book> subscriber : subscribers) {
            try {
                subscriber.onNext(newBook);
            } catch (Exception e) {
                subscribers.remove(subscriber);
            }
        }

        responseObserver.onNext(response);
        responseObserver.onCompleted();
    }

    @Override
    public void watchBooks(Books.WatchBooksRequest request, StreamObserver<Books.Book> responseObserver) {
        subscribers.add(responseObserver);
    }
}
