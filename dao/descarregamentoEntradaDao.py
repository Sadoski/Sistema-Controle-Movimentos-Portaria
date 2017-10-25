import sys
import time
import datetime
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mysql.connector import Error
from conexao.conexao import ConexaoDb, mysql


class DescarreEntradaDao(object):
    def __init__(self):
        self.__conexao = ConexaoDb()
        self.__cursor = self.__conexao.conn.cursor()
        self.__ts = time.time()
        self.__dataHora = datetime.datetime.fromtimestamp(self.__ts).strftime('%Y-%m-%d %H:%M:%S')

    def pesquisarNumeroNota(self, numero):
        try:
            _sql = "SELECT n.numero_nota, r.numer_romaneio, r.certificada, q.descricao FROM romaneios r INNER JOIN notas_fiscais n ON n.id_entrada_notas_fiscais = r.id_entrada_notas_fiscais INNER JOIN fornecedor f ON f.id_fornecedor = n.id_fornecedor INNER JOIN empresa e ON e.id_empresa = n.id_empresa INNER JOIN motorista m ON m.id_motorista = n.id_motorista INNER JOIN metragem q ON q.id_metragem = r.id_metragem  where n.numero_nota = '" + numero + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarNumeroRomaneio(self, numero):
        try:
            _sql = "SELECT n.numero_nota, r.numer_romaneio, r.certificada, q.descricao FROM romaneios r INNER JOIN notas_fiscais n ON n.id_entrada_notas_fiscais = r.id_entrada_notas_fiscais INNER JOIN fornecedor f ON f.id_fornecedor = n.id_fornecedor INNER JOIN empresa e ON e.id_empresa = n.id_empresa INNER JOIN motorista m ON m.id_motorista = n.id_motorista INNER JOIN metragem q ON q.id_metragem = r.id_metragem  where n.numero_nota = '" + numero + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

