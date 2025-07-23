# House Performance - Teste Prático - Parte 2

Este projeto faz parte da realização do teste prático da House Performance, que consiste em subir os dados 
de uma planilha fornecida em um banco de dados de minha escolha. 

Neste projeto, já importei os dados da planilha em um arquivo .csv denominado "hp_data_raw.csv". A partir daqui, usarei Docker para
subir dois contêineres:

1. Um container com o banco MySQL 8.0 com uma base de dados inicial configurada via script SQL.
2. Um container Python 3.12, responsável por realizar o processamento e a carga dos dados no banco usando um script.

----------------------
## PRÉ-REQUISITOS
----------------------
- Docker instalado
- Docker Compose instalado

----------------------
## ESTRUTURA DO PROJETO
----------------------
- docker-compose.yml: Arquivo de definição dos serviços
- init_db.sql: Script SQL executado na inicialização do MySQL
- upload_data.py: Script Python que faz a carga de dados
- hp_data_raw.csv: Arquivo .csv contendo os dados a serem carregados

----------------------
## COMO EXECUTAR
----------------------
1. Abra o terminal na raiz do projeto (onde está o arquivo `docker-compose.yml`).

2. Execute o seguinte comando para iniciar os serviços:

```bash
   docker compose up -d
```

   Esse comando irá:
   - Subir um container MySQL na porta 3306, com a base de dados `hp_mysql` e o script `init_db.sql` carregado automaticamente.
   - Subir um container Python que instalará as dependências (`numpy`, `pandas`, `sqlalchemy`, `pymysql`) e executará o script `upload_data.py`.

3. Aguarde alguns instantes enquanto os containers são iniciados.

----------------------
# VERIFICAÇÃO
----------------------
- Verifique se o container `mysql8` está rodando com:

```bash
  docker ps
```

- Para visualizar os logs do loader Python:

```bash
  docker logs <id_ou_nome_do_container_python_loader>
```

----------------------
# PARA PARAR OS SERVIÇOS
----------------------
Execute:
```bash
   docker compose down
```

----------------------
# ACESSANDO O BANCO
----------------------
O banco pode ser acessado usando algum gerenciador de banco de dados, como o DBeaver (recomendado) ou realizando a 
conexão direta pelo terminal do Docker usando o comando:

```bash
    docker exec -it mysql8 mysql -u root -p
```
