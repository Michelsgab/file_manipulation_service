import mysql.connector
from mysql.connector import Error


class get_data:
    def __init__(self):
        self.__errors = None

    def get_connections(self):
        conn = None
        try:
            conn = mysql.connector.connect(host='localhost', database='projeto_evidencia', user='root',
                                           password='123456789')
        except Error as err:
            self.__errors = err
        return conn

    def close_connections(self, connection):
        try:
            connection.close()
        except Error as err:
            self.__errors += err

    def get_errors(self):
        return self.__errors
