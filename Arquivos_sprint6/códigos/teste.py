import boto3
import os
from datetime import datetime

# Configurações do AWS S3
bucket_name = 'mybucket-raw-zone'
region_name = 'us-east-1'
aws_access_key_id = 'XXXXXXXXXXXXXXXXXXXX'
aws_secret_access_key = 'XXXXXXXXXXXXXXXXXXXX'
aws_session_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'

# Dados de configuração
raw_zone_prefix = 'raw_zone'
data_processamento = '2024/07/10'

# Função para verificar se o bucket existe
def check_bucket_exists(bucket_name, s3_client):
    try:
        s3_client.head_bucket(Bucket=bucket_name)
        return True
    except Exception as e:
        return False

# Função para criar o bucket se ele não existir
def create_bucket(bucket_name, region, s3_client):
    try:
        if region == 'us-east-1':
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region}
            )
        print(f'Bucket {bucket_name} criado com sucesso na região {region}.')
    except s3_client.exceptions.BucketAlreadyOwnedByYou:
        print(f'O bucket {bucket_name} já é de sua propriedade.')
    except Exception as e:
        print(f'Erro ao criar o bucket: {e}')

# Função para realizar a ingestão de um arquivo para o S3
def upload_to_s3(file_path, bucket_name, s3_key, s3_client):
    s3_client.upload_file(file_path, bucket_name, s3_key)

# Inicializa o cliente S3
s3_client = boto3.client(
    's3',
    region_name=region_name,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    aws_session_token=aws_session_token
)

# Verifica e cria o bucket se necessário
if not check_bucket_exists(bucket_name, s3_client):
    create_bucket(bucket_name, region_name, s3_client)
else:
    print(f'O bucket {bucket_name} já existe.')

# Diretórios locais onde os arquivos CSV estão localizados
local_files = {
    'filmes': '/app/desafio/movies.csv',
    'series': '/app/desafio/series.csv'
}

# Configurações específicas para cada tipo de dado
config = {
    'filmes': {
        'origem_dado': 'filmes',
        'formato_dado': 'CSV',
        'especificacao_dado': 'dados_integros'
    },
    'series': {
        'origem_dado': 'series',
        'formato_dado': 'CSV',
        'especificacao_dado': 'dados_integros'
    }
}

# Percorre cada arquivo e carrega para o S3
for tipo_dado, file_path in local_files.items():
    file_name = os.path.basename(file_path)
    s3_key = f"{raw_zone_prefix}/{config[tipo_dado]['origem_dado']}/{config[tipo_dado]['formato_dado']}/{config[tipo_dado]['especificacao_dado']}/{data_processamento}/{file_name}"
    upload_to_s3(file_path, bucket_name, s3_key, s3_client)
    print(f'Arquivo {file_name} enviado para o S3 na categoria {tipo_dado}.')

print('Processo de ingestão concluído.')