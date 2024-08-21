# Descrição da Tarefa
Processar e integrar dados da camada Trusted para a camada Refined, e realizar a modelagem desses dados
## Passos Executados
1. Recarregamento e Padronização dos Dados
Durante o processamento de dados, percebi que algumas colunas estavam nulas, o que comprometia a qualidade da análise, então precisei refazer a etapa que transformava os dados pro formato parquet.
* Recarreguei os dados na camada Trusted para garantir que todas as informações fossem corretamente processadas.
* Aproveitei a oportunidade para padronizar os nomes das colunas, traduzindo todos os nomes para o português, o que facilita a compreensão e o uso dos dados em análises futuras.
2. Integração dos Dados CSV e JSON
Após a padronização, foi necessário integrar os dados provenientes de arquivos CSV e JSON:
Combinei os dados dos arquivos CSV e JSON para criar um conjunto de dados mais completo, garantindo que todas as informações relevantes fossem incluídas na análise.
3. Processamento para a Camada Refined
O próximo passo foi processar os dados para a camada Refined:
Utilizei ferramentas de processamento de dados para transformar e refinar as informações, tornando-as prontas para análise detalhada e relatórios.
4. Criação de Crawler e Tabelas
Para organizar e estruturar os dados na camada Trusted e Refined, criei um Crawler:
O Crawler foi configurado para identificar e criar tabelas no AWS Glue com base nos dados refinados.
5. Desenvolvimento de Views e Consultas
Com os dados organizados, desenvolvi views personalizadas de cada questão que vou responder no desafio final para facilitar a análise.

### Observação
Alteração das Consultas: Mantive as consultas para:
Piores Avaliações: Consultas que identificam os filmes com as piores avaliações.
Avaliação por Década: Consultas que analisam a média de avaliações por década.
Substituí a consulta de Duração pela de Idioma, ajustando o foco das análises para:
Distribuição por Idioma: Identificação e análise da distribuição dos filmes por idioma, oferecendo uma visão sobre a diversidade linguística dos filmes analisados.

### Evidências de Execução
![imagens](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/main/Sprint%209/Evid%C3%AAncias/Captura%20de%20tela%202024-08-21%20161613.png)
![imagens](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/main/Sprint%209/Evid%C3%AAncias/Captura%20de%20tela%202024-08-21%20161706.png)
![imagens](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/main/Sprint%209/Evid%C3%AAncias/Captura%20de%20tela%202024-08-21%20161747.png)


### Arquivos Desafio
[arquivos](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/main/Sprint%209/Desafio/Entreg%C3%A1veis)

## Mudança das questões

### Quais são os filmes de ação e aventura com as piores avaliações?
Motivação: Identificar filmes com as avaliações mais baixas ajuda a entender onde e por que essas produções falharam, seja em termos de narrativa, direção, atuação ou outros aspectos técnicos e criativos. Essa análise pode destacar padrões comuns entre filmes mal recebidos e oferecer insights sobre os desafios do gênero.

### Qual década tem os filmes de ação e aventura com a média de avaliação mais baixa?
Motivação: Analisar a qualidade média dos filmes de ação e aventura por década pode revelar mudanças nas tendências cinematográficas e na qualidade das produções ao longo do tempo. Isso pode indicar períodos de declínio ou inovação dentro do gênero, oferecendo uma visão histórica das transformações e dos desafios enfrentados pelos cineastas.

### Qual é a média de avaliação dos filmes de ação e aventura por idioma?
Motivação: Analisar a média de avaliação por idioma permite entender como filmes em diferentes idiomas são recebidos pela crítica e pelo público. Isso pode revelar tendências de qualidade associadas a produções de certos países ou culturas e oferecer insights sobre a diversidade e a recepção global dos filmes de ação e aventura.

#### Objetivo da Análise:
Essa análise visa fornecer uma compreensão abrangente dos aspectos negativos e da qualidade diversificada dos filmes de ação e aventura. Ao identificar as piores avaliações, explorar a qualidade média por década e por idioma, podemos obter insights valiosos sobre a evolução, os desafios e a recepção cultural desse gênero popular em diferentes partes do mundo.







