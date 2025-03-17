import pytest
from src.domain.value_objects.email_address import EmailAddress

def test_email_address_valido():
    email = EmailAddress("joao@example.com")
    assert email.address == "joao@example.com"

def test_email_address_invalido():
    with pytest.raises(ValueError) as excinfo:
        EmailAddress("joaoexample.com")  # Falta '@'
    assert "Endereço de e-mail inválido" in str(excinfo.value)
