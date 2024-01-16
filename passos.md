1. Criar e ativar virtualenvironment 
2. Instalar o DJango: pip install django
3. Criando projeto admin do django: django-admin startproject medicSearchAdmin . (Ponto  para criar o projeto no diretório corrente)

4. Configurações do projeto detalhado em cada commit no github.
5. Executar aplicação DJango: python manage.py runserver

### Passos para criação de tabelas da aplicação:
1. python manage.py migrate (criará a estrutura principal de banco de dados)
2. Criar super usuário: python manage.py createsuperuser

### Criando Primeiro APP
1. python manage.py startapp medicSearch

### Criando tabelas, com base no módulo models
makemigrations cria um novo arquivo na pasta migrations com as alterações feitas nas models ativas (declaradas no __init__py)

Depois de rodar o comando de makemigrations, é necessário executar o comando migrate, que identifica um novo arquivo na pasta migrations e rodará as modificções descritas na base de dados

Comandos:
    1. python manage.py makemigrations medicSearch (medicSearch é o app onde está nossas models)

    2. python manage.py migrate medicSearch

# Baixando biblioteca para trabalhar com upload. A lib não será usada diretamente, mas o django fará uso da mesma:
    pip install Pillow

