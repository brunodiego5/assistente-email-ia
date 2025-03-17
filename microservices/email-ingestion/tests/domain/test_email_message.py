from datetime import datetime
from src.domain.entities.email_message import EmailMessage
from src.domain.value_objects.email_address import EmailAddress

def test_criacao_email_message():
    msg = EmailMessage(
        message_id="abc123",
        subject="Teste",
        body="Corpo do e-mail",
        from_email=EmailAddress("alice@example.com"),
        to_email=EmailAddress("bob@example.com"),
    )

    assert msg.message_id == "abc123"
    assert msg.subject == "Teste"
    assert msg.body == "Corpo do e-mail"
    assert msg.from_email.address == "alice@example.com"
    assert msg.to_email.address == "bob@example.com"
    assert isinstance(msg.date_received, datetime)

def test_email_message_repr():
    msg = EmailMessage(
        message_id="abc123",
        subject="Teste",
        body="Corpo do e-mail",
        from_email=EmailAddress("alice@example.com"),
        to_email=EmailAddress("bob@example.com"),
    )
    representation = repr(msg)
    assert "EmailMessage" in representation
    assert "abc123" in representation
