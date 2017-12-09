import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mysql.connector import Error

from classes.classMensagemBox import MensagemBox
from conexao.conexao import ConexaoDb, mysql
from classes.classUsuario import Usuario

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class LogarDao(object):


    def __init__(self):
        self.__conexao = ConexaoDb()
        self.__cursor = self.__conexao.conn.cursor()

    def salto(self, usuario):
        try:
            sql = "select salto from usuarios where login = '" + usuario + "'"
            self.__cursor.execute(sql)
            result = self.__cursor.fetchone()[0]

            return result
        except BaseException as os:
            return False


    def login(self, pUsuario, pSenha):

        __sql = "select * from usuarios where login= '"+pUsuario+"' and senha = '"+pSenha+"'"
        self.__cursor.execute(__sql)

        result = self.__cursor.fetchall()
        self.__conexao.conn.commit()
        try:
            if result:
                for i in result:
                    return result
                self.__cursor.close()

            else:
                MensagemBox().warning('Atenção', 'Senha incorreto!')

        except BaseException as os:
            MensagemBox().critico('Erro', 'Erro ao autenticar usuario')
