# -*- coding: utf-8 -*- 

from dash.dependencies import Input, Output
import json2dash # importando o pacote json2dash
from app import app # importando o objeto dash chamado app do arquivo app.py

# Ao importar app, o dicionário app.dic_app estará disponível.
# tem "start_page_name" e "start_page_filename", que são usadas na inicialização.
app.dics, app.layouts = json2dash.initialize(app.dic_app)

# Carrega a página inicial da aplicação.
app.layout = json2dash.start_page_layout(app)

# Inicializa a variável server (necessária para o deploy no heroku).
server = app.server

#  Callbacks
@app.callback(
    Output('div_main', 'children'),
    [
        Input('url', 'pathname')
    ]
)
def display_layout(pathname):
    return json2dash.route(pathname, app)

#  run_server (rodando a aplicação)
if __name__ == '__main__':
    app.run_server(debug=True) # versão para teste