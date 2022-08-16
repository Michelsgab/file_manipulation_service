import base64
from dao.ProjetoDAO import ProjetoDAO


class ProjetoService:
    def __init__(self):
        self.projeto = ProjetoDAO()

    def find_all(self):
        return self.projeto.find_all_projetos()

    def find_by_id(self, id):
        return self.projeto.find_by_id_projetos(id)

    def create(self, projeto):
        with open(f'imagens/{projeto.nome}.png', 'wb') as imagem_nova:
            imagem_nova.write(base64.decodebytes(bytes( projeto.foto, 'UTF8')))
        projeto.foto = f"Imagem do {projeto.nome}"

        with open(f'curriculo/{projeto.nome}.pdf', 'wb') as pdf_novo:
            pdf_novo.write(base64.decodebytes(bytes(projeto.curriculo, 'UTF8')))
        projeto.foto = f"Curriculo do {projeto.nome}"
        self.projeto.create_projetos(projeto)

    def update(self, projeto, id):
        with open(f'imagens/{projeto.nome}.png', 'wb') as imagem_nova:
            imagem_nova.write(base64.decodebytes(bytes(projeto.foto, 'UTF8')))
        projeto.foto = f"Imagem do {projeto.nome}"
        
        with open(f'curriculo/{projeto.nome}.pdf', 'wb') as pdf_novo:
            pdf_novo.write(base64.decodebytes(bytes(projeto.curriculo, 'UTF8')))
        projeto.foto = f"Curriculo do {projeto.nome}"

        self.projeto.update_projetos(projeto, id)

    def delete(self, id):
        self.projeto.delete_projetos(id)
