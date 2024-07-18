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
![execução do container](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/main/Sprint%206/Desafio/Entreg%C3%A1veis/evid%C3%AAncias/evidencia_s6.png)


![conteúdo do bucket](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/main/Sprint%206/Desafio/Entreg%C3%A1veis/evid%C3%AAncias/evidencia2_s6.png)


## Explicação da análise do desafio final

O objetivo desta análise é explorar filmes do gênero ação e aventura para responder às seguintes perguntas:

1. **Quais são os Top 5 filmes mais longos de ação e aventura lançados a partir do ano 2000?**
   - **Motivação:** Filmes longos geralmente indicam produções complexas e de grande investimento. Analisar esses filmes pode revelar como o tempo de tela é usado para desenvolver tramas detalhadas e envolventes, cruciais para o gênero.

2. **Quais são os filmes de ação e aventura com as piores avaliações?**
   - **Motivação:** Identificar filmes com avaliações baixas ajuda a entender falhas em narrativa, direção, atuação ou outros aspectos técnicos e criativos.

3. **Qual década tem os filmes de ação e aventura com a média de avaliação mais baixa?**
   - **Motivação:** Analisar a qualidade média dos filmes por década pode revelar tendências e mudanças na produção cinematográfica ao longo do tempo, indicando períodos de dificuldades ou transformações no gênero.

Esta análise visa não apenas responder perguntas específicas, mas também oferecer insights sobre a evolução e os desafios dos filmes de ação e aventura. Entender esses aspectos pode fornecer informações valiosas sobre a produção e recepção desse gênero popular.


## Arquivos Desafio
[arquivos](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/main/Sprint%206/Desafio/Entreg%C3%A1veis)

### Evidências
[evidências](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/main/Sprint%206/Desafio/Entreg%C3%A1veis/evid%C3%AAncias)

