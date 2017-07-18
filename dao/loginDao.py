import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mysql.connector import Error
from conexao.conexao import ConexaoDb, mysql
from classes.classPrincipal import Principal
from telas.frmMainHouse import Ui_frmMainHouse
app = QtGui.QApplication(sys.argv)


class LogarDao(object):

    def __init__(self):
        self.__conexao = ConexaoDb()

    def login(self, pUsuario, pSenha):
        __sql = "select * from usuarios where usuario= '"+pUsuario+"' and senha = '"+pSenha+"'"
        self.__conexao.cursor.execute(__sql)

        result = self.__conexao.cursor.fetchall()
        try:
            if result:
                for i in result:
                    principal = Principal()
                    principal.show()
                    sys.exit(self.app.exec_())

            else:
                w = QWidget()
                result = QMessageBox.warning(w, 'Atenção', "Usuario ou Senha incorreto!")


        except mysql.connector.Error as e:
            w = QWidget()
            result = QMessageBox.critical(w, 'Erro', "Erro fatal no banco de dados")

        #self.__conexao.cursor.close()




