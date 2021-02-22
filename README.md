### control-musics-with-django

- criar ambiente virtual: python -m venv venv
- ativar o ambiente virtual: navegue  até a pasta Script e digite "activate"
- instalar o django no ambiente virtual: pip install django

- criar um projeto django: django-admin startproject music_control .
- crar uma app: python manage.py startapp musics
- depois é necessário geristrar a app no projeto: seu_projeto/settings.py 
  INSTALLED_APPS - adicione a app no array

- crie pela primeira vez o banco de dados: python manage.py migrate

- para rodar o servidor: python manage.py runserver
- para criar um super usuario: python manage.py createsuperuser

- observa tudo que é novo na pasta models e cria um arquivo migrations
  executar: python manage.py makemigrations
  dentro da pasta migrations que descreve como o django deve criar as tabelas no banco de dados

- apos esses passos execute: python manage.py migrate
  para realmente aplicar o conteudo da pasta migrations e criar a tabela dentro do banco
