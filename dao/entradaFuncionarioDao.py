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
        self.__ts = time.time()
        self.__dataHora = datetime.datetime.fromtimestamp(self.__ts).strftime('%Y-%m-%d')


    def pesquisarSaida(self):
        try:
            _sql = "SELECT p.id_saida_funcionario, p.data, p.hora, s.nome_razao, s.sobrenome_fantasia, t.descricao, l.descricao FROM saida_funcionario p INNER JOIN funcionario f ON f.id_funcionario = p.id_funcionario INNER JOIN pessoa_fisica e ON e.id_pessoa_fisica = f.id_pessoa_fisica INNER JOIN pessoa s ON s.id_pessoa = e.id_pessoa INNER JOIN setores t ON t.id_setores = f.id_setores INNER JOIN cargo l ON l.id_cargo = f.id_cargo WHERE p.status = 'Aberto' and p.data = '"+self.__dataHora+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarIdFuncionario(self, codigo):
        try:
            _sql = "SELECT p.id_funcionario FROM saida_funcionario p INNER JOIN funcionario f ON f.id_funcionario = p.id_funcionario INNER JOIN pessoa_fisica e ON e.id_pessoa_fisica = f.id_pessoa_fisica INNER JOIN pessoa s ON s.id_pessoa = e.id_pessoa INNER JOIN setores t ON t.id_setores = f.id_setores INNER JOIN cargo l ON l.id_cargo = f.id_cargo WHERE p.id_saida_funcionario = '"+codigo+"'"
            print(_sql)
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
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
            QMessageBox.information(QWidget(), 'Mensagem', "Entrada realizado com sucesso!")
            return True
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False

    def updateSaidaFuncionario(self):
        try:
            __sql = "UPDATE saida_funcionario SET status = 'Fechado'"
            self.__cursor.execute(__sql)
            self.__conexao.conn.commit()
            # self.__cursor.close()
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao atualizar as informações no banco de dados")
            self.__conexao.conn.rollback()
            return False