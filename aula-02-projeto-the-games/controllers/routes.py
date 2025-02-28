from flask import render_template, request

jogadores = ["MiDNa", "davi_lambari",
             "fanylinda", "suaIrmã", "edsonGf"]


def init_app(app):

    # criando a rota principal do site

    @app.route('/')
    # criando função no python
    # view function - Função de visualização
    def home():

        return render_template('index.html',)

    @app.route('/games', methods=['GET', 'POST'])
    def games():

        game = {'Título': 'The Legend of Zelda: Breath of the Wild',
                'Ano': 2017,
                'categoria': 'Mundo Aberto'}

        if request.method == 'POST':
            if request.form.get('jogador'):  # name do input
                jogadores.append(request.form.get('jogador'))

        return render_template('games.html',
                               game=game,
                               jogadores=jogadores
                               )