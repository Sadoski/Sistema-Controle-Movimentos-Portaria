import mysql.connector
from mysql.connector import errorcode
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class ConexaoDb(object):

    def __init__(self):
        try:

            self.conn = mysql.connector.connect(user='root', password='',
                                                host='127.1.1.1',
                                                database='sistemasportaria')
        except mysql.connector.Error as e:

            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                w = QWidget()
                QMessageBox.critical(w, 'Erro', "Usuário/Senha do banco MySql errado(s)")
            elif e.errno == errorcode.ER_BAD_DB_ERROR:
                w = QWidget()
                QMessageBox.critical(w, 'Erro', "Banco de Dados inexistente!")
            else:
                w = QWidget()
                QMessageBox.critical(w, 'Erro', "Erro fatal no banco de dados")


            self.conn.close()