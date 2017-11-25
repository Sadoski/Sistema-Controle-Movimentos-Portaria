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

    def pesquisarPessoaJuridica(self, pessoaJuridica):
        try:
            _sql = "SELECT * FROM pessoa_juridica WHERE razao_social = %s and  cnpj = %s and ins_estadual = %s"
            _valores = (pessoaJuridica.getRazao, pessoaJuridica.getCnpj, pessoaJuridica.getInscricao)
            self.__cursor.execute(_sql, _valores)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def cadastrarPessoaJuridica(self, pessoaJuridica):
        try:
            _sql = "INSERT INTO pessoa_juridica (razao_social, fantasia, cnpj, ins_estadual, endereco, numero, complemento, bairro, id_cidade, site, cadastrado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            _valores = (pessoaJuridica.getRazao, pessoaJuridica.getFantasia, pessoaJuridica.getCnpj, pessoaJuridica.getInscricao, pessoaJuridica.getEndereco, pessoaJuridica.getNumero, pessoaJuridica.getComplemento, pessoaJuridica.getBairro, pessoaJuridica.getIdCidade, pessoaJuridica.getSite, self.__dataHora)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            # self.__cursor.close()
            QMessageBox.warning(QWidget(), 'Mensagem', "Cadastro realizado com sucesso!")
        except BaseException as os:
            QMessageBox.warning(QWidget(), 'Erro', "Erro ao inserir as informações no banco de dados")
            return False

    def atualizarPessoaJuridica(self, pessoaJuridica):

        try:
            __sql = "UPDATE pessoa_juridica SET razao_social = %s, fantasia = %s, cnpj = %s, ins_estadual = %s, endereco = %s, numero = %s, complemento = %s, bairro = %s, id_cidade = %s, site = %s, atualizado = %s WHERE id_pessoa_juridica = %s"
            _valores = (pessoaJuridica.getRazao, pessoaJuridica.getFantasia, pessoaJuridica.getCnpj, pessoaJuridica.getInscricao, pessoaJuridica.getEndereco, pessoaJuridica.getNumero, pessoaJuridica.getComplemento, pessoaJuridica.getBairro, pessoaJuridica.getIdCidade, pessoaJuridica.getSite, self.__dataHora, pessoaJuridica.getIdPesJuridica)
            a = self.__cursor.execute(__sql, _valores)
            self.__conexao.conn.commit()
            #self.__cursor.close()
            QMessageBox.warning(QWidget(), 'Mensagem', "Cadastro atualizado com sucesso!")
        except mysql.connector.Error as e:
            QMessageBox.warning(QWidget(), 'Erro', "Erro ao atualizar as informações no banco de dados")
            return False

    def deletarPessoaJuridica(self, pessoaJuridica):
        try:
            __sql = "DELETE FROM pessoa_juridica WHERE id_pessoa_juridica = '"+pessoaJuridica+"'"
            self.__cursor.execute(__sql)
            self.__conexao.conn.commit()
            #self.__cursor.close()
            QMessageBox.warning(QWidget(), 'Mensagem', "Cadastro deletado com sucesso!")
        except mysql.connector.Error as e:
            QMessageBox.warning(QWidget(), 'Erro', "Erro ao deletar as informações no banco de dados")
            return False