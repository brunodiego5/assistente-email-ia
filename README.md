# Assistente de E-mail com IA

Este projeto tem como objetivo implementar um assistente automatizado para leitura e classificação inteligente de e-mails utilizando inteligência artificial, microserviços e tecnologias modernas.

## Visão Geral

O assistente conecta-se ao provedor de e-mails via IMAP (inicialmente Outlook), classifica automaticamente as mensagens utilizando IA e armazena resultados em um banco MongoDB. O usuário pode consultar facilmente as classificações através de uma API REST simples.

## Requisitos Principais (MVP v1.0)

### Funcionais:
- Leitura automática dos e-mails da caixa de entrada e spam (via IMAP).
- Classificação inteligente dos e-mails com IA.
- Armazenamento dos resultados em MongoDB.
- API REST para consulta das classificações.

### Não Funcionais:
- Estrutura baseada em Arquitetura Limpa e Domain-Driven Design (DDD).
- Suporte inicial para processamento de até 1000 e-mails.
- Credenciais protegidas via variáveis de ambiente.
- Logs estruturados para observabilidade e troubleshooting.

## Tecnologias Utilizadas
- Python
- MongoDB
- RabbitMQ
- IMAP (Outlook)
- APIs REST
- Inteligência Artificial (IA)
- Docker / Docker Compose

## Estrutura do Projeto

```
assistente-email-ia/
 ├─ docs/                  
 │   ├─ diagrams/         (Diagramas do sistema - C4 Model)
 ├─ microservices/
 │   ├─ gateway/
 │   ├─ email-ingestion/
 │   ├─ classification/
 │
 ├─ docker-compose.yml
 ├─ README.md
 └─ .gitignore
```

## Como Executar

### Pré-requisitos
- Docker
- Docker Compose

### Passos
1. Clone este repositório.
2. Rode o ambiente com Docker Compose:
   ```bash
   docker-compose up
   ```
3. Utilize a API REST exposta para interagir com o sistema.

## Documentação
Consulte a pasta `docs` para diagramas e documentações adicionais sobre o projeto.

