package entity;

import io.quarkus.hibernate.orm.panache.PanacheEntityBase;
import jakarta.persistence.*;
import jakarta.xml.bind.annotation.XmlAccessType;
import jakarta.xml.bind.annotation.XmlAccessorType;
import lombok.*;

@Entity
@Table(name = "tauthor")
@Getter @Setter @NoArgsConstructor @AllArgsConstructor
@XmlAccessorType(XmlAccessType.FIELD)
public class Author extends PanacheEntityBase {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "nAuthorID")
    public Integer id;

    @Column(name = "cName", nullable = false, length = 40)
    private String name;

    @Column(name = "cSurname", nullable = false, length = 60)
    private String surname;

    public Author(String name, String surname) {
        this.name = name;
        this.surname = surname;
    }
}
