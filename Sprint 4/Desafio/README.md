# Descrição da tarefa
1- Executar o carguru.py em um Contêiner Docker

2- Questionamento sobre a reutilização de conteiners

3- Criar um contêiner Docker para gerar hashes SHA-1 de strings fornecidas pelo usuário

## Passos Executados
1- Primeiro, criei um arquivo chamado Dockerfile no mesmo diretório do script carguru.py.
O conteúdo do Dockerfile especifica uma imagem base do Python, copia o script Python para o contêiner, instala quaisquer dependências necessárias e define o comando de execução do contêiner. Utilizei o comando docker build -t carguru-image . no terminal para construir a imagem Docker a partir do Dockerfile. Este comando criaou uma imagem chamada carguru-image. Após construir a imagem, executei o contêiner com o comando docker run --rm carguru-image. Este comando cria e inicia o contêiner a partir da imagem carguru-image e executa o script carguru.py. 

2- É possível reutilizar containers. Para reutilizar um container parado, você pode reiniciá-lo utilizando o comando docker start. Este comando inicia um container que foi previamente criado e executado.

3- Primeiramente, criei um script Python chamado app.py. Este script implementa o algoritmo necessário para:
 * Receber uma string via input.
 * Gerar o hash da string usando o algoritmo SHA-1.
 * Imprimir o hash na tela utilizando o método hexdigest.
 * Retornar ao passo 1 até que o usuário decida sair.
 
 Em seguida, criei um arquivo Dockerfile que define a imagem Docker necessária para executar o script Python. O Dockerfile utiliza uma imagem base do Python, copia o script para o contêiner, define o diretório de trabalho e especifica o comando para executar o script Python.
 Para construir a imagem Docker a partir do Dockerfile, executei o comando docker build -t mascarar-dados . Este comando cria uma imagem chamada mascarar-dados. Para iniciar um contêiner a partir da imagem criada e permitir a entrada de dados, utilizei o comando docker run -it mascarar-dados


## Arquivos gerados
[acessar](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/main/Sprint%204/Desafio/Entreg%C3%A1veis)

### Evidências
[acessar](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/main/Sprint%204/Evid%C3%AAncias)

![imagem](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/main/Sprint%204/Evid%C3%AAncias/ev2.png)

![imagem](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/main/Sprint%204/Evid%C3%AAncias/ev6.png)


