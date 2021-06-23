# aula01_git

Sistema de cadrastro de produtos

Utilizando operações CRUD é possível add produtos e suas descrições.
Também é possivel alterações nos produtos e deleta-los

# Instalação

Para executar o projeto é recomendade criar um ambiente virtual 
Com seu ambiente virtual configurado, instale as seguintes dependências

pip install -r requirements.txt

Crie as migrations com:

python manage.py makemigrations

Para efetivar as Migrations no banco de dados:

python manage.py migrate

#Execução

python manage.py runserver
