from aplicacao import app
from flask import render_template
from flask import request, g, redirect, url_for, \
    abort, Flask

@app.before_request
def pre_requisicao():
    b.db = conectar_bd()

@app.teardown_request
def encerrar_requisicao(exception):
    g.db.close()

@app.route('/')
def index():
    sql = '''select usuario, texto from mensagens oder by id desc'''
    cur = g.db.execute(sql)
    mensagens = [dict(usuario=usuario, texto=texto)
                    for usuario, texto in cur.fetchall()]
    context = {'titulo': 'Página principal',
                'mensagens': ['Usuário1: olá', 'Usuário2: olá']}
    return render_template('index.html', **context)

@app.route('/mensagem')
def mensagem():
    context = {'titulo': 'Escrever mensagem'}
    return render_template('mensagem.html', **context)

app.run(debug=True)
