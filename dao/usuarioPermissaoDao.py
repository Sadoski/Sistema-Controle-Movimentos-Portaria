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


class UsuarioPermissaoDao(object):
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

    def pesquisarFuncionario(self, codigo):
        try:
            _sql = "SELECT f.id_funcionario, p.nome_razao, p.sobrenome_fantasia, p.cpf_cnpj, p.rg_inscricao, s.expeditor, s.uf, s.aniversario, g.sexo, p.endereco, p.numero, p.complemento, p.bairro, s.mae, s.pai, c.nome, e.nome, c.cep, f.data_admissao, f.data_demissao, f.num_carteira, f.serie, f.uf, f.data_emissao, f.pis_pasep, i.descricao, d.descricao, r.descricao, t.descricao,  o.descricao, f.observacao, b.descricao, f.situacao  FROM funcionario f INNER JOIN civil i ON i.id_civil = f.id_civil INNER JOIN deficiencia d ON d.id_deficiencia = f.id_deficiencia INNER JOIN categoria_trabalho r ON r.id_categoria_trabalho = f.id_categoria_trabalho INNER JOIN setores t ON t.id_setores = f.id_setores INNER JOIN cargo o ON o.id_cargo = f.id_cargo INNER JOIN jornada_trabalho b ON b.id_jornada_trabalho = f.id_jornada_trabalho INNER JOIN pessoa_fisica s ON s.id_pessoa_fisica = f.id_pessoa_fisica INNER JOIN genero g ON g.id_genero = s.id_genero INNER JOIN pessoa p ON p.id_pessoa = s.id_pessoa INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado  WHERE f.id_funcionario = '"+ codigo +"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarPermissoes(self, idFormulario, ativo, cadastro, cancela, deleta, edita):
        try:
            _sql = "SELECT id_permissoes FROM permissoes WHERE id_formularios = '"+idFormulario+"' AND ativar = '"+ativo+"' AND cadastra = '"+cadastro+"' AND cancelar = '"+cancela+"' AND deleta = '"+deleta+"' AND altera = '"+edita+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def cadatrar(self, usuario):
        try:
            __sql = "INSERT INTO usuarios (id_funcionario, login, senha, salto, cadastrado) VALUES (%s, %s, %s, %s, %s)"
            __valores = (usuario.getIdFuncionario, usuario.getLogin, usuario.getSenha, usuario.getSalto, self.__dataHora)
            self.__cursor.execute(__sql, __valores)
            self.__conexao.conn.commit()

        except mysql.connector.Error as e:
            w = QWidget()
            result = QMessageBox.critical(w, 'Erro', "Erro ao inserir as informações no banco de dados", e)
            self.__conexao.conn.rollback()

    def cadatrarPermissao(self, idFormulario, ativo, cadastro, cancela, deleta, edita):
        try:
            __sql = "INSERT INTO permissoes (id_formularios, ativar, cadastra, cancelar, deleta, altera) VALUES (%s, %s, %s, %s, %s, %s)"
            __valores = (idFormulario, ativo, cadastro, cancela, deleta, edita)
            self.__cursor.execute(__sql, __valores)
            self.__conexao.conn.commit()

        except mysql.connector.Error as e:
            w = QWidget()
            result = QMessageBox.critical(w, 'Erro', "Erro ao inserir as informações no banco de dados", e)
            self.__conexao.conn.rollback()

    def cadatrarPermissaoUsuario(self, idPemissao, usuario):
        try:
            __sql = "INSERT INTO permissoes_usuarios (id_permissoes, id_usuarios) VALUES (%s, %s)"
            __valores = (idPemissao, usuario)
            self.__cursor.execute(__sql, __valores)
            self.__conexao.conn.commit()

        except mysql.connector.Error as e:
            w = QWidget()
            result = QMessageBox.critical(w, 'Erro', "Erro ao inserir as informações no banco de dados", e)
            self.__conexao.conn.rollback()