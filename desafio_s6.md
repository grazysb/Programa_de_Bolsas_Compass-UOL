# Descrição da tarefa
Realizar uma Ingestão Batch dos arquivos CSV em Bucket Amazon S3 RAW Zone.

## Passos Executados
* Primeiro, adicionei os arquivos CSV (movies.csv e series.csv) no mesmo diretório onde o código Python e o Dockerfile estão localizados, para que o Docker consiga acessar esses arquivos durante a execução. 

* Em seguida, desenvolvi o código python para realizar a ingestão:

1. Configurei as credenciais de acesso.
2. Implementei funções para verificar se o bucket existe e criá-lo caso não exista.
3. Desenvolvi a função upload_to_s3 para enviar os arquivos para o S3.
4. Inicializei o cliente boto3 com as credenciais configuradas.
5. Verifiquei se o bucket já existe e criei-o se necessário.
6. Especifiquei os caminhos dos arquivos CSV locais.
7. Percorri cada arquivo e o carreguei para o S3 seguindo a estrutura especificada.

##### Estrutura "Raw Zone"
A "raw zone" é uma área do bucket S3 onde os dados são armazenados em seu formato bruto, sem qualquer tipo de transformação ou processamento.

* Depois, criei um Dockerfile para executar o script em python.
1. Utilizar uma imagem base do Python 3.8.
2. Definir o diretório de trabalho no contêiner.
3. Copiar os arquivos do diretório local para o diretório de trabalho no contêiner.
4. Instalar as dependências necessárias (boto3).
5. Definir o comando para executar o script Python.

* Por fim, executei os comandos de Docker build e Docker run.

### Evidências de execução

![execução do container](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/20bc68fa8a1228b0c537286e46c0ab57501a45f4/Arquivos_sprint6/evidencia2_s6.png)

![conteúdo do bucket](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/20bc68fa8a1228b0c537286e46c0ab57501a45f4/Arquivos_sprint6/evidencia2_s6.png)




## Explicação da análise do desafio final

## Arquivos Desafio
[arquivos](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/24c08a68cc130bd504c3e4fe78fe3b60e2c08616/Arquivos_sprint5)

### Evidências
[evidências](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/9cf3fd94e088e83707ec6e3a1d71af3244672e0e/Arquivos_sprint5/Evid%C3%AAncias)

#### Certificados
- Certificado do curso AWS Certified Cloud Practitioner
[certificado](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/0adca54ecffea514504c42ca1be2e57d92759589/Certificado%20s5%20-%20AWS.pdf)