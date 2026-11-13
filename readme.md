Sistema web simples desenvolvido em Python com o framework Django para o cadastro e visualização de alunos, cursos e matrículas. O gerenciamento dos dados é feito através do painel administrativo (Django Admin) e a listagem é exibida em páginas web.

## Pré-requisitos:

* Python 3
* Gerenciador de pacotes `pip`
* Git

## Como baixar e executar

Comando para clonar o repositório:

```bash
git clone https://github.com/Adryan-Inacio/EA1-Cesmac.git

Acesse a pasta do projeto:

cd sistema_educacao

Instale o Django:

pip install django

Aplique as migrações do banco de dados:

python manage.py migrate

Crie um usuário administrador para acessar o painel de cadastro ou use o que eu já criei:

python manage.py createsuperuser
ou
username: admin
senha: cesmac123

Inicie o servidor local:

python manage.py runserver

Acessando o sistema
Com o servidor em execução, abra o navegador e acesse os endereços abaixo:

Painel Administrativo: http://127.0.0.1:8000/admin/

Lista de Alunos: http://127.0.0.1:8000/alunos/

Lista de Cursos: http://127.0.0.1:8000/cursos/