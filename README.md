## Musics control with django

### Para logar no admin 'http://127.0.0.1:8000/admin/', use o usuário 'django' com a senha 'django'

###### 1 - Para rodar esse projeto é necessário ter o python instalado 
- Caso não tenha ele instalado, faça o download no site oficial e instale: https://www.python.org/downloads/

###### 2 - Faça o clone desse repositório em sua máquina
- git clone https://github.com/diogoss120/musics-control-with-django.git
- git pull origin master

###### 3 - Também é necessário criar um ambiente virtual para instalar o django
-  Pelo terminal, navegue até a pasta onde foi feito o clone desse repositório
-  Ex: 'cd D:\project_django2'

###### 4 - Crie o ambiente virtual: 
- Quando estiver dentro do diretório do projeto execute no terminal:
- python -m venv venv

###### 5 - Ative o ambiente virtual: 
- No windows navegue  até a pasta Script 'cd venv\Scripts' digite "activate" e tecle enter
- Se estiver no linux: source venv/Scripts/activate

###### 6 - Instale o django no ambiente virtual: 
- pip install django

###### 7 - Inicie o servidor: 
- python manage.py runserver
- Acesse a url http://127.0.0.1:8000/ no seu navegador
