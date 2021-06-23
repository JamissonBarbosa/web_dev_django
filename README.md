# Projeto - Sistema de Cadastro

Sistema de cadrastro de produtos

Utilizando operações CRUD é possível add produtos e suas descrições.
Também é possivel alterações nos produtos e deleta-los

# Instalação

Para executar o projeto é recomendade criar um ambiente virtual 
Com seu ambiente virtual configurado, instale as seguintes dependências
```xml
pip install -r requirements.txt
```
Crie as migrations com:
```xml
python manage.py makemigrations
```

Para efetivar as Migrations no banco de dados:
```xml
python manage.py migrate
```

# Execução
```xml
python manage.py runserver
```
