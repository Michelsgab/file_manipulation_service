from flask import Response, request
from dao.ProjetoDAO import ProjetoDAO


class ProjetoService:
    def __init__(self):
        self.projeto = ProjetoDAO()

    def find_all(self):
        return self.projeto.find_all_projetos()

    def find_by_id(self, id):
        return self.projeto.find_by_id_projetos(id)

    def create(self, projeto):
        self.projeto.create_projetos(projeto)

    def update(self, projeto, id):
        self.projeto.update_projetos(projeto, id)

    def delete(self, id):
        self.projeto.delete_projetos(id)
