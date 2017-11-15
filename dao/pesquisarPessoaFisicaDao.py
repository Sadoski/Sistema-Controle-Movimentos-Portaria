from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mysql.connector import Error
from conexao.conexao import ConexaoDb, mysql

class PesquisarPessoaFisicaDao(object):
    def __init__(self):
        self.__conexao = ConexaoDb()
        self.__cursor = self.__conexao.conn.cursor()

    def pesquisaCodigo(self, pesquisa):
        try:
            _sql = "SELECT p.id_pessoa_fisica, p.nome, p.cpf, p.rg, p.expeditor, p.aniversario, g.sexo, p.endereco, p.numero, p.complemento, p.bairro, c.nome, e.nome, c.cep, p.mae, p.pai FROM pessoa_fisica p INNER JOIN genero g ON g.id_genero = p.id_genero INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado WHERE p.id_pessoa_fisica = '"+ pesquisa +"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaNome(self, pesquisa):
        try:
            _sql = "SELECT p.id_pessoa_fisica, p.nome, p.cpf, p.rg, p.expeditor, p.aniversario, g.sexo, p.endereco, p.numero, p.complemento, p.bairro, c.nome, e.nome, c.cep, p.mae, p.pai FROM pessoa_fisica p INNER JOIN genero g ON g.id_genero = p.id_genero INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado WHERE p.nome LIKE '%"+ pesquisa +"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaCpf(self, pesquisa):
        try:
            _sql = "SELECT p.id_pessoa_fisica, p.nome, p.cpf, p.rg, p.expeditor, p.aniversario, g.sexo, p.endereco, p.numero, p.complemento, p.bairro, c.nome, e.nome, c.cep, p.mae, p.pai FROM pessoa_fisica p INNER JOIN genero g ON g.id_genero = p.id_genero INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado WHERE p.cpf = '"+ pesquisa +"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaRg(self, pesquisa):
        try:
            _sql = "SELECT p.id_pessoa_fisica, p.nome, p.cpf, p.rg, p.expeditor, p.aniversario, g.sexo, p.endereco, p.numero, p.complemento, p.bairro, c.nome, e.nome, c.cep, p.mae, p.pai FROM pessoa_fisica p INNER JOIN genero g ON g.id_genero = p.id_genero INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado WHERE p.rg = '"+ pesquisa +"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaMae(self, pesquisa):
        try:
            _sql = "SELECT p.id_pessoa_fisica, p.nome, p.cpf, p.rg, p.expeditor, p.aniversario, g.sexo, p.endereco, p.numero, p.complemento, p.bairro, c.nome, e.nome, c.cep, p.mae, p.pai FROM pessoa_fisica p INNER JOIN genero g ON g.id_genero = p.id_genero INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado WHERE p.mae = '"+ pesquisa +"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaPai(self, pesquisa):
        try:
            _sql = "SELECT p.id_pessoa_fisica, p.nome, p.cpf, p.rg, p.expeditor, p.aniversario, g.sexo, p.endereco, p.numero, p.complemento, p.bairro, c.nome, e.nome, c.cep, p.mae, p.pai FROM pessoa_fisica p INNER JOIN genero g ON g.id_genero = p.id_genero INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado WHERE p.pai = '"+ pesquisa +"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False