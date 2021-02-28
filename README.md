## Musics control with django

###### 1 - Para rodar esse projeto:
- É necessário ter o python instalado
- Se ele não estiver instalado baixe e instale pelo site oficial: https://www.python.org/downloads/

###### 2 - Faça o clone ou download desse repositório em sua máquina:
- Usando o git bash, escolha um diretório de sua preferencia e execute os comandos:
- git clone https://github.com/diogoss120/musics-control-with-django.git

###### 3 - Criar o ambiente virtual para instalar o django:
-  Navegue até a pasta onde foi feito o clone desse repositório
-  cd musics-control-with-django/

###### 4 - Crie o ambiente virtual: 
- Quando estiver dentro do diretório do projeto, execute os comandos:
- python -m venv venv

###### 5 - Ative o ambiente virtual: 
- source venv/Scripts/activate

###### 6 - Instale o framework django e o pacote openpyxl: 
- pip install django
- pip install openpyxl

###### 7 - Inicie o servidor: 
- python manage.py runserver
- Acesse a url http://127.0.0.1:8000/ no seu navegador

#### Para logar no admin 'http://127.0.0.1:8000/admin/':
- Use o usuário 'django' com a senha 'django' para fazer o login
- Os artistas são adicionados somente pelo admin
- Já as músicas podem ser manipuladas pela interface

#### Navegação pela interface:
- Basta clicar sobre o nome de um artista para editar as músicas dele
- Para editar uma música basta clicar sobre ela e a mesma será disponibilizada em uma tela para edição
- Na barra lateral existem atalhos para voltar a para a Home e adicionar uma Nova musica

#### Exportar músicas para um arquivo excel:
- Acesse a url http://127.0.0.1:8000/admin/musics/artist/ ou navegue pelo admin até ela
- Selecione os artistas desejados, selecione a Action: Export musics from artist e clique em GO
