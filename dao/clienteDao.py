import sys
import time
import datetime
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mysql.connector import Error
from conexao.conexao import ConexaoDb, mysql

class ClienteDao(object):
    def __init__(self):
        self.__conexao = ConexaoDb()
        self.__cursor = self.__conexao.conn.cursor()
        self.__ts = time.time()
        self.__dataHora = datetime.datetime.fromtimestamp(self.__ts).strftime('%Y-%m-%d %H:%M:%S')

    def ultimoRegistro(self):
        try:
            _sql = "SELECT LAST_INSERT_ID()"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()

            return result

        except BaseException as os:
            return False

    def cadastrarCliente(self, cliente):
        try:
            _sql = "INSERT INTO cliente (fantasia, razao_social, cnpj, inscricao_estadual, endereco, numero_endereco, complemento, bairro, telefone, site, email, cadastrado, id_cidades, id_empresa) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            _valores = (cliente.getFantasia, cliente.getRazaoSocial, cliente.getCnpj, cliente.getInscricaoEstadual, cliente.getEndereco, cliente.getNumero, cliente.getComplemento, cliente.getBairro, cliente.getTelefone, cliente.getSite, cliente.getEmail, self.__dataHora, cliente.getCidade, cliente.getEmpresa)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            # self.__cursor.close()
            QMessageBox.warning(QWidget(), 'Mensagem', "Cadastro realizado com sucesso!")

        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False

    def atualizarCliente(self, cliente):

        try:
            __sql = "UPDATE cliente SET fantasia = %s, razao_social = %s, cnpj = %s, inscricao_estadual = %s, endereco = %s, numero_endereco = %s, complemento = %s, bairro = %s, telefone = %s, site = %s, email = %s, atualizado = %s, id_cidades = %s, id_empresa = %s WHERE id_cliente = %s"
            _valores = (cliente.getFantasia, cliente.getRazaoSocial, cliente.getCnpj, cliente.getInscricaoEstadual, cliente.getEndereco, cliente.getNumero, cliente.getComplemento, cliente.getBairro, cliente.getTelefone, cliente.getSite, cliente.getEmail, self.__dataHora, cliente.getCidade, cliente.getEmpresa, cliente.getIdCliente)
            self.__cursor.execute(__sql, _valores)
            self.__conexao.conn.commit()
            # self.__cursor.close()
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao atualizar as informações no banco de dados")
            self.__conexao.conn.rollback()
            return False

    def deletarCliente(self, cliente):
        try:
            __sql = "DELETE FROM cliente WHERE id_cliente = '" + cliente + "'"
            self.__cursor.execute(__sql)
            self.__conexao.conn.commit()
            # self.__cursor.close()
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao deletar as informações no banco de dados")
            self.__conexao.conn.rollback()
            return False

    def pesquisaCodigoJuridica(self, pesquisa):
        try:
            _sql = "SELECT e.id_cliente, j.fantasia, j.razao_social, j.cnpj, j.ins_estadual, j.endereco, j.numero, j.complemento, j.bairro, c.nome, s.nome, c.cep, e.situacao FROM cliente e INNER JOIN pessoa_juridica j ON j.id_pessoa_juridica = e.id_pessoa_juridica INNER JOIN cidade c ON c.id_cidade = j.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE  e.id_cliente = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaFantasiaJuridica(self, pesquisa):
        try:
            _sql = "SELECT e.id_cliente, j.fantasia, j.razao_social, j.cnpj, j.ins_estadual, j.endereco, j.numero, j.complemento, j.bairro, c.nome, s.nome, c.cep, e.situacao FROM cliente e INNER JOIN pessoa_juridica j ON j.id_pessoa_juridica = e.id_pessoa_juridica INNER JOIN cidade c ON c.id_cidade = j.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE  e.fantasia LIKE '%"+pesquisa+"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaRazaoSocialJuridica(self, pesquisa):
        try:
            _sql = "SELECT e.id_cliente, j.fantasia, j.razao_social, j.cnpj, j.ins_estadual, j.endereco, j.numero, j.complemento, j.bairro, c.nome, s.nome, c.cep, e.situacao FROM cliente e INNER JOIN pessoa_juridica j ON j.id_pessoa_juridica = e.id_pessoa_juridica INNER JOIN cidade c ON c.id_cidade = j.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE  e.razao_social LIKE '%"+pesquisa+"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaCnpjJuridica(self, pesquisa):
        try:
            _sql = "SELECT e.id_cliente, j.fantasia, j.razao_social, j.cnpj, j.ins_estadual, j.endereco, j.numero, j.complemento, j.bairro, c.nome, s.nome, c.cep, e.situacao FROM cliente e INNER JOIN pessoa_juridica j ON j.id_pessoa_juridica = e.id_pessoa_juridica INNER JOIN cidade c ON c.id_cidade = j.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE  e.cnpj = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaInscEstadualJuridica(self, pesquisa):
        try:
            _sql = "SELECT e.id_cliente, j.fantasia, j.razao_social, j.cnpj, j.ins_estadual, j.endereco, j.numero, j.complemento, j.bairro, c.nome, s.nome, c.cep, e.situacao FROM cliente e INNER JOIN pessoa_juridica j ON j.id_pessoa_juridica = e.id_pessoa_juridica INNER JOIN cidade c ON c.id_cidade = j.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE  e.inscricao_estadual = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaCodigoFisica(self, pesquisa):
        try:
            _sql = "SELECT e.id_cliente, j.apelido, j.nome, j.cpf, j.rg, j.endereco, j.numero, j.complemento, j.bairro, c.nome, s.nome, c.cep, e.situacao FROM cliente e INNER JOIN pessoa_fisica j ON j.id_pessoa_fisica = e.id_pessoa_fisica INNER JOIN cidade c ON c.id_cidade = j.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE e.id_cliente = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaApelidoFisica(self, pesquisa):
        try:
            _sql = "SELECT e.id_cliente, j.apelido, j.nome, j.cpf, j.rg, j.endereco, j.numero, j.complemento, j.bairro, c.nome, s.nome, c.cep, e.situacao FROM cliente e INNER JOIN pessoa_fisica j ON j.id_pessoa_fisica = e.id_pessoa_fisica INNER JOIN cidade c ON c.id_cidade = j.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE e.apelido LIKE '%"+pesquisa+"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarNomeFisica(self, pesquisa):
        try:
            _sql = "SELECT e.id_cliente, j.apelido, j.nome, j.cpf, j.rg, j.endereco, j.numero, j.complemento, j.bairro, c.nome, s.nome, c.cep, e.situacao FROM cliente e INNER JOIN pessoa_fisica j ON j.id_pessoa_fisica = e.id_pessoa_fisica INNER JOIN cidade c ON c.id_cidade = j.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE e.nome LIKE '%"+pesquisa+"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaCpfFisica(self, pesquisa):
        try:
            _sql = "SELECT e.id_cliente, j.apelido, j.nome, j.cpf, j.rg, j.endereco, j.numero, j.complemento, j.bairro, c.nome, s.nome, c.cep, e.situacao FROM cliente e INNER JOIN pessoa_fisica j ON j.id_pessoa_fisica = e.id_pessoa_fisica INNER JOIN cidade c ON c.id_cidade = j.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE e.cpf = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaRgFisica(self, pesquisa):
        try:
            _sql = "SELECT e.id_cliente, j.apelido, j.nome, j.cpf, j.rg, j.endereco, j.numero, j.complemento, j.bairro, c.nome, s.nome, c.cep, e.situacao FROM cliente e INNER JOIN pessoa_fisica j ON j.id_pessoa_fisica = e.id_pessoa_fisica INNER JOIN cidade c ON c.id_cidade = j.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE e.rg = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarClienteIdFisico(self, cliente):
        try:
            _sql = "SELECT * FROM cliente e INNER JOIN pessoa_fisica p ON p.id_pessoa_fisica = e.id_pessoa_fisica WHERE p.id_pessoa_fisica = '"+ cliente +"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarClienteIdJuridico(self, cliente):
        try:
            _sql = "SELECT * FROM cliente e INNER JOIN pessoa_juridica p ON p.id_pessoa_juridica = e.id_pessoa_juridica WHERE p.id_pessoa_juridica = '"+ cliente +"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarPessoaFisica(self, pessoaFisica):
        try:
            _sql = "SELECT cpf, rg, nome, apelido FROM pessoa_fisica WHERE id_pessoa_fisica = '"+pessoaFisica+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarPessoaJuridica(self, pessoaJuridica):
        try:
            _sql = "SELECT cnpj, ins_estadual, razao_social, fantasia FROM pessoa_juridica WHERE id_pessoa_juridica = '"+pessoaJuridica+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False


    def cadastrarTelefone(self, empresa):

        try:
            _sql = "INSERT INTO telefone (contato, telefone) VALUES (%s, %s)"
            _valores = (empresa.getContato, empresa.getTelefone)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            #self.__cursor.close()

        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False

    def cadastrarTelefoneCliente(self, idTelefone, idEmpresa):

        try:
            _sql = "INSERT INTO telefone_cliente (id_telefone, id_empresa) VALUES (%s, %s)"
            _valores = (idTelefone, idEmpresa)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            #self.__cursor.close()

        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False

    def cadastrarEmail(self, empresa):

        try:
            _sql = "INSERT INTO email (contato, email) VALUES (%s, %s)"
            _valores = (empresa.getContato, empresa.getEmail)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            #self.__cursor.close()

        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados email ")
            self.__conexao.conn.rollback()
            return False

    def cadastrarEmailCliente(self, idEmail, idEmpresa):

        try:
            _sql = "INSERT INTO email_cliente (id_email, id_empresa) VALUES (%s, %s)"
            _valores = (idEmail, idEmpresa)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            #self.__cursor.close()

        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados  email")
            self.__conexao.conn.rollback()
            return False