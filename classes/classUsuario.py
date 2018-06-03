import sys
import bcrypt
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from conexao.conexao import ConexaoDb, mysql
from mysql.connector import Error

class Usuario(object):

    def __init__(self):
        self.__conexao = ConexaoDb()
        self.__cursor = self.__conexao.conn.cursor()

    def getSalto(self):
        return bcrypt.gensalt()

    def criptografar(self, senha, salto):
        return bcrypt.hashpw(senha.encode('utf8'), salto.encode('utf8')).decode('utf-8')
