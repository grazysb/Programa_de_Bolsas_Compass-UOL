# Resumo dos assuntos da Sprint
## Docker
* Docker é uma plataforma aberta para desenvolvimento, envio e execução de aplicações. Ele permite que os desenvolvedores empacotem aplicações e suas dependências em um contêiner, que pode ser executado em qualquer ambiente que tenha o Docker instalado. Isso garante que a aplicação se comporte da mesma forma, independentemente de onde esteja sendo executada.
* Uma imagem Docker é um pacote imutável contendo tudo o que é necessário para executar uma aplicação, como código, bibliotecas e dependências. 
* Os contêineres são instâncias dessas imagens, que encapsulam a aplicação e suas dependências, garantindo execução consistente em qualquer ambiente, de forma isolada e eficiente.
* As redes Docker permitem a comunicação entre contêineres e o mundo exterior, facilitando a configuração e o gerenciamento da conectividade.
* Volumes são utilizados para persistir dados fora do ciclo de vida dos contêineres, garantindo que informações importantes não sejam perdidas.
* Docker Compose é uma ferramenta que define e gerencia aplicações multi-contêiner usando um arquivo YAML, simplificando a orquestração de aplicações complexas.
* Docker Swarm é uma ferramenta de orquestração que permite criar e gerenciar clusters de contêineres, proporcionando alta disponibilidade e balanceamento de carga.
* Kubernetes é uma plataforma de orquestração de contêineres que automatiza a implantação, escalonamento e operação de contêineres em clusters de servidores, oferecendo funcionalidades avançadas para ambientes complexos e distribuídos. 

### Guia Básico:
* docker pull <imagem>: Baixa uma imagem do Docker Hub.
* docker images: Lista todas as imagens locais.
* docker rmi <imagem>: Remove uma imagem localmente.
* docker run <opções> <imagem>: Cria e inicia um novo contêiner a partir de uma imagem.
* -d: Executa o contêiner em segundo plano (detached mode).
* -p <host_port>:<container_port>: Mapeia portas entre o host e o contêiner.
* --name <nome>: Nomeia o contêiner.
* -it: Permite a interação com o terminal do contêiner.
* docker ps: Lista os contêineres em execução.
* docker ps -a: Lista todos os contêineres, incluindo os parados.
* docker stop <contêiner>: Para um contêiner em execução.
* docker start <contêiner>: Inicia um contêiner parado.
* docker restart <contêiner>: Reinicia um contêiner.
* docker rm <contêiner>: Remove um contêiner parad


## Link para a pasta desafio
[desafio](https://github.com/grazysb/Programa_de_Bolsas_Compass-UOL/blob/954e5fb5fcfc893be0cb151d43cdde9beb24ea05/desafio_s4.md)

#### Link certificado AWS
