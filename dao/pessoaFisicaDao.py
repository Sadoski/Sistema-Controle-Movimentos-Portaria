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

    def cadastrarPessoaFisica(self, pessoaFisica):
        try:
            _sql = "INSERT INTO pessoa_fisica (nome, cpf, rg, expeditor, aniversario, endereco, numero, complemento, bairro, mae, pai, id_genero, id_cidade, cadastrado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            _valores = (pessoaFisica.getNome, pessoaFisica.getCpf, pessoaFisica.getRg, pessoaFisica.getExpeditor, pessoaFisica.getData, pessoaFisica.getEndereco, pessoaFisica.getNumero, pessoaFisica.getComplemento, pessoaFisica.getBairro, pessoaFisica.getMae, pessoaFisica.getPai, pessoaFisica.getSexo, pessoaFisica.getIdCidade, self.__dataHora)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()

            # self.__cursor.close()
            QMessageBox.warning(QWidget(), 'Mensagem', "Cadastro realizado com sucesso!")
        except BaseException as os:
            QMessageBox.warning(QWidget(), 'Erro', "Erro ao inserir as informações no banco de dados")
            self.__conexao.conn.rollback()
            return False

    def atualizarPessoaFisica(self, pessoaFisica):

        try:
            __sql = "UPDATE pessoa_fisica SET nome = %s, cpf = %s, rg = %s, expeditor = %s, aniversario = %s, endereco = %s, numero = %s, complemento = %s, bairro = %s, mae = %s, pai = %s, id_genero = %s,  id_cidade = %s, atualizado = %s WHERE id_pessoa_fisica = %s"
            _valores = (pessoaFisica.getNome, pessoaFisica.getCpf, pessoaFisica.getRg, pessoaFisica.getExpeditor, pessoaFisica.getData, pessoaFisica.getEndereco, pessoaFisica.getNumero, pessoaFisica.getComplemento, pessoaFisica.getBairro, pessoaFisica.getMae, pessoaFisica.getPai, pessoaFisica.getSexo, pessoaFisica.getIdCidade, self.__dataHora, pessoaFisica.getIdPesFisica)
            a = self.__cursor.execute(__sql, _valores)
            self.__conexao.conn.commit()
            #self.__cursor.close()
            QMessageBox.warning(QWidget(), 'Mensagem', "Cadastro atualizado com sucesso!")

        except mysql.connector.Error as e:
            QMessageBox.warning(QWidget(), 'Erro', "Erro ao atualizar as informações no banco de dados")
            return False

    def deletarPessoaFisica(self, pessoaFisica):
        try:
            __sql = "DELETE FROM pessoa_fisica WHERE id_pessoa_fisica = '"+pessoaFisica+"'"
            self.__cursor.execute(__sql)
            self.__conexao.conn.commit()
            #self.__cursor.close()
            QMessageBox.warning(QWidget(), 'Mensagem', "Cadastro deletado com sucesso!")
        except mysql.connector.Error as e:
            QMessageBox.warning(QWidget(), 'Erro', "Erro ao deletar as informações no banco de dados")
            return False