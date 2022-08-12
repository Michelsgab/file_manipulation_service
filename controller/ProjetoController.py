import json
from flask import *
from server.appserver import server
from model.ProjetoModel import Projeto
from service.ProjetoService import ProjetoService

service = ProjetoService()
app = server.app


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


def popula_objeto(json_response):
    nome = json_response.get('nome')
    descricao = json_response.get('descricao')
    cargo = json_response['cargo']
    empresa = json_response['empresa']
    email = json_response['email']
    github = json_response['github']
    linkedin = json_response['linkedin']
    telefone = json_response['telefone']
    curriculo = json_response['curriculo']
    foto = json_response['foto']
    return Projeto(None, nome, descricao, cargo, empresa, email, github,
                   linkedin, telefone, curriculo, foto)
