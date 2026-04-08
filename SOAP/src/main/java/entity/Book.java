package entity;


import io.quarkus.hibernate.orm.panache.PanacheEntityBase;
import jakarta.persistence.*;
import jakarta.xml.bind.annotation.XmlAccessType;
import jakarta.xml.bind.annotation.XmlAccessorType;
import lombok.*;

@Entity
@Table(name = "tbook")
@Getter @Setter @NoArgsConstructor @AllArgsConstructor
@XmlAccessorType(XmlAccessType.FIELD)
public class Book extends PanacheEntityBase {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "nBookID")
    public Integer id;

    @Column(name = "cTitle", nullable = false, length = 255)
    private String title;

    @Column(name = "nAuthorID", nullable = false)
    private Integer authorId;

    @Column(name = "nPublishingCompanyID", nullable = false)
    private Integer publisherId;

    @Column(name = "nPublishingYear", nullable = false)
    private int publishingYear;

    public Book(String title, int authorId, int publisherId, int publishingYear) {
        this.title = title;
        this.authorId = authorId;
        this.publisherId = publisherId;
        this.publishingYear = publishingYear;
    }
}