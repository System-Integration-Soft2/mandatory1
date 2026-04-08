package entity;

import io.quarkus.hibernate.orm.panache.PanacheEntityBase;
import jakarta.persistence.*;
import jakarta.xml.bind.annotation.XmlAccessType;
import jakarta.xml.bind.annotation.XmlAccessorType;
import lombok.*;

@Entity
@Table(name = "tpublishingcompany")
@Getter @Setter @NoArgsConstructor @AllArgsConstructor
@XmlAccessorType(XmlAccessType.FIELD)
public class Publisher extends PanacheEntityBase {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "nPublishingCompanyID")
    public Integer id;

    @Column(name = "cName", nullable = false, length = 40)
    private String name;

    public Publisher(String name) {
        this.name = name;
    }
}