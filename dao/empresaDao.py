# coding=utf-8
import sys
import time
import datetime
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mysql.connector import Error
from conexao.conexao import ConexaoDb, mysql
from controller.getSetCidade import Cidades
from controller.getSetEmpresa import Empresas


class EmpresaDao(object):
    def __init__(self):
        self.__conexao = ConexaoDb()
        self.__cursor = self.__conexao.conn.cursor()
        self.__ts = time.time()
        self.__dataHora = datetime.datetime.fromtimestamp(self.__ts).strftime('%Y-%m-%d %H:%M:%S')

    def tipoEmpresa(self):
        try:
            __sql = "select descricao from tipo_empresa"
            self.__cursor.execute(__sql)
            result = self.__cursor.fetchall()
            self.__cursor.close()
            return result
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao pesquisar o tipo de empresa no banco de dados ")
            return False

    def idTipoEmpresa(self, descricao):
        try:
            _sql = "select id_tipo_empresa from tipo_empresa where descricao = '"+descricao+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            return result
            self.__cursor.close()
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao pesquisar o tipo de empresa no banco de dados ")
            return False

    def cadastroEmpresa(self, _tipoEmpresa, _cnpj, _inscricaoEstadual, _fantasia, _razaoSocial, _endereco, _numero, _complemento, _bairro, _cidade, _telefone):
        self.__tipo = _tipoEmpresa
        self.__cnpj = _cnpj
        self.__inscricaoEstadual = _inscricaoEstadual
        self.__fantasia = _fantasia
        self.__razaoSocial = _razaoSocial
        self.__endereco = _endereco
        self.__numero = _numero
        self.__complemento = _complemento
        self.__cidade = _cidade
        self.__bairro = _bairro
        self.__telefone = _telefone
        try:
            _sql = "INSERT INTO empresa (fantasia, razao_social, cnpj, inscricao_estadual, endereco, numero_endereco, complemento, bairro, telefone, site, situacao, cadastrado, atualizado, id_cidades, id_tipo_empresa) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"%(self.__fantasia, self.__razaoSocial, self.__cnpj, self.__inscricaoEstadual, self.__endereco, self.__numero, self.__complemento, self.__bairro, self.__telefone, None, None, None, None, self.__cidade, self.__tipo)
            #_valores = (empresas.fantasia, empresas.razaoSocial, empresas.cnpj, empresas.inscricaoEstadual, empresas.endereco, empresas.numero, empresas.complemento, empresas.bairro, empresas.telefone, self.__dataHora, empresas.cidade, empresas.tipoEmpresa)
            self.__cursor.execute(_sql)
            self.__conexao.conn.commit()
            self.__cursor.close()
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()


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
            __sql = "INSERT INTO empresa (id_cidade, id_tipo_empresa, fantasia, razao_social, cnpj, inscricao_estadual, incricao_municipal, endereco, numero, bairro, telefone site, situacao, atualizado) Values ('"+self.__cidade+"',(select id_tipo_empresa from tipo_empresa where descricao = '"+self.__tipo+"'), '"+self.__fantasia+"', '"+self.__razaoSocial+"', '"+self.__cnpj+"', '"+self.__inscricaoEstadual+"', '"+self.__inscricaoMunicial+"', '"+self.__endereco+"', '"+self.__numero+"', '"+self.__complemento+"', '"+self.__bairro+"', '"+self.__telefone+"', '"+self.__site+"', 'Operando', '"+self.__dataHora+"')"

            self.__cursor.execute(__sql)
            self.__conexao.conn.commit()
            self.__cursor.close()
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados", e)
            self.__conexao.conn.rollback()


    def pesquisarCidades(self, cep):
        _sql = "SELECT c.id_cidade, c.nome, e.nome from cidade c inner join estado e e.id_estado = c.id_estado where c.cep = '"+cep+"'"
        try:
            lista = []
            cursor = self.__cursor.execute(_sql)
            for (id, nome, estado) in cursor:
                novo = Cidades(id, nome, estado)
                lista.append(novo)
            self.__conexao.conn.close()
        except BaseException as os:
            return False

        return lista

