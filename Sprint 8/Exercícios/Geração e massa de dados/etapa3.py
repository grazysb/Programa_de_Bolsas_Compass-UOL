import random
import names

# Passo 3: Definir a semente e parâmetros
random.seed(40)
qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

# Passo 4: Gerar nomes únicos
aux = [names.get_full_name() for _ in range(qtd_nomes_unicos)]

print(f"Gerando {qtd_nomes_aleatorios} nomes aleatórios")

# Gerar lista de nomes aleatórios
dados = [random.choice(aux) for _ in range(qtd_nomes_aleatorios)]

# Passo 5: Salvar em um arquivo de texto
with open('nomes_aleatorios.txt', 'w') as file:
    for nome in dados:
        file.write(nome + '\n')

print("Arquivo 'nomes_aleatorios.txt' gerado com sucesso.")
