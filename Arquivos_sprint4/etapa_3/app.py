import hashlib

while True:
    string = input("Digite uma string para gerar o hash (ou digite 'exit' para sair): ")

    if string.lower() == 'exit':
        break

    hash_object = hashlib.sha1(string.encode())

    print("Hash SHA-1 da string:", hash_object.hexdigest())
