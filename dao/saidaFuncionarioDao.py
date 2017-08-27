import sys
import time
import datetime
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mysql.connector import Error
from conexao.conexao import ConexaoDb, mysql


class SaidaFuncionarioDao(object):
    def __init__(self):
        self.__conexao = ConexaoDb()
        self.__cursor = self.__conexao.conn.cursor()

    def pesquisarFuncionario(self, nome):
        try:
            _sql = "SELECT f.id_funcionario, d.id_funcao, t.descricao, l.descricao FROM funcionario f INNER JOIN funcao d ON d.id_funcao = f.id_funcao INNER JOIN setores t ON t.id_setores = d.id_setores INNER JOIN cargo l ON l.id_cargo = d.id_cargo WHERE f.nome = '"+nome+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarIdFuncao(self, funcao):
        try:
            _sql = "SELECT d.id_funcao FROM funcionario f INNER JOIN funcao d ON d.id_funcao = f.id_funcao INNER JOIN setores t ON t.id_setores = d.id_setores INNER JOIN cargo l ON l.id_cargo = d.id_cargo WHERE f.id_funcionario = '"+funcao+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarIdSaidaFuncionario(self, funcao):
        try:
            _sql = "SELECT m.id_saida_funcionario  FROM saida_funcionario m INNER JOIN funcionario f ON f.id_funcionario = m.id_funcionario INNER JOIN funcao d ON D.id_funcao = f.id_funcao INNER JOIN setores s ON s.id_setores = d.id_setores INNER JOIN cargo c ON c.id_cargo = d.id_cargo WHERE m.id_saida_funcionario = '"+funcao+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def cadastro(self, funcionario):
        try:
            _sql = "INSERT INTO saida_funcionario (id_funcionario, id_funcao, data, hora) VALUES (%s, %s, %s, %s)"
            _valores = (funcionario.getIdFuncionario, funcionario.getIdFuncao, funcionario.getData, funcionario.getHora)
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

    def editar(self, funcionario):

        try:
            __sql = "UPDATE saida_funcionario SET id_funcionario = %s, id_funcao = %s, data = %s, hora = %s  WHERE id_saida_funcionario = %s"
            _valores = (funcionario.getIdFuncionario, funcionario.getIdFuncao, funcionario.getData, funcionario.getHora, funcionario.getIdSaida)

            self.__cursor.execute(__sql, _valores)
            self.__conexao.conn.commit()
            QMessageBox.warning(QWidget(), 'Mensagem', "Edição realizado com sucesso!")
            # self.__cursor.close()
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao atualizar as informações no banco de dados")
            self.__conexao.conn.rollback()
            return False

    def deletar(self, saida):
        try:
            __sql = "DELETE FROM saida_funcionario WHERE id_saida_funcionario = '" + saida + "'"
            self.__cursor.execute(__sql)
            self.__conexao.conn.commit()
            # self.__cursor.close()
            QMessageBox.warning(QWidget(), 'Mensagem', "Exclusão realizado com sucesso!")
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao deletar as informações no banco de dados")
            self.__conexao.conn.rollback()
            return False

    def pesquisarCodigoFuncionario(self, funcionario):
        try:
            _sql = "SELECT f.id_funcionario, f.nome, m.data, m.hora, d.id_funcao, s.descricao, c.descricao  FROM saida_funcionario m INNER JOIN funcionario f ON f.id_funcionario = m.id_funcionario INNER JOIN funcao d ON D.id_funcao = f.id_funcao INNER JOIN setores s ON s.id_setores = d.id_setores INNER JOIN cargo c ON c.id_cargo = d.id_cargo WHERE f.id_funcionario = '"+funcionario+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarNomeFuncionario(self, funcionario):
        try:
            _sql = "SELECT f.id_funcionario,f.nome, m.data, m.hora, d.id_funcao, s.descricao, c.descricao  FROM saida_funcionario m INNER JOIN funcionario f ON f.id_funcionario = m.id_funcionario INNER JOIN funcao d ON D.id_funcao = f.id_funcao INNER JOIN setores s ON s.id_setores = d.id_setores INNER JOIN cargo c ON c.id_cargo = d.id_cargo WHERE f.nome LIKE '%"+funcionario+"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarRgFuncionario(self, funcionario):
        try:
            _sql = "SELECT f.id_funcionario,f.nome, m.data, m.hora, d.id_funcao, s.descricao, c.descricao  FROM saida_funcionario m INNER JOIN funcionario f ON f.id_funcionario = m.id_funcionario INNER JOIN funcao d ON D.id_funcao = f.id_funcao INNER JOIN setores s ON s.id_setores = d.id_setores INNER JOIN cargo c ON c.id_cargo = d.id_cargo WHERE f.rg = '"+funcionario+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarCpfFuncionario(self, funcionario):
        try:
            _sql = "SELECT f.id_funcionario,f.nome, m.data, m.hora, d.id_funcao, s.descricao, c.descricao  FROM saida_funcionario m INNER JOIN funcionario f ON f.id_funcionario = m.id_funcionario INNER JOIN funcao d ON D.id_funcao = f.id_funcao INNER JOIN setores s ON s.id_setores = d.id_setores INNER JOIN cargo c ON c.id_cargo = d.id_cargo WHERE f.cpf ='"+funcionario+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False
