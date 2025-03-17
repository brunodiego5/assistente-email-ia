from src.domain.entities.email_message import EmailMessage

def preview_email(message: EmailMessage, max_length: int = 100) -> str:
    """
    Exemplo de serviço de domínio que gera um preview do corpo do e-mail,
    sem depender de infraestrutura externa (DB, Rede, etc.).
    """
    body_preview = (message.body[:max_length] + '...') if len(message.body) > max_length else message.body
    return (
        f"De: {message.from_email}\n"
        f"Para: {message.to_email}\n"
        f"Assunto: {message.subject}\n\n"
        f"Corpo (preview):\n{body_preview}"
    )

def is_spam_by_subject(message: EmailMessage) -> bool:
    """
    Exemplo de método de domínio que aplica uma regra simples 
    (verificar se 'SPAM' está no assunto).
    """
    if "SPAM" in message.subject.upper():
        return True
    return False
