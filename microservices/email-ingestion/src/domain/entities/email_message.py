from datetime import datetime
from typing import Optional
from src.domain.value_objects.email_address import EmailAddress

class EmailMessage:
    """
    Entidade de domínio que representa um e-mail dentro do contexto de ingestão.
    """
    def __init__(
        self,
        message_id: str,
        subject: str,
        body: str,
        from_email: EmailAddress,
        to_email: EmailAddress,
        date_received: Optional[datetime] = None
    ):
        self.message_id = message_id
        self.subject = subject
        self.body = body
        self.from_email = from_email
        self.to_email = to_email
        self.date_received = date_received or datetime.utcnow()

    def __repr__(self):
        return (
            f"<EmailMessage(id={self.message_id}, "
            f"subject={self.subject}, "
            f"from_email={self.from_email}, "
            f"to_email={self.to_email}, "
            f"date_received={self.date_received})>"
        )
