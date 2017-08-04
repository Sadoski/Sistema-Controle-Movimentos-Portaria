from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mysql.connector import Error
from conexao.conexao import ConexaoDb, mysql


class CidadesEstadosDao(object):
    def __init__(self):
        self.__conexao = ConexaoDb()
        self.__cursor = self.__conexao.conn.cursor()

    def cidade(self, cep):
        try:
            _sql = "SELECT c.nome, e.nome FROM cidade c FROM INNER JOIN estado e ON e.id_estado = c.id_estado WHERE c.cep = '"+cep+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            return result
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao pesquisar a cidade no banco de dados ")
            return False

    def idCidade(self, cep):
        try:
            _sql = "SELECT c.*, e.* FROM cidade c INNER JOIN estado e ON e.id_estado = c.id_estado WHERE c.cep = '"+cep+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            return result
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao pesquisar a cidade no banco de dados ")
            return False