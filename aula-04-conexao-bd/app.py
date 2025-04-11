# pip gerenciador de pacotes do python
# pip install flask
# importando pacote do Flask
from flask import Flask
# importanto o PyMySql
import pymysql
# importando arquivo routes do controllers
from controllers import routes
# Importando os models
from models.database import db

# carregando o Flask na variável app
app = Flask(__name__, template_folder="views")

# Enviando o Flask (app) para a função init_app do routes
routes.init_app(app)

# Define o nome do banco de dados
DB_NAME = 'games'
# Configura o Flask com o banco definido
app.config['DATABASE_NAME'] = DB_NAME

# Passando o endereço do banco ao Flask
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root@localhost/{DB_NAME}'

if __name__ == '__main__':
    # Criando os dados de conexão
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 charset='utf8mb4',
                                 cursorclass='pymysql.cursors.DictCursor')
    # Tentando criar o banco
    # Try trata o sucesso
    try:
        # with cria um recurso temporariamente
        with connection.cursor() as cursor: # as dá um alias(apelido)
            #Cria o BD se ele não existir
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS{DB_NAME}")
            print("O Banco de Dados está criado!")
    # Except trata a falha
    except Exception as e: # as dá um alias(apelido)
        print(f"Erro ao criar o Banco de Dados: {e}")
    # Rodando o servidor no localhost, porta 5000
    finally:
        connection.close()
    # Passando o Flask ao SQLAlchemy
    db.init_app(app=app)
    
    # Criando as tabelas a partir do model
    with app.test_request_context():
        db.create_all()
    
    # App.run inicializa a aplicação Flask
    app.run(host='0.0.0.0', port=5000, debug=True)
