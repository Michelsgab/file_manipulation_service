import DAO
from flask import Flask, jsonify


api = Flask(__name__)


@api.route("/all", methods=['GET'])
def index():
    DAO.results()
    dados = DAO.results()

    return jsonify(dados)


@api.route("/dados", methods=['POST'])
def insert():
    DAO.inserir()
    dados = DAO.results()

    return jsonify(dados)


@api.route("/select/<int:id>", methods=['GET'])
def select(id):
    dados = DAO.consult_id(str(id))

    return jsonify(dados)


api.run(debug=True)
