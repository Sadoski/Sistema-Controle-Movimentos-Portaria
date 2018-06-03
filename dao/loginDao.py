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

    def pesqPermissoesUsuario(self, codigo):
        try:
            _sql = "SELECT p.id_formularios, p.ativar, p.cadastra, p.cancelar, p.deleta, p.altera from permissoes_usuarios pu INNER JOIN permissoes p ON p.id_permissoes = pu.id_permissoes INNER JOIN usuarios u ON u.id_usuarios = pu.id_usuarios WHERE pu.id_usuarios = '" + codigo + "' ORDER BY p.id_formularios"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False
