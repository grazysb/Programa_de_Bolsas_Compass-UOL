# Descrição da tarefa
Praticar conhecimento de AWS fazendo consultas de SQL em arquivos diretamente no S3

## Passos Executados
Primeiro, garanti que a tabela de dados estivesse no formato CSV correto, e depois para garantir a compatibilidade, transformei o arquivo CSV para UTF-8. Em seguida, criei um bucket e subi a minha base de dados pra lá.

 Para gerar o código Python que executa as consultas S3 Select, comecei importando a biblioteca boto3 e configurando as credenciais AWS e informações do bucket. Criei uma função execute_s3_select para iniciar uma sessão AWS, criar um cliente S3 e executar a consulta S3 Select, processando e imprimindo os resultados da consulta. A função também captura e imprime qualquer exceção que ocorra durante a execução.

Escrevi três consultas SQL diferentes. A primeira consulta seleciona todas as linhas onde TMBDI é maior que 50 e ANO DESEMB é maior que 2015, limitando os resultados a 5 linhas. A segunda consulta calcula a soma e a média de TMBDI, convertendo os valores para float. A terceira consulta utiliza várias funções: uma condicional para categorizar TMBDI em 'ALTO' ou 'BAIXO', uma substring para extrair o ano de ANO DESEMB, uma função para calcular o comprimento da string RF DESPACHO e uma conversão de TMBDI para float.

## Arquivos gerados
[acessar](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/main/Sprint%205/Desafio/Entreg%C3%A1veis)

### Evidências
[acessar](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/main/Sprint%205/Desafio/Entreg%C3%A1veis/Desafio/Evid%C3%AAncias%20Desafio)

![imagem](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/main/Sprint%205/Desafio/Entreg%C3%A1veis/Desafio/Evid%C3%AAncias%20Desafio/Captura%20de%20tela%202024-06-30%20132650.png)

![imagem](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/main/Sprint%205/Desafio/Entreg%C3%A1veis/Desafio/Evid%C3%AAncias%20Desafio/Captura%20de%20tela%202024-06-30%20145116.png)

![imagem](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/main/Sprint%205/Desafio/Entreg%C3%A1veis/Desafio/Evid%C3%AAncias%20Desafio/Captura%20de%20tela%202024-06-30%20145231.png)
