import sys
import time
import datetime
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mysql.connector import Error
from conexao.conexao import ConexaoDb, mysql

class MotoristaDao(object):
    def __init__(self):
        self.__conexao = ConexaoDb()
        self.__cursor = self.__conexao.conn.cursor()
        self.__ts = time.time()
        self.__dataHora = datetime.datetime.fromtimestamp(self.__ts).strftime('%Y-%m-%d %H:%M:%S')

    def pesquisarCategoria(self):
        try:
            _sql = "SELECT descricao FROM categoria_cnh"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarTipoVeiculo(self):
        try:
            _sql = "SELECT descricao FROM tipo_veiculo"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarIdMotorista(self, motorista):
        try:
            _sql = " SELECT id_motorista FROM motorista WHERE nome = %s and rg = %s and cpf = %s and pis = %s and cnh = %s"
            _valores = (motorista.getNome, motorista.getRg, motorista.getCpf, motorista.getPis, motorista.getCnh)
            self.__cursor.execute(_sql, _valores)
            result = self.__cursor.fetchone()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarIdTipoVeiculo(self, tipo):
        try:
            _sql = " SELECT id_tipo_veiculo FROM tipo_veiculo WHERE descricao = '"+tipo+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def cadastrarMotorista(self, motorista):
        try:
            _sql = "INSERT INTO motorista (nome, data_nascimento, rg, expeditor, cpf, pis, cnh, categoria_cnh, endereco, numero_endereco, complemento, bairro, telefone, celular, sexo, cadastrado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            _valores = (motorista.getNome, motorista.getNascimento, motorista.getRg, motorista.getExpeditor, motorista.getCpf, motorista.getPis, motorista.getCnh, motorista.getCategoria, motorista.getEndereco, motorista.getNumero, motorista.getComplemento, motorista.getBairro, motorista.getTelefone, motorista.getCelular, motorista.getSexo, self.__dataHora)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            # self.__cursor.close()
            QMessageBox.warning(QWidget(), 'Mensagem', "Cadastro realizado com sucesso!")

        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False

    def cadastrarVeiculoMotorista(self, veiculo):
        try:
            _sql = "INSERT INTO veiculo_motorista (id_motorista, marca, modelo, placa, cadastrado) VALUES (%s, %s, %s, %s, %s)"
            _valores = (veiculo.getIdMotorista, veiculo.getTipoVeiculo, veiculo.getMarca, veiculo.getModelo, veiculo.getPlaca, self.__dataHora)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            # self.__cursor.close()
            QMessageBox.warning(QWidget(), 'Mensagem', "Cadastro realizado com sucesso!")

        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False