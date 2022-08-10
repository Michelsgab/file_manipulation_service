from flask import Flask
import mysql.connector
from mysql.connector import Error

def conect():
    try:
        global con
        con = mysql.connector.connect(localhost= 'localhost', database= 'projeto_evidencia', user='root', password='123456789')
    except Erro as erro:
        print('O erro é:', erro)

