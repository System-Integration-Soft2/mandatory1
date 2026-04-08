package fault;

import jakarta.xml.ws.WebFault;
import lombok.Getter;

@WebFault(name = "ValidationFault")
@Getter
public class ValidationFault extends Exception {
    private final String message;

    public ValidationFault(String message) {
        super(message);
        this.message = message;
    }
}
