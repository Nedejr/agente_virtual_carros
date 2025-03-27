# Agente Virtual Carros

Agente virtual que permite consultar opções de carros em uma base de dados SQlite.

## Tecnologias Utilizadas

- Python 3.12
- Flask (backend)
- SQLAlchemy, SQlite (banco de dados)
- requests para requisições no server

## Funcionalidades

O sistema implementa um esquema para representar automóveis no banco de dados, contendo os seguintes atributos:

- Marca: Fabricante do veículo (ex.: Toyota, Ford, Honda).
- Modelo: Nome do modelo específico do automóvel (ex.: Corolla, Fiesta, Civic).
- Ano: Ano de fabricação do veículo.
- Tipo de combustível: Combustível utilizado pelo veículo (ex.: Gasolina, Diesel, Elétrico, Flex).
- Cor: Cor predominante do automóvel.
- Quilometragem: Distância total percorrida pelo veículo.
- Preço: Preço de venda do automóvel
- Número de portas: Quantidade de portas do automóvel.
- Câmbio: Tipo de câmbio utilizado (ex.: Manual, Automático).
- Observação : Características adicionais do automóvwl

Para popular o banco de dados, o sistema conta com um script automatizado que insere pelo menos 100 registros de veículos com dados simulados. Esses dados são gerados de forma randômica, garantindo diversidade de marcas, modelos, anos, combustíveis e outras características.

### Aplicação Interativa via Terminal

A aplicação permite interação direta via terminal, oferecendo uma experiência fluida ao usuário por meio de um agente virtual. A dinâmica da interação segue os seguintes passos:

1. Início da Aplicação

Ao ser executada, a aplicação apresenta um agente virtual que cumprimenta o usuário e oferece assistência na busca por veículos.

2. Coleta de Critérios de Busca

O agente faz perguntas ao usuário para entender suas preferências, como:

- Marca desejada.
- Modelo específico.
- Ano mínimo e máximo de fabricação.
- Tipo de combustível preferido.
- Faixa de preço estimada.
- Cor

3. Processamento da Busca

Após coletar as informações do usuário, a aplicação segue o seguinte fluxo:

- O cliente MCP envia os dados para o servidor MCP.
- O servidor MCP processa a requisição, consulta o banco de dados e retorna os veículos que atendem aos critérios informados.


4. Exibição dos Resultados

O agente virtual recebe a lista de veículos compatíveis e exibe os resultados de forma organizada, incluindo:

- id
- marca 
- modelo
- ano 
- cor
- tipo
- quilometragem
- preco


## Instalação

### Pré-requisitos

- Python 3.12
- pip (gerenciador de pacotes do Python)

### Passos para Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/usuario/nome-do-repositorio.git


2. Acesse o diretório da aplicação:
    ```bash
    cd nome-do-repositorio

3. Crie um ambiente virtual (opcional, mas recomendado):
    ```bash
    python3 -m venv venv

4. Ative o ambiente virtual:

- No Linux/Mac:
    ```bash
    source venv/bin/activate

- No Windows:
    ```bash
    venv\Scripts\activate

5. Instale as dependências:
    ```bash
    pip install -r requirements.txt

### Como Executar

1. Rodar no terminal o servidor MCP:
    ```bash
    python servidor_mcp.py

2. Abrir outra janela no terminal e rodar a aplicação
    ```bash
    python main.py

### Estrutura de Arquivos

#### carros.db:
Este é o arquivo do banco de dados SQLite que armazenará as informações dos carros.
Ele será criado automaticamente quando python servedir_mcp.py for executado a primeira vez.

#### database.py
Este arquivo conterá todo o código relacionado à interação com o banco de dados SQLite usando SQLAlchemy.
Incluirá a configuração do banco de dados, inserção dos registros de carros e a função consultar_carros.

#### carrega_dados.py
Este arquivo contém a lógica para geração de carros 'mockados' de forma aleatória.

#### main.py
Este arquivo será o ponto de entrada principal do projeto.
Ele importará as funções dos outros arquivos, configurará a requisição MCP e processará a resposta.
Aqui ficará o código de chamada da função de requisição mcp, e o tratamento dos dados retornados.

#### models.py
Este arquivo contéam a definição do modelo Carro.

#### README.md 
Este arquivo.

#### requirements.txt
Lista de dependências da aplicação.

#### requisicao_mcp.py
Este arquivo define uma função para enviar requisições POST em formato JSON para um servidor MCP e retornar a resposta como um dicionário Python, tratando possíveis erros de conexão.

#### servidor_mcp.py
Este arquivo implementa um servidor MCP utilizando o Flask com um endpoint (/mcp) que recebe requisições POST em JSON. Ele processa consultas de carros com base em critérios como marca, modelo, ano, combustível, preço e cor, utilizando a função consultar_carros do módulo database. Se os parâmetros forem válidos, retorna uma lista de carros encontrados; caso contrário, retorna um erro.


