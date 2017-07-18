import mysql.connector
from mysql.connector import Error
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class ConexaoDb(object):

    def __init__(self):
        try:

            self.conn = mysql.connector.connect(user='root', password='123456',
                                                host='127.1.1.1',
                                                database='sistemasportaria')
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.critical(w, 'Erro', "Erro fatal no banco de dados")