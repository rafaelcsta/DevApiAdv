from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {'nome':'Rafael','habilidades':['Python', 'Flask']},
    {'nome':'Costa','habilidades':['Python', 'Html']}
]

@app.route('/dev/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status':'erro', 'mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procute o administrador da API'
            response = {'status':'erro', 'mensagem':mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso', 'mensagem':'Registro excluído'})

if __name__ == '__main__':
    app.run(debug=True)