max_average_per_movie = 0
actor_with_max_average = ""

with open(r'C:\Users\grazy\Desktop\curso- python\Atividade_II\actors.csv', 'r', encoding='utf-8') as arquivo:
    arquivo.readline()
    
    for linha in arquivo:
        campos = linha.strip().split(',')
        
        if len(campos) >= 4:
            try:
                average_per_movie = float(campos[3].strip())
                actor = campos[0]
                
                if average_per_movie > max_average_per_movie:
                    max_average_per_movie = average_per_movie
                    actor_with_max_average = actor
            except ValueError:
                pass

if actor_with_max_average:
    print(f"O(a) ator/atriz com a maior media de receita de bilheteria bruta por filme: {actor_with_max_average}, com uma media de {max_average_per_movie:.2f}.")
else:
    print("Nao foram encontrados dados validos para calcular a media.")
