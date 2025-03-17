# src/infrastructure/email/imap_connector.py
import imaplib
import email
from typing import List

class IMAPConnector:
    """
    Responsável por conectar-se ao servidor IMAP (Outlook, Gmail etc.),
    buscar mensagens e disponibilizá-las para o Domínio.
    """

    def __init__(self, host: str, port: int, user: str, password: str):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.connection = None

    def connect(self) -> None:
        """
        Efetua conexão IMAP com SSL e faz login.
        """
        try:
            self.connection = imaplib.IMAP4_SSL(self.host, self.port)
            self.connection.login(self.user, self.password)
            print("IMAP conectado com sucesso.")
        except Exception as e:
            print(f"Erro ao conectar no IMAP: {e}")
            raise

    def fetch_unread_messages(self) -> List[email.message.Message]:
        """
        Retorna uma lista de objetos email.message.Message
        representando e-mails não lidos.
        """
        if not self.connection:
            raise ConnectionError("IMAP não está conectado.")

        self.connection.select("INBOX")
        # Busca apenas e-mails não lidos (UNSEEN)
        status, message_ids = self.connection.search(None, "(UNSEEN)")

        if status != "OK":
            print("Não foi possível buscar mensagens não lidas.")
            return []

        messages = []
        for msg_id in message_ids[0].split():
            _, data = self.connection.fetch(msg_id, "(RFC822)")
            raw_email = data[0][1]
            msg = email.message_from_bytes(raw_email)
            messages.append(msg)

        return messages

    def mark_as_read(self, message_id: bytes) -> None:
        """
        Marca determinada mensagem (pelo ID IMAP) como lida (SEEN).
        """
        if not self.connection:
            raise ConnectionError("IMAP não está conectado.")

        try:
            # Exemplo de marcação:
            self.connection.store(message_id, "+FLAGS", "\\Seen")
        except Exception as e:
            print(f"Erro ao marcar como lido: {e}")
            raise

    def close(self) -> None:
        """
        Desconecta do servidor IMAP.
        """
        if self.connection:
            self.connection.logout()
            self.connection = None
            print("IMAP desconectado.")
