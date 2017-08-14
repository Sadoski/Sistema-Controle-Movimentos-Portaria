# coding=utf-8
import sys
import time
import datetime
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mysql.connector import Error
from conexao.conexao import ConexaoDb, mysql
from controller.getSetCidade import Cidades
from controller.getSetEmpresa import Empresas


class SetoresCargosDao(object):
    def __init__(self):
        self.__conexao = ConexaoDb()
        self.__cursor = self.__conexao.conn.cursor()
        self.__ts = time.time()
        self.__dataHora = datetime.datetime.fromtimestamp(self.__ts).strftime('%Y-%m-%d %H:%M:%S')

    def cadastrarSetor(self, setor):
        try:
            _sql = "INSERT INTO setores (descricao, id_empresa, cadastrado) VALUES (%s, %s, %s)"
            _valores = (setor.getSetor, setor.getIdEmpresa, self.__dataHora)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            # self.__cursor.close()
            w = QWidget()
            QMessageBox.warning(w, 'Mensagem', "Cadastro realizado com sucesso!")
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False

    def cadastrarCargo(self, cargo):
        try:
            _sql = "INSERT INTO cargo (descricao, id_empresa, cadastrado) VALUES (%s, %s, %s)"
            _valores = (cargo.getCargo, cargo.getIdEmpresa, self.__dataHora)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            # self.__cursor.close()
            w = QWidget()
            QMessageBox.warning(w, 'Mensagem', "Cadastro realizado com sucesso!")
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False

    def cadastrarRelacao(self, relacao):
        try:
            _sql = "INSERT INTO funcao (id_cargo, id_setores, cadastrado) VALUES (%s, %s, %s)"
            _valores = (relacao.getIdCargo, relacao.getIdSetor, self.__dataHora)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            # self.__cursor.close()
            w = QWidget()
            QMessageBox.warning(w, 'Mensagem', "Cadastro realizado com sucesso!")
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False

    def pesquisaSetor(self):
        try:
            __sql = "SELECT descricao FROM setores"
            self.__cursor.execute(__sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False

    def pesquisarIdSetoresEmpresa(self, setores):
        try:
            _sql = "SELECT s.id_setores, s.descricao, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual, t.descricao from setores s INNER JOIN empresa e ON e.id_empresa = s.id_empresa INNER JOIN tipo_empresa t ON t.id_tipo_empresa = e.id_tipo_empresa where s.id_setores = '" + setores + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarFantasiaSetoresEmpresa(self, setores):
        try:
            _sql = "SELECT s.id_setores, s.descricao, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual, t.descricao from setores s INNER JOIN empresa e ON e.id_empresa = s.id_empresa INNER JOIN tipo_empresa t ON t.id_tipo_empresa = e.id_tipo_empresa where e.fantasia LIKE '%"+setores+"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarRazaoSocialSetoresEmpresa(self, setores):
        try:
            _sql = "SELECT s.id_setores, s.descricao, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual, t.descricao from setores s INNER JOIN empresa e ON e.id_empresa = s.id_empresa INNER JOIN tipo_empresa t ON t.id_tipo_empresa = e.id_tipo_empresa where e.razao_social LIKE '%"+setores+"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarCnpjSetoresEmpresa(self, setores):
        try:
            _sql = "SELECT s.id_setores, s.descricao, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual, t.descricao from setores s INNER JOIN empresa e ON e.id_empresa = s.id_empresa INNER JOIN tipo_empresa t ON t.id_tipo_empresa = e.id_tipo_empresa where e.cnpj = '" + setores + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarInscEstadualSetoresEmpresa(self, setores):
        try:
            _sql = "SELECT s.id_setores, s.descricao, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual, t.descricao from setores s INNER JOIN empresa e ON e.id_empresa = s.id_empresa INNER JOIN tipo_empresa t ON t.id_tipo_empresa = e.id_tipo_empresa where e.inscricao_estadual = '" + setores + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarSetoresEmpresa(self, setores):
        try:
            _sql = "SELECT s.id_setores, s.descricao, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual, t.descricao from setores s INNER JOIN empresa e ON e.id_empresa = s.id_empresa INNER JOIN tipo_empresa t ON t.id_tipo_empresa = e.id_tipo_empresa where s.descricao = '" + setores + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarIdCargoEmpresa(self, cargo):
        try:
            _sql = "SELECT c.id_cargo, c.descricao, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual, t.descricao from cargo c INNER JOIN empresa e ON e.id_empresa = c.id_empresa INNER JOIN tipo_empresa t ON t.id_tipo_empresa = e.id_tipo_empresa where c.id_cargo = '" + cargo + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarFantasiaCargoEmpresa(self, cargo):
        try:
            _sql = "SELECT c.id_cargo, c.descricao, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual, t.descricao from cargo c INNER JOIN empresa e ON e.id_empresa = c.id_empresa INNER JOIN tipo_empresa t ON t.id_tipo_empresa = e.id_tipo_empresa where e.fantasia LIKE '%"+cargo+"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarRazaoSocialCargoEmpresa(self, cargo):
        try:
            _sql = "SELECT c.id_cargo, c.descricao, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual, t.descricao from cargo c INNER JOIN empresa e ON e.id_empresa = c.id_empresa INNER JOIN tipo_empresa t ON t.id_tipo_empresa = e.id_tipo_empresa where e.razao_social LIKE '%"+cargo+"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarCnpjCargoEmpresa(self, cargo):
        try:
            _sql = "SELECT c.id_cargo, c.descricao, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual, t.descricao from cargo c INNER JOIN empresa e ON e.id_empresa = c.id_empresa INNER JOIN tipo_empresa t ON t.id_tipo_empresa = e.id_tipo_empresa where e.cnpj = '" + cargo + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarInscEstadualCargoEmpresa(self, cargo):
        try:
            _sql = "SELECT c.id_cargo, c.descricao, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual, t.descricao from cargo c INNER JOIN empresa e ON e.id_empresa = c.id_empresa INNER JOIN tipo_empresa t ON t.id_tipo_empresa = e.id_tipo_empresa where e.inscricao_estadual = '" + cargo + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarCargoEmpresa(self, cargo):
        try:
            _sql = "SELECT c.id_cargo, c.descricao, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual, t.descricao from cargo c INNER JOIN empresa e ON e.id_empresa = c.id_empresa INNER JOIN tipo_empresa t ON t.id_tipo_empresa = e.id_tipo_empresa where c.descricao = '" + cargo + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarIdRelacaoEmpresa(self, relacao):
        try:
            _sql = "SELECT f.id_funcao, s.descricao, c.descricao, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual, t.descricao from funcao f INNER JOIN setores s ON s.id_setores = f.id_setores INNER JOIN cargo c ON c.id_cargo = f.id_cargo INNER JOIN empresa e ON e.id_empresa = s.id_empresa INNER JOIN tipo_empresa t ON t.id_tipo_empresa = e.id_tipo_empresa where f.id_funcao = '"+relacao+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarFantasiaRelacaoEmpresa(self, relacao):
        try:
            _sql = "SELECT f.id_funcao, s.descricao, c.descricao, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual, t.descricao from funcao f INNER JOIN setores s ON s.id_setores = f.id_setores INNER JOIN cargo c ON c.id_cargo = f.id_cargo INNER JOIN empresa e ON e.id_empresa = s.id_empresa INNER JOIN tipo_empresa t ON t.id_tipo_empresa = e.id_tipo_empresa where e.fantasia LIKE '%"+relacao+"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarRazaoSocialRelacaoEmpresa(self, relacao):
        try:
            _sql = "SELECT f.id_funcao, s.descricao, c.descricao, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual, t.descricao from funcao f INNER JOIN setores s ON s.id_setores = f.id_setores INNER JOIN cargo c ON c.id_cargo = f.id_cargo INNER JOIN empresa e ON e.id_empresa = s.id_empresa INNER JOIN tipo_empresa t ON t.id_tipo_empresa = e.id_tipo_empresa where e.razao_social LIKE '%"+relacao+"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarCnpjRelacaoEmpresa(self, relacao):
        try:
            _sql = "SELECT f.id_funcao, s.descricao, c.descricao, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual, t.descricao from funcao f INNER JOIN setores s ON s.id_setores = f.id_setores INNER JOIN cargo c ON c.id_cargo = f.id_cargo INNER JOIN empresa e ON e.id_empresa = s.id_empresa INNER JOIN tipo_empresa t ON t.id_tipo_empresa = e.id_tipo_empresa where e.cnpj = '"+relacao+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarSetorRelacaoEmpresa(self, relacao):
        try:
            _sql = "SELECT f.id_funcao, s.descricao, c.descricao, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual, t.descricao from funcao f INNER JOIN setores s ON s.id_setores = f.id_setores INNER JOIN cargo c ON c.id_cargo = f.id_cargo INNER JOIN empresa e ON e.id_empresa = s.id_empresa INNER JOIN tipo_empresa t ON t.id_tipo_empresa = e.id_tipo_empresa where s.descricao LIKE '%"+relacao+"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarCargoRelacaoEmpresa(self, relacao):
        try:
            _sql = "SELECT f.id_funcao, s.descricao, c.descricao, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual, t.descricao from funcao f INNER JOIN setores s ON s.id_setores = f.id_setores INNER JOIN cargo c ON c.id_cargo = f.id_cargo INNER JOIN empresa e ON e.id_empresa = s.id_empresa INNER JOIN tipo_empresa t ON t.id_tipo_empresa = e.id_tipo_empresa where c.descricao LIKE '%"+relacao+"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaCargo(self):
        try:
            __sql = "SELECT descricao FROM cargo"
            self.__cursor.execute(__sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False

    def verificarSetor(self, setor):
        try:
            __sql = "SELECT id_setores FROM setores WHERE descricao = '"+setor+"'"
            self.__cursor.execute(__sql)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()
            return result
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False

    def verificarCargo(self, cargo):
        try:
            __sql = "SELECT id_cargo FROM cargo WHERE descricao = '"+cargo+"'"
            self.__cursor.execute(__sql)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()
            return result
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False

    def pesquisarFuncao(self, funcao):
        try:
            __sql = "SELECT c.descricao FROM funcao f INNER JOIN setores s ON s.id_setores = f.id_setores INNER JOIN cargo c ON c.id_cargo = f.id_cargo WHERE s.descricao = '"+funcao+"'"
            self.__cursor.execute(__sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False