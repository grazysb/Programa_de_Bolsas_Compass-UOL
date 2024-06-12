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


### Arquivos Gerados
[arquivos](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/tree/76a34d2273e132774781bab9f7bbd5a39da06d43/Arquivos_sprint4)