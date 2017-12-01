from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from conexao.conexao import ConexaoDb, mysql
from controller.getSetTipoEmpresa import TipoEmpresa


class TipoEmpresaDao(object):
    def __init__(self):
        self.__conexao = ConexaoDb()
        self.__cursor = self.__conexao.conn.cursor()

    def tipoEmpresa(self):
        try:
            __sql = "select descricao from tipo_empresa"
            self.__cursor.execute(__sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao pesquisar o tipo de empresa no banco de dados ")

    def idTipoEmpresa(self, descricao):
        try:
            _sql = "select id_tipo_empresa from tipo_empresa where descricao = '"+descricao+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            return result
            #self.__cursor.close()
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao pesquisar o tipo de empresa no banco de dados ")