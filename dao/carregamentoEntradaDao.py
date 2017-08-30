import sys
import time
import datetime
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mysql.connector import Error
from conexao.conexao import ConexaoDb, mysql

class CarregamentoEntradaDao(object):
    def __init__(self):
        self.__conexao = ConexaoDb()
        self.__cursor = self.__conexao.conn.cursor()

    def pesquisarTipoCarga(self):
        try:
            _sql = "SELECT descricao FROM tipo_carga"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarProduto(self, produto):
        try:
            _sql = "SELECT p.descricao FROM carga_produto a INNER JOIN tipo_carga c ON c.id_tipo_carga = a.id_tipo_carga INNER JOIN produto p ON p.id_produto = a.id_produto WHERE c.descricao = '"+produto+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarIdTipoCarga(self, carga):
        try:
            _sql = "SELECT id_tipo_carga FROM tipo_carga WHERE descricao = '"+carga+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarIdProduto(self, produto):
        try:
            _sql = "SELECT id_produto FROM produto WHERE descricao = '"+produto+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False