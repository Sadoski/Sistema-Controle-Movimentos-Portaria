import sys
import time
import datetime
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mysql.connector import Error
from conexao.conexao import ConexaoDb, mysql

class MotoristaDao(object):
    def __init__(self):
        self.__conexao = ConexaoDb()
        self.__cursor = self.__conexao.conn.cursor()
        self.__ts = time.time()
        self.__dataHora = datetime.datetime.fromtimestamp(self.__ts).strftime('%Y-%m-%d %H:%M:%S')

    def pesquisarCategoria(self):
        try:
            _sql = "SELECT descricao FROM categoria_cnh"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarTipoVeiculo(self):
        try:
            _sql = "SELECT descricao FROM tipo_veiculo"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarIdMotorista(self, motorista):
        try:
            _sql = " SELECT id_motorista FROM motorista WHERE nome = %s and rg = %s and cpf = %s and pis = %s and cnh = %s"
            _valores = (motorista.getNome, motorista.getRg, motorista.getCpf, motorista.getPis, motorista.getCnh)
            self.__cursor.execute(_sql, _valores)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarIdTipoVeiculo(self, tipo):
        try:
            _sql = " SELECT id_tipo_veiculo FROM tipo_veiculo WHERE descricao = '"+tipo+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarIdCategoriaCnh(self, tipo):
        try:
            _sql = " SELECT id_categoria_cnh FROM categoria_cnh WHERE descricao = '"+tipo+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def cadastrarMotorista(self, motorista):
        try:
            _sql = "INSERT INTO motorista (nome,data_nascimento,rg,expeditor,cpf,pis,cnh,id_categoria_cnh,endereco,numero,complemento,bairro,tefefone,celular,sexo,id_cidade,cadastrado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            _valores = (motorista.getNome, motorista.getNascimento, motorista.getRg, motorista.getExpeditor, motorista.getCpf, motorista.getPis, motorista.getCnh, motorista.getCategoria, motorista.getEndereco, motorista.getNumero, motorista.getComplemento, motorista.getBairro, motorista.getTelefone, motorista.getCelular, motorista.getSexo, motorista.getCidade, self.__dataHora)
            print(_valores)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            # self.__cursor.close()
            QMessageBox.warning(QWidget(), 'Mensagem', "Cadastro realizado com sucesso!")

        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False

    def cadastrarVeiculoMotorista(self, veiculo):
        try:
            _sql = "INSERT INTO veiculo_motorista(id_motorista,id_tipo_veiculo,marca,modelo,placa,cadastrado) VALUES (%s, %s, %s, %s, %s, %s)"
            _valores = (veiculo.getIdMotorista, veiculo.getTipoVeiculo, veiculo.getMarca, veiculo.getModelo, veiculo.getPlaca, self.__dataHora)
            print(_valores)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            # self.__cursor.close()
            QMessageBox.warning(QWidget(), 'Mensagem', "Cadastro realizado com sucesso!")

        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False

    def atualizarMotorista(self, motorista):

        try:
            __sql = "UPDATE motorista SET nome = %s,  data_nascimento = %s ,rg = %s, expeditor = %s, cpf = %s, pis = %s, cnh = %s, id_categoria_cnh = %s, endereco = %s, numero = %s, complemento = %s, bairro = %s, telefone = %s, celular = %s, sexo = %s, id_cidade = %s, atualizado = %s WHERE id_funcionario = %s"
            _valores = (motorista.getNome, motorista.getNascimento, motorista.getRg, motorista.getExpeditor, motorista.getCpf, motorista.getPis, motorista.getCnh, motorista.getCategoria, motorista.getEndereco, motorista.getNumero, motorista.getComplemento, motorista.getBairro, motorista.getTelefone, motorista.getCelular, motorista.getSexo, motorista.getCidade, self.__dataHora, motorista.getIdMotorista)

            self.__cursor.execute(__sql, _valores)
            self.__conexao.conn.commit()
            QMessageBox.warning(QWidget(), 'Mensagem', "Edição realizado com sucesso!")
            #self.__cursor.close()
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao atualizar as informações no banco de dados")
            self.__conexao.conn.rollback()
            return False

    def atualizarVeiculoMotorista(self, veiculo):

        try:
            __sql = "UPDATE motorista SET id_motorista = %s, id_tipo_veiculo = %s, marca = %s, modelo = %s, placa = %s, atualizado = %s WHERE id_veiculo = %s"
            _valores = (veiculo.getIdMotorista, veiculo.getTipoVeiculo, veiculo.getMarca, veiculo.getModelo, veiculo.getPlaca, self.__dataHora, veiculo.getIdVeiculo)

            self.__cursor.execute(__sql, _valores)
            self.__conexao.conn.commit()
            QMessageBox.warning(QWidget(), 'Mensagem', "Edição realizado com sucesso!")
            # self.__cursor.close()
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao atualizar as informações no banco de dados")
            self.__conexao.conn.rollback()
            return False

    def deletarMotorista(self, motorista):
        try:
            __sql = "DELETE FROM motorista WHERE id_motorista = '" + motorista + "'"
            self.__cursor.execute(__sql)
            self.__conexao.conn.commit()
            # self.__cursor.close()
            QMessageBox.warning(QWidget(), 'Mensagem', "Exclusão realizado com sucesso!")
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao deletar as informações no banco de dados")
            self.__conexao.conn.rollback()
            return False

    def pesquisarCodigoMotorista(self, motorista):
        try:
            _sql = "SELECT m.id_motorista, m.nome, m.data_nascimento, m.rg, m.expeditor, m.cpf, m.pis, m.cnh, n.descricao, m.sexo, m.endereco, m.numero, m.complemento, m.bairro, m.telefone, m.celular, c.cep, c.nome, e.nome, t.descricao, v.marca, v.modelo, v.placa FROM veiculo_motorista v INNER JOIN tipo_veiculo t ON t.id_tipo_veiculo = v.id_tipo_veiculo INNER JOIN motorista m On m.id_motorista = v.id_motorista INNER JOIN categoria_cnh n ON n.id_categoria_cnh = m.id_categoria_cnh INNER JOIN cidade c ON c.id_cidade = m.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado WHERE m.id_motorista = '"+motorista+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            self.__cursor.close()
            return result
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao pesquisar a cidade no banco de dados ")
            return False

    def pesquisarNomeMotorista(self, motorista):
        try:
            _sql = "SELECT m.id_motorista, m.nome, m.data_nascimento, m.rg, m.expeditor, m.cpf, m.pis, m.cnh, n.descricao, m.sexo, m.endereco, m.numero, m.complemento, m.bairro, m.telefone, m.celular, c.cep, c.nome, e.nome, t.descricao, v.marca, v.modelo, v.placa FROM veiculo_motorista v INNER JOIN tipo_veiculo t ON t.id_tipo_veiculo = v.id_tipo_veiculo INNER JOIN motorista m On m.id_motorista = v.id_motorista INNER JOIN categoria_cnh n ON n.id_categoria_cnh = m.id_categoria_cnh INNER JOIN cidade c ON c.id_cidade = m.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado WHERE m.nome LIKE '%"+motorista+"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            self.__cursor.close()
            return result
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao pesquisar a cidade no banco de dados ")
            return False

    def pesquisarCpfMotorista(self, motorista):
        try:
            _sql = "SELECT m.id_motorista, m.nome, m.data_nascimento, m.rg, m.expeditor, m.cpf, m.pis, m.cnh, n.descricao, m.sexo, m.endereco, m.numero, m.complemento, m.bairro, m.telefone, m.celular, c.cep, c.nome, e.nome, t.descricao, v.marca, v.modelo, v.placa FROM veiculo_motorista v INNER JOIN tipo_veiculo t ON t.id_tipo_veiculo = v.id_tipo_veiculo INNER JOIN motorista m On m.id_motorista = v.id_motorista INNER JOIN categoria_cnh n ON n.id_categoria_cnh = m.id_categoria_cnh INNER JOIN cidade c ON c.id_cidade = m.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado WHERE m.cpf = '"+motorista+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            self.__cursor.close()
            return result
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao pesquisar a cidade no banco de dados ")
            return False

    def pesquisarRgMotorista(self, motorista):
        try:
            _sql = "SELECT m.id_motorista, m.nome, m.data_nascimento, m.rg, m.expeditor, m.cpf, m.pis, m.cnh, n.descricao, m.sexo, m.endereco, m.numero, m.complemento, m.bairro, m.telefone, m.celular, c.cep, c.nome, e.nome, t.descricao, v.marca, v.modelo, v.placa FROM veiculo_motorista v INNER JOIN tipo_veiculo t ON t.id_tipo_veiculo = v.id_tipo_veiculo INNER JOIN motorista m On m.id_motorista = v.id_motorista INNER JOIN categoria_cnh n ON n.id_categoria_cnh = m.id_categoria_cnh INNER JOIN cidade c ON c.id_cidade = m.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado WHERE m.rg = '"+motorista+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            self.__cursor.close()
            return result
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao pesquisar a cidade no banco de dados ")
            return False

    def pesquisarCnhMotorista(self, motorista):
        try:
            _sql = "SELECT m.id_motorista, m.nome, m.data_nascimento, m.rg, m.expeditor, m.cpf, m.pis, m.cnh, n.descricao, m.sexo, m.endereco, m.numero, m.complemento, m.bairro, m.telefone, m.celular, c.cep, c.nome, e.nome, t.descricao, v.marca, v.modelo, v.placa FROM veiculo_motorista v INNER JOIN tipo_veiculo t ON t.id_tipo_veiculo = v.id_tipo_veiculo INNER JOIN motorista m On m.id_motorista = v.id_motorista INNER JOIN categoria_cnh n ON n.id_categoria_cnh = m.id_categoria_cnh INNER JOIN cidade c ON c.id_cidade = m.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado WHERE m.cnh = '"+motorista+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            self.__cursor.close()
            return result
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao pesquisar a cidade no banco de dados ")
            return False

    def pesquisarPisMotorista(self, motorista):
        try:
            _sql = "SELECT m.id_motorista, m.nome, m.data_nascimento, m.rg, m.expeditor, m.cpf, m.pis, m.cnh, n.descricao, m.sexo, m.endereco, m.numero, m.complemento, m.bairro, m.telefone, m.celular, c.cep, c.nome, e.nome, t.descricao, v.marca, v.modelo, v.placa FROM veiculo_motorista v INNER JOIN tipo_veiculo t ON t.id_tipo_veiculo = v.id_tipo_veiculo INNER JOIN motorista m On m.id_motorista = v.id_motorista INNER JOIN categoria_cnh n ON n.id_categoria_cnh = m.id_categoria_cnh INNER JOIN cidade c ON c.id_cidade = m.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado WHERE m.pis = '"+motorista+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            self.__cursor.close()
            return result
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao pesquisar a cidade no banco de dados ")
            return False