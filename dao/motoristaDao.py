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

    def ultimoRegistro(self):
        try:
            _sql = "SELECT LAST_INSERT_ID()"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()

            return result

        except BaseException as os:
            return False

    def pesquisarMotoristaFisico(self, motorista):
        try:
            _sql = "SELECT * FROM pessoa p INNER JOIN pessoa_fisica j ON j.id_pessoa = p.id_pessoa INNER JOIN motorista e ON e.id_pessoa_fisica = j.id_pessoa_fisica INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE  t.descricao = 'PESSOA FISÍCA' AND e.id_pessoa_fisica  = '"+ motorista +"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarCategoria(self):
        try:
            _sql = "SELECT * FROM categoria_cnh"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarMotoristaIdFisico(self, motorista):
        try:
            _sql = "SELECT * FROM motorista m INNER JOIN pessoa_fisica f ON f.id_pessoa_fisica = m.id_pessoa_fisica INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa WHERE f.id_pessoa_fisica = '"+ motorista +"'"
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

    def cadastrarTelefone(self, empresa):

        try:
            _sql = "INSERT INTO telefone (contato, telefone) VALUES (%s, %s)"
            _valores = (empresa.getContato, empresa.getTelefone)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            #self.__cursor.close()

        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False

    def cadastrarTelefoneMotorista(self, idTelefone, idPessoa):

        try:
            _sql = "INSERT INTO telefone_motorista (id_telefone, id_motorista) VALUES (%s, %s)"
            _valores = (idTelefone, idPessoa)

            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            #self.__cursor.close()

        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False

    def cadastrarEmail(self, motorista):

        try:
            _sql = "INSERT INTO email (contato, email) VALUES (%s, %s)"
            _valores = (motorista.getContato, motorista.getEmail)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            #self.__cursor.close()

        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados email ")
            self.__conexao.conn.rollback()
            return False

    def cadastrarEmailMotorista(self, idEmail, idPessoa):

        try:
            _sql = "INSERT INTO email_motorista (id_email, id_motorista) VALUES (%s, %s)"
            _valores = (idEmail, idPessoa)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            #self.__cursor.close()

        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados  email")
            self.__conexao.conn.rollback()
            return False

    def pesquisarPessoaFis(self, pessoaFisica):
        try:
            _sql = "SELECT p.id_pessoa FROM pessoa_fisica f INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa WHERE f.id_pessoa_fisica = '"+pessoaFisica+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def cadastrarMotorista(self, motorista):
        try:
            _sql = "INSERT INTO motorista (cnh, pis, observacao, id_categoria_cnh, id_pessoa_fisica, cadastrado) VALUES (%s, %s, %s, %s, %s, %s)"
            _valores = (motorista.getCnh, motorista.getPis, motorista.getObservacao, motorista.getCategoria, motorista.getIdPessoaFisica, self.__dataHora)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            # self.__cursor.close()
            QMessageBox.warning(QWidget(), 'Mensagem', "Cadastro realizado com sucesso!")

        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False

    def cadastrarVeiculoMotorista(self, marca, modelo, placa):
        try:
            _sql = "INSERT INTO veiculo_motorista (marca, modelo, placa, cadastrado) VALUES (%s, %s, %s, %s)"
            _valores = (marca, modelo, placa, self.__dataHora)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            # self.__cursor.close()
            QMessageBox.warning(QWidget(), 'Mensagem', "Cadastro realizado com sucesso!")

        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False

    def pesquisaCodigoFisica(self, pesquisa):
        try:
            _sql = "SELECT m.id_motorista, p.nome_razao, p.sobrenome_fantasia, m.cnh, p.cpf_cnpj, p.rg_inscricao, f.expeditor, f.uf, m.pis, f.aniversario, g.sexo, f.mae, f.pai, p.endereco, p.numero, p.complemento, p.bairro, c.nome, e.nome, c.cep, t.descricao, v.marca, v.modelo, v.placa, m.observacao, m.situacao FROM motorista m INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista INNER JOIN categoria_cnh t ON t.id_categoria_cnh = m.id_categoria_cnh INNER JOIN pessoa_fisica f ON f.id_pessoa_fisica = m.id_pessoa_fisica INNER JOIN genero g ON g.id_genero = f.id_genero INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado  WHERE m.id_motorista = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarNomeFisica(self, pesquisa):
        try:
            _sql = "SELECT m.id_motorista, p.nome_razao, p.sobrenome_fantasia, m.cnh, p.cpf_cnpj, p.rg_inscricao, f.expeditor, f.uf, m.pis, f.aniversario, g.sexo, f.mae, f.pai, p.endereco, p.numero, p.complemento, p.bairro, c.nome, e.nome, c.cep, t.descricao, v.marca, v.modelo, v.placa, m.observacao, m.situacao FROM motorista m INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista INNER JOIN categoria_cnh t ON t.id_categoria_cnh = m.id_categoria_cnh INNER JOIN pessoa_fisica f ON f.id_pessoa_fisica = m.id_pessoa_fisica INNER JOIN genero g ON g.id_genero = f.id_genero INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado WHERE p.nome_razao LIKE '%"+pesquisa+"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaCpfFisica(self, pesquisa):
        try:
            _sql = "SELECT m.id_motorista, p.nome_razao, p.sobrenome_fantasia, m.cnh, p.cpf_cnpj, p.rg_inscricao, f.expeditor, f.uf, m.pis, f.aniversario, g.sexo, f.mae, f.pai, p.endereco, p.numero, p.complemento, p.bairro, c.nome, e.nome, c.cep, t.descricao, v.marca, v.modelo, v.placa, m.observacao, m.situacao FROM motorista m INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista INNER JOIN categoria_cnh t ON t.id_categoria_cnh = m.id_categoria_cnh INNER JOIN pessoa_fisica f ON f.id_pessoa_fisica = m.id_pessoa_fisica INNER JOIN genero g ON g.id_genero = f.id_genero INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado WHERE p.cpf_cnpj = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaRgFisica(self, pesquisa):
        try:
            _sql = "SELECT m.id_motorista, p.nome_razao, p.sobrenome_fantasia, m.cnh, p.cpf_cnpj, p.rg_inscricao, f.expeditor, f.uf, m.pis, f.aniversario, g.sexo, f.mae, f.pai, p.endereco, p.numero, p.complemento, p.bairro, c.nome, e.nome, c.cep, t.descricao, v.marca, v.modelo, v.placa, m.observacao, m.situacao FROM motorista m INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista INNER JOIN categoria_cnh t ON t.id_categoria_cnh = m.id_categoria_cnh INNER JOIN pessoa_fisica f ON f.id_pessoa_fisica = m.id_pessoa_fisica INNER JOIN genero g ON g.id_genero = f.id_genero INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado  WHERE p.rg_inscricao = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaNumCarteira(self, pesquisa):
        try:
            _sql = "SELECT m.id_motorista, p.nome_razao, p.sobrenome_fantasia, m.cnh, p.cpf_cnpj, p.rg_inscricao, f.expeditor, f.uf, m.pis, f.aniversario, g.sexo, f.mae, f.pai, p.endereco, p.numero, p.complemento, p.bairro, c.nome, e.nome, c.cep, t.descricao, v.marca, v.modelo, v.placa, m.observacao, m.situacao FROM motorista m INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista INNER JOIN categoria_cnh t ON t.id_categoria_cnh = m.id_categoria_cnh INNER JOIN pessoa_fisica f ON f.id_pessoa_fisica = m.id_pessoa_fisica INNER JOIN genero g ON g.id_genero = f.id_genero INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado WHERE m.cnh = '" + pesquisa + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaPis(self, pesquisa):
        try:
            _sql = "SELECT m.id_motorista, p.nome_razao, p.sobrenome_fantasia, m.cnh, p.cpf_cnpj, p.rg_inscricao, f.expeditor, f.uf, m.pis, f.aniversario, g.sexo, f.mae, f.pai, p.endereco, p.numero, p.complemento, p.bairro, c.nome, e.nome, c.cep, t.descricao, v.marca, v.modelo, v.placa, m.observacao, m.situacao FROM motorista m INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista INNER JOIN categoria_cnh t ON t.id_categoria_cnh = m.id_categoria_cnh INNER JOIN pessoa_fisica f ON f.id_pessoa_fisica = m.id_pessoa_fisica INNER JOIN genero g ON g.id_genero = f.id_genero INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estadoWHERE m.pis = '" + pesquisa + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarPessoaCodigo(self, funcionario):
        try:
            _sql = "SELECT p.id_pessoa FROM motorista m INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista INNER JOIN tipo_veiculo t ON t.id_tipo_veiculo = v.id_tipo_veiculo INNER JOIN pessoa_fisica f ON f.id_pessoa_fisica = m.id_pessoa_fisica INNER JOIN genero g ON g.id_genero = f.id_genero INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado  WHERE m.id_motorista = '"+ funcionario +"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarPessoaFisicaId(self, funcionario):
        try:
            _sql = "SELECT f.id_pessoa_fisica FROM pessoa_fisica f INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa WHERE p.id_pessoa = '" + funcionario + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaTelefone(self, pesquisa):
        try:
            _sql = "SELECT t.id_telefone, l.contato, l.telefone FROM telefone_motorista t INNER JOIN telefone l ON l.id_telefone = t.id_telefone INNER JOIN motorista c ON c.id_motorista = t.id_motorista WHERE t.id_motorista = '" + pesquisa + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaEmail(self, pesquisa):
        try:
            _sql = "SELECT t.id_email, l.contato, l.email FROM email_motorista t INNER JOIN email l ON l.id_email = t.id_email INNER JOIN motorista c ON c.id_motorista = t.id_motorista WHERE t.id_motorista  = '" + pesquisa + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def deletarTelefone(self, idTelefone, idMotorista):

        try:
            _sql = "DELETE FROM telefone_motorista WHERE id_telefone = %s AND id_motorista = %s"
            __valor = (idTelefone, idMotorista)
            self.__cursor.execute(_sql, __valor)
            self.__conexao.conn.commit()
            #self.__cursor.close()

        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False

    def deletarContatoTelefone(self, idTelefone):

        try:
            _sql = "DELETE FROM telefone WHERE id_telefone = '" + idTelefone + "'"
            self.__cursor.execute(_sql)
            self.__conexao.conn.commit()
            # self.__cursor.close()

        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False

    def deletarEmail(self, idEmail, idMotorista):

        try:
            _sql = "DELETE FROM email_motorista WHERE id_email = %s AND id_motorista = %s"
            __valor = (idEmail, idMotorista)
            self.__cursor.execute(_sql, __valor)
            self.__conexao.conn.commit()
            # self.__cursor.close()

        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados email ")
            self.__conexao.conn.rollback()
            return False

    def deletarContatoEmail(self, idEmail):

        try:
            _sql = "DELETE FROM email WHERE id_email = '" + idEmail + "'"
            self.__cursor.execute(_sql)
            self.__conexao.conn.commit()
            # self.__cursor.close()

        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados email ")
            self.__conexao.conn.rollback()
            return False

    def pesquisaTelefoneMotorista(self, idTelefone, idFuncionario):
        try:
            _sql = "SELECT * FROM telefone_motorista t INNER JOIN telefone l ON l.id_telefone = t.id_telefone INNER JOIN motorista c ON c.id_motorista = t.id_motorista WHERE t.id_telefone = '" + idTelefone + "' AND  t.id_funcionario = '" + idFuncionario + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaEmailMotorista(self, idEmail, idFuncionario):
        try:
            _sql = "SELECT * FROM email_motorista t INNER JOIN email l ON l.id_email = t.id_email INNER JOIN motorista c ON c.id_motorista = t.id_motorista WHERE t.id_telefone = '" + idEmail + "' AND  t.id_funcionario = '" + idFuncionario + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False












    '''
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
            _sql = "INSERT INTO motorista (nome, data_nascimento, rg, expeditor, cpf, pis, cnh, id_categoria_cnh, endereco, numero, complemento, bairro, tefefone, celular, sexo, id_cidade, cadastrado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
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
    '''