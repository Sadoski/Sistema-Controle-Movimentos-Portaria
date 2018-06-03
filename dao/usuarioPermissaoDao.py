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

    def pesquisarIdFuncionario(self, idUsuario):
        try:
            _sql = "SELECT u.id_funcionario FROM usuarios u INNER JOIN funcionario n ON n.id_funcionario = u.id_funcionario WHERE u.id_usuarios = '"+idUsuario+"'"
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
            _sql = "SELECT id_permissoes FROM permissoes WHERE id_formularios = '"+str(idFormulario)+"' AND ativar = '"+str(ativo)+"' AND cadastra = '"+str(cadastro)+"' AND cancelar = '"+str(cancela)+"' AND deleta = '"+str(deleta)+"' AND altera = '"+str(edita)+"'"
            print(_sql)
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
            QMessageBox.information(QWidget(), 'Mensagem', "Usuario cadastrado com sucesso")
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
            __valores = (str(idPemissao), str(usuario))
            self.__cursor.execute(__sql, __valores)
            self.__conexao.conn.commit()

        except:
            w = QWidget()
            result = QMessageBox.critical(w, 'Erro', "Erro ao inserir as informações no banco de dados")
            self.__conexao.conn.rollback()

    def editarUsuarioSenha(self, usuario):
        try:
            __sql = "UPDATE usuarios SET  login = %s, senha = %s, salto = %s, alterado = %s WHERE  id_usuarios = %s"
            __valores = (usuario.getLogin, usuario.getSenha, usuario.getSalto, self.__dataHora, usuario.getIdFuncionario)
            self.__cursor.execute(__sql, __valores)
            self.__conexao.conn.commit()
            QMessageBox.information(QWidget(), 'Mensagem', "Usuario alterado com sucesso")
        except :
            w = QWidget()
            result = QMessageBox.critical(w, 'Erro', "Erro ao inserir as informações no banco de dados")
            self.__conexao.conn.rollback()

    def editarUsuario(self, login, idUsuario):
        try:
            __sql = "UPDATE usuarios SET  login = %s WHERE  id_usuarios = %s"
            __valores = (login, idUsuario)
            self.__cursor.execute(__sql, __valores)
            self.__conexao.conn.commit()
            QMessageBox.information(QWidget(), 'Mensagem', "Usuario alterado com sucesso")
        except:
            w = QWidget()
            result = QMessageBox.critical(w, 'Erro', "Erro ao inserir as informações no banco de dados")
            self.__conexao.conn.rollback()

    def deletarUsuario(self, idUsuario):
        try:
            __sql = "DELETE FROM usuarios WHERE id_usuarios = '" + str(idUsuario) + "'"
            self.__cursor.execute(__sql)
            self.__conexao.conn.commit()
            # self.__cursor.close()
            QMessageBox.information(QWidget(), 'Mensagem', "Usuario deletada com sucesso")

        except:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao deletar as informações no banco de dados")
            self.__conexao.conn.rollback()
            return False

    def deletarPermissoesUsuario(self, idUsuario):
        try:
            __sql = "DELETE FROM permissoes_usuarios WHERE id_usuarios = '" + str(idUsuario) + "'"
            self.__cursor.execute(__sql)
            self.__conexao.conn.commit()
            # self.__cursor.close()

            return True
        except:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao deletar as informações no banco de dados")
            self.__conexao.conn.rollback()
            return False

    def pesquisaCodigoUsuario(self, codigo):
        try:
            _sql = "SELECT u.id_usuarios, p.nome_razao, p.sobrenome_fantasia, s.descricao, c.descricao, u.login FROM usuarios u INNER JOIN funcionario n ON n.id_funcionario = u.id_funcionario INNER JOIN setores s ON s.id_setores = n.id_setores INNER JOIN cargo c ON c.id_cargo = n.id_cargo INNER JOIN pessoa_fisica f ON f.id_pessoa_fisica = n.id_pessoa_fisica INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa WHERE u.id_usuarios = '" + codigo + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarNomeFuncionario(self, codigo):
        try:
            _sql = "SELECT u.id_usuarios, p.nome_razao, p.sobrenome_fantasia, s.descricao, c.descricao, u.login FROM usuarios u INNER JOIN funcionario n ON n.id_funcionario = u.id_funcionario INNER JOIN setores s ON s.id_setores = n.id_setores INNER JOIN cargo c ON c.id_cargo = n.id_cargo INNER JOIN pessoa_fisica f ON f.id_pessoa_fisica = n.id_pessoa_fisica INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa WHERE p.nome_razao LIKE '%" + codigo + "%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaSetor(self, codigo):
        try:
            _sql = "SELECT u.id_usuarios, p.nome_razao, p.sobrenome_fantasia, s.descricao, c.descricao, u.login FROM usuarios u INNER JOIN funcionario n ON n.id_funcionario = u.id_funcionario INNER JOIN setores s ON s.id_setores = n.id_setores INNER JOIN cargo c ON c.id_cargo = n.id_cargo INNER JOIN pessoa_fisica f ON f.id_pessoa_fisica = n.id_pessoa_fisica INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa WHERE s.descricao = '" + codigo + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaCargo(self, codigo):
        try:
            _sql = "SELECT u.id_usuarios, p.nome_razao, p.sobrenome_fantasia, s.descricao, c.descricao, u.login FROM usuarios u INNER JOIN funcionario n ON n.id_funcionario = u.id_funcionario INNER JOIN setores s ON s.id_setores = n.id_setores INNER JOIN cargo c ON c.id_cargo = n.id_cargo INNER JOIN pessoa_fisica f ON f.id_pessoa_fisica = n.id_pessoa_fisica INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa WHERE c.descricao = '" + codigo + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaLogin(self, codigo):
        try:
            _sql = "SELECT u.id_usuarios, p.nome_razao, p.sobrenome_fantasia, s.descricao, c.descricao, u.login FROM usuarios u INNER JOIN funcionario n ON n.id_funcionario = u.id_funcionario INNER JOIN setores s ON s.id_setores = n.id_setores INNER JOIN cargo c ON c.id_cargo = n.id_cargo INNER JOIN pessoa_fisica f ON f.id_pessoa_fisica = n.id_pessoa_fisica INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa WHERE u.login = '" + codigo + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesqPermissoesUsuario(self, codigo):
        try:
            _sql = "SELECT p.id_formularios, p.ativar, p.cadastra, p.cancelar, p.deleta, p.altera from permissoes_usuarios pu INNER JOIN permissoes p ON p.id_permissoes = pu.id_permissoes INNER JOIN usuarios u ON u.id_usuarios = pu.id_usuarios WHERE pu.id_usuarios = '" + codigo + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False