import DAO
from flask import Flask, jsonify


api = Flask(__name__)


@api.route("/all", methods=['GET'])
def index():
    DAO.results()
    dados = DAO.results()

    return jsonify(dados)


@api.route("/dados", methods=['POST', 'GET'])
def insert():
    DAO.inserir()
    dados = DAO.results()

    return jsonify(dados)


api.run(debug=True)
