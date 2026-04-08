package fault;

import jakarta.xml.ws.WebFault;
import lombok.Getter;

@WebFault(name = "NotFoundFault")
@Getter
public class NotFoundFault extends Exception {
    private final String message;

    public NotFoundFault(String message) {
        super(message);
        this.message = message;
    }
}

