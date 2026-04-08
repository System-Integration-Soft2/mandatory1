package entity;


import io.quarkus.hibernate.orm.panache.PanacheEntity;
import jakarta.persistence.*;
import lombok.*;

@Entity
@Table(name = "book")
@Getter @Setter @NoArgsConstructor @AllArgsConstructor
public class Book extends PanacheEntity {
    @Column(nullable = false, length = 255)
    private String title;

    @Column(name = "author_id", nullable = false)
    private Long authorId;

    @Column(name = "publisher_id", nullable = false)
    private Long publisherId;

    @Column(name = "publishing_year", nullable = false)
    private int publishingYear;
}