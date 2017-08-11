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

    def cadastroEmpresa(self, empresa):

        try:
            _sql = "INSERT INTO empresa (fantasia, razao_social, cnpj, inscricao_estadual, inscricao_municipal, endereco, numero_endereco, complemento, bairro, telefone, cadastrado, id_cidades, id_tipo_empresa, site, situacao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            _valores = (empresa.getFantasia, empresa.getRazaoSocial, empresa.getCnpj, empresa.getInscricaoEstadual, empresa.getInscricaoMunicipal, empresa.getEndereco, empresa.getNumero, empresa.getComplemento, empresa.getBairro, empresa.getTelefone, self.__dataHora, empresa.getCidade, empresa.getTipoEmpresa, empresa.getSite, empresa.getSituacao)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            #self.__cursor.close()
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False

    def atualizarEmpresa(self, empresa):

        try:
            __sql = "UPDATE empresa SET fantasia = %s, razao_social = %s, cnpj = %s, inscricao_estadual = %s, inscricao_municipal = %s, endereco = %s, numero_endereco = %s, complemento = %s, bairro = %s, telefone = %s, atualizado = %s, id_cidades = %s, id_tipo_empresa = %s, site = %s, situacao = %s where id_empresa = %s"
            _valores = (empresa.getFantasia, empresa.getRazaoSocial, empresa.getCnpj, empresa.getInscricaoEstadual, empresa.getInscricaoMunicipal, empresa.getEndereco, empresa.getNumero, empresa.getComplemento, empresa.getBairro, empresa.getTelefone, self.__dataHora, empresa.getCidade, empresa.getTipoEmpresa, empresa.getSite, empresa.getSituacao, empresa.getIdEmpresa)

            self.__cursor.execute(__sql, _valores)
            self.__conexao.conn.commit()
            #self.__cursor.close()
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao atualizar as informações no banco de dados")
            self.__conexao.conn.rollback()
            return False

    def deletarEmpresa(self, empresa):
        try:
            __sql = "DELETE FROM empresa WHERE id_empresa = '"+empresa+"'"
            self.__cursor.execute(__sql)
            self.__conexao.conn.commit()
            #self.__cursor.close()
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao deletar as informações no banco de dados")
            self.__conexao.conn.rollback()
            return False


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


    def pesquisaCodigo(self, pesquisa):
        try:
            _sql = "SELECT e.id_empresa, t.descricao, e.cnpj, e.inscricao_estadual, e.inscricao_municipal, e.fantasia, e.razao_social,  e.endereco, e.numero_endereco, e.complemento, e.bairro, e.telefone, e.site, c.cep, c.nome, d.nome, e.situacao from empresa e INNER JOIN cidade c on c.id_cidade = e.id_cidades INNER JOIN estado d on d.id_estado = c.id_estado INNER JOIN tipo_empresa t on t.id_tipo_empresa = e.id_tipo_empresa where  e.id_empresa = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaFantasia(self, pesquisa):
        try:
            _sql = "SELECT e.id_empresa, t.descricao, e.cnpj, e.inscricao_estadual, e.inscricao_municipal, e.fantasia, e.razao_social,  e.endereco, e.numero_endereco, e.complemento, e.bairro, e.telefone, e.site, c.cep, c.nome, d.nome, e.situacao from empresa e INNER JOIN cidade c on c.id_cidade = e.id_cidades INNER JOIN estado d on d.id_estado = c.id_estado INNER JOIN tipo_empresa t on t.id_tipo_empresa = e.id_tipo_empresa where  e.fantasia LIKE '%"+pesquisa+"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaRazaoSocial(self, pesquisa):
        try:
            _sql = "SELECT e.id_empresa, t.descricao, e.cnpj, e.inscricao_estadual, e.inscricao_municipal, e.fantasia, e.razao_social,  e.endereco, e.numero_endereco, e.complemento, e.bairro, e.telefone, e.site, c.cep, c.nome, d.nome, e.situacao from empresa e INNER JOIN cidade c on c.id_cidade = e.id_cidades INNER JOIN estado d on d.id_estado = c.id_estado INNER JOIN tipo_empresa t on t.id_tipo_empresa = e.id_tipo_empresa where  e.razao_social LIKE '%"+pesquisa+"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaCnpj(self, pesquisa):
        try:
            _sql = "SELECT e.id_empresa, t.descricao, e.cnpj, e.inscricao_estadual, e.inscricao_municipal, e.fantasia, e.razao_social,  e.endereco, e.numero_endereco, e.complemento, e.bairro, e.telefone, e.site, c.cep, c.nome, d.nome, e.situacao from empresa e INNER JOIN cidade c on c.id_cidade = e.id_cidades INNER JOIN estado d on d.id_estado = c.id_estado INNER JOIN tipo_empresa t on t.id_tipo_empresa = e.id_tipo_empresa where  e.cnpj = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaInscEstadual(self, pesquisa):
        try:
            _sql = "SELECT e.id_empresa, t.descricao, e.cnpj, e.inscricao_estadual, e.inscricao_municipal, e.fantasia, e.razao_social,  e.endereco, e.numero_endereco, e.complemento, e.bairro, e.telefone, e.site, c.cep, c.nome, d.nome, e.situacao from empresa e INNER JOIN cidade c on c.id_cidade = e.id_cidades INNER JOIN estado d on d.id_estado = c.id_estado INNER JOIN tipo_empresa t on t.id_tipo_empresa = e.id_tipo_empresa where  e.inscricao_estadual = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaEmpresa(self, pesquisa):
        try:
            _sql = "SELECT id_empresa, razao_social, cnpj, inscricao_estadual from empresa where  fantasia = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaEmpresaSetCar(self, pesquisa):
        try:
            _sql = "SELECT e.id_empresa, e.razao_social, t.descricao,  e.cnpj, e.inscricao_estadual from empresa e INNER JOIN tipo_empresa t on t.id_tipo_empresa = e.id_tipo_empresa where  fantasia = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def confirmarEmpresa(self, setorCargo):
        try:
            _sql = "SELECT id_empresa FROM empresa WHERE fantasia = %s AND razao_social = %s AND cnpj = %s AND inscricao_estadual = %s AND id_empresa = %s"
            _valores = (setorCargo.getFantasia, setorCargo.getRazaoSocial, setorCargo.getCnpj, setorCargo.getInscricao, setorCargo.getIdEmpresa)
            self.__cursor.execute(_sql, _valores)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False