import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mysql.connector import Error
from conexao.conexao import ConexaoDb, mysql
from classes.classUsuario import Usuario


class LogarDao(object):


    def __init__(self):
        self.__conexao = ConexaoDb()
        self.app = QtGui.QApplication(sys.argv)

    def login(self, pUsuario, pSenha):
        #__concatena = pUsuario+pSenha
        #__usuario = Usuario()
        #__salto = __usuario.salto(pUsuario)
        #__strSenha = str(__concatena)
        #__strSalto = str(__salto)
        #__senhaCripto = __usuario.criptografar(__concatena, __salto)


        __sql = "select * from usuarios where login= '"+pUsuario+"' and senha = '"+pSenha+"'"
        self.__conexao.cursor.execute(__sql)

        result = self.__conexao.cursor.fetchall()
        try:
            if result:
                for i in result:
                    return result
                    self.__conexao.conn.close()


            else:
                w = QWidget()
                result = QMessageBox.warning(w, 'Atenção', "Usuario ou Senha incorreto!")

            self.__conexao.conn.close()
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.critical(w, 'Erro', "Erro fatal no banco de dados", e)
            self.__conexao.conn.close()

        finally:
            try:
                self.__conexao.conn.close()
            except mysql.connector.Error as e:
                w = QWidget()
                QMessageBox.critical(w, 'Erro', "Erro ao fechar Base de Dados", e)