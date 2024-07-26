# Descrição da tarefa
Realizar uma Ingestão de dados no formato JSON que complementem a análise que será feita no desafio final.

## Passos Executados
1. Configuração Inicial e Instalação de Dependências
Para iniciar o desenvolvimento do desafio, o primeiro passo foi preparar o ambiente de desenvolvimento. Instalei as bibliotecas necessárias que eram: boto3 para interação com o AWS S3 e tmdbv3api para acessar a API do TMDb. 
2. Criação da Layer para AWS Lambda
Com as bibliotecas instaladas, criei uma layer personalizada para a função Lambda. A layer permite incluir pacotes de dependência que não estão presentes no ambiente padrão do Lambda.
Primeiro, criei uma pasta chamada python e instalei as bibliotecas necessárias nesta pasta, Depois, compactei a pasta python em um arquivo ZIP, que seria usado para criar a layer no AWS Lambda, Então, acessei o console do AWS Lambda, criei uma nova layer e fiz o upload do arquivo layer.zip.
3. Desenvolvimento do Código
Desenvolvi um código que tem a tarefa de buscar dados de filmes da API TMDB, filtrar filmes de ação e aventura e armazenar os dados no S3. O código foi desenvolvido com as seguintes funcionalidades principais:
Configuração do TMDb e AWS S3: Configuração das credenciais e instâncias necessárias para interagir com a API TMDB e o bucket S3.
Busca e Filtragem de Filmes: A função Lambda obtém filmes populares da API TMDb, filtra aqueles que pertencem aos gêneros de ação e aventura, e prepara os dados para armazenamento.
Divisão dos Dados: Os dados são divididos em arquivos JSON, cada um contendo no máximo 100 registros, para garantir que os arquivos não se tornem muito grandes. 
4. Testes Locais
Antes de fazer o upload do código para o AWS Lambda, testei a função localmente com o auxilio de um arquivo .env.
5. Compactação e Upload para AWS Lambda
Após confirmar que o código estava funcionando corretamente, compactei o código da função Lambda em um arquivo ZIP e carreguei o arquivo para o AWS Lambda.
O arquivo ZIP foi enviado para a função Lambda no console AWS, e a configuração da função foi ajustada para usar a layer criada anteriormente.

6. Execução e Armazenamento dos Dados
A função Lambda foi executada, gerando cerca de 30 arquivos JSON. Essa quantidade de arquivos foi resultado da condição de limitar a 100 registros por arquivo, garantindo que cada arquivo JSON não excedesse o tamanho especificado. Os arquivos JSON foram armazenados no bucket S3 na estrutura de diretórios definida, organizados por data e conforme a filtragem dos dados. 

### Observação
Fiz a ingestão apenas dos dados de filmes porque a minha análise será voltada apenas para eles, e por isso não vi necessidade de realizar uma ingestão de dados novos sobre series. 

### Evidências de execução
![execução](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/main/Sprint%207/Evid%C3%AAncias/Captura%20de%20tela%202024-07-26%20123202.png)


![conteúdo do bucket](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/main/Sprint%207/Evid%C3%AAncias/Captura%20de%20tela%202024-07-26%20123240.png)


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
[arquivos](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/main/Sprint%207/Desafio/Entreg%C3%A1veis)

### Evidências
![imagens](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/main/Sprint%207/Evid%C3%AAncias/Captura%20de%20tela%202024-07-26%20123343.png)

![imagem](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/main/Sprint%207/Evid%C3%AAncias/Captura%20de%20tela%202024-07-26%20123513.png)