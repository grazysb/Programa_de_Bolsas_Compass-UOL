def convert_to_utf8(input_file_path, output_file_path, original_encoding):
    try:
        # Abrir o arquivo de entrada na codificação original
        with open(input_file_path, 'r', encoding=original_encoding) as input_file:
            # Ler o conteúdo do arquivo de entrada
            content = input_file.read()

        # Escrever o conteúdo em um novo arquivo com codificação UTF-8
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(content)

        print(f'Arquivo convertido para UTF-8 com sucesso e salvo em {output_file_path}')
    except Exception as e:
        print(f'Ocorreu um erro durante a conversão: {e}')

# Exemplo de uso
input_file_path = 'C:\\Users\\grazy\\Desktop\\desafios5\\tempo-medio-de-importacao-por-regiao-fiscal-consolidado-ATT.csv'
output_file_path = 'C:\\Users\\grazy\\Desktop\\desafios5\\tempo-medio-de-importacao-por-regiao-fiscal-consolidado-ATT-utf8.csv'
original_encoding = 'ISO-8859-1'  
convert_to_utf8(input_file_path, output_file_path, original_encoding)
