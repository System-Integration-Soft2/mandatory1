package ws;


import jakarta.inject.Inject;
import jakarta.jws.WebMethod;
import jakarta.jws.WebParam;
import jakarta.jws.WebService;
import entity.Author;
import entity.Book;
import entity.Publisher;
import fault.ConflictFault;
import fault.NotFoundFault;
import fault.ValidationFault;
import service.AuthorService;
import service.BookService;
import service.PublisherService;

import java.util.List;

@WebService(
        serviceName     = "LibraryService",
        portName        = "LibraryPort",
        targetNamespace = "http://library.org/soap"
)
public class LibraryWebService {

    @Inject AuthorService    authorService;
    @Inject PublisherService publisherService;
    @Inject BookService      bookService;

    // ── Book ──────────────────────────────────────────────────
    @WebMethod
    public int createBook(
            @WebParam(name = "title") String title,
            @WebParam(name = "authorId") int authorId,
            @WebParam(name = "publisherId") int publisherId,
            @WebParam(name = "publishingYear") int publishingYear)
            throws ValidationFault {
        return bookService.create(title, authorId, publisherId, publishingYear);
    }

    @WebMethod
    public Book getBookById(
            @WebParam(name = "id") int id)
            throws NotFoundFault {
        return bookService.getById(id);
    }

    @WebMethod
    public void updateBook(
            @WebParam(name = "id") int id,
            @WebParam(name = "title") String title,
            @WebParam(name = "authorId") int authorId,
            @WebParam(name = "publisherId") int publisherId,
            @WebParam(name = "publishingYear") int publishingYear)
            throws NotFoundFault, ValidationFault {
        bookService.update(id, title, authorId, publisherId, publishingYear);
    }

    @WebMethod
    public void deleteBook(
            @WebParam(name = "id") int id)
            throws NotFoundFault {
        bookService.delete(id);
    }

    // ── Author ────────────────────────────────────────────────
    @WebMethod
    public int createAuthor(
            @WebParam(name = "name") String name,
            @WebParam(name = "surname") String surname)
            throws ValidationFault {
        return authorService.create(name, surname);
    }

    @WebMethod
    public Author getAuthorById(
            @WebParam(name = "id") int id)
            throws NotFoundFault {
        return authorService.getById(id);
    }

    @WebMethod
    public List<Author> listAuthors() {
        return authorService.listAll();
    }

    @WebMethod
    public void updateAuthor(
            @WebParam(name = "id") int id,
            @WebParam(name = "name") String name,
            @WebParam(name = "surname") String surname)
            throws NotFoundFault, ValidationFault {
        authorService.update(id, name, surname);
    }

    @WebMethod
    public void deleteAuthor(
            @WebParam(name = "id") int id)
            throws NotFoundFault, ConflictFault {
        authorService.delete(id);
    }

    // ── Publisher ─────────────────────────────────────────────
    @WebMethod
    public int createPublisher(
            @WebParam(name = "name") String name)
            throws ValidationFault {
        return publisherService.create(name);
    }

    @WebMethod
    public Publisher getPublisherById(
            @WebParam(name = "id") int id)
            throws NotFoundFault {
        return publisherService.getById(id);
    }

    @WebMethod
    public List<Publisher> listPublishers() {
        return publisherService.listAll();
    }

    @WebMethod
    public void updatePublisher(
            @WebParam(name = "id") int id,
            @WebParam(name = "name") String name)
            throws NotFoundFault, ValidationFault {
        publisherService.update(id, name);
    }

    @WebMethod
    public void deletePublisher(
            @WebParam(name = "id") int id)
            throws NotFoundFault, ConflictFault {
        publisherService.delete(id);
    }
}