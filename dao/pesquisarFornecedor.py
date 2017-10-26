import sys
import time
import datetime
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mysql.connector import Error
from conexao.conexao import ConexaoDb, mysql


class PesquisarFornecedorDao(object):
    def __init__(self):
        self.__conexao = ConexaoDb()
        self.__cursor = self.__conexao.conn.cursor()
        self.__ts = time.time()
        self.__dataHora = datetime.datetime.fromtimestamp(self.__ts).strftime('%Y-%m-%d %H:%M:%S')

    def pesquisaCodigo(self, pesquisa):
        try:
            _sql = "SELECT f.id_fornecedor, f.fantasia, f.razao_social, f.cnpj, f.inscricao_estadual, f.endereco, f.numero_endereco, f.bairro, c.nome, s.nome, c.cep FROM fornecedor f INNER JOIN cidade c ON c.id_cidade = f.id_cidades INNER JOIN estado s ON s.id_estado = c.id_estado INNER JOIN empresa e ON e.id_empresa = f.id_empresa WHERE f.id_fornecedor = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaFantasia(self, pesquisa):
        try:
            _sql = "SELECT f.id_fornecedor, f.fantasia, f.razao_social, f.cnpj, f.inscricao_estadual, f.endereco, f.numero_endereco, f.bairro, c.nome, s.nome, c.cep FROM fornecedor f INNER JOIN cidade c ON c.id_cidade = f.id_cidades INNER JOIN estado s ON s.id_estado = c.id_estado INNER JOIN empresa e ON e.id_empresa = f.id_empresa WHERE f.fantasia = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaRazaoSocial(self, pesquisa):
        try:
            _sql = "SELECT f.id_fornecedor, f.fantasia, f.razao_social, f.cnpj, f.inscricao_estadual, f.endereco, f.numero_endereco, f.bairro, c.nome, s.nome, c.cep FROM fornecedor f INNER JOIN cidade c ON c.id_cidade = f.id_cidades INNER JOIN estado s ON s.id_estado = c.id_estado INNER JOIN empresa e ON e.id_empresa = f.id_empresa WHERE f.razao_social = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaCnpj(self, pesquisa):
        try:
            _sql = "SELECT f.id_fornecedor, f.fantasia, f.razao_social, f.cnpj, f.inscricao_estadual, f.endereco, f.numero_endereco, f.bairro, c.nome, s.nome, c.cep FROM fornecedor f INNER JOIN cidade c ON c.id_cidade = f.id_cidades INNER JOIN estado s ON s.id_estado = c.id_estado INNER JOIN empresa e ON e.id_empresa = f.id_empresa WHERE f.cnpj = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaInscEstadual(self, pesquisa):
        try:
            _sql = "SELECT f.id_fornecedor, f.fantasia, f.razao_social, f.cnpj, f.inscricao_estadual, f.endereco, f.numero_endereco, f.bairro, c.nome, s.nome, c.cep FROM fornecedor f INNER JOIN cidade c ON c.id_cidade = f.id_cidades INNER JOIN estado s ON s.id_estado = c.id_estado INNER JOIN empresa e ON e.id_empresa = f.id_empresa WHERE f.cnpj, f.inscricao_estadual = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False