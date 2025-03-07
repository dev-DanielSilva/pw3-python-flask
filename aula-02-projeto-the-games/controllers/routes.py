from flask import render_template, request

jogadores = ["MiDna", "davi_lambari",
             "fanylinda", "SuaIrmã", "Iruah"]
# Array de objetos
gameList = [{'Título': 'The Legend of Zelda: Breath of the Wild',
             'Ano': 2017,
             'Categoria': 'Mundo Aberto'},
            ]


def init_app(app):

    # criando a rota principal do site

    @app.route('/')
    # criando função no python
    # view function - Função de visualização
    def home():

        return render_template('index.html',)

    @app.route('/games', methods=['GET', 'POST'])
    def games():
        # Acessando o primeiro jogo da lista de jogos
        game = gameList[0]
        if request.method == 'POST':
            if request.form.get('jogador'):  # name do input
                jogadores.append(request.form.get('jogador'))

        return render_template('games.html',
                               game=game,
                               jogadores=jogadores
                               )
    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():
        if request.method == "POST":
            if request.form.get('titulo') and request.form.get('ano') and request.form.get('categoria'):
                gameList.append({'Título': request.form.get('titulo'),
                                 'Ano': request.form.get('ano'),
                                 'Categoria': request.form.get('categoria')
                                 })
        return render_template('cadgames.html',
                               gameList=gameList)
        
    