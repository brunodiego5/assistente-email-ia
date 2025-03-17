import re

class EmailAddress:
    """
    Value Object que representa um endereço de e-mail válido.
    Pode validar o formato ou aplicar outras regras.
    """

    _EMAIL_REGEX = r"(^[^\s@]+@[^\s@]+\.[^\s@]+$)"

    def __init__(self, address: str):
        if not self._is_valid_email(address):
            raise ValueError(f"Endereço de e-mail inválido: {address}")
        self._address = address

    def __str__(self):
        return self._address

    def __repr__(self):
        return f"EmailAddress({self._address})"

    @property
    def address(self):
        return self._address

    def _is_valid_email(self, email: str) -> bool:
        return re.match(self._EMAIL_REGEX, email) is not None
