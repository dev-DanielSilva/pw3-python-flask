# Comentário em Python
# Importando o pacote do Flask
from flask import Flask
# Não precisa informar o tipo de varíavel, a partir do valor que damos a ela, ela recebe o seu tipo
# Carregando o Flask na variável App
app = Flask(__name__)

# Criando a rota Principal do site
@app.route('/')
# Criando função no Python
def home():
    return '<h1>Meu primeiro site em Flask. Seja bem-vindo!</h1>'

@app.route('/games')
def games():
    return '<h1>Bem-vindo a página de games!</h1><br><p>Aqui você encontrará os melhores jogos da história!</p>'

if __name__ == '__main__':
    # Rodando o servidor no localhost, porta 5000
    app.run(host="localhost", port=5000, debug=True)