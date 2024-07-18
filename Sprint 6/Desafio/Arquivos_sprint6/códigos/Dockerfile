# Use a imagem base que inclui Python e boto3
FROM python:3.8-slim

# Instale dependências necessárias
RUN pip install boto3

# Crie um diretório de trabalho
WORKDIR /app

# Copie o código Python para o diretório de trabalho no container
COPY . .

# Comando padrão para executar o script Python de ingestão
CMD ["python", "./teste.py"]
