from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mysql.connector import Error
from conexao.conexao import ConexaoDb, mysql

class PesquisarPessoaJuridicaDao(object):
    def __init__(self):
        self.__conexao = ConexaoDb()
        self.__cursor = self.__conexao.conn.cursor()

    def pesquisaCodigo(self, pesquisa):
        try:
            _sql = "SELECT p.id_pessoa_juridica, p.razao_social, p.fantasia, p.cnpj, p.ins_estadual, p.endereco, p.numero, p.complemento, p.bairro, c.nome, e.nome, c.cep, p.site FROM pessoa_juridica p INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado WHERE p.id_pessoa_juridica = '"+ pesquisa +"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaRazaoSocial(self, pesquisa):
        try:
            _sql = "SELECT p.id_pessoa_juridica, p.razao_social, p.fantasia, p.cnpj, p.ins_estadual, p.endereco, p.numero, p.complemento, p.bairro, c.nome, e.nome, c.cep, p.site FROM pessoa_juridica p INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado WHERE p.razao_social LIKE '%"+ pesquisa +"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaFantasia(self, pesquisa):
        try:
            _sql = "SELECT p.id_pessoa_juridica, p.razao_social, p.fantasia, p.cnpj, p.ins_estadual, p.endereco, p.numero, p.complemento, p.bairro, c.nome, e.nome, c.cep, p.site FROM pessoa_juridica p INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado WHERE p.fantasia LIKE  '%"+ pesquisa +"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaCnpj(self, pesquisa):
        try:
            _sql = "SELECT p.id_pessoa_juridica, p.razao_social, p.fantasia, p.cnpj, p.ins_estadual, p.endereco, p.numero, p.complemento, p.bairro, c.nome, e.nome, c.cep, p.site FROM pessoa_juridica p INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado WHERE p.cnpj = '"+ pesquisa +"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaInsEstadual(self, pesquisa):
        try:
            _sql = "SELECT p.id_pessoa_juridica, p.razao_social, p.fantasia, p.cnpj, p.ins_estadual, p.endereco, p.numero, p.complemento, p.bairro, c.nome, e.nome, c.cep, p.site FROM pessoa_juridica p INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado WHERE p.ins_estadual = '"+ pesquisa +"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False