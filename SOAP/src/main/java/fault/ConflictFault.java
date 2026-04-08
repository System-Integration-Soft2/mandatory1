package fault;

import jakarta.xml.ws.WebFault;
import lombok.Getter;

@WebFault(name = "ConflictFault")
@Getter
public class ConflictFault extends Exception {
    private final String message;

    public ConflictFault(String message) {
        super(message);
        this.message = message;
    }
}