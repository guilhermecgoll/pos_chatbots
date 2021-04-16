import flask
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/consulta_iptu', methods=['GET'])
def consulta_iptu():
    code = request.args.get('codigo','')
    if code == '':
        return 'O código não foi informado'
    code = int(code)
    if code is None or code % 2 != 0:
        return f'Não foi encontrada nenhuma pendência para o imóvel de código {code}'
    else:
        return f'Foi encontrada uma pendência para o imóvel de código {code}. Por favor, dirija-se até a Seplan para regularização.'

if __name__ == "__main__":
    app.run()