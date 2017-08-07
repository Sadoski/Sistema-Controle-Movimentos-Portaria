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
            #self.__cursor.close()
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

    def cadastroEmpresa(self, tipoEmpresa, cnpj, inscricaoEstadual, inscricaoMunicipal, fantasia, razaoSocial, endereco, numero, complemento, bairro, cidade, telefone):
        self.__tipo = tipoEmpresa
        self.__cnpj = cnpj
        self.__inscricaoEstadual = inscricaoEstadual
        self.__inscricaoMunicipal = inscricaoMunicipal
        self.__fantasia = fantasia
        self.__razaoSocial = razaoSocial
        self.__endereco = endereco
        self.__numero = numero
        self.__complemento = complemento
        self.__cidade = cidade
        self.__bairro = bairro
        self.__telefone = telefone
        try:
            _sql = "INSERT INTO empresa (fantasia, razao_social, cnpj, inscricao_estadual, inscricao_municipal, endereco, numero_endereco, complemento, bairro, telefone, cadastrado, id_cidades, id_tipo_empresa, situacao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            _valores = (self.__fantasia, self.__razaoSocial, self.__cnpj, self.__inscricaoEstadual, self.__inscricaoMunicipal, self.__endereco, self.__numero, self.__complemento, self.__bairro, self.__telefone, self.__dataHora, self.__cidade, self.__tipo, "Operando")
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            self.__cursor.close()
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
            print(e)
            self.__conexao.conn.rollback()
            return False


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
            __sql = "UPDATE empresa SET fantasia = %s, razao_social = %s, cnpj = %s, inscricao_estadual = %s, inscricao_municipal = %s, endereco = %s, numero_endereco = %s, complemento = %s, bairro = %s, telefone = %s, atualizado = %s, id_cidades = %s, id_tipo_empresa = %s"
            _valores = (self.__fantasia, self.__razaoSocial, self.__cnpj, self.__inscricaoEstadual, self.__endereco, self.__numero, self.__complemento, self.__bairro, self.__telefone, self.__dataHora, self.__cidade, self.__tipo)

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

    def pesquisa(self, pesquisa):
        _sql = "SELECT e.id_empresa, t.descricao, e.cnpj, e.inscricao_estadual, e.inscricao_municipal, e.fantasia, e.razao_social,  e.endereco, e.numero_endereco, e.complemento, e.bairro, c.cep, c.nome, d.nome, e.site, e.telefone from empresa e INNER JOIN cidade c on c.id_cidade = e.id_cidades INNER JOIN estado d on d.id_estado = c.id_estado INNER JOIN tipo_empresa t on t.id_tipo_empresa = e.id_tipo_empresa where  e.id_empresa = '"+pesquisa+"' or e.fantasia = '"+pesquisa+"' or e.razao_social = '"+pesquisa+"' or e.cnpj = '"+pesquisa+"' or e.inscricao_estadual = '"+pesquisa+"' or e.endereco = '"+pesquisa+"' or e.numero_endereco = '"+pesquisa+"' or e.complemento = '"+pesquisa+"' or e.bairro = '"+pesquisa+"' or e.telefone = '"+pesquisa+"' or c.cep = '"+pesquisa+"' or c.nome = '"+pesquisa+"' or c.id_estado = '"+pesquisa+"' or d.nome = '"+pesquisa+"' or t.descricao = '"+pesquisa+"'"
        self.__cursor.execute(_sql)
        result = self.__cursor.fetchall()
        #self.__cursor.close()
        return result

    def pesquisaCodigo(self, pesquisa):
        _sql = "SELECT e.id_empresa, t.descricao, e.cnpj, e.inscricao_estadual, e.inscricao_municipal, e.fantasia, e.razao_social,  e.endereco, e.numero_endereco, e.complemento, e.bairro, e.telefone, e.telefone, c.cep, c.nome, d.nome from empresa e INNER JOIN cidade c on c.id_cidade = e.id_cidades INNER JOIN estado d on d.id_estado = c.id_estado INNER JOIN tipo_empresa t on t.id_tipo_empresa = e.id_tipo_empresa where  e.id_empresa = '"+pesquisa+"'"
        self.__cursor.execute(_sql)
        result = self.__cursor.fetchall()
        #self.__cursor.close()
        return result

    def pesquisaFantasia(self, pesquisa):
        _sql = "SELECT e.id_empresa, t.descricao, e.cnpj, e.inscricao_estadual, e.inscricao_municipal, e.fantasia, e.razao_social,  e.endereco, e.numero_endereco, e.complemento, e.bairro, e.telefone, e.site, c.cep, c.nome, d.nome from empresa e INNER JOIN cidade c on c.id_cidade = e.id_cidades INNER JOIN estado d on d.id_estado = c.id_estado INNER JOIN tipo_empresa t on t.id_tipo_empresa = e.id_tipo_empresa where  e.fantasia LIKE '%"+pesquisa+"%'"
        self.__cursor.execute(_sql)
        result = self.__cursor.fetchall()
        #self.__cursor.close()
        return result

    def pesquisaRazaoSocial(self, pesquisa):
        _sql = "SELECT e.id_empresa, t.descricao, e.cnpj, e.inscricao_estadual, e.inscricao_municipal, e.fantasia, e.razao_social,  e.endereco, e.numero_endereco, e.complemento, e.bairro, e.telefone, e.site, c.cep, c.nome, d.nome from empresa e INNER JOIN cidade c on c.id_cidade = e.id_cidades INNER JOIN estado d on d.id_estado = c.id_estado INNER JOIN tipo_empresa t on t.id_tipo_empresa = e.id_tipo_empresa where  e.razao_social LIKE '%"+pesquisa+"%'"
        self.__cursor.execute(_sql)
        result = self.__cursor.fetchall()
        #self.__cursor.close()
        return result

    def pesquisaCnpj(self, pesquisa):
        _sql = "SELECT e.id_empresa, t.descricao, e.cnpj, e.inscricao_estadual, e.inscricao_municipal, e.fantasia, e.razao_social,  e.endereco, e.numero_endereco, e.complemento, e.bairro, e.telefone, e.site, c.cep, c.nome, d.nome from empresa e INNER JOIN cidade c on c.id_cidade = e.id_cidades INNER JOIN estado d on d.id_estado = c.id_estado INNER JOIN tipo_empresa t on t.id_tipo_empresa = e.id_tipo_empresa where  e.cnpj = '"+pesquisa+"'"
        self.__cursor.execute(_sql)
        result = self.__cursor.fetchall()
        #self.__cursor.close()
        return result

    def pesquisaInscEstadual(self, pesquisa):
        _sql = "SELECT e.id_empresa, t.descricao, e.cnpj, e.inscricao_estadual, e.inscricao_municipal, e.fantasia, e.razao_social,  e.endereco, e.numero_endereco, e.complemento, e.bairro, e.telefone, e.site, c.cep, c.nome, d.nome from empresa e INNER JOIN cidade c on c.id_cidade = e.id_cidades INNER JOIN estado d on d.id_estado = c.id_estado INNER JOIN tipo_empresa t on t.id_tipo_empresa = e.id_tipo_empresa where  e.inscricao_estadual = '"+pesquisa+"'"
        self.__cursor.execute(_sql)
        result = self.__cursor.fetchall()
        #self.__cursor.close()
        return result