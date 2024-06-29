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


## Desafio Final
[arquivos](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/tree/0d3241cb1589e310c3df85e18a1237f1846961b0/Arquivos_sprint4)

### Evidências
[evidências](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/tree/49069f59be7555415e263f18720230739b9d236c/Arquivos_sprint4/Evid%C3%AAncias)

#### Certificados
- Certificado do curso AWS Partner: Accreditation
[certificado](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/47e6199dce93ba857c775202903b04d9fd8effaa/Certificado%203%20AWS.pdf)