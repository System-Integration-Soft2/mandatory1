package entity;

import io.quarkus.hibernate.orm.panache.PanacheEntity;
import jakarta.persistence.*;
import lombok.*;

@Entity
@Table(name = "publisher")
@Getter @Setter @NoArgsConstructor @AllArgsConstructor
public class Publisher extends PanacheEntity {
    @Column(nullable = false, length = 40)
    private String name;
}