import requests
import pandas as pd
from IPython.display import display

# Substitua aqui com a sua chave de API do TMDB
api_key = "27edd5a09a2acda8847f8c0590aea70a"

# URL para obter os filmes mais bem avaliados
url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=pt-BR"

try:
    # Fazendo a requisição GET
    response = requests.get(url)

    # Verificando o código de status da resposta
    if response.status_code == 200:
        # Convertendo a resposta para JSON
        data = response.json()
        
        # Lista para armazenar os dados dos filmes
        filmes = []

        # Iterando sobre os resultados
        for movie in data['results']:
            df = {
                'Titulo': movie['title'],
                'Data de lançamento': movie['release_date'],
                'Visão geral': movie['overview'],
                'Votos': movie['vote_count'],
                'Média de votos': movie['vote_average']
            }
            filmes.append(df)

        # Criando um DataFrame do pandas
        df = pd.DataFrame(filmes)
        
        # Exibindo o DataFrame
        display(df)
    else:
        print(f"Erro na requisição: {response.status_code}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")