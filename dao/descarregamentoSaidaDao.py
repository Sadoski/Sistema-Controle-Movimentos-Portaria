import sys
import time
import datetime
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mysql.connector import Error
from conexao.conexao import ConexaoDb, mysql


class DescarreSaidaDao(object):
    def __init__(self):
        self.__conexao = ConexaoDb()
        self.__cursor = self.__conexao.conn.cursor()
        self.__ts = time.time()
        self.__dataHora = datetime.datetime.fromtimestamp(self.__ts).strftime('%Y-%m-%d %H:%M:%S')

    def pesquisarIdMotorista(self, pesquisar):
        try:
            _sql = "SELECT m.id_motorista FROM entrada_veiculo_descarregamento e INNER JOIN motorista m ON m.id_motorista = e.id_motorista INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista INNER JOIN pessoa_fisica f ON f.id_pessoa_fisica =m.id_pessoa_fisica INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa WHERE e.id_entrada_vei_desc = '"+pesquisar+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarEntrada(self):
        try:
            _sql = "SELECT e.id_entrada_vei_desc, e.data, e.hora, p.nome_razao, p.sobrenome_fantasia, v.marca, v.modelo, v.placa FROM entrada_veiculo_descarregamento e INNER JOIN motorista m ON m.id_motorista = e.id_motorista INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista INNER JOIN pessoa_fisica f ON f.id_pessoa_fisica =m.id_pessoa_fisica INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa WHERE e.status = 'Aberto'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def cadastrar(self, campos):
        try:
            _sql = "INSERT INTO saida_veiculos_descarregamento (data, hora, id_entrada_vei_desc) VALUES (%s, %s, %s)"
            _valores = (campos.getData, campos.getHora, campos.getIdEntrada)

            self.__cursor.execute(_sql, _valores)
            self.__cursor.execute("UPDATE entrada_veiculo_descarregamento set status = 'Fechado' WHERE id_entrada_vei_desc = '"+campos.getIdEntrada+"'")
            self.__conexao.conn.commit()
            #self.__cursor.close()
            QMessageBox.information(QWidget(), 'Mensagem', "Saida realizado com sucesso!")
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados")
            self.__conexao.conn.rollback()
            return False