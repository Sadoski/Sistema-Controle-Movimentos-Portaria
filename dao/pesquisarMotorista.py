import sys
import time
import datetime
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mysql.connector import Error
from conexao.conexao import ConexaoDb, mysql


class PesquisarMotoristaDao(object):
    def __init__(self):
        self.__conexao = ConexaoDb()
        self.__cursor = self.__conexao.conn.cursor()
        self.__ts = time.time()
        self.__dataHora = datetime.datetime.fromtimestamp(self.__ts).strftime('%Y-%m-%d %H:%M:%S')

    def pesquisarCodigoMotorista(self, motorista):
        try:
            _sql = "SELECT m.id_motorista, m.nome, m.rg, m.expeditor, m.cpf, m.endereco, m.numero, m.bairro,  c.nome, e.nome, c.cep, v.marca, v.modelo, v.placa FROM veiculo_motorista v INNER JOIN tipo_veiculo t ON t.id_tipo_veiculo = v.id_tipo_veiculo INNER JOIN motorista m On m.id_motorista = v.id_motorista INNER JOIN categoria_cnh n ON n.id_categoria_cnh = m.id_categoria_cnh INNER JOIN cidade c ON c.id_cidade = m.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado WHERE m.cnh = '"+motorista+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            self.__cursor.close()
            return result
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao pesquisar a cidade no banco de dados ")
            return False

    def pesquisarNomeMotorista(self, motorista):
        try:
            _sql = "SELECT m.id_motorista, m.nome, m.rg, m.expeditor, m.cpf, m.endereco, m.numero, m.bairro,  c.nome, e.nome, c.cep, v.marca, v.modelo, v.placa FROM veiculo_motorista v INNER JOIN tipo_veiculo t ON t.id_tipo_veiculo = v.id_tipo_veiculo INNER JOIN motorista m On m.id_motorista = v.id_motorista INNER JOIN categoria_cnh n ON n.id_categoria_cnh = m.id_categoria_cnh INNER JOIN cidade c ON c.id_cidade = m.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado WHERE m.cnh = '"+motorista+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            self.__cursor.close()
            return result
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao pesquisar a cidade no banco de dados ")
            return False

    def pesquisarCpfMotorista(self, motorista):
        try:
            _sql = "SELECT m.id_motorista, m.nome, m.rg, m.expeditor, m.cpf, m.endereco, m.numero, m.bairro,  c.nome, e.nome, c.cep, v.marca, v.modelo, v.placa FROM veiculo_motorista v INNER JOIN tipo_veiculo t ON t.id_tipo_veiculo = v.id_tipo_veiculo INNER JOIN motorista m On m.id_motorista = v.id_motorista INNER JOIN categoria_cnh n ON n.id_categoria_cnh = m.id_categoria_cnh INNER JOIN cidade c ON c.id_cidade = m.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado WHERE m.cnh = '"+motorista+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            self.__cursor.close()
            return result
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao pesquisar a cidade no banco de dados ")
            return False

    def pesquisarRgMotorista(self, motorista):
        try:
            _sql = "SELECT m.id_motorista, m.nome, m.rg, m.expeditor, m.cpf, m.endereco, m.numero, m.bairro,  c.nome, e.nome, c.cep, v.marca, v.modelo, v.placa FROM veiculo_motorista v INNER JOIN tipo_veiculo t ON t.id_tipo_veiculo = v.id_tipo_veiculo INNER JOIN motorista m On m.id_motorista = v.id_motorista INNER JOIN categoria_cnh n ON n.id_categoria_cnh = m.id_categoria_cnh INNER JOIN cidade c ON c.id_cidade = m.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado WHERE m.cnh = '"+motorista+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            self.__cursor.close()
            return result
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao pesquisar a cidade no banco de dados ")
            return False

    def pesquisarCnhMotorista(self, motorista):
        try:
            _sql = "SELECT m.id_motorista, m.nome, m.rg, m.expeditor, m.cpf, m.endereco, m.numero, m.bairro,  c.nome, e.nome, c.cep, v.marca, v.modelo, v.placa FROM veiculo_motorista v INNER JOIN tipo_veiculo t ON t.id_tipo_veiculo = v.id_tipo_veiculo INNER JOIN motorista m On m.id_motorista = v.id_motorista INNER JOIN categoria_cnh n ON n.id_categoria_cnh = m.id_categoria_cnh INNER JOIN cidade c ON c.id_cidade = m.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado WHERE m.cnh = '"+motorista+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            self.__cursor.close()
            return result
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao pesquisar a cidade no banco de dados ")
            return False