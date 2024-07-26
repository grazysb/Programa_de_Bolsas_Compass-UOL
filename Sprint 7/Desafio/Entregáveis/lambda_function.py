import json
import boto3
from tmdbv3api import TMDb
from tmdbv3api import Movie
from datetime import datetime

# Configurações do TMDb
tmdb = TMDb()
tmdb.api_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'
movie = Movie()

# Configurações do AWS S3 com credenciais de acesso
s3 = boto3.client('s3', 
                  aws_access_key_id='XXXXXXXXXXXXXXX', 
                  aws_secret_access_key='XXXXXXXXXXXXXXXXXXX',
                  aws_session_token='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',  
                  region_name='us-east-1') 

bucket_name = 'mybucket-raw-zone'

def lambda_handler(event, context):
    all_movies = []
    page = 1
    max_size_mb = 5
    max_size_bytes = max_size_mb * 1024 * 1024  # Convert MB to bytes
    max_records_per_file = 100

    while True:
        # Obtém os filmes da página atual
        response = movie.popular(page=page)
        if not response:
            break

        all_movies.extend(response)
        page += 1

        # Limite de tamanho de dados já obtidos
        data = json.dumps(all_movies, default=str)
        if len(data.encode('utf-8')) > max_size_bytes:
            break

    # Filtra apenas os filmes de ação (genre_id 28) ou aventura (genre_id 12)
    filtered_movies = [
        {
            'id': m.id,
            'title': m.title,
            'release_date': m.release_date if m.release_date else '',
            'vote_average': m.vote_average,
            'overview': m.overview,
            'popularity': m.popularity,
            'original_language': m.original_language,
            'genre_ids': m.genre_ids if m.genre_ids else [],
            'budget': m.budget if hasattr(m, 'budget') else 'N/A',  # Inclui o orçamento se disponível
            'revenue': m.revenue if hasattr(m, 'revenue') else 'N/A',  # Inclui a receita se disponível
        }
        for m in all_movies
        if 28 in m.genre_ids or 12 in m.genre_ids
    ]

    # Divide os dados em arquivos com no máximo 100 registros
    def chunks(data, chunk_size):
        for i in range(0, len(data), chunk_size):
            yield data[i:i + chunk_size]

    filtered_movies_chunks = list(chunks(filtered_movies, max_records_per_file))

    # Envia os arquivos para o S3
    for i, chunk in enumerate(filtered_movies_chunks):
        # Converte o chunk para JSON
        chunk_data = json.dumps(chunk, default=str)
        
        # Verifica se o tamanho do chunk excede o limite
        if len(chunk_data.encode('utf-8')) > max_size_bytes:
            raise Exception("Tamanho do chunk excede o limite de 5 MB. Ajuste necessário.")

        # Define o caminho e nome do arquivo no S3 com data dinâmica
        current_date = datetime.now().strftime('%Y/%m/%d')
        file_key = f'raw/TMDB/JSON/movies/{current_date}/action_adventure_movies_part_{i+1}.json'
        
        # Envia o JSON para o S3
        s3.put_object(Bucket=bucket_name, Key=file_key, Body=chunk_data, ContentType='application/json')

    return {
        'statusCode': 200,
        'body': json.dumps('Filmes de ação e aventura foram enviados com sucesso para o S3!')
    }

# Para teste local, simule um evento e contexto
if __name__ == "__main__":
    mock_event = {}
    mock_context = {}
    print(lambda_handler(mock_event, mock_context))