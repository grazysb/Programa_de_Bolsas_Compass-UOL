contagem_filmes = {}

with open(r'C:\Users\grazy\Desktop\curso- python\Atividade_II\actors.csv', 'r', encoding='utf-8') as arquivo:
    next(arquivo)
    
    for linha in arquivo:
        campos = linha.strip().split(',')
        
        filme = campos[4].strip()
        
        if filme in contagem_filmes:
            contagem_filmes[filme] += 1
        else:
            contagem_filmes[filme] = 1

etapa4 = sorted(contagem_filmes.items(), key=lambda x: (-x[1], x[0]))

with open('etapa4.txt', 'w', encoding='utf-8') as arquivo_saida:
    for filme, frequencia in etapa4:
        arquivo_saida.write(f"O filme {filme} aparece {frequencia} vez(es) no dataset.\n")
