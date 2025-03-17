# src/infrastructure/db/mongo_repository.py
from typing import Optional
from pymongo import MongoClient
from src.domain.entities.email_message import EmailMessage

class EmailMessageRepository:
    """
    Repositório para persistir e recuperar objetos EmailMessage no MongoDB.
    """

    def __init__(self, mongo_url: str, db_name: str = "assistente_email"):
        self.client = MongoClient(mongo_url)
        self.db = self.client[db_name]
        self.collection = self.db["emails"]

    def save_email_message(self, message: EmailMessage) -> None:
        """
        Persiste o EmailMessage na coleção 'emails'.
        """
        doc = {
            "message_id": message.message_id,
            "subject": message.subject,
            "body": message.body,
            "from_email": str(message.from_email),
            "to_email": str(message.to_email),
            "date_received": message.date_received
        }
        self.collection.insert_one(doc)

    def find_by_message_id(self, message_id: str) -> Optional[dict]:
        """
        Retorna o documento armazenado para o message_id informado, ou None se não existir.
        """
        doc = self.collection.find_one({"message_id": message_id})
        return doc

    def list_all_messages(self) -> list:
        """
        Retorna uma lista de todos os e-mails armazenados.
        """
        return list(self.collection.find())

    def close_connection(self):
        self.client.close()
