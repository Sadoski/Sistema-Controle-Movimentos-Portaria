import sys
import mysql.connector
from mysql.connector import errorcode
from classes.classMensagemBox import MensagemBox

class ConexaoDb(object):

    def __init__(self):
        try:

            self.conn = mysql.connector.connect(user='root', password='',
                                                host='127.1.1.1',
                                                database='sistemasportaria')
        except mysql.connector.Error as e:

            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                MensagemBox().critico('Erro', 'Usuário/Senha do banco MySql errado(s)')
            elif e.errno == errorcode.ER_BAD_DB_ERROR:
                MensagemBox().critico('Erro', 'Banco de Dados inexistente!')
            else:
                MensagemBox().critico('Erro', 'Erro fatal no banco de dados')

            sys.exit(0)