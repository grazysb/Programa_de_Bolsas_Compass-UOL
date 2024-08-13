
# Descrição da Tarefa
Processar e integrar dados da camada Raw Zone para a camada Trusted, utilizando o Apache Spark através do serviço AWS Glue. O objetivo é gerar uma visão padronizada dos dados, armazená-los no formato PARQUET no S3, e torná-los acessíveis via AWS Athena.
## Passos Executados
1. Criei um novo database chamado raw_data no Glue Data Catalog para catalogar as tabelas na camada Trusted.
2. Preparei o bucket S3 para armazenar os dados processados da camada Trusted, estruturando diretórios específicos para dados JSON e CSV.
3. Configurei crawlers no AWS Glue para catalogar os dados brutos na Raw Zone. Esses crawlers escanearam os diretórios no S3, identificaram os esquemas dos arquivos CSV e JSON, e criaram tabelas correspondentes no Glue Data Catalog. Isso facilitou o acesso e o processamento dos dados nos jobs Spark subsequentes.
4. Criei um Job no AWS Glue para processar arquivos CSV da camada Raw Zone. O job foi configurado para ler os dados da tabela CSV existente, previamente catalogada pelo crawler.
5. Desenvolvi um script em PySpark para:
Ler e transformar os dados CSV.
Persistir os dados processados na camada Trusted no formato PARQUET.
6. Executei o Job e validei a gravação dos dados na camada Trusted, criando uma tabela externa no AWS Athena para confirmar o formato PARQUET.

* Processamento dos Dados JSON
Criei um Job no AWS Glue para processar dados JSON provenientes da API TMDB,  configurado para ler dados da tabela JSON existente na Raw Zone.
Desenvolvi um script em PySpark para:
Ler e transformar os dados JSON.
Persistir os dados processados na camada Trusted no formato PARQUET, particionados por data.
Execução e Validação: Executei o Job e confirmei a gravação dos dados na camada Trusted, validando o particionamento e criando uma tabela externa no AWS Athena.

* Consulta dos Dados na Camada Trusted via AWS Athena
Criação de Tabelas Externas: Criei tabelas externas no AWS Athena para acessar os dados na Trusted Zone, utilizando comandos SQL para definir a estrutura e o local dos dados no S3.

* Execução de Consultas SQL: Realizei consultas SQL no AWS Athena para garantir que os dados estavam no formato correto e acessíveis para análise.

### Evidências de Execução
![imagens](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/main/Sprint%208/Desafio/Entreg%C3%A1veis/Captura%20de%20tela%202024-08-13%20180202.png)
![imagens](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/main/Sprint%208/Desafio/Entreg%C3%A1veis/Captura%20de%20tela%202024-08-13%20180231.png)

### Arquivos Desafio
[arquivos](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/main/Sprint%208/Desafio/Entreg%C3%A1veis)

## Explicação das questões
O objetivo desta análise é explorar dados extraídos da API do TMDB para filmes do gênero ação e aventura, focando em várias dimensões relevantes, como orçamento, popularidade, idioma, e avaliações. Esses dados são essenciais para responder às seguintes perguntas e fornecer insights valiosos sobre a produção e recepção desses filmes.

#### Quais são os Top 5 filmes mais longos de ação e aventura lançados a partir do ano 2000?
Motivação: Filmes com longas durações geralmente envolvem produções complexas e altos investimentos, refletidos em aspectos como desenvolvimento de enredo, efeitos visuais, e caracterização dos personagens. Analisar esses filmes pode revelar como o tempo de tela é utilizado para criar tramas detalhadas e envolventes, que são cruciais para o sucesso em gêneros como ação e aventura.

#### Quais são os filmes de ação e aventura com as piores avaliações?
Motivação: Identificar os filmes com as piores avaliações ajuda a entender as razões por trás do fracasso de certos filmes, sejam elas problemas na narrativa, direção, atuação ou falhas técnicas. Esse entendimento pode ser crucial para evitar os mesmos erros em futuras produções.

#### Qual década tem os filmes de ação e aventura com a média de avaliação mais baixa?
Motivação: Analisar a qualidade média dos filmes por década pode revelar tendências e mudanças na indústria cinematográfica ao longo do tempo. Isso pode indicar períodos em que o gênero enfrentou desafios ou, inversamente, evoluiu e se adaptou a novas expectativas do público.

##### Dados Extraídos e Sua Relevância
* Orçamento (Budget): O orçamento é um dos principais indicadores do nível de investimento em um filme. Ele pode estar relacionado à qualidade da produção, efeitos especiais, elenco, e outros recursos que afetam diretamente a percepção do filme pelo público. Comparar orçamentos entre filmes de sucesso e fracasso pode fornecer insights sobre a eficácia do gasto em produções de ação e aventura.

* Popularidade (Popularity): Este dado reflete o interesse do público em determinado filme, que pode ser influenciado por campanhas de marketing, a fama do elenco, ou a recepção crítica inicial. Filmes populares nem sempre são os mais bem avaliados, mas entender essa métrica pode ajudar a analisar o impacto cultural e comercial de cada produção.

* Idioma Original (Original Language): O idioma de um filme pode afetar sua recepção em diferentes mercados e determinar sua acessibilidade para públicos globais. A análise da distribuição de idiomas entre os filmes de ação e aventura pode fornecer insights sobre a globalização do gênero e a penetração em diferentes mercados internacionais.

* Data de Lançamento (Release Date): Entender o período de lançamento é essencial para contextualizar o filme dentro de tendências históricas e sociais, como o avanço da tecnologia em efeitos especiais ou mudanças nos gostos do público. Essa métrica também permite a comparação de filmes dentro de períodos específicos, como décadas.

* Média de Votos (Vote Average): A média de votos é um indicativo direto da recepção crítica e popular de um filme. Avaliações baixas podem sinalizar problemas significativos, enquanto altas avaliações podem indicar sucesso tanto crítico quanto comercial. Comparar essas avaliações entre diferentes períodos e orçamentos pode fornecer uma compreensão mais profunda da relação entre qualidade percebida e sucesso financeiro.

#### Finalidade da Análise
Esta análise não se limita a responder perguntas específicas sobre os filmes de ação e aventura, mas também visa oferecer insights sobre a evolução, os desafios e as estratégias que influenciam o sucesso ou fracasso dessas produções. Ao entender esses aspectos, pode-se obter informações valiosas para produtores, diretores e outros stakeholders da indústria cinematográfica, auxiliando em decisões sobre investimentos futuros, estratégias de marketing, e desenvolvimento de conteúdo.






