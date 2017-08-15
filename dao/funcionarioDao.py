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


class FuncionarioDao(object):
    def __init__(self):
        self.__conexao = ConexaoDb()
        self.__cursor = self.__conexao.conn.cursor()
        self.__ts = time.time()
        self.__dataHora = datetime.datetime.fromtimestamp(self.__ts).strftime('%Y-%m-%d %H:%M:%S')

    def funcao(self, setor, cargo):
        try:
            _sql = "SELECT f.id_funcao FROM funcao f INNER JOIN setores s ON s.id_setores = f.id_setores INNER JOIN cargo c ON c.id_cargo = f.id_cargo WHERE s.descricao = %s AND c.descricao = %s"
            _valores = (setor, cargo)
            self.__cursor.execute(_sql, _valores)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def cadastroFuncionario(self, funcionario):

        try:
            _sql = "INSERT INTO funcionario (nome,rg,expeditor,cpf,data_nascimento,sexo,nome_mae,nome_pai,telefone,celular,endereco,numero_endereco,complemento,bairro,cadastrado,id_funcao,id_empresa,id_cidade) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            _valores = (funcionario.getNome, funcionario.getRg, funcionario.getExpeditor, funcionario.getCpf, funcionario.getNascimento, funcionario.getSexo, funcionario.getMae, funcionario.getPai, funcionario.getTelefone, funcionario.getCelular, funcionario.getEndereco, funcionario.getNumero, funcionario.getComplemento, funcionario.getBairro, self.__dataHora,  funcionario.getFuncao, funcionario.getEmpresa, funcionario.getCidade)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            #self.__cursor.close()
            QMessageBox.warning(QWidget(), 'Mensagem', "Cadastro realizado com sucesso!")

        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False

    def atualizarFuncioario(self, funcionario):

        try:
            __sql = "UPDATE funcionario SET nome = %s, rg = %s, expeditor = %s, cpf = %s, data_nascimento = %s, sexo = %s, nome_mae = %s, nome_pai = %s, endereco = %s, numero_endereco = %s, complemento = %s, bairro = %s, telefone = %s, celular = %s, atualizado = %s, id_funcao = %s, id_empresa = %s,  id_cidade = %s WHERE id_funcionario = %s"
            _valores = (funcionario.getNome, funcionario.getRg, funcionario.getExpeditor, funcionario.getCpf, funcionario.getNascimento, funcionario.getSexo, funcionario.getMae, funcionario.getPai, funcionario.getEndereco, funcionario.getNumero, funcionario.getComplemento, funcionario.getBairro,  funcionario.getTelefone, funcionario.getCelular, self.__dataHora,  funcionario.getFuncao, funcionario.getEmpresa, funcionario.getCidade, funcionario.getIdFuncionario)

            self.__cursor.execute(__sql, _valores)
            self.__conexao.conn.commit()
            QMessageBox.warning(QWidget(), 'Mensagem', "Edição realizado com sucesso!")
            #self.__cursor.close()
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao atualizar as informações no banco de dados")
            self.__conexao.conn.rollback()
            return False

    def deletarFuncionario(self, funcionario):
        try:
            __sql = "DELETE FROM funcionario WHERE id_funcionario = '" + funcionario + "'"
            self.__cursor.execute(__sql)
            self.__conexao.conn.commit()
            # self.__cursor.close()
            QMessageBox.warning(QWidget(), 'Mensagem', "Exclusão realizado com sucesso!")
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao deletar as informações no banco de dados")
            self.__conexao.conn.rollback()
            return False

    def pesquisarCodigoFuncionario(self, funcionario):
        try:
            _sql = "SELECT f.id_funcionario, f.nome, f.rg, f.expeditor, f.cpf, f.data_nascimento, f.sexo, f.nome_mae, f.nome_pai, f.endereco, f.numero_endereco, f.complemento, f.bairro, c.cep, c.nome, e.nome, f.telefone, f.celular, t.descricao, l.descricao, m.fantasia, m.razao_social, m.cnpj, m.inscricao_estadual FROM funcionario f INNER JOIN cidade c ON c.id_cidade = f.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado INNER JOIN funcao d ON d.id_funcao = f.id_funcao INNER JOIN setores t ON t.id_setores = d.id_setores INNER JOIN cargo l ON l.id_cargo = d.id_cargo INNER JOIN empresa m ON m.id_empresa = f.id_empresa WHERE f.id_funcionario = '"+funcionario+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarNomeFuncionario(self, funcionario):
        try:
            _sql = "SELECT f.id_funcionario, f.nome, f.rg, f.expeditor, f.cpf, f.data_nascimento, f.sexo, f.nome_mae, f.nome_pai, f.endereco, f.numero_endereco, f.complemento, f.bairro, c.cep, c.nome, e.nome, f.telefone, f.celular, t.descricao, l.descricao, m.fantasia, m.razao_social, m.cnpj, m.inscricao_estadual FROM funcionario f INNER JOIN cidade c ON c.id_cidade = f.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado INNER JOIN funcao d ON d.id_funcao = f.id_funcao INNER JOIN setores t ON t.id_setores = d.id_setores INNER JOIN cargo l ON l.id_cargo = d.id_cargo INNER JOIN empresa m ON m.id_empresa = f.id_empresa WHERE f.nome LIKE '%"+funcionario+"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarRgFuncionario(self, funcionario):
        try:
            _sql = "SELECT f.id_funcionario, f.nome, f.rg, f.expeditor, f.cpf, f.data_nascimento, f.sexo, f.nome_mae, f.nome_pai, f.endereco, f.numero_endereco, f.complemento, f.bairro, c.cep, c.nome, e.nome, f.telefone, f.celular, t.descricao, l.descricao, m.fantasia, m.razao_social, m.cnpj, m.inscricao_estadual FROM funcionario f INNER JOIN cidade c ON c.id_cidade = f.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado INNER JOIN funcao d ON d.id_funcao = f.id_funcao INNER JOIN setores t ON t.id_setores = d.id_setores INNER JOIN cargo l ON l.id_cargo = d.id_cargo INNER JOIN empresa m ON m.id_empresa = f.id_empresa WHERE f.rg = '"+funcionario+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarCpfFuncionario(self, funcionario):
        try:
            _sql = "SELECT f.id_funcionario, f.nome, f.rg, f.expeditor, f.cpf, f.data_nascimento, f.sexo, f.nome_mae, f.nome_pai, f.endereco, f.numero_endereco, f.complemento, f.bairro, c.cep, c.nome, e.nome, f.telefone, f.celular, t.descricao, l.descricao, m.fantasia, m.razao_social, m.cnpj, m.inscricao_estadual FROM funcionario f INNER JOIN cidade c ON c.id_cidade = f.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado INNER JOIN funcao d ON d.id_funcao = f.id_funcao INNER JOIN setores t ON t.id_setores = d.id_setores INNER JOIN cargo l ON l.id_cargo = d.id_cargo INNER JOIN empresa m ON m.id_empresa = f.id_empresa WHERE f.cpf = '"+funcionario+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarFantasiaEmpFuncionario(self, funcionario):
        try:
            _sql = "SELECT f.id_funcionario, f.nome, f.rg, f.expeditor, f.cpf, f.data_nascimento, f.sexo, f.nome_mae, f.nome_pai, f.endereco, f.numero_endereco, f.complemento, f.bairro, c.cep, c.nome, e.nome, f.telefone, f.celular, t.descricao, l.descricao, m.fantasia, m.razao_social, m.cnpj, m.inscricao_estadual FROM funcionario f INNER JOIN cidade c ON c.id_cidade = f.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado INNER JOIN funcao d ON d.id_funcao = f.id_funcao INNER JOIN setores t ON t.id_setores = d.id_setores INNER JOIN cargo l ON l.id_cargo = d.id_cargo INNER JOIN empresa m ON m.id_empresa = f.id_empresa WHERE m.fantasia LIKE '%"+funcionario+"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarRazaoSocialEmpFuncionario(self, funcionario):
        try:
            _sql = "SELECT f.id_funcionario, f.nome, f.rg, f.expeditor, f.cpf, f.data_nascimento, f.sexo, f.nome_mae, f.nome_pai, f.endereco, f.numero_endereco, f.complemento, f.bairro, c.cep, c.nome, e.nome, f.telefone, f.celular, t.descricao, l.descricao, m.fantasia, m.razao_social, m.cnpj, m.inscricao_estadual FROM funcionario f INNER JOIN cidade c ON c.id_cidade = f.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado INNER JOIN funcao d ON d.id_funcao = f.id_funcao INNER JOIN setores t ON t.id_setores = d.id_setores INNER JOIN cargo l ON l.id_cargo = d.id_cargo INNER JOIN empresa m ON m.id_empresa = f.id_empresa WHERE m.razao_social LIKE '%"+funcionario+"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False