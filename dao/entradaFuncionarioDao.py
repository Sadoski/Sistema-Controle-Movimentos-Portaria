import sys
import time
import datetime
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mysql.connector import Error
from conexao.conexao import ConexaoDb, mysql


class EntradaFuncionarioDao(object):
    def __init__(self):
        self.__conexao = ConexaoDb()
        self.__cursor = self.__conexao.conn.cursor()


    def pesquisarNome(self, nome):
        try:
            _sql = "SELECT p.id_saida_funcionario, f.id_funcionario, f.nome, t.descricao, l.descricao, p.data, p.hora FROM saida_funcionario p INNER JOIN funcionario f ON f.id_funcionario = p.id_funcionario INNER JOIN funcao d ON d.id_funcao = f.id_funcao INNER JOIN setores t ON t.id_setores = d.id_setores INNER JOIN cargo l ON l.id_cargo = d.id_cargo WHERE f.nome like '%"+nome+"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarCpf(self, cpf):
        try:
            _sql = "SELECT p.id_saida_funcionario, f.id_funcionario, f.nome, t.descricao, l.descricao, p.data, p.hora FROM saida_funcionario p INNER JOIN funcionario f ON f.id_funcionario = p.id_funcionario INNER JOIN funcao d ON d.id_funcao = f.id_funcao INNER JOIN setores t ON t.id_setores = d.id_setores INNER JOIN cargo l ON l.id_cargo = d.id_cargo WHERE f.cpf = '"+cpf+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarRg(self, rg):
        try:
            _sql = "SELECT p.id_saida_funcionario, f.id_funcionario, f.nome, t.descricao, l.descricao, p.data, p.hora FROM saida_funcionario p INNER JOIN funcionario f ON f.id_funcionario = p.id_funcionario INNER JOIN funcao d ON d.id_funcao = f.id_funcao INNER JOIN setores t ON t.id_setores = d.id_setores INNER JOIN cargo l ON l.id_cargo = d.id_cargo WHERE f.rg = '"+rg+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarSetor(self, setor):
        try:
            _sql = "SELECT p.id_saida_funcionario, f.id_funcionario, f.nome, t.descricao, l.descricao, p.data, p.hora FROM saida_funcionario p INNER JOIN funcionario f ON f.id_funcionario = p.id_funcionario INNER JOIN funcao d ON d.id_funcao = f.id_funcao INNER JOIN setores t ON t.id_setores = d.id_setores INNER JOIN cargo l ON l.id_cargo = d.id_cargo WHERE t.descricao = '"+setor+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarCargo(self, cargo):
        try:
            _sql = "SELECT p.id_saida_funcionario, f.id_funcionario, f.nome, t.descricao, l.descricao, p.data, p.hora FROM saida_funcionario p INNER JOIN funcionario f ON f.id_funcionario = p.id_funcionario INNER JOIN funcao d ON d.id_funcao = f.id_funcao INNER JOIN setores t ON t.id_setores = d.id_setores INNER JOIN cargo l ON l.id_cargo = d.id_cargo WHERE l.descricao = '"+cargo+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def cadastro(self, entrada):
        try:
            _sql = "INSERT INTO entrada_funcionario (id_saida_funcionario, data, hora) VALUES (%s, %s, %s)"
            _valores = (entrada.getIdSaida, entrada.getData, entrada.getHora)
            print(_valores)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            # self.__cursor.close()
            QMessageBox.warning(QWidget(), 'Mensagem', "Cadastro realizado com sucesso!")
            return True
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False