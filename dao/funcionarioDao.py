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

    def ultimoRegistro(self):
        try:
            _sql = "SELECT LAST_INSERT_ID()"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()

            return result

        except BaseException as os:
            return False

    def estadoCivil(self):
        try:
            _sql = "SELECT id_civil, descricao FROM civil"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def deficiencia(self):
        try:
            _sql = "SELECT id_deficiencia, descricao FROM deficiencia "
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def categoriaTrabalho(self):
        try:
            _sql = "SELECT id_categoria_trabalho, descricao FROM categoria_trabalho"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def setores(self):
        try:
            _sql = "SELECT id_setores, descricao FROM setores"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def cargos(self):
        try:
            _sql = "SELECT id_cargo, descricao FROM cargo"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def jornada(self):
        try:
            _sql = "SELECT id_jornada_trabalho, descricao FROM jornada_trabalho"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarFuncionarioIdFisico(self, cliente):
        try:
            _sql = "SELECT * FROM funcionario e INNER JOIN pessoa_fisica p ON p.id_pessoa_fisica = e.id_pessoa_fisica INNER JOIN pessoa f ON p.id_pessoa = f.id_pessoa WHERE e.id_pessoa_fisica  = '"+ cliente +"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarPessoaFisica(self, pessoaFisica):
        try:
            _sql = "SELECT p.cpf_cnpj, p.rg_inscricao, p.nome_razao, p.sobrenome_fantasia FROM pessoa_fisica f INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa WHERE f.id_pessoa_fisica = '"+pessoaFisica+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False


    def pesquisarFuncionarioFisico(self, empresa):
        try:
            _sql = "SELECT * FROM pessoa p INNER JOIN pessoa_fisica j ON j.id_pessoa = p.id_pessoa INNER JOIN funcionario e ON e.id_pessoa_fisica = j.id_pessoa_fisica INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE  t.descricao = 'PESSOA FISÍCA' AND e.id_pessoa_fisica = '"+ empresa +"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarPessoaFisico(self, pessoaFisica):
        try:
            _sql = "SELECT p.id_pessoa FROM pessoa_fisica f INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa WHERE f.id_pessoa_fisica = '"+pessoaFisica+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
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
            # self.__cursor.close()

        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False

    def cadastrarTelefoneFuncionario(self, idTelefone, idPessoa):

        try:
            _sql = "INSERT INTO telefone_funcionario (id_telefone, id_cliente) VALUES (%s, %s)"
            _valores = (idTelefone, idPessoa)

            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            # self.__cursor.close()

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

    def cadastrarEmailFuncionario(self, idEmail, idPessoa):

        try:
            _sql = "INSERT INTO email_funcionario (id_email, id_cliente) VALUES (%s, %s)"
            _valores = (idEmail, idPessoa)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            #self.__cursor.close()

        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados  email")
            self.__conexao.conn.rollback()
            return False

    def cadastrarFuncionarioFisico(self, funcionario):
        try:
            _sql = "INSERT INTO funcionario (id_pessoa_fisica, situacao, observacao, data_demissao, data_admissao, num_carteira, serie, uf, data_emissao, pis_pasep, id_civil, id_deficiencia, id_categoria_trabalho, id_setores, id_cargo, cadastrado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            _valores = (funcionario.getIdPessoaFisica, funcionario.getSituacao, funcionario.getObservacao, funcionario.getDemissao, funcionario.getAdmissao, funcionario.getNumCarteira,  funcionario.setSerie, funcionario.getUf, funcionario.getEmissao, funcionario.getCivil, funcionario.getDeficiencia, funcionario.getCategoria, funcionario.getSetor, funcionario.getCargo, funcionario.getPis, self.__dataHora)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            # self.__cursor.close()
            QMessageBox.information(QWidget(), 'Mensagem', "Cadastro realizado com sucesso!")

        except mysql.connector.Error as e:
            QMessageBox.warning(QWidget(), 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False

    def cadastrarHorarios(self, semana, inicio, iniIntervalo, fimIntervalo, termino, s):
        try:
            _sql = "INSERT INTO horario_jornada (dia, hora_entrada, hora_ini_intervalo, hora_fim_intervalo, hora_saida, id_jornada_trabalho, id_funcionario) VALUES (%s, %s, %s, %s, %s, %s)"
            _valores = (semana, inicio, iniIntervalo, fimIntervalo, termino, idFuncionario)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            # self.__cursor.close()
        except mysql.connector.Error as e:
            QMessageBox.warning(QWidget(), 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False














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