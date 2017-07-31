# coding=utf-8
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mysql.connector import Error
from conexao.conexao import ConexaoDb, mysql

import time
import datetime

class tipoEmpresaDao(object):
    def __init__(self):
        self.__conexao = ConexaoDb()
        self.__ts = time.time()
        self.__dataHora = datetime.datetime.fromtimestamp(self.__ts).strftime('%Y-%m-%d %H:%M:%S')

    def tipoEmpresa(self):
        __sql = "select descricao from tipo_empresa"
        self.__conexao.cursor.execute(__sql)

        result = self.__conexao.cursor.fetchall()
        self.__conexao.conn.close()

        return result

    def cadastroEmpresa(self, tipo, cnpj, inscricaoEstadual, inscricaoMunicipal, fantasia, razaoSosial, endereco, numero, complemento, bairro, cidade, telefone):
        self.__tipo = tipo
        self.__cnpj = cnpj
        self.__inscricaoEstadual = inscricaoEstadual
        self.__inscricaoMunicipal = inscricaoMunicipal
        self.__fantasia = fantasia
        self.__razaoSocial = razaoSosial
        self.__endereco = endereco
        self.__numero = numero
        self.__complemento = complemento
        self.__cidade = cidade
        self.__bairro = bairro
        self.__telefone = telefone
        #self.__site = site

        try:
            __sql = "INSERT INTO empresa (id_cidade,id_tipo_empresa, fantasia, razao_social, cnpj, inscricao_estadual, incricao_municipal, endereco, numero, bairro, telefone, situacao, cadastrado) Values (%i, (select id_tipo_empresa from tipo_empresa where descricao = %s), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,)"%(self.__cidade, self.__tipo, self.__fantasia, self.__razaoSocial, self.__cnpj, self.__inscricaoEstadual, self.__inscricaoMunicipal, self.__endereco, self.__numero ,self.__complemento, self.__bairro, self.__telefone,'Operando', self.__dataHora)

            self.__conexao.cursor.execute(__sql)
            self.__conexao.conn.commit()

        except mysql.connector.Error as e:
            w = QWidget()
            result = QMessageBox.critical(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()

        finally:
            try:
                self.__conexao.conn.close()
            except mysql.connector.Error as e:
                w = QWidget()
                result = QMessageBox.critical(w, 'Erro', "Erro ao fechar Base de Dados", e)

    def atualizarEmpresa(self, tipo, cnpj, inscricaoEstadual, inscricaoMunicipal, fantasia, razaoSosial, endereco, numero, complemento, bairro, cidade, telefone, site):
        self.__tipo = tipo
        self.__cnpj = cnpj
        self.__inscricaoEstadual = inscricaoEstadual
        self.__inscricaoMunicipal = inscricaoMunicipal
        self.__fantasia = fantasia
        self.__razaoSocial = razaoSosial
        self.__endereco = endereco
        self.__numero = numero
        self.__complemento = complemento
        self.__cidade = cidade
        self.__bairro = bairro
        self.__telefone = telefone
        self.__site = site

        try:
            __sql = "INSERT INTO empresa (id_cidade,id_tipo_empresa, fantasia, razao_social, cnpj, inscricao_estadual, incricao_municipal, endereco, numero, bairro, telefone site, situacao, atualizado) Values ('"+self.__cidade+"',(select id_tipo_empresa from tipo_empresa where descricao = '"+self.__tipo+"'), '"+self.__fantasia+"', '"+self.__razaoSocial+"', '"+self.__cnpj+"', '"+self.__inscricaoEstadual+"', '"+self.__inscricaoMunicial+"', '"+self.__endereco+"', '"+self.__numero+"', '"+self.__complemento+"', '"+self.__bairro+"', '"+self.__telefone+"', '"+self.__site+"', 'Operando', '"+self.__dataHora+"')"

            self.__conexao.cursor.execute(__sql)
            self.__conexao.conn.commit()

        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.critical(w, 'Erro', "Erro ao inserir as informações no banco de dados", e)
            self.__conexao.conn.rollback()

        finally:
            try:
                self.__conexao.conn.close()
            except mysql.connector.Error as e:
                w = QWidget()
                QMessageBox.critical(w, 'Erro', "Erro ao fechar Base de Dados", e)

    def pesquisarCidades(self, cep):
        __sql = "SELECT c.id_cidade, c.nome, e.nome from cidade c inner join estado e e.id_estado = c.id_estado where c.cep = '"+cep+"'"
        self.__conexao.cursor.execute(__sql)
        result = self.__conexao.cursor.fetchall()
        self.__conexao.conn.close()

        return result

