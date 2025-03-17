# src/application/use_cases/ingest_email_use_case.py
from src.domain.entities.email_message import EmailMessage
from src.domain.value_objects.email_address import EmailAddress
from src.infrastructure.email.imap_connector import IMAPConnector
from src.infrastructure.db.mongo_repository import EmailMessageRepository
from typing import Optional

class IngestEmailUseCase:
    """
    Caso de uso que orquestra todo o fluxo de ingestão de e-mails:
      1. Conecta ao IMAP.
      2. Busca mensagens não lidas.
      3. Converte cada mensagem em EmailMessage (Entidade).
      4. Persiste no MongoDB.
      5. (Opcional) Publica em fila RabbitMQ.
      6. Desconecta ao final.
    """

    def __init__(
        self,
        imap_host: str,
        imap_port: int,
        imap_user: str,
        imap_password: str,
        mongo_url: str,
        mongo_db_name: str = "assistente_email"
    ):
        self.imap_connector = IMAPConnector(imap_host, imap_port, imap_user, imap_password)
        self.repository = EmailMessageRepository(mongo_url, mongo_db_name)

    def execute(self):
        self.imap_connector.connect()
        messages = self.imap_connector.fetch_unread_messages()

        for raw_msg in messages:
            # Extraindo alguns campos básicos do e-mail
            message_id = raw_msg.get("Message-ID", "sem-id").strip()
            subject = raw_msg.get("Subject", "(sem assunto)").strip()
            from_ = raw_msg.get("From", "desconhecido").strip()
            to_ = raw_msg.get("To", "desconhecido").strip()

            # Criando entidade de domínio
            email_entity = EmailMessage(
                message_id=message_id,
                subject=subject,
                body=self._get_body_as_text(raw_msg),
                from_email=EmailAddress(from_),
                to_email=EmailAddress(to_)
            )
            # Persistindo no Mongo
            self.repository.save_email_message(email_entity)

        self.imap_connector.close()

    def _get_body_as_text(self, raw_msg) -> str:
        """
        Pega o corpo (text/plain) se existir, senão devolve vazio.
        """
        body = ""
        if raw_msg.is_multipart():
            for part in raw_msg.walk():
                content_type = part.get_content_type()
                if content_type == "text/plain":
                    body += part.get_payload(decode=True).decode(errors="replace")
        else:
            # Se não é multipart, pega diretamente
            body = raw_msg.get_payload(decode=True).decode(errors="replace")
        return body