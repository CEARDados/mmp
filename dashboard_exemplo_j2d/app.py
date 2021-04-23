# -*- coding: utf-8 -*- 
# conda activate exemploJsonDash
# json2dash @ git+https://SEUTOKEN@github.com/CEARDados/mm.git

import dash # importando o pacote dash
import json2dash # importando o pacote json2dash

configuration_file = "configuration.json"

# função responsável por ler o arquivo enviado pelo usuário e
# retornar um dicionário com as informações
dic_app = json2dash.json2dash.read_configuration_json(configuration_file)

# Cria a aplicação
app = dash.Dash(
    dic_app['name'], # nome da aplicação
    meta_tags = json2dash.format_meta_tags(dic_app)
)

app.title = dic_app['name']

# essencial caso o usuário utilize callbacks para atualização dinâmica de layout
app.config.suppress_callback_exceptions = True
app.dic_app = dic_app