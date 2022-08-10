from flask import Flask

api = Flask(__name__)

@api.route("/")
def index():
    return 'api rodando'


api.run(debug= True)