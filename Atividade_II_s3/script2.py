total_gross = 0
num_filmes = 0

with open(r'C:\Users\grazy\Desktop\curso- python\Atividade_II\actors.csv', 'r', encoding='utf-8') as arquivo:
    arquivo.readline()
    
    for linha in arquivo:
        campos = linha.strip().split(',')
        
        if len(campos) >= 6:
            try:
                gross = float(campos[5].strip())
                total_gross += gross
                num_filmes += 1
            except ValueError:
                pass

if num_filmes > 0:
    media_gross = total_gross / num_filmes
    print(f"A media da receita de bilheteria bruta por principais filmes, considerando todos os atores: {media_gross}")
else:
    print("Nao foram encontrados dados validos para calcular a media.")
