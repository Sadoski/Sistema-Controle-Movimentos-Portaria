import sys
import time
import datetime
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mysql.connector import Error
from conexao.conexao import ConexaoDb, mysql


class FornecedorDao(object):
    def __init__(self):
        self.__conexao = ConexaoDb()
        self.__cursor = self.__conexao.conn.cursor()
        self.__ts = time.time()
        self.__dataHora = datetime.datetime.fromtimestamp(self.__ts).strftime('%Y-%m-%d %H:%M:%S')

    def cadastrarFornecedor(self, fornecedor):
        try:
            _sql = "INSERT INTO fornecedor (fantasia, razao_social, cnpj, inscricao_estadual, endereco, numero_endereco, complemento, bairro, telefone, site, email, cadastrado, id_cidades, id_empresa) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            _valores = (fornecedor.getFantasia, fornecedor.getRazaoSocial, fornecedor.getCnpj, fornecedor.getInscricaoEstadual, fornecedor.getEndereco, fornecedor.getNumero, fornecedor.getComplemento, fornecedor.getBairro, fornecedor.getTelefone, fornecedor.getSite, fornecedor.getEmail, self.__dataHora, fornecedor.getCidade, fornecedor.getEmpresa)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            # self.__cursor.close()
            QMessageBox.warning(QWidget(), 'Mensagem', "Cadastro realizado com sucesso!")

        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False

    def atualizarFornecedor(self, fornecedor):

        try:
            __sql = "UPDATE fornecedor SET fantasia = %s, razao_social = %s, cnpj = %s, inscricao_estadual = %s, endereco = %s, numero_endereco = %s, complemento = %s, bairro = %s, telefone = %s, site = %s, email = %s, atualizado = %s, id_cidades = %s, id_empresa = %s WHERE id_fornecedor = %s"
            _valores = (fornecedor.getFantasia, fornecedor.getRazaoSocial, fornecedor.getCnpj, fornecedor.getInscricaoEstadual, fornecedor.getEndereco, fornecedor.getNumero, fornecedor.getComplemento, fornecedor.getBairro, fornecedor.getTelefone, fornecedor.getSite, fornecedor.getEmail, self.__dataHora, fornecedor.getCidade, fornecedor.getEmpresa, fornecedor.getIdFornecedor)
            self.__cursor.execute(__sql, _valores)
            self.__conexao.conn.commit()
            # self.__cursor.close()
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao atualizar as informações no banco de dados")
            self.__conexao.conn.rollback()
            return False

    def deletarFornecedor(self, fornecedor):
        try:
            __sql = "DELETE FROM fornecedor WHERE id_fornecedor = '" + fornecedor + "'"
            self.__cursor.execute(__sql)
            self.__conexao.conn.commit()
            # self.__cursor.close()
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao deletar as informações no banco de dados")
            self.__conexao.conn.rollback()
            return False

    def pesquisaCodigo(self, pesquisa):
        try:
            _sql = " SELECT f.id_fornecedor, f.fantasia, f.razao_social, f.cnpj, f.inscricao_estadual, f.endereco, f.numero_endereco, f.complemento, f.bairro, f.telefone, f.site, f.email, c.cep, c.nome, s.nome, e.id_empresa, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual FROM fornecedor f INNER JOIN cidade c ON c.id_cidade = f.id_cidades INNER JOIN estado s ON s.id_estado = c.id_estado INNER JOIN empresa e ON e.id_empresa = f.id_empresa WHERE f.id_fornecedor = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaFantasia(self, pesquisa):
        try:
            _sql = " SELECT f.id_fornecedor, f.fantasia, f.razao_social, f.cnpj, f.inscricao_estadual, f.endereco, f.numero_endereco, f.complemento, f.bairro, f.telefone, f.site, f.email, c.cep, c.nome, s.nome, e.id_empresa, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual FROM fornecedor f INNER JOIN cidade c ON c.id_cidade = f.id_cidades INNER JOIN estado s ON s.id_estado = c.id_estado INNER JOIN empresa e ON e.id_empresa = f.id_empresa WHERE f.fantasia LIKE '%"+pesquisa+"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaRazaoSocial(self, pesquisa):
        try:
            _sql = " SELECT f.id_fornecedor, f.fantasia, f.razao_social, f.cnpj, f.inscricao_estadual, f.endereco, f.numero_endereco, f.complemento, f.bairro, f.telefone, f.site, f.email, c.cep, c.nome, s.nome, e.id_empresa, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual FROM fornecedor f INNER JOIN cidade c ON c.id_cidade = f.id_cidades INNER JOIN estado s ON s.id_estado = c.id_estado INNER JOIN empresa e ON e.id_empresa = f.id_empresa WHERE f.razao_social LIKE '%"+pesquisa+"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaCnpj(self, pesquisa):
        try:
            _sql = " SELECT f.id_fornecedor, f.fantasia, f.razao_social, f.cnpj, f.inscricao_estadual, f.endereco, f.numero_endereco, f.complemento, f.bairro, f.telefone, f.site, f.email, c.cep, c.nome, s.nome, e.id_empresa, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual FROM fornecedor f INNER JOIN cidade c ON c.id_cidade = f.id_cidades INNER JOIN estado s ON s.id_estado = c.id_estado INNER JOIN empresa e ON e.id_empresa = f.id_empresa WHERE f.cnpj = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaInscEstadual(self, pesquisa):
        try:
            _sql = " SELECT f.id_fornecedor, f.fantasia, f.razao_social, f.cnpj, f.inscricao_estadual, f.endereco, f.numero_endereco, f.complemento, f.bairro, f.telefone, f.site, f.email, c.cep, c.nome, s.nome, e.id_empresa, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual FROM fornecedor f INNER JOIN cidade c ON c.id_cidade = f.id_cidades INNER JOIN estado s ON s.id_estado = c.id_estado INNER JOIN empresa e ON e.id_empresa = f.id_empresa WHERE f.inscricao_estadual = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False