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
            _valores = (pessoaFisica.getNome, pessoaFisica.getCpf, pessoaFisica.getRg, pessoaFisica.getExpeditor, pessoaFisica.getData, pessoaFisica.getEndereco, pessoaFisica.getNumero, pessoaFisica.getComplemento, pessoaFisica.getBairro, pessoaFisica.getMae, pessoaFisica.getPai, pessoaFisica.getSexo, pessoaFisica.getCidade, self.__dataHora)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            # self.__cursor.close()
            QMessageBox.warning(QWidget(), 'Mensagem', "Cadastro realizado com sucesso!")
        except BaseException as os:
            return False