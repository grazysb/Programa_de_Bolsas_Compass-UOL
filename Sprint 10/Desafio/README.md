# Descrição da Tarefa
Montar um dashboard e através dele fazer uma análise do conjunto de dados.
Etapas Realizadas
1. Criação do Dashboard no Amazon QuickSight:
Com os dados prontos e carregados no QuickSight, o primeiro passo foi conectar a fonte de dados e desenvolver visualizações que pudessem responder às perguntas específicas da análise.

* Conexão com o Dataset: Conectei o QuickSight ao banco de dados trusted_data_db.new_fato_filmes para carregar e preparar os dados.
Criação de Visualizações Personalizadas: Utilizei gráficos de linhas, barras e tabelas para destacar as tendências dos dados. 

2. Consultas SQL Utilizadas
Questão 1: Média de Avaliação por Década
Objetivo: Determinar a média de avaliação dos filmes por década, considerando apenas filmes com mais de 100.000 votos, o que permite fazer uma análise mais coerente.
![imagem](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/main/Sprint%2010/Evid%C3%AAncias/Captura%20de%20tela%202024-09-08%20223428.png)

![imagem](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/main/Sprint%2010/Evid%C3%AAncias/Captura%20de%20tela%202024-09-08%20223452.png)

O gráfico de linhas mostra que as décadas mais antigas tendem a ter médias de avaliação mais altas, mas isso é muitas vezes devido ao baixo número de filmes avaliados. Décadas mais recentes, que têm uma quantidade maior de filmes, apresentam médias de avaliação mais baixas devido à diversidade de filmes e, consequentemente, à maior variação de qualidade.

Questão 2: Total de Filmes por Década
Objetivo: Contar o número total de filmes por década para entender o volume de produções em diferentes períodos.
Esta consulta, combinada com a anterior, mostra a correlação entre o número de filmes produzidos por década e suas respectivas médias de avaliação. Isso reforça a análise de que a avaliação média pode ser influenciada pelo volume de filmes disponíveis.

Questão 3: Distribuição de Idiomas Originais dos Filmes
Objetivo: Entender a distribuição dos idiomas originais dos filmes e sua representatividade no dataset.

![imagem](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/main/Sprint%2010/Evid%C3%AAncias/Captura%20de%20tela%202024-09-08%20223527.png)

O gráfico de barras revela que 93% dos filmes têm o inglês como idioma original, destacando a predominância de Hollywood no mercado global de cinema. Outros 26 idiomas estão representados, mas em uma proporção bem menor, refletindo o impacto global limitado das produções em idiomas não ingleses.
Questão 4: Total de Idiomas no Dataset
Objetivo: Calcular o número total de idiomas originais representados no dataset.

![imagem](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/main/Sprint%2010/Evid%C3%AAncias/Captura%20de%20tela%202024-09-08%20223539.png)

Esta consulta mostrou que o dataset contém filmes em 26 idiomas diferentes. Apesar de a maioria ser em inglês, a presença de outros idiomas reflete uma diversidade cultural que, embora pequena, está presente no cinema global.

O uso de consultas SQL personalizadas permitiu a criação de visualizações precisas e informativas no QuickSight, ajudando a entender as tendências e padrões no mercado cinematográfico global. Ao focar em métricas como a média de avaliação por década e a distribuição de idiomas, o dashboard oferece uma visão interessante do panorama de filmes, destacando a influência de Hollywood e a evolução das produções cinematográficas ao longo dos anos, mas levantando a questão das perspectivas e proporções de cada década.