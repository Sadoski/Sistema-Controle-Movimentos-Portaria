import sys
import time
import datetime
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mysql.connector import Error
from conexao.conexao import ConexaoDb, mysql

class CarregamentoSaidaDao(object):
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

    def pesquisarNomeMotorista(self, nome):
        try:
            _sql = "SELECT c.id_entrada_vei_carre, m.id_motorista, m.nome, v.marca, v.modelo, v.placa, c.data, c.hora, i.descricao, o.descricao, l.id_cliente, l.fantasia, l.razao_social, l.cnpj, l.inscricao_estadual, e.id_empresa, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual FROM entrada_veiculo_carregamento c INNER JOIN motorista m ON m.id_motorista = c.id_motorista INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista INNER JOIN carga_produto a ON a.id_carga_produto = c.id_carga_produto INNER JOIN tipo_carga i On i.id_tipo_carga = a.id_tipo_carga INNER JOIN produto o ON o.id_produto = a.id_produto INNER JOIN cliente l ON l.id_cliente = c.id_cliente INNER JOIN empresa e ON e.id_empresa = c.id_empresa INNER JOIN carga_produto p ON p.id_carga_produto = c.id_carga_produto WHERE m.nome LIKE '%"+nome+"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

