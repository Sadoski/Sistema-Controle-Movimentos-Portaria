import time
import datetime
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mysql.connector import Error
from conexao.conexao import ConexaoDb, mysql

class PessoaJuridicaDao(object):

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

    def pesquisarPessoaJuridica(self, pessoaJuridica):
        try:
            _sql = "SELECT * FROM pessoa WHERE nome_razao = %s and  cpf_cnpj = %s and rg_inscricao = %s"
            _valores = (pessoaJuridica.getRazao, pessoaJuridica.getCnpj, pessoaJuridica.getInscricao)
            self.__cursor.execute(_sql, _valores)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarIdPessoaJuridica(self, pessoaJuridica):
        try:
            _sql = "SELECT p.id_pessoa_juridica FROM pessoa p INNER JOIN pessoa_juridica j ON j.id_pessoa = p.id_pessoa INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE  t.descricao = 'PESSOA JURIDICA' AND p.id_pessoa = '"+ str(pessoaJuridica) +"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def cadastrarPessoa(self, pessoaJuridica):
        try:
            _sql = "INSERT INTO pessoa (nome_razao, sobrenome_fantasia, cpf_cnpj, rg_inscricao, endereco, numero, complemento, bairro, id_cidade, id_tipo_pessoa, cadastrado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            _valores = (pessoaJuridica.getRazao, pessoaJuridica.getFantasia, pessoaJuridica.getCnpj, pessoaJuridica.getInscricao, pessoaJuridica.getEndereco, pessoaJuridica.getNumero, pessoaJuridica.getComplemento, pessoaJuridica.getBairro, pessoaJuridica.getIdCidade, pessoaJuridica.getIdTipoPessoa,   self.__dataHora)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()

            # self.__cursor.close()
            return True
        except BaseException as os:
            self.__conexao.conn.rollback()
            return False

    def cadastrarPessoaJuridica(self, pessoaJuridica):
        try:
            _sql = "INSERT INTO pessoa_juridica ( site, id_pessoa, cadastrado) VALUES (%s, %s, %s)"
            _valores = ( pessoaJuridica.getSite, pessoaJuridica.getIdPessoa, self.__dataHora)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            # self.__cursor.close()
            return True
        except BaseException as os:
            return False

    def atualizarPessoa(self, pessoaJuridica):

        try:
            __sql = "UPDATE pessoa SET nome_razao = %s, sobrenome_fantasia = %s, cpf_cnpj = %s, rg_inscricao = %s, endereco = %s, numero = %s, complemento = %s, bairro = %s, id_cidade = %s, id_tipo_pessoa = %s, atualizado = %s WHERE id_pessoa = %s"
            _valores = (pessoaJuridica.getRazao, pessoaJuridica.getFantasia, pessoaJuridica.getCnpj, pessoaJuridica.getInscricao, pessoaJuridica.getEndereco, pessoaJuridica.getNumero, pessoaJuridica.getComplemento, pessoaJuridica.getBairro, pessoaJuridica.getIdCidade, pessoaJuridica.getIdTipoPessoa,   self.__dataHora, pessoaJuridica.getIdPessoa)
            self.__cursor.execute(__sql, _valores)
            self.__conexao.conn.commit()
            #self.__cursor.close()
            return True
        except mysql.connector.Error as e:
            return False

    def atualizarPessoaJuridica(self, pessoaJuridica):

        try:
            __sql = "UPDATE pessoa_juridica SET site = %s,  atualizado = %s WHERE id_pessoa_juridica = %s"
            _valores = ( pessoaJuridica.getSite, self.__dataHora, pessoaJuridica.getIdPesJuridica)
            self.__cursor.execute(__sql, _valores)
            self.__conexao.conn.commit()
            #self.__cursor.close()
            return True
        except mysql.connector.Error as e:
            return False

    def deletarPessoa(self, pessoaJuridica):
        try:
            __sql = "DELETE FROM pessoa WHERE id_pessoa = '"+pessoaJuridica+"'"
            self.__cursor.execute(__sql)
            self.__conexao.conn.commit()
            #self.__cursor.close()
            return True
        except mysql.connector.Error as e:
            return False

    def deletarPessoaJuridica(self, pessoaJuridica):
        try:
            __sql = "DELETE FROM pessoa_juridica WHERE id_pessoa_juridica = '"+pessoaJuridica+"'"
            self.__cursor.execute(__sql)
            self.__conexao.conn.commit()
            #self.__cursor.close()
            return True
        except mysql.connector.Error as e:
            return False

    def pesquisarTabelaCliente(self, pessoa):
        try:
            __sql = "SELECT * FROM cliente c INNER JOIN pessoa_juridica f ON f.id_pessoa_juridica = c.id_pessoa_juridica INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa WHERE p.id_pessoa = '" + pessoa + "'"
            self.__cursor.execute(__sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except mysql.connector.Error as e:
            return False

    def pesquisarTabelaFornecedor(self, pessoa):
        try:
            __sql = "SELECT * FROM fornecedor c INNER JOIN pesssoa_juridica f ON f.id_pessoa_juridica = c.id_pessoa_juridica INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa WHERE p.id_pessoa = '" + pessoa + "'"
            self.__cursor.execute(__sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except mysql.connector.Error as e:
            return False

    def pesquisarTabelaEmpresa(self, pessoa):
        try:
            __sql = "SELECT * FROM empresa c INNER JOIN pessoa_juridica f ON f.id_pessoa_juridica = c.id_pessoa_juridica INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa WHERE p.id_pessoa = '" + pessoa + "'"
            self.__cursor.execute(__sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except mysql.connector.Error as e:
            return False