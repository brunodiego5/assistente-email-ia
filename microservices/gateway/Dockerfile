FROM python:3.11-slim

WORKDIR /app

COPY ./src /app

# Instala dependências
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["python", "main.py"]
