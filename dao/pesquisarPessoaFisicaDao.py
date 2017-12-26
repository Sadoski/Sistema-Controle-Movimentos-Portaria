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
            _sql = "SELECT f.id_pessoa, f.nome, f.apelido, f.cpf, f.rg, f.expeditor, f.uf, f.aniversario, g.sexo, f.mae, f.pai, e.endereco, e.numero, e.complemento, e.bairro, c.nome, s.nome, c.cep FROM pessoa p INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN pessoa_fisica f ON f.id_pessoa = p.id_pessoa INNER JOIN genero g ON g.id_genero = f.id_genero INNER JOIN endereco_pessoa e ON e.id_pessoa = p.id_pessoa INNER JOIN cidade c ON c.id_cidade = e.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE  t.descricao = 'PESSOA FISICA' AND p.id_pessoa = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaNome(self, pesquisa):
        try:
            _sql = "SELECT f.id_pessoa, f.nome, f.apelido, f.cpf, f.rg, f.expeditor, f.uf, f.aniversario, g.sexo, f.mae, f.pai, e.endereco, e.numero, e.complemento, e.bairro, c.nome, s.nome, c.cep FROM pessoa p INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN pessoa_fisica f ON f.id_pessoa = p.id_pessoa INNER JOIN genero g ON g.id_genero = f.id_genero INNER JOIN endereco_pessoa e ON e.id_pessoa = p.id_pessoa INNER JOIN cidade c ON c.id_cidade = e.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE  t.descricao = 'PESSOA FISICA' AND  f.nome LIKE '%"+ pesquisa +"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaApelido(self, pesquisa):
        try:
            _sql = "SELECT f.id_pessoa, f.nome, f.apelido, f.cpf, f.rg, f.expeditor, f.uf, f.aniversario, g.sexo, f.mae, f.pai, e.endereco, e.numero, e.complemento, e.bairro, c.nome, s.nome, c.cep FROM pessoa p INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN pessoa_fisica f ON f.id_pessoa = p.id_pessoa INNER JOIN genero g ON g.id_genero = f.id_genero INNER JOIN endereco_pessoa e ON e.id_pessoa = p.id_pessoa INNER JOIN cidade c ON c.id_cidade = e.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE  t.descricao = 'PESSOA FISICA' AND f.apelido LIKE '%"+ pesquisa +"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaCpf(self, pesquisa):
        try:
            _sql = "SELECT f.id_pessoa, f.nome, f.apelido, f.cpf, f.rg, f.expeditor, f.uf, f.aniversario, g.sexo, f.mae, f.pai, e.endereco, e.numero, e.complemento, e.bairro, c.nome, s.nome, c.cep FROM pessoa p INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN pessoa_fisica f ON f.id_pessoa = p.id_pessoa INNER JOIN genero g ON g.id_genero = f.id_genero INNER JOIN endereco_pessoa e ON e.id_pessoa = p.id_pessoa INNER JOIN cidade c ON c.id_cidade = e.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE  t.descricao = 'PESSOA FISICA' AND f.cpf = '"+ pesquisa +"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaRg(self, pesquisa):
        try:
            _sql = "SELECT f.id_pessoa, f.nome, f.apelido, f.cpf, f.rg, f.expeditor, f.uf, f.aniversario, g.sexo, f.mae, f.pai, e.endereco, e.numero, e.complemento, e.bairro, c.nome, s.nome, c.cep FROM pessoa p INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN pessoa_fisica f ON f.id_pessoa = p.id_pessoa INNER JOIN genero g ON g.id_genero = f.id_genero INNER JOIN endereco_pessoa e ON e.id_pessoa = p.id_pessoa INNER JOIN cidade c ON c.id_cidade = e.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE  t.descricao = 'PESSOA FISICA' AND f.rg = '"+ pesquisa +"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaMae(self, pesquisa):
        try:
            _sql = "SELECT f.id_pessoa, f.nome, f.apelido, f.cpf, f.rg, f.expeditor, f.uf, f.aniversario, g.sexo, f.mae, f.pai, e.endereco, e.numero, e.complemento, e.bairro, c.nome, s.nome, c.cep FROM pessoa p INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN pessoa_fisica f ON f.id_pessoa = p.id_pessoa INNER JOIN genero g ON g.id_genero = f.id_genero INNER JOIN endereco_pessoa e ON e.id_pessoa = p.id_pessoa INNER JOIN cidade c ON c.id_cidade = e.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE  t.descricao = 'PESSOA FISICA' AND f.mae = '"+ pesquisa +"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaPai(self, pesquisa):
        try:
            _sql = "SELECT f.id_pessoa, f.nome, f.apelido, f.cpf, f.rg, f.expeditor, f.uf, f.aniversario, g.sexo, f.mae, f.pai, e.endereco, e.numero, e.complemento, e.bairro, c.nome, s.nome, c.cep FROM pessoa p INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN pessoa_fisica f ON f.id_pessoa = p.id_pessoa INNER JOIN genero g ON g.id_genero = f.id_genero INNER JOIN endereco_pessoa e ON e.id_pessoa = p.id_pessoa INNER JOIN cidade c ON c.id_cidade = e.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE  t.descricao = 'PESSOA FISICA' AND f.pai = '"+ pesquisa +"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False