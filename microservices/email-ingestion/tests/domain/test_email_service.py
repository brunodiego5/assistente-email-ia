from src.domain.services.email_service import preview_email, is_spam_by_subject
from src.domain.entities.email_message import EmailMessage
from src.domain.value_objects.email_address import EmailAddress

def test_preview_email_curto():
    msg = EmailMessage(
        message_id="001",
        subject="Curto",
        body="Corpo",
        from_email=EmailAddress("alice@example.com"),
        to_email=EmailAddress("bob@example.com"),
    )
    result = preview_email(msg, max_length=10)
    # Como o corpo tem só 5 caracteres, não deve ter '...' ao final
    assert "Corpo" in result
    assert "..." not in result

def test_preview_email_longo():
    msg = EmailMessage(
        message_id="002",
        subject="Longo",
        body="Este texto é bastante grande para o preview",
        from_email=EmailAddress("alice@example.com"),
        to_email=EmailAddress("bob@example.com"),
    )
    result = preview_email(msg, max_length=10)
    # Deve conter '...' pois o corpo ultrapassa 10 caracteres
    assert "..." in result

def test_is_spam_by_subject_true():
    msg = EmailMessage(
        message_id="003",
        subject="SPAM Oferta",
        body="Não perca!",
        from_email=EmailAddress("spam@example.com"),
        to_email=EmailAddress("victim@example.com"),
    )
    assert is_spam_by_subject(msg) is True

def test_is_spam_by_subject_false():
    msg = EmailMessage(
        message_id="004",
        subject="Convite para reunião",
        body="Discussão de projeto",
        from_email=EmailAddress("alice@example.com"),
        to_email=EmailAddress("bob@example.com"),
    )
    assert is_spam_by_subject(msg) is False
