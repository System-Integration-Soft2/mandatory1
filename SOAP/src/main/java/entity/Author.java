package entity;

import io.quarkus.hibernate.orm.panache.PanacheEntity;
import jakarta.persistence.*;
import lombok.*;

@Entity
@Table(name = "author")
@Getter @Setter @NoArgsConstructor @AllArgsConstructor
public class Author extends PanacheEntity {
    @Column(nullable = false, length = 40)
    private String name;

    @Column(nullable = false, length = 60)
    private String surname;
}
