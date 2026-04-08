INSERT INTO author (name, surname) VALUES ('George', 'Orwell');
INSERT INTO author (name, surname) VALUES ('J.R.R.', 'Tolkien');

INSERT INTO publisher (name) VALUES ('Secker & Warburg');
INSERT INTO publisher (name) VALUES ('Allen & Unwin');

INSERT INTO book (title, author_id, publisher_id, publishing_year) VALUES ('1984', 1, 1, 1949);
INSERT INTO book (title, author_id, publisher_id, publishing_year) VALUES ('The Lord of the Rings', 2, 2, 1954);