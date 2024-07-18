# Descrição da tarefa
Praticar conhecimento de AWS fazendo consultas de SQL em arquivos diretamente no S3

## Passos Executados
Primeiro, garanti que a tabela de dados estivesse no formato CSV correto, e depois para garantir a compatibilidade, transformei o arquivo CSV para UTF-8. Em seguida, criei um bucket e subi a minha base de dados pra lá.

 Para gerar o código Python que executa as consultas S3 Select, comecei importando a biblioteca boto3 e configurando as credenciais AWS e informações do bucket. Criei uma função execute_s3_select para iniciar uma sessão AWS, criar um cliente S3 e executar a consulta S3 Select, processando e imprimindo os resultados da consulta. A função também captura e imprime qualquer exceção que ocorra durante a execução.

Escrevi três consultas SQL diferentes. A primeira consulta seleciona todas as linhas onde TMBDI é maior que 50 e ANO DESEMB é maior que 2015, limitando os resultados a 5 linhas. A segunda consulta calcula a soma e a média de TMBDI, convertendo os valores para float. A terceira consulta utiliza várias funções: uma condicional para categorizar TMBDI em 'ALTO' ou 'BAIXO', uma substring para extrair o ano de ANO DESEMB, uma função para calcular o comprimento da string RF DESPACHO e uma conversão de TMBDI para float.

## Desafio Final
[arquivos](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/24c08a68cc130bd504c3e4fe78fe3b60e2c08616/Arquivos_sprint5)

### Evidências
[evidências](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/9cf3fd94e088e83707ec6e3a1d71af3244672e0e/Arquivos_sprint5/Evid%C3%AAncias)

#### Certificados
- Certificado do curso AWS Certified Cloud Practitioner
[certificado](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/0adca54ecffea514504c42ca1be2e57d92759589/Certificado%20s5%20-%20AWS.pdf)