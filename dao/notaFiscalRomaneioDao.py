import sys
import time
import datetime
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mysql.connector import Error
from conexao.conexao import ConexaoDb, mysql

class NotaFiscalRomanieo(object):
    def __init__(self):
        self.__conexao = ConexaoDb()
        self.__cursor = self.__conexao.conn.cursor()
        self.__ts = time.time()
        self.__dataHora = datetime.datetime.fromtimestamp(self.__ts).strftime('%Y-%m-%d %H:%M:%S')

    def pesquisarTipoCarga(self):
        try:
            _sql = "SELECT descricao FROM tipo_carga"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
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

    def pesquisarFornecedor(self, fornecedor):
        try:
            _sql = "SELECT f.id_fornecedor, f.razao_social, f.cnpj, f.inscricao_estadual FROM fornecedor f INNER JOIN cidade c ON c.id_cidade = f.id_cidades INNER JOIN estado s ON s.id_estado = c.id_estado INNER JOIN empresa e ON e.id_empresa = f.id_empresa WHERE f.fantasia = '"+fornecedor+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
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
            _sql = "SELECT m.id_motorista, m.rg, m.cpf, v.marca, v.modelo, v.placa FROM veiculo_motorista v INNER JOIN tipo_veiculo t ON t.id_tipo_veiculo = v.id_tipo_veiculo INNER JOIN motorista m On m.id_motorista = v.id_motorista INNER JOIN categoria_cnh n ON n.id_categoria_cnh = m.id_categoria_cnh INNER JOIN cidade c ON c.id_cidade = m.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado WHERE m.nome = '"+motorista+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False