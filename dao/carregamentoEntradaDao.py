import sys
import time
import datetime
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mysql.connector import Error
from conexao.conexao import ConexaoDb, mysql

class CarregamentoEntradaDao(object):
    def __init__(self):
        self.__conexao = ConexaoDb()
        self.__cursor = self.__conexao.conn.cursor()

    def pesquisarTipoCarga(self):
        try:
            _sql = "SELECT descricao FROM tipo_carga"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarIdCargaProduto(self, carga, produto):
        try:
            _sql = "SELECT a.id_carga_produto FROM carga_produto a INNER JOIN tipo_carga c ON c.id_tipo_carga = a.id_tipo_carga INNER JOIN produto p ON p.id_produto = a.id_produto WHERE c.descricao = %s AND p.descricao = %s"
            _valores = (carga, produto)
            print(_valores)
            self.__cursor.execute(_sql, _valores)
            result = self.__cursor.fetchone()[0]
            print(result)
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarProduto(self, produto):
        try:
            _sql = "SELECT p.descricao FROM carga_produto a INNER JOIN tipo_carga c ON c.id_tipo_carga = a.id_tipo_carga INNER JOIN produto p ON p.id_produto = a.id_produto WHERE c.descricao = '"+produto+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarIdTipoCarga(self, carga):
        try:
            _sql = "SELECT id_tipo_carga FROM tipo_carga WHERE descricao = '"+carga+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarIdProduto(self, produto):
        try:
            _sql = "SELECT id_produto FROM produto WHERE descricao = '"+produto+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarEmpresa(self, empresa):
        try:
            _sql = "SELECT e.id_empresa, e.razao_social, e.cnpj, e.inscricao_estadual FROM empresa e INNER JOIN cidade c on c.id_cidade = e.id_cidades INNER JOIN estado d on d.id_estado = c.id_estado INNER JOIN tipo_empresa t on t.id_tipo_empresa = e.id_tipo_empresa where  e.fantasia = '"+empresa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarMotorista(self, motorista):
        try:
            _sql = "SELECT m.id_motorista, v.marca, v.modelo, v.placa FROM veiculo_motorista v INNER JOIN tipo_veiculo t ON t.id_tipo_veiculo = v.id_tipo_veiculo INNER JOIN motorista m On m.id_motorista = v.id_motorista INNER JOIN categoria_cnh n ON n.id_categoria_cnh = m.id_categoria_cnh INNER JOIN cidade c ON c.id_cidade = m.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado WHERE m.nome = '"+motorista+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarCliente(self, cliente):
        try:
            _sql = "SELECT f.id_cliente, f.razao_social, f.cnpj, f.inscricao_estadual FROM cliente f INNER JOIN cidade c ON c.id_cidade = f.id_cidades INNER JOIN estado s ON s.id_estado = c.id_estado INNER JOIN empresa e ON e.id_empresa = f.id_empresa WHERE f.fantasia = '"+cliente+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def cadastrar(self, entrada):
        try:
            _sql = "INSERT INTO entrada_veiculo_carregamento (data, hora, id_carga_produto, id_motorista, id_cliente, id_empresa) VALUES (%s, %s, %s, %s, %s, %s)"
            _valores = (entrada.getData, entrada.getHora, entrada.getCargaProduto, entrada.getIdMotorista, entrada.getIdCliente, entrada.getIdEmpresa)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            # self.__cursor.close()
            QMessageBox.warning(QWidget(), 'Mensagem', "Cadastro realizado com sucesso!")
            return  True
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False