package com.api.grpcmandatory;

import book.BookServiceGrpc;
import book.Books;
import io.grpc.stub.StreamObserver;
import net.devh.boot.grpc.server.service.GrpcService;

import java.util.ArrayList;
import java.util.List;

@GrpcService
public class BookServiceImpl extends BookServiceGrpc.BookServiceImplBase {

    private final List<Books.Book> bookList = new ArrayList<>();

    private final List<StreamObserver<Books.Book>> subscribers = new ArrayList<>();


    @Override
    public void getBookById(Books.GetBookByIdRequest request, StreamObserver<Books.GetBookByIdResponse> responseObserver) {

        Books.Book found = bookList.stream()
                .filter(book -> book.getId().equals(request.getId()))
                .findFirst()
                .orElse(null);

        if (found == null) {
            responseObserver.onError(
                    io.grpc.Status.NOT_FOUND
                            .withDescription("Book not found")
                            .asRuntimeException()
            );
            return;
        }

        Books.GetBookByIdResponse response = Books.GetBookByIdResponse.newBuilder()
                .setId(found.getId())
                .setTitle(found.getTitle())
                .setAuthorId(found.getAuthorId())
                .setPublisherId(found.getPublisherId())
                .setPublishingYear(found.getPublishingYear())
                .build();

        responseObserver.onNext(response);
        responseObserver.onCompleted();
    }


    @Override
    public void createBook(Books.CreateBookRequest request, StreamObserver<Books.CreateBookResponse> responseObserver) {
        String generatedId = java.util.UUID.randomUUID().toString();

        Books.Book newBook = Books.Book.newBuilder()
                .setId(generatedId)
                .setTitle(request.getTitle())
                .setAuthorId(request.getAuthorId())
                .setPublisherId(request.getPublisherId())
                .setPublishingYear(request.getPublishingYear())
                .build();

        bookList.add(newBook);

        for (StreamObserver<Books.Book> subscriber : subscribers) {
            subscriber.onNext(newBook);
        }

        Books.CreateBookResponse response = Books.CreateBookResponse.newBuilder()
                .setId(generatedId)
                .setTitle(newBook.getTitle())
                .setAuthorId(newBook.getAuthorId())
                .setPublisherId(newBook.getPublisherId())
                .setPublishingYear(newBook.getPublishingYear())
                .build();

        responseObserver.onNext(response);
        responseObserver.onCompleted();
    }

    @Override
    public void watchBooks(Books.WatchBooksRequest request, StreamObserver<Books.Book> responseObserver) {
        subscribers.add(responseObserver);

        for (Books.Book book : bookList) {
            responseObserver.onNext(book);
        }
    }
}
