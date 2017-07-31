import bcrypt
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from conexao.conexao import ConexaoDb, mysql
from mysql.connector import Error

class Usuario(object):

    def __init__(self):
        self.__conexao = ConexaoDb()

    def salto(self):
        return bcrypt.gensalt(8)

    def criptografar(self, senha, salto):
        return bcrypt.hashpw(senha.encode('utf8'), salto)

    def armazenarSenha(self, funcionario, login, senha, salto,):
        try:
            __sql = "INSERT INTO usuarios (id_funcionario, id_tipo_usuario login, senha, salto) VALUES ('"+funcionario+"', '"+login+"', '"+senha+"', '"+salto+"')"
            self.__conexao.cursor.execute(__sql)
            self.__conexao.conn.commit()

        except mysql.connector.Error as e:
            w = QWidget()
            result = QMessageBox.critical(w, 'Erro', "Erro ao inserir as informações no banco de dados", e)
            self.__conexao.conn.rollback()

        finally:
            try:
                self.__conexao.conn.close()
            except mysql.connector.Error as e:
                w = QWidget()
                QMessageBox.critical(w, 'Erro', "Erro ao fechar Base de Dados", e)

    def salto(self, login):
        __sql = "select salto from usuarios where login= '"+login+"'"
        try:
            self.__conexao.cursor.execute(__sql)
            __salto = self.__conexao.cursor.fetchone()
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.critical(w, 'Erro', "Erro ao fazer a pesquisa banco de dados", e)
            self.__conexao.conn.rollback()

        finally:
            try:
                self.__conexao.conn.close()
            except mysql.connector.Error as e:
                w = QWidget()
                QMessageBox.critical(w, 'Erro', "Erro ao fechar Base de Dados", e)
        return __salto
