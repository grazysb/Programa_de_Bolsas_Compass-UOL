import csv

# Passo 1: Criar e inicializar a lista com 20 nomes de animais 
animais = [
    "Golfinho", "Tubarão", "Baleia", "Polvo", "Foca", "Atum", "Baiacu",
    "Estrela-do-mar", "Cavalo-marinho", "Caranguejo", "Lula", "Pinguim", "Raia",
    "Tartaruga-marinha", "Peixe-palhaço", "Cavalo", "Gato", "Cachorro", "Lagosta", "Girafa"
]

# Ordenar a lista em ordem crescente
animais.sort()

# Passo 2: Iterar sobre os itens e imprimir um a um
for animal in animais:
    print(animal)

# Armazenar o conteúdo da lista em um arquivo CSV
with open('animais.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for animal in animais:
        writer.writerow([animal])
