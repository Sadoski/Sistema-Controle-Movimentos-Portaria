import sys
import time
import datetime
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mysql.connector import Error
from conexao.conexao import ConexaoDb, mysql


class SaidaFuncionarioDao(object):
    def __init__(self):
        self.__conexao = ConexaoDb()
        self.__cursor = self.__conexao.conn.cursor()

    def pesquisarFuncionario(self, codigo):
        try:
            _sql = "SELECT f.id_funcionario, p.nome_razao, p.sobrenome_fantasia, p.cpf_cnpj, p.rg_inscricao, s.expeditor, s.uf, s.aniversario, g.sexo, p.endereco, p.numero, p.complemento, p.bairro, s.mae, s.pai, c.nome, e.nome, c.cep, f.data_admissao, f.data_demissao, f.num_carteira, f.serie, f.uf, f.data_emissao, f.pis_pasep, i.descricao, d.descricao, r.descricao, t.descricao,  o.descricao, f.observacao, b.descricao, f.situacao  FROM funcionario f INNER JOIN civil i ON i.id_civil = f.id_civil INNER JOIN deficiencia d ON d.id_deficiencia = f.id_deficiencia INNER JOIN categoria_trabalho r ON r.id_categoria_trabalho = f.id_categoria_trabalho INNER JOIN setores t ON t.id_setores = f.id_setores INNER JOIN cargo o ON o.id_cargo = f.id_cargo INNER JOIN jornada_trabalho b ON b.id_jornada_trabalho = f.id_jornada_trabalho INNER JOIN pessoa_fisica s ON s.id_pessoa_fisica = f.id_pessoa_fisica INNER JOIN genero g ON g.id_genero = s.id_genero INNER JOIN pessoa p ON p.id_pessoa = s.id_pessoa INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado  WHERE f.id_funcionario = '"+ codigo +"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False


    def cadastro(self, funcionario):
        try:
            _sql = "INSERT INTO saida_funcionario (id_funcionario, data, hora, status) VALUES (%s, %s, %s, %s)"
            _valores = (funcionario.getIdFuncionario, funcionario.getData, funcionario.getHora, 'Aberto')
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            # self.__cursor.close()
            QMessageBox.information(QWidget(), 'Mensagem', "Saida realizado com sucesso!")
            return True
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False

    def pesquisarCodFuncRel(self, pesquisar):
        try:
            _sql = "SELECT p.id_saida_funcionario, p.data, p.hora, n.data, n.hora, s.nome_razao, t.descricao, l.descricao FROM saida_funcionario p LEFT OUTER JOIN entrada_funcionario n ON n.id_saida_funcionario = p.id_saida_funcionario INNER JOIN funcionario f ON f.id_funcionario = p.id_funcionario INNER JOIN pessoa_fisica e ON e.id_pessoa_fisica = f.id_pessoa_fisica INNER JOIN pessoa s ON s.id_pessoa = e.id_pessoa INNER JOIN setores t ON t.id_setores = f.id_setores INNER JOIN cargo l ON l.id_cargo = f.id_cargo WHERE p.id_funcionario = '"+pesquisar+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarFuncioFuncRel(self, pesquisar):
        try:
            _sql = "SELECT p.id_saida_funcionario, p.data, p.hora, n.data, n.hora, s.nome_razao, t.descricao, l.descricao FROM saida_funcionario p LEFT OUTER JOIN entrada_funcionario n ON n.id_saida_funcionario = p.id_saida_funcionario INNER JOIN funcionario f ON f.id_funcionario = p.id_funcionario INNER JOIN pessoa_fisica e ON e.id_pessoa_fisica = f.id_pessoa_fisica INNER JOIN pessoa s ON s.id_pessoa = e.id_pessoa INNER JOIN setores t ON t.id_setores = f.id_setores INNER JOIN cargo l ON l.id_cargo = f.id_cargo WHERE s.nome_razao LIKE  '%"+pesquisar+"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarSetorFuncRel(self, pesquisar):
        try:
            _sql = "SELECT p.id_saida_funcionario, p.data, p.hora, n.data, n.hora, s.nome_razao, t.descricao, l.descricao FROM saida_funcionario p LEFT OUTER JOIN entrada_funcionario n ON n.id_saida_funcionario = p.id_saida_funcionario INNER JOIN funcionario f ON f.id_funcionario = p.id_funcionario INNER JOIN pessoa_fisica e ON e.id_pessoa_fisica = f.id_pessoa_fisica INNER JOIN pessoa s ON s.id_pessoa = e.id_pessoa INNER JOIN setores t ON t.id_setores = f.id_setores INNER JOIN cargo l ON l.id_cargo = f.id_cargo WHERE t.descricao = '"+pesquisar+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarCargoFuncRel(self, pesquisar):
        try:
            _sql = "SELECT p.id_saida_funcionario, p.data, p.hora, n.data, n.hora, s.nome_razao, t.descricao, l.descricao FROM saida_funcionario p LEFT OUTER JOIN entrada_funcionario n ON n.id_saida_funcionario = p.id_saida_funcionario INNER JOIN funcionario f ON f.id_funcionario = p.id_funcionario INNER JOIN pessoa_fisica e ON e.id_pessoa_fisica = f.id_pessoa_fisica INNER JOIN pessoa s ON s.id_pessoa = e.id_pessoa INNER JOIN setores t ON t.id_setores = f.id_setores INNER JOIN cargo l ON l.id_cargo = f.id_cargo WHERE l.descricao = '"+pesquisar+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False