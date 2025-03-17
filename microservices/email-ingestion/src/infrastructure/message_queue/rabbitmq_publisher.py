# src/infrastructure/message_queue/rabbitmq_publisher.py
import pika
import json

class RabbitMQPublisher:
    """
    Classe responsável por publicar mensagens em uma fila do RabbitMQ.
    """

    def __init__(self, host: str, port: int = 5672, user: str = "guest", password: str = "guest"):
        credentials = pika.PlainCredentials(user, password)
        self.connection_params = pika.ConnectionParameters(host=host, port=port, credentials=credentials)

    def publish_incoming_email(self, queue_name: str, email_data: dict):
        """
        Publica um dicionário (ex.: dados do e-mail) em formato JSON na fila informada.
        """
        connection = pika.BlockingConnection(self.connection_params)
        channel = connection.channel()

        channel.queue_declare(queue=queue_name, durable=True)
        body = json.dumps(email_data)
        channel.basic_publish(
            exchange='',
            routing_key=queue_name,
            body=body,
            properties=pika.BasicProperties(delivery_mode=2)  # '2' para mensagem persistente
        )

        connection.close()

        print(f"Mensagem publicada na fila '{queue_name}'.")
