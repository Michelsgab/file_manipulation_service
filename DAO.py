from flask import request
import mysql.connector
from mysql.connector import Error


def conect():
    try:
        global con
        con = mysql.connector.connect(host='localhost', database='projeto_evidencia', user='root',
                                      password='123456789')
    except Error as erro:
        print('O erro é:', erro)


def inserir():
    request_data = request.get_json()

    if request_data:
        if 'nome' in request_data:
            nome = request_data['nome']
        if 'cargo' in request_data:
            cargo = request_data['cargo']
        if 'empresa' in request_data:
            empresa = request_data['empresa']
        if 'email' in request_data:
            email = request_data['email']
        if 'github' in request_data:
            github = request_data['github']
        if 'linkedin' in request_data:
            linkedin = request_data['linkedin']
        if 'telefone' in request_data:
            telefone = request_data['telefone']

    dados = f"('{nome}','{cargo}','{empresa}','{email}','{github}','{linkedin}','{telefone}')"
    comando_sql = f""" INSERT INTO funcionarios (nome,cargo,empresa,email,github,linkedin,telefone)
     VALUES {dados}"""

    try:
        conect()
        if con.is_connected():
            cursor = con.cursor()
            cursor.execute(comando_sql)
            con.commit()
            print(cursor.rowcount, "Inseridos na tabela")
    except Error as erro:
        print("O erro: ", erro)
    finally:
        if con.is_connected():
            cursor.close()
            con.close()


def results():
    try:
        conect()
        if con.is_connected():
            cursor = con.cursor()
            comando_sql = "SELECT * FROM funcionarios"
            cursor.execute(comando_sql)
            linhas = cursor.fetchall()
            dados = []

            for linha in linhas:
                dado = {}
                dado['id'] = linha[0]
                dado['nome'] = linha[1]
                dado['cargo'] = linha[2]
                dado['empresa'] = linha[3]
                dado['email'] = linha[4]
                dado['github'] = linha[5]
                dado['linkedin'] = linha[6]
                dado['telefone'] = linha[7]
                dados.append(dado)
            return dados
    except Error as erro:
        print("O erro: ", erro)
    finally:
        if con.is_connected():
            cursor.close()
            con.close()
