import logging

from dao.factory.factory import get_data
from model.ProjetoModel import Projeto

logging.basicConfig(format="%(asctime)s %(message)s", level=logging.DEBUG)


class ProjetoDAO:
    def __init__(self):
        self._con = None
        try:
            connection = get_data()
            self._con = connection.get_connections()
        except Exception as err:
            raise err

    def find_all_projetos(self):
        lista_projetos = []
        sql_command = "SELECT * FROM funcionarios"
        cursor = self._con.cursor()
        try:
            logging.info("INICIANDO MÉTODOA find_all_projetos de ProjetoDAO")
            projeto = Projeto()
            cursor.execute(sql_command)
            row = cursor.fetchone()
            while row:
                projeto.id = row[0]
                projeto.nome = row[1]
                projeto.descricao = row[2]
                projeto.cargo = row[3]
                projeto.empresa = row[4]
                projeto.email = row[5]
                projeto.github = row[6]
                projeto.linkedin = row[7]
                projeto.telefone = row[8]
                projeto.curriculo = row[9]
                projeto.foto = row[10]
                lista_projetos.append(dict(projeto))
                row = cursor.fetchone()
            lista_projetos_dict = []
            for projeto in lista_projetos:
                lista_projetos_dict.append(dict(projeto))

            return lista_projetos_dict
        except Exception as err:
            logging.error(f"OCORREU UM ERRO DURANTE A EXECUCAO DO METODO find_all_projetos DE ProjetoDAO:\n {err.args}")
        finally:
            logging.info("MÉTODO find_all_projetos FINALIZADO")
            cursor.close()

    def find_by_id_projetos(self, id):
        sql_command = f"SELECT * FROM funcionarios WHERE ID = {id}"
        cursor = self._con.cursor()
        try:
            logging.info("INICIANDO MÉTODOA find_by_id_projetos de ProjetoDAO")
            projeto = Projeto()
            cursor.execute(sql_command)
            row = cursor.fetchone()
            while row:
                projeto.id = row[0]
                projeto.nome = row[1]
                projeto.descricao = row[2]
                projeto.cargo = row[3]
                projeto.empresa = row[4]
                projeto.email = row[5]
                projeto.github = row[6]
                projeto.linkedin = row[7]
                projeto.telefone = row[8]
                projeto.curriculo = row[9]
                projeto.foto = row[10]
                row = cursor.fetchone()

            return dict(projeto)
        except Exception as err:
            logging.error(
                f"OCORREU UM ERRO DURANTE A EXECUCAO DO METODO find_by_id_projetos DE ProjetoDAO:\n {err.args}")
        finally:
            logging.info("MÉTODO find_by_id_projetos FINALIZADO")
            cursor.close()

    def create_projetos(self, projeto):
        sql_command = """INSERT INTO 
        funcionarios (nome, descricao, cargo, empresa, email, github, linkedin, telefone, curriculo, foto) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor = self._con.cursor()
        try:
            logging.info("INICIANDO MÉTODOA create_projetos de ProjetoDAO")
            cursor.execute(sql_command, (projeto.nome, projeto.descricao, projeto.cargo, projeto.empresa,
                           projeto.email, projeto.github, projeto.linkedin, projeto.telefone, projeto.curriculo,
                           projeto.foto))
            self._con.commit()

        except Exception as err:
            logging.error(
                f"OCORREU UM ERRO DURANTE A EXECUCAO DO METODO create_projetos DE ProjetoDAO:\n {err.args}")
        finally:
            logging.info("MÉTODO create_projetos FINALIZADO")
            cursor.close()

    def update_projetos(self, projeto, id):
        sql_command = f'''UPDATE funcionarios SET 
        nome = %s, descricao = %s, cargo = %s, empresa = %s, email = %s, github = %s, linkedin = %s, telefone = %s,
        curriculo = %s, foto = %s WHERE id = %s'''
        cursor = self._con.cursor()
        try:
            logging.info("INICIANDO MÉTODOA update_projetos de ProjetoDAO")
            print(id)
            cursor.execute(sql_command, (projeto.nome, projeto.descricao, projeto.cargo, projeto.empresa,
                           projeto.email, projeto.github, projeto.linkedin, projeto.telefone, projeto.curriculo,
                           projeto.foto, id))
            self._con.commit()
        except Exception as err:
            logging.error(
                f"OCORREU UM ERRO DURANTE A EXECUCAO DO METODO update_projetos DE ProjetoDAO:\n {err.args}")
        finally:
            logging.info("MÉTODO update_projetos FINALIZADO")
            cursor.close()

    def delete_projetos(self, id):
        sql_command = f"DELETE FROM funcionarios WHERE id = {id}"
        cursor = self._con.cursor()
        try:
            logging.info("INICIANDO MÉTODOA delete_projetos de ProjetoDAO")
            cursor.execute(sql_command)
            self._con.commit()
            return f"Funcionário do id: {id} foi deletado."
        except Exception as err:
            logging.error(
                f"OCORREU UM ERRO DURANTE A EXECUCAO DO METODO delete_projetos DE ProjetoDAO:\n {err.args}")
        finally:
            logging.info("MÉTODO update_projetos FINALIZADO")
            cursor.close()
