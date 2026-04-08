package service;

import jakarta.enterprise.context.ApplicationScoped;
import jakarta.transaction.Transactional;
import entity.Book;
import entity.Publisher;
import fault.ConflictFault;
import fault.NotFoundFault;
import fault.ValidationFault;

import java.util.List;

@ApplicationScoped
public class PublisherService {

    @Transactional
    public int create(String name) throws ValidationFault {
        if (name == null || name.isBlank())
            throw new ValidationFault("name is required");
        Publisher p = new Publisher(name.trim());
        p.persist();
        return p.id;
    }

    public Publisher getById(int id) throws NotFoundFault {
        Publisher p = Publisher.findById(id);
        if (p == null) throw new NotFoundFault("Publisher with id " + id + " not found");
        return p;
    }

    public List<Publisher> listAll() {
        return Publisher.listAll();
    }

    @Transactional
    public void update(int id, String name) throws NotFoundFault, ValidationFault {
        if (name == null || name.isBlank())
            throw new ValidationFault("name is required");
        Publisher p = Publisher.findById(id);
        if (p == null) throw new NotFoundFault("Publisher with id " + id + " not found");
        p.setName(name.trim());
    }

    @Transactional
    public void delete(int id) throws NotFoundFault, ConflictFault {
        Publisher p = Publisher.findById(id);
        if (p == null) throw new NotFoundFault("Publisher with id " + id + " not found");
        long refs = Book.count("publisherId", id);
        if (refs > 0)
            throw new ConflictFault("Publisher " + id + " is referenced by one or more books");
        p.delete();
    }
}