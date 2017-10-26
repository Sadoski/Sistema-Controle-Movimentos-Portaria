# coding=utf-8
import sys
import time
import datetime
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mysql.connector import Error
from conexao.conexao import ConexaoDb, mysql



class PesquisaEmpresaDao(object):
    def __init__(self):
        self.__conexao = ConexaoDb()
        self.__cursor = self.__conexao.conn.cursor()
        self.__ts = time.time()
        self.__dataHora = datetime.datetime.fromtimestamp(self.__ts).strftime('%Y-%m-%d %H:%M:%S')

    def pesquisaCodigo(self, pesquisa):
        try:
            _sql = "SELECT e.id_empresa, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual, e.inscricao_municipal, t.descricao,  e.endereco, e.numero_endereco, e.complemento, e.bairro,  c.nome, d.nome, c.cep from empresa e INNER JOIN cidade c on c.id_cidade = e.id_cidades INNER JOIN estado d on d.id_estado = c.id_estado INNER JOIN tipo_empresa t on t.id_tipo_empresa = e.id_tipo_empresa where  e.id_empresa = '" + pesquisa + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaFantasia(self, pesquisa):
        try:
            _sql = "SELECT e.id_empresa, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual, e.inscricao_municipal, t.descricao,  e.endereco, e.numero_endereco, e.complemento, e.bairro,  c.nome, d.nome, c.cep from empresa e INNER JOIN cidade c on c.id_cidade = e.id_cidades INNER JOIN estado d on d.id_estado = c.id_estado INNER JOIN tipo_empresa t on t.id_tipo_empresa = e.id_tipo_empresa where  e.fantasia = '" + pesquisa + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False


    def pesquisaRazaoSocial(self, pesquisa):
            try:
                _sql = "SELECT e.id_empresa, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual, e.inscricao_municipal, t.descricao,  e.endereco, e.numero_endereco, e.complemento, e.bairro,  c.nome, d.nome, c.cep from empresa e INNER JOIN cidade c on c.id_cidade = e.id_cidades INNER JOIN estado d on d.id_estado = c.id_estado INNER JOIN tipo_empresa t on t.id_tipo_empresa = e.id_tipo_empresa where  e.razao_social = '" + pesquisa + "'"
                self.__cursor.execute(_sql)
                result = self.__cursor.fetchall()
                # self.__cursor.close()
                return result
            except BaseException as os:
                return False


    def pesquisaCnpj(self, pesquisa):
        try:
            _sql = "SELECT e.id_empresa, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual, e.inscricao_municipal, t.descricao,  e.endereco, e.numero_endereco, e.complemento, e.bairro,  c.nome, d.nome, c.cep from empresa e INNER JOIN cidade c on c.id_cidade = e.id_cidades INNER JOIN estado d on d.id_estado = c.id_estado INNER JOIN tipo_empresa t on t.id_tipo_empresa = e.id_tipo_empresa where  e.cnpj = '" + pesquisa + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False


    def pesquisaInscEstadual(self, pesquisa):
        try:
            _sql = "SELECT e.id_empresa, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual, e.inscricao_municipal, t.descricao,  e.endereco, e.numero_endereco, e.complemento, e.bairro,  c.nome, d.nome, c.cep from empresa e INNER JOIN cidade c on c.id_cidade = e.id_cidades INNER JOIN estado d on d.id_estado = c.id_estado INNER JOIN tipo_empresa t on t.id_tipo_empresa = e.id_tipo_empresa where  e.inscricao_estadual = '" + pesquisa + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False