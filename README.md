# Apresentação

Olá, me chamo Grazielly, tenho 18 anos, nasci em Irecê na Bahia, e hoje moro em Vitória da Conquista. No meu tempo livre, gosto muito de ler e acompanhar esportes. Além disso, tenho um grande interesse por matemática e gosto de estudar sobre.

## Formação

Estou no 1° semestre de Sistemas de Informação no IFBA de Vitória da Conquista. Anteriormente, fiz o Ensino Médio integrado com o curso técnico em Informática, também no IFBA, porém estudei mais a parte de hardware e manutenção de computadores. O Programa de Bolsas da Compass está sendo a minha primeira experiência profissional.

![logo_IFBA](https://lh6.googleusercontent.com/proxy/JoHYr7N1V2xxeTS2j0wQnRsolCnrti03jwelgCS-TAt2g8-aBK3JdxOTbQGEWWC6I11ZRiluWFTatAERpLRvVLiCBZ8sQBA)


# Resumos
## Linux
- **Comandos Básicos**: Aprendizado de comandos fundamentais como `ls`, `cd`, `cp`, `mv`, `rm`, `cat`, `echo`, `chmod`, `chown`, entre outros.
- **Gerenciamento de Pacotes**: Utilização de gerenciadores de pacotes como `apt` e `yum` para instalar, atualizar e remover software.
- **Permissões de Arquivos**: Entendimento de como funcionam as permissões de arquivos e diretórios no Linux.
- **Shell Scripting**: Criação de scripts básicos para automação de tarefas no bash.

## Git e GitHub
- **Conceitos Básicos**: Compreensão do que é controle de versão e sua importância.
- **Comandos Essenciais**: Uso de comandos como `git init`, `git clone`, `git add`, `git commit`, `git push`, `git pull`, e `git merge`.
- **Colaboração**: Utilização do GitHub para colaboração em projetos, incluindo pull requests, issues e forks.

## SQL
- **Consultas Básicas**: Utilização de comandos `SELECT`, `INSERT`, `UPDATE` e `DELETE`.
- **Joins**: Uso de diferentes tipos de joins (INNER, LEFT, RIGHT) para combinar dados de múltiplas tabelas.
- **Funções Agregadas**: Aplicação de funções como `SUM()`, `COUNT()`, `AVG()`, `MAX()`, e `MIN()`.
- **Filtros e Ordenação**: Utilização de `WHERE`, `ORDER BY` e `GROUP BY` para filtrar e ordenar dados.

## Python
- **Sintaxe Básica**: Aprendizado da sintaxe básica de Python, incluindo variáveis, loops, condicionais e funções.
- **Estruturas de Dados**: Utilização de listas, tuplas, dicionários e conjuntos.
- **Bibliotecas**: Exploração de bibliotecas populares como `pandas`, e `matplotlib` para manipulação e visualização de dados.
- **Programação Orientada a Objetos**: Criação de classes e objetos.

## Docker
- **Conceitos Básicos**: Compreensão do que são containers e por que são úteis.
- **Comandos Essenciais**: Utilização de comandos como `docker build`, `docker run`, `docker-compose`, `docker pull`, e `docker push`.
- **Dockerfile**: Criação de Dockerfiles para definir imagens personalizadas.
- **Docker Compose**: Uso de Docker Compose para orquestrar múltiplos containers.

## AWS Cloud Quest
- **Conceitos Básicos**: Introdução aos principais serviços da AWS, incluindo EC2, S3, e IAM.
- **Configuração e Gerenciamento**: Criação e gerenciamento de instâncias EC2, buckets S3 e bancos de dados RDS.
- **Segurança**: Configuração de políticas de segurança com IAM.

## Serverless Analytics
O serverless analytics permite que você execute análises de dados sem a necessidade de gerenciar servidores. Os serviços são totalmente gerenciados pela AWS, escalando automaticamente conforme necessário.

## Amazon Athena
Um serviço de consulta interativa que facilita a análise de dados diretamente no Amazon S3 usando SQL padrão.
#### Características
* Serverless: Não requer infraestrutura gerenciada.
* Integração com S3: Consulta dados diretamente nos buckets do S3.
* Fácil de usar: Suporte para SQL padrão.

## AWS Glue
Um serviço de ETL (Extract, Transform, Load) totalmente gerenciado.
#### Características
* Catálogo de Dados: Criação automática de catálogos de dados.
* Suporte a Workflows: Permite criar pipelines de ETL.
* Integração com outros serviços AWS: Como Amazon S3, Amazon RDS, e Amazon Redshift.

## Amazon Redshift
Um serviço de data warehousing rápido e totalmente gerenciado.
#### Características
* Alta performance: Suporte para consultas analíticas complexas.
* Escalabilidade: Capacidade de escalar de forma horizontal e vertical.
* Integração: Compatível com SQL e integração com outros serviços AWS.

## Amazon QuickSight
Um serviço de business intelligence (BI) que permite criar visualizações interativas e dashboards.
#### Características
* Fácil de usar: Interface intuitiva e criação rápida de visualizações.
* Análises embutidas: Capacidade de embutir análises em aplicativos.
* Auto-análise: Insights automáticos baseados em ML.

## Amazon EMR
Um serviço gerenciado de Hadoop que permite processar grandes volumes de dados usando frameworks como Apache Spark, HBase, Presto, e Flink.
#### Características
* Flexibilidade: Suporte para múltiplos frameworks de big data.
* Custo-efetivo: Paga-se apenas pelo que se usa.
* Integração com S3: Armazena dados no S3 para análise.
* Data Warehousing na AWS
* Objetivo: Centralizar grandes volumes de dados de diferentes fontes para análise e relatório.
#### Serviços:
* Amazon Redshift: Principal serviço de data warehousing.
* AWS Glue: Para ETL e integração de dados.
* Amazon S3: Armazenamento de dados de baixo custo e alta durabilidade.

## Spark
O Apache Spark é uma plataforma de processamento de dados em grande escala que permite realizar análises rápidas e eficientes em grandes volumes de dados. Desenvolvido originalmente pela AMPLab da Universidade da Califórnia, Berkeley, o Spark oferece uma estrutura unificada para o processamento de dados em lote e em tempo real.
#### Características
* Processamento em Memória: Spark realiza o processamento em memória (in-memory), o que o torna significativamente mais rápido que sistemas tradicionais como o Hadoop MapReduce.
* API Unificada: Oferece APIs em várias linguagens, incluindo Python, Java, Scala e R, permitindo flexibilidade para desenvolvedores.
* Liderança em Velocidade: Capaz de ser até 100 vezes mais rápido que o Hadoop em certas tarefas de processamento.
* Suporte a Diversos Workloads: Pode lidar com processamento em lote, streaming, SQL, machine learning e análise de gráficos, tudo dentro da mesma plataforma.
* Escalabilidade: Spark pode ser escalado em clusters de milhares de nós, permitindo o processamento de petabytes de dados.
* Suporte a Distribuição e Tolerância a Falhas: Gerencia o processamento distribuído e oferece tolerância a falhas, garantindo a execução de tarefas mesmo em casos de falhas de nó.

## Sprints

* Sprint 1: [Acessar](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/7bf3094b727b5e95491a731b14ded205b1eba58a/Sprint%201)
* Sprint 2: [Acessar](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/7bf3094b727b5e95491a731b14ded205b1eba58a/Sprint%202)
* Sprint 3: [Acessar](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/0a5d4abb8199117b9e3eee1b9d503a8316c127d2/Sprint%203)
* Sprint 4: [Acessar](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/7bf3094b727b5e95491a731b14ded205b1eba58a/Sprint%204)
* Sprint 5: [Acessar](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/fe8b7a87bdd00b7550792491396ea337f4ef39d5/Sprint%205)
* Sprint 6: [Acessar](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/7bf3094b727b5e95491a731b14ded205b1eba58a/Sprint%206)
* Sprint 7: [Acessar](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/fffa50beb7e5c154da6c18f6331d2f7807157ce2/README.md)
* Sprint 8: [Acessar](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/48352beb1195d1f697d8a368afe2ee0be5d9109a/Sprint%208)
* Sprint 9:[Acessar]()


## Explicação da análise do desafio final

O objetivo desta análise é explorar filmes do gênero ação e aventura para responder às seguintes perguntas:

1. **Qual é a média de avaliação dos filmes de ação e aventura por idioma?**
   - **Motivação:** Analisar a média de avaliação por idioma permite entender como filmes em diferentes idiomas são recebidos pela crítica e pelo público. Isso pode revelar tendências de qualidade associadas a produções de certos países ou culturas e oferecer insights sobre a diversidade e a recepção global dos filmes de ação e aventura.

2. **Quais são os filmes de ação e aventura com as piores avaliações?**
   - **Motivação:** Identificar filmes com avaliações baixas ajuda a entender falhas em narrativa, direção, atuação ou outros aspectos técnicos e criativos.

3. **Qual década tem os filmes de ação e aventura com a média de avaliação mais baixa?**
   - **Motivação:** Analisar a qualidade média dos filmes por década pode revelar tendências e mudanças na produção cinematográfica ao longo do tempo, indicando períodos de dificuldades ou transformações no gênero.

Esta análise visa não apenas responder perguntas específicas, mas também oferecer insights sobre a evolução e os desafios dos filmes de ação e aventura. Entender esses aspectos pode fornecer informações valiosas sobre a produção e recepção desse gênero popular.
