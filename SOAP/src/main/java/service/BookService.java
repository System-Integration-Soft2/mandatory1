package service;

import jakarta.enterprise.context.ApplicationScoped;
import jakarta.transaction.Transactional;
import entity.Author;
import entity.Book;
import entity.Publisher;
import fault.NotFoundFault;
import fault.ValidationFault;

import java.util.List;

@ApplicationScoped
public class BookService {

    @Transactional
    public long create(String title, long authorId, long publisherId, int publishingYear)
            throws ValidationFault {
        if (title == null || title.isBlank())
            throw new ValidationFault("title is required");
        if (publishingYear < 1900)
            throw new ValidationFault("publishingYear must be >= 1900");
        if (Author.findById(authorId) == null)
            throw new ValidationFault("Author with id " + authorId + " does not exist");
        if (Publisher.findById(publisherId) == null)
            throw new ValidationFault("Publisher with id " + publisherId + " does not exist");
        Book b = new Book(title.trim(), authorId, publisherId, publishingYear);
        b.persist();
        return b.id;
    }

    public Book getById(long id) throws NotFoundFault {
        Book b = Book.findById(id);
        if (b == null) throw new NotFoundFault("Book with id " + id + " not found");
        return b;
    }

    public List<Book> listAll() {
        return Book.listAll();
    }

    @Transactional
    public void update(long id, String title, long authorId, long publisherId, int publishingYear)
            throws NotFoundFault, ValidationFault {
        if (title == null || title.isBlank())
            throw new ValidationFault("title is required");
        if (publishingYear < 1900)
            throw new ValidationFault("publishingYear must be >= 1900");
        if (Author.findById(authorId) == null)
            throw new ValidationFault("Author with id " + authorId + " does not exist");
        if (Publisher.findById(publisherId) == null)
            throw new ValidationFault("Publisher with id " + publisherId + " does not exist");
        Book b = Book.findById(id);
        if (b == null) throw new NotFoundFault("Book with id " + id + " not found");
        b.setTitle(title.trim());
        b.setAuthorId(authorId);
        b.setPublisherId(publisherId);
        b.setPublishingYear(publishingYear);
    }

    @Transactional
    public void delete(long id) throws NotFoundFault {
        Book b = Book.findById(id);
        if (b == null) throw new NotFoundFault("Book with id " + id + " not found");
        b.delete();
    }
}