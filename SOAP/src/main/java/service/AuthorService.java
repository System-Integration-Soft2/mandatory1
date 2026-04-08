package service;


import jakarta.enterprise.context.ApplicationScoped;
import jakarta.transaction.Transactional;
import entity.Author;
import entity.Book;
import fault.ConflictFault;
import fault.NotFoundFault;
import fault.ValidationFault;

import java.util.List;

@ApplicationScoped
public class AuthorService {

    @Transactional
    public long create(String name, String surname) throws ValidationFault {
        if (name == null || name.isBlank())
            throw new ValidationFault("name is required");
        if (surname == null || surname.isBlank())
            throw new ValidationFault("surname is required");
        Author a = new Author(name.trim(), surname.trim());
        a.persist();
        return a.id;
    }

    public Author getById(long id) throws NotFoundFault {
        Author a = Author.findById(id);
        if (a == null) throw new NotFoundFault("Author with id " + id + " not found");
        return a;
    }

    public List<Author> listAll() {
        return Author.listAll();
    }

    @Transactional
    public void update(long id, String name, String surname)
            throws NotFoundFault, ValidationFault {
        if (name == null || name.isBlank())
            throw new ValidationFault("name is required");
        if (surname == null || surname.isBlank())
            throw new ValidationFault("surname is required");
        Author a = Author.findById(id);
        if (a == null) throw new NotFoundFault("Author with id " + id + " not found");
        a.setName(name.trim());
        a.setSurname(surname.trim());
    }

    @Transactional
    public void delete(long id) throws NotFoundFault, ConflictFault {
        Author a = Author.findById(id);
        if (a == null) throw new NotFoundFault("Author with id " + id + " not found");
        long refs = Book.count("authorId", id);
        if (refs > 0)
            throw new ConflictFault("Author " + id + " is referenced by one or more books");
        a.delete();
    }
}
