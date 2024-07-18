with open(r'C:\Users\grazy\Desktop\curso- python\Atividade_II\actors.csv', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

cabecalho = linhas.pop(0)

receita_por_ator = {}

for linha in linhas:
    campos = linha.strip().split(',')
    
    nome_ator = campos[0]
    
    if len(campos) >= 6 and campos[5]:
        try:
            receita_bruta = float(campos[5])
            
            if nome_ator in receita_por_ator:
                receita_por_ator[nome_ator] += receita_bruta
            else:
                receita_por_ator[nome_ator] = receita_bruta
        except ValueError:
            pass

atores_ordenados = sorted(receita_por_ator.items(), key=lambda x: x[1], reverse=True)

with open('Etapa5.txt', 'w', encoding='utf-8') as arquivo_saida:
    for nome_ator, receita_bruta in atores_ordenados:
        arquivo_saida.write(f"{nome_ator} - {receita_bruta}\n")
