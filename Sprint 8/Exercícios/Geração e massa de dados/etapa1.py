import random

# Passo 1: Gerar uma lista de 250 inteiros aleatórios
lista = [random.randint(1, 100) for _ in range(250)]

# Passo 2: Inverter a lista usando o método reverse()
lista.reverse()

# Passo 3: Imprimir a lista invertida
print(lista)
