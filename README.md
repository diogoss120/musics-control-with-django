<h1 align="center">Musics control with django</h1>

<p>
O objetivo desse projeto é desenvolver um CRUD de músicas no front-end utilizando a abordagem de templates do Django e sem nenhum framework front-end, fazendo uso de html, css e javascript puros.
Os artistas são cadastrados através do admin do Django, onde também foi desenvolvida uma ação para exportar todas as canções de um ou mais artistas em formato de planilha.
</p>


## Pré-requisitos

###### 1 - Ter o python instalado:
- É necessário ter o python instalado
- Se ele não estiver instalado baixe e instale pelo site oficial: https://www.python.org/downloads/

###### 2 - Faça o clone desse repositório em sua máquina:
- Usando o git bash, escolha um diretório de sua preferencia e execute os comandos:
- git clone https://github.com/diogoss120/musics-control-with-django.git

###### 3 - Crie o ambiente virtual:
- Navegue até a pasta onde foi feito o clone desse repositório
- cd musics-control-with-django/
- python -m venv venv

###### 4 - Ative o ambiente virtual: 
- source venv/Scripts/activate

###### 5 - Faça a instalação dos pacotes necessários: 
- pip install -r requirements.txt

###### 6 - Inicie o servidor: 
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


## 🛠 Tecnologias
As seguintes ferramentas foram usadas na construção do projeto:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [JavaScript](https://www.javascript.com/)
- [Html](https://developer.mozilla.org/pt-BR/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS)
