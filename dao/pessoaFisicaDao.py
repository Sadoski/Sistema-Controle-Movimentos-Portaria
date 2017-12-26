import time
import datetime
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mysql.connector import Error
from conexao.conexao import ConexaoDb, mysql

class PessoaFisicaDao(object):

    def __init__(self):
        self.__conexao = ConexaoDb()
        self.__cursor = self.__conexao.conn.cursor()
        self.__ts = time.time()
        self.__dataHora = datetime.datetime.fromtimestamp(self.__ts).strftime('%Y-%m-%d %H:%M:%S')

    def ultimoRegistro(self):
        try:
            _sql = "SELECT LAST_INSERT_ID()"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()

            return result

        except BaseException as os:
            return False

    def pesquisarPessoaFisica(self, pessoaFisica):
        try:
            _sql = "SELECT * FROM pessoa_fisica WHERE nome = %s and  cpf = %s and rg = %s"
            _valores = (pessoaFisica.getNome, pessoaFisica.getCpf, pessoaFisica.getRg)
            self.__cursor.execute(_sql, _valores)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarIdPessoaFisica(self, pessoaFisica):
        try:
            _sql = "SELECT f.id_pessoa_fisica FROM pessoa p INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN pessoa_fisica f ON f.id_pessoa = p.id_pessoa INNER JOIN genero g ON g.id_genero = f.id_genero INNER JOIN endereco_pessoa e ON e.id_pessoa = p.id_pessoa INNER JOIN cidade c ON c.id_cidade = e.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE p.id_pessoa = '"+pessoaFisica+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarIdEnderecoPessoaFisica(self, pessoaFisica):
        try:
            _sql = "SELECT e.id_endereco_pessoa FROM pessoa p INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN pessoa_fisica f ON f.id_pessoa = p.id_pessoa INNER JOIN genero g ON g.id_genero = f.id_genero INNER JOIN endereco_pessoa e ON e.id_pessoa = p.id_pessoa INNER JOIN cidade c ON c.id_cidade = e.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE p.id_pessoa = '"+pessoaFisica+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def cadastrarPessoa(self, pessoaFisica):
        try:
            _sql = "INSERT INTO pessoa (id_tipo_pessoa, cadastrado) VALUES (%s, %s)"
            _valores = (pessoaFisica, self.__dataHora)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()

            # self.__cursor.close()
            return True
        except BaseException as os:
            self.__conexao.conn.rollback()
            return False

    def cadastrarPessoaFisica(self, pessoaFisica):
        try:
            _sql = "INSERT INTO pessoa_fisica (nome, apelido, cpf, rg, expeditor, uf, aniversario, mae, pai, id_genero, id_pessoa,  cadastrado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            _valores = (pessoaFisica.getNome, pessoaFisica.getApelido, pessoaFisica.getCpf, pessoaFisica.getRg, pessoaFisica.getExpeditor, pessoaFisica.getUf, pessoaFisica.getData,  pessoaFisica.getMae, pessoaFisica.getPai, pessoaFisica.getSexo, pessoaFisica.getIdPessoa, self.__dataHora)

            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()

            # self.__cursor.close()
            return True
        except BaseException as os:
            self.__conexao.conn.rollback()
            return False


    def cadastrarEnderecoPessoa(self, pessoaFisica):
        try:
            _sql = "INSERT INTO endereco_pessoa (endereco, numero, complemento, bairro, id_cidade, id_pessoa) VALUES (%s, %s, %s, %s, %s, %s)"
            _valores = (pessoaFisica.getEndereco, pessoaFisica.getNumero, pessoaFisica.getComplemento, pessoaFisica.getBairro,  pessoaFisica.getIdCidade, pessoaFisica.getIdPessoa)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()

            # self.__cursor.close()
            return True
        except BaseException as os:
            self.__conexao.conn.rollback()
            return False

    def atualizarPessoa(self, pessoaFisica):

        try:
            __sql = "UPDATE pessoa SET atualizado = %s"
            _valores = (self.__dataHora)
            self.__cursor.execute(__sql, _valores)
            self.__conexao.conn.commit()
            #self.__cursor.close()
            return True
        except mysql.connector.Error as e:
            return False

    def atualizarPessoaFisica(self, pessoaFisica):

        try:
            __sql = "UPDATE pessoa_fisica SET nome = %s, apelido = %s, cpf = %s, rg = %s, expeditor = %s, uf = %s, aniversario = %s, mae = %s, pai = %s, id_genero = %s, atualizado = %s WHERE id_pessoa_fisica = %s"
            _valores = (pessoaFisica.getNome, pessoaFisica.getApelido, pessoaFisica.getCpf, pessoaFisica.getRg, pessoaFisica.getExpeditor, pessoaFisica.getUf, pessoaFisica.getData, pessoaFisica.getMae, pessoaFisica.getPai, pessoaFisica.getSexo, self.__dataHora, pessoaFisica.getIdPesFisica)
            self.__cursor.execute(__sql, _valores)
            self.__conexao.conn.commit()
            #self.__cursor.close()
            return True
        except mysql.connector.Error as e:
            return False

    def atualizarEnderecoPessoaFisica(self, pessoaFisica):

        try:
            __sql = "UPDATE endereco_pessoa SET endereco = %s, numero = %s, complemento = %s, bairro = %s, id_cidade = %s WHERE id_endereco_pessoa = %s"
            _valores = (pessoaFisica.getEndereco, pessoaFisica.getNumero, pessoaFisica.getComplemento, pessoaFisica.getBairro,  pessoaFisica.getIdCidade, pessoaFisica.getIdEnderecoPessoa)
            self.__cursor.execute(__sql, _valores)
            self.__conexao.conn.commit()
            #self.__cursor.close()
            return True
        except mysql.connector.Error as e:
            return False

    def deletarPessoa(self, pessoaFisica):
        try:
            __sql = "DELETE FROM pessoa WHERE id_pessoa = '"+pessoaFisica+"'"
            self.__cursor.execute(__sql)
            self.__conexao.conn.commit()
            #self.__cursor.close()
            return True
        except mysql.connector.Error as e:
            return False

    def deletarPessoaFisica(self, pessoaFisica):
        try:
            __sql = "DELETE FROM pessoa_fisica WHERE id_pessoa = '"+pessoaFisica+"'"
            self.__cursor.execute(__sql)
            self.__conexao.conn.commit()
            #self.__cursor.close()
            return True
        except mysql.connector.Error as e:
            return False

    def deletarEnderecoPessoaFisica(self, pessoaFisica):
        try:
            __sql = "DELETE FROM endereco_pessoa WHERE id_pessoa = '"+pessoaFisica+"'"
            self.__cursor.execute(__sql)
            self.__conexao.conn.commit()
            #self.__cursor.close()
            return True
        except mysql.connector.Error as e:
            return False