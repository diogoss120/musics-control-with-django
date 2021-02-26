## Musics control with django

###### 1 - Para rodar esse projeto:
- É necessário ter o python instalado, instale: https://www.python.org/downloads/

###### 2 - Faça o clone ou download desse repositório em sua máquina:
- Usando o git bash, escolha um diretório de sua preferencia e execute os comandos:
- git clone https://github.com/diogoss120/musics-control-with-django.git
- git pull origin master

###### 3 - Também é necessário criar um ambiente virtual para instalar o django:
-  Pelo terminal, navegue até a pasta onde foi feito o clone desse repositório
-  cd musics-control-with-django/

###### 4 - Crie o ambiente virtual: 
- Quando estiver dentro do diretório do projeto execute no terminal:
- python -m venv venv

###### 5 - Ative o ambiente virtual: 
- Git bash: source venv/Scripts/activate

###### 6 - Instale o django no ambiente virtual: 
- Installe o django: pip install django
- E o pacote openpyxl: pip install openpyxl

###### 7 - Inicie o servidor: 
- python manage.py runserver
- Acesse a url http://127.0.0.1:8000/ no seu navegador

#### Para logar no admin 'http://127.0.0.1:8000/admin/':
- O django disponibiliza um sistema administrador nativo
- Use o usuário 'django' com a senha 'django' para fazer o login
- Os artistas são adicionados somente pelo admin
- Já as músicas podem ser manipuladas pela interface

#### Navegação pela interface:
- Basta clicar sobre o nome artista para editar os adicionar musicas referentes a ele
- Para editar uma música, basta clicar sobre ela e a mesma será disponibilizada em uma tela para edição
- Cabeçalho possui atalhos para voltar a Home e adicionar uma Nova musica

#### Exportar músicas para um arquivo excel:
- Acesse a url http://127.0.0.1:8000/admin/musics/artist/ ou navegue pelo admin até ela
- Selecione o/os artistas desejados, selecione a Action: Export musics from artist e clique em GO