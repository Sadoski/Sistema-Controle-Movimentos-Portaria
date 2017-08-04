import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mysql.connector import Error
from conexao.conexao import ConexaoDb, mysql
from classes.classUsuario import Usuario
from classes.classPrincipal import Principal


class LogarDao(object):


    def __init__(self):
        self.__conexao = ConexaoDb()
        self.__cursor = self.__conexao.conn.cursor()

    def login(self, pUsuario, pSenha):
        #__concatena = pUsuario+pSenha
        #__usuario = Usuario()
        #__salto = __usuario.salto(pUsuario)
        #__strSenha = str(__concatena)
        #__strSalto = str(__salto)
        #__senhaCripto = __usuario.criptografar(__concatena, __salto)


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
                w = QWidget()
                result = QMessageBox.warning(w, 'Atenção', "Usuario ou Senha incorreto!")

        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.critical(w, 'Erro', "Erro fatal no banco de dados", e)