max_num_movies = 0
actor_with_max_movies = ""

with open(r'C:\Users\grazy\Desktop\curso- python\Atividade_II\actors.csv', 'r', encoding='utf-8') as arquivo:
    arquivo.readline()
    
    for linha in arquivo:
        num_quotes = 0
        campo_atual = ""
        campos = []
        
        for char in linha:
            if char == "," and num_quotes % 2 == 0:
                campos.append(campo_atual.strip())
                campo_atual = ""
            elif char == "\"":
                num_quotes += 1
            else:
                campo_atual += char
        
        campos.append(campo_atual.strip())
        
        if len(campos) >= 3:
            num_movies = int(campos[2])  
            
            if num_movies > max_num_movies:
                max_num_movies = num_movies
                actor_with_max_movies = campos[0]

print(f"O ator/atrizes com o maior numero de filmes: {actor_with_max_movies}, com um total de {max_num_movies} filmes.")
