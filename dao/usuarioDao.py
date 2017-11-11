# coding=utf-8
import sys
import time
import datetime
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mysql.connector import Error
from conexao.conexao import ConexaoDb, mysql
from controller.getSetCidade import Cidades
from controller.getSetEmpresa import Empresas


class UsuarioDao(object):
    def __init__(self):
        self.__conexao = ConexaoDb()
        self.__cursor = self.__conexao.conn.cursor()
        self.__ts = time.time()
        self.__dataHora = datetime.datetime.fromtimestamp(self.__ts).strftime('%Y-%m-%d %H:%M:%S')

    def pesquisarFuncionarioCod(self, pesquisa):
        try:
            _sql = "SELECT f.id_funcionario, f.nome, f.rg, f.cpf, t.descricao, l.descricao FROM funcionario f INNER JOIN cidade c ON c.id_cidade = f.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado INNER JOIN funcao d ON d.id_funcao = f.id_funcao INNER JOIN setores t ON t.id_setores = d.id_setores INNER JOIN cargo l ON l.id_cargo = d.id_cargo INNER JOIN empresa m ON m.id_empresa = f.id_empresa WHERE f.id_funcionario = '" + pesquisa + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarFuncionarioNome(self, pesquisa):
        try:
            _sql = "SELECT f.id_funcionario, f.nome, f.rg, f.cpf, t.descricao, l.descricao FROM funcionario f INNER JOIN cidade c ON c.id_cidade = f.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado INNER JOIN funcao d ON d.id_funcao = f.id_funcao INNER JOIN setores t ON t.id_setores = d.id_setores INNER JOIN cargo l ON l.id_cargo = d.id_cargo INNER JOIN empresa m ON m.id_empresa = f.id_empresa WHERE f.nome LIKE '%" + pesquisa + "%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarFuncionarioCpf(self, pesquisa):
        try:
            _sql = "SELECT f.id_funcionario, f.nome, f.rg, f.cpf, t.descricao, l.descricao FROM funcionario f INNER JOIN cidade c ON c.id_cidade = f.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado INNER JOIN funcao d ON d.id_funcao = f.id_funcao INNER JOIN setores t ON t.id_setores = d.id_setores INNER JOIN cargo l ON l.id_cargo = d.id_cargo INNER JOIN empresa m ON m.id_empresa = f.id_empresa WHERE f.cpf = '" + pesquisa + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarUsuarioCod(self, pesquisa):
        try:
            _sql = "SELECT u.id_usuarios, u.login, f.nome, t.descricao, l.descricao FROM usuarios u INNER JOIN funcionario f ON f.id_funcionario = u.id_funcionario INNER JOIN cidade c ON c.id_cidade = f.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado INNER JOIN funcao d ON d.id_funcao = f.id_funcao INNER JOIN setores t ON t.id_setores = d.id_setores INNER JOIN cargo l ON l.id_cargo = d.id_cargo INNER JOIN empresa m ON m.id_empresa = f.id_empresa WHERE u.id_usuarios = '" + pesquisa + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarUsuarioNome(self, pesquisa):
        try:
            _sql = "SELECT u.id_usuarios, u.login, f.nome, t.descricao, l.descricao FROM usuarios u INNER JOIN funcionario f ON f.id_funcionario = u.id_funcionario INNER JOIN cidade c ON c.id_cidade = f.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado INNER JOIN funcao d ON d.id_funcao = f.id_funcao INNER JOIN setores t ON t.id_setores = d.id_setores INNER JOIN cargo l ON l.id_cargo = d.id_cargo INNER JOIN empresa m ON m.id_empresa = f.id_empresa WHERE u.login LIKE '%" + pesquisa + "%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarUsuarioNomeFun(self, pesquisa):
        try:
            _sql = "SELECT u.id_usuarios, u.login, f.nome, t.descricao, l.descricao FROM usuarios u INNER JOIN funcionario f ON f.id_funcionario = u.id_funcionario INNER JOIN cidade c ON c.id_cidade = f.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado INNER JOIN funcao d ON d.id_funcao = f.id_funcao INNER JOIN setores t ON t.id_setores = d.id_setores INNER JOIN cargo l ON l.id_cargo = d.id_cargo INNER JOIN empresa m ON m.id_empresa = f.id_empresa WHERE f.nome LIKE '%" + pesquisa + "%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False