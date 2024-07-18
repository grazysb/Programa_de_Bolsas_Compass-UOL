# Descrição da Tarefa Final
Normalizar a base de dados disponibilizada e produzir um modelo relacional e outro dimensional a partir da tabela primária.

## Passos Executados 
Inicialmente analisei os dados e a frequência que eles apareciam de acordo com as tabelas. Depois, dividi a tabela principal em várias tabelas para otimizar a busca e evitar repetição de dados, e as conectei de modo que elas ficassem ligadas à tabelas que tenham relações diretas. Por fim, inseri os dados em cada coluna.
Para a modelagem dimensional, eu centralizei a tabela "locacao", e distribuí as outras tabelas de acordo com seções mais específicas (informações sobre o carro, informaçoes sobre o cliente...), depois criei as views para cada dimensão. Achei mais fácil reorganizar as tabelas no formato normal antes de criar as views.
#### Observação
Senti dificuldade para criar as relações entre tabelas através dos códigos, então as executei manualmente pela interface do DBeaver



### Arquivos gerados
[arquivos](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/main/Sprint%202/Desafio/Entreg%C3%A1veis)

#### Evidências
![imagem](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/main/Sprint%202/Desafio/Entreg%C3%A1veis/Evid%C3%AAncias/modelo_dim.png)

![imagem](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/main/Sprint%202/Desafio/Entreg%C3%A1veis/Evid%C3%AAncias/modelo_rel.png)
