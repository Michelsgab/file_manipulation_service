import json
from flask import *
from flask_cors import CORS
from server.appserver import server
from model.ProjetoModel import Projeto
from service.ProjetoService import ProjetoService

diretorio_curriculo = "C:\\Users\\Magna\\Desktop\\projeto-evidencia-service\\curriculo\\"
diretorio_imagem = "C:\\Users\\Magna\\Desktop\\projeto-evidencia-service\\imagens\\"

service = ProjetoService()
app = server.app
CORS(app)


@app.route("/projetos", methods=['GET'])
def get_projetos():
    projeto = service.find_all()
    return json.dumps(projeto)


@app.route("/projetos/<id>", methods=['GET'])
def get_projetos_id(id):
    projeto = service.find_by_id(id)
    return json.dumps(projeto)


@app.route("/projetos", methods=['POST'])
def post_projetos():
    json_cliente = request.get_json()
    projeto = popula_objeto(json_cliente)
    service.create(projeto)
    return Response("Projeto criado", status=201)


@app.route("/projetos/<int:id>", methods=['PUT'])
def put_projetos(id):
    json_cliente = request.get_json()
    projeto = popula_objeto(json_cliente)
    service.update(projeto, id)
    return Response("Projeto atualizado", status=200)


@app.route("/projetos/<id>", methods=['DELETE'])
def delete_projetos(id):
    service.delete(id)
    return Response("Projeto deletado", status=204)


@app.route("/projetos/curriculos/<nome_curriculo>", methods=['GET'])
def curriculo_usuario(nome_curriculo):
    return send_from_directory(diretorio_curriculo, nome_curriculo, as_attachment=True)


@app.route("/projetos/imagens/<nome_imagem>", methods=['GET'])
def imagem_usuario(nome_imagem):
    return send_from_directory(diretorio_imagem, nome_imagem)


def popula_objeto(json_response):
    nome = json_response.get('nome')
    descricao = json_response.get('descricao')
    cargo = json_response.get('cargo')
    empresa = json_response.get('empresa')
    email = json_response.get('email')
    github = json_response.get('github')
    linkedin = json_response.get('linkedin')
    telefone = json_response.get('telefone')
    curriculo = json_response.get('curriculo')
    foto = json_response.get('foto')
    return Projeto(None, nome, descricao, cargo, empresa, email, github,
                   linkedin, telefone, curriculo, foto)
