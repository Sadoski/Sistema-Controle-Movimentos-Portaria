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
            _sql = "SELECT * FROM pessoa WHERE nome_razao = %s and  cpf_cnpj = %s and rg_inscricao = %s"
            _valores = (pessoaFisica.getNome, pessoaFisica.getCpf, pessoaFisica.getRg)
            self.__cursor.execute(_sql, _valores)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarIdPessoaFisica(self, pessoaFisica):
        try:
            _sql = "SELECT p.id_pessoa, p.nome_razao, p.sobrenome_fantasia, p.cpf_cnpj, p.rg_inscricao, f.expeditor, f.uf, f.aniversario, g.sexo, f.mae, f.pai, p.endereco, p.numero, p.complemento, p.bairro, c.nome, s.nome, c.cep FROM pessoa p INNER JOIN pessoa_fisica f ON f.id_pessoa = p.id_pessoa INNER JOIN genero g ON g.id_genero = f.id_genero INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE p.id_pessoa = '"+str(pessoaFisica)+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def cadastrarPessoa(self, pessoaFisica):
        try:
            _sql = "INSERT INTO pessoa (nome_razao, sobrenome_fantasia, cpf_cnpj, rg_inscricao, endereco, numero, complemento, bairro, id_cidade, id_tipo_pessoa, cadastrado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            _valores = (pessoaFisica.getNome, pessoaFisica.getApelido, pessoaFisica.getCpf, pessoaFisica.getRg, pessoaFisica.getEndereco, pessoaFisica.getNumero, pessoaFisica.getComplemento, pessoaFisica.getBairro,  pessoaFisica.getIdCidade, pessoaFisica.getIdTipoPessoa, self.__dataHora)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()

            # self.__cursor.close()
            return True
        except BaseException as os:
            self.__conexao.conn.rollback()
            return False

    def cadastrarPessoaFisica(self, pessoaFisica):
        try:
            _sql = "INSERT INTO pessoa_fisica ( expeditor, uf, aniversario, mae, pai, id_genero, id_pessoa,  cadastrado) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)"
            _valores = ( pessoaFisica.getExpeditor, pessoaFisica.getUf, pessoaFisica.getData,  pessoaFisica.getMae, pessoaFisica.getPai, pessoaFisica.getSexo, pessoaFisica.getIdPessoa, self.__dataHora)

            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()

            # self.__cursor.close()
            return True
        except BaseException as os:
            self.__conexao.conn.rollback()
            return False

    def atualizarPessoa(self, pessoaFisica):

        try:
            __sql = "UPDATE pessoa SET nome_razao = %s, sobrenome_fantasia = %s, cpf_cnpj = %s, rg_inscricao = %s, endereco = %s, numero = %s, complemento = %s, bairro = %s, id_cidade = %s, id_tipo_pessoa = %s, atualizado = %s WHERE id_pessoa = %s"
            _valores = (pessoaFisica.getNome, pessoaFisica.getApelido, pessoaFisica.getCpf, pessoaFisica.getRg, pessoaFisica.getEndereco, pessoaFisica.getNumero, pessoaFisica.getComplemento, pessoaFisica.getBairro,  pessoaFisica.getIdCidade, pessoaFisica.getIdTipoPessoa, self.__dataHora, pessoaFisica.getIdPessoa)
            self.__cursor.execute(__sql, _valores)
            self.__conexao.conn.commit()
            #self.__cursor.close()
            return True
        except mysql.connector.Error as e:
            return False

    def atualizarPessoaFisica(self, pessoaFisica):

        try:
            __sql = "UPDATE pessoa_fisica SET expeditor = %s, uf = %s, aniversario = %s, mae = %s, pai = %s, id_genero = %s, id_pessoa = %s, atualizado = %s WHERE id_pessoa_fisica = %s"
            _valores = ( pessoaFisica.getExpeditor, pessoaFisica.getUf, pessoaFisica.getData,  pessoaFisica.getMae, pessoaFisica.getPai, pessoaFisica.getSexo, pessoaFisica.getIdPessoa, self.__dataHora, pessoaFisica.getIdPesFisica)
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

    def pesquisarTabelaCliente(self, pessoa):
        try:
            __sql = "SELECT * FROM cliente c INNER JOIN pesssoa_fisica f ON f.id_pessoa_fisica = c.id_pessoa_fisica INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa WHERE p.id_pessoa = '"+pessoa+"'"
            self.__cursor.execute(__sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except mysql.connector.Error as e:
            return False

    def pesquisarTabelaFornecedor(self, pessoa):
        try:
            __sql = "SELECT * FROM fornecedor c INNER JOIN pesssoa_fisica f ON f.id_pessoa_fisica = c.id_pessoa_fisica INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa WHERE p.id_pessoa = '"+pessoa+"'"
            self.__cursor.execute(__sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except mysql.connector.Error as e:
            return False

    def pesquisarTabelaFuncionario(self, pessoa):
        try:
            __sql = "SELECT * FROM funcionario c INNER JOIN pesssoa_fisica f ON f.id_pessoa_fisica = c.id_pessoa_fisica INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa WHERE p.id_pessoa = '"+pessoa+"'"
            self.__cursor.execute(__sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except mysql.connector.Error as e:
            return False
