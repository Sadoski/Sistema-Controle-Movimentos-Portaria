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
            _sql = "INSERT INTO motorista (cnh, pis, observacao, situacao, id_categoria_cnh, id_pessoa_fisica, cadastrado) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            _valores = (motorista.getCnh, motorista.getPis, motorista.getObservacao, motorista.getSituacao, motorista.getCategoria, motorista.getIdPessoaFisica, self.__dataHora)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            # self.__cursor.close()
            QMessageBox.information(QWidget(), 'Mensagem', "Cadastro realizado com sucesso!")

        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False

    def cadastrarVeiculoMotorista(self, marca, modelo, placa, idMotorista):
        try:
            _sql = "INSERT INTO veiculo_motorista (marca, modelo, placa, situacao, id_motorista, cadastrado) VALUES (%s, %s, %s, %s, %s, %s)"
            _valores = (marca, modelo, placa, 1, idMotorista, self.__dataHora)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            # self.__cursor.close()

        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False

    def pesquisarVeiculo(self, idMotorista, situacao):
        try:
            _sql = "SELECT id_veiculo FROM veiculo_motorista  WHERE id_motorista = '"+idMotorista+"' AND situacao = '"+situacao+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaCodigoFisica(self, pesquisa):
        try:
            _sql = "SELECT m.id_motorista, p.nome_razao, p.sobrenome_fantasia, m.cnh, p.cpf_cnpj, p.rg_inscricao, f.expeditor, f.uf, m.pis, f.aniversario, g.sexo, f.mae, f.pai, p.endereco, p.numero, p.complemento, p.bairro, c.nome, e.nome, c.cep, t.descricao, v.marca, v.modelo, v.placa, m.observacao, m.situacao FROM motorista m INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista INNER JOIN categoria_cnh t ON t.id_categoria_cnh = m.id_categoria_cnh INNER JOIN pessoa_fisica f ON f.id_pessoa_fisica = m.id_pessoa_fisica INNER JOIN genero g ON g.id_genero = f.id_genero INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado  WHERE m.id_motorista = '"+pesquisa+"' AND v.situacao = 1"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarNomeFisica(self, pesquisa):
        try:
            _sql = "SELECT m.id_motorista, p.nome_razao, p.sobrenome_fantasia, m.cnh, p.cpf_cnpj, p.rg_inscricao, f.expeditor, f.uf, m.pis, f.aniversario, g.sexo, f.mae, f.pai, p.endereco, p.numero, p.complemento, p.bairro, c.nome, e.nome, c.cep, t.descricao, v.marca, v.modelo, v.placa, m.observacao, m.situacao FROM motorista m INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista INNER JOIN categoria_cnh t ON t.id_categoria_cnh = m.id_categoria_cnh INNER JOIN pessoa_fisica f ON f.id_pessoa_fisica = m.id_pessoa_fisica INNER JOIN genero g ON g.id_genero = f.id_genero INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado WHERE p.nome_razao LIKE '%"+pesquisa+"%' AND v.situacao = 1"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()

            return result
        except BaseException as os:
            return False

    def pesquisaCpfFisica(self, pesquisa):
        try:
            _sql = "SELECT m.id_motorista, p.nome_razao, p.sobrenome_fantasia, m.cnh, p.cpf_cnpj, p.rg_inscricao, f.expeditor, f.uf, m.pis, f.aniversario, g.sexo, f.mae, f.pai, p.endereco, p.numero, p.complemento, p.bairro, c.nome, e.nome, c.cep, t.descricao, v.marca, v.modelo, v.placa, m.observacao, m.situacao FROM motorista m INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista INNER JOIN categoria_cnh t ON t.id_categoria_cnh = m.id_categoria_cnh INNER JOIN pessoa_fisica f ON f.id_pessoa_fisica = m.id_pessoa_fisica INNER JOIN genero g ON g.id_genero = f.id_genero INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado WHERE p.cpf_cnpj = '"+pesquisa+"' AND v.situacao = 1"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaRgFisica(self, pesquisa):
        try:
            _sql = "SELECT m.id_motorista, p.nome_razao, p.sobrenome_fantasia, m.cnh, p.cpf_cnpj, p.rg_inscricao, f.expeditor, f.uf, m.pis, f.aniversario, g.sexo, f.mae, f.pai, p.endereco, p.numero, p.complemento, p.bairro, c.nome, e.nome, c.cep, t.descricao, v.marca, v.modelo, v.placa, m.observacao, m.situacao FROM motorista m INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista INNER JOIN categoria_cnh t ON t.id_categoria_cnh = m.id_categoria_cnh INNER JOIN pessoa_fisica f ON f.id_pessoa_fisica = m.id_pessoa_fisica INNER JOIN genero g ON g.id_genero = f.id_genero INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado  WHERE p.rg_inscricao = '"+pesquisa+"' AND v.situacao = 1"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaNumCarteira(self, pesquisa):
        try:
            _sql = "SELECT m.id_motorista, p.nome_razao, p.sobrenome_fantasia, m.cnh, p.cpf_cnpj, p.rg_inscricao, f.expeditor, f.uf, m.pis, f.aniversario, g.sexo, f.mae, f.pai, p.endereco, p.numero, p.complemento, p.bairro, c.nome, e.nome, c.cep, t.descricao, v.marca, v.modelo, v.placa, m.observacao, m.situacao FROM motorista m INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista INNER JOIN categoria_cnh t ON t.id_categoria_cnh = m.id_categoria_cnh INNER JOIN pessoa_fisica f ON f.id_pessoa_fisica = m.id_pessoa_fisica INNER JOIN genero g ON g.id_genero = f.id_genero INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado WHERE m.cnh = '" + pesquisa + "' AND v.situacao = 1"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaPis(self, pesquisa):
        try:
            _sql = "SELECT m.id_motorista, p.nome_razao, p.sobrenome_fantasia, m.cnh, p.cpf_cnpj, p.rg_inscricao, f.expeditor, f.uf, m.pis, f.aniversario, g.sexo, f.mae, f.pai, p.endereco, p.numero, p.complemento, p.bairro, c.nome, e.nome, c.cep, t.descricao, v.marca, v.modelo, v.placa, m.observacao, m.situacao FROM motorista m INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista INNER JOIN categoria_cnh t ON t.id_categoria_cnh = m.id_categoria_cnh INNER JOIN pessoa_fisica f ON f.id_pessoa_fisica = m.id_pessoa_fisica INNER JOIN genero g ON g.id_genero = f.id_genero INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estadoWHERE m.pis = '" + pesquisa + "' AND v.situacao = 1"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarPessoaCodigo(self, funcionario):
        try:
            _sql = "SELECT p.id_pessoa FROM motorista m INNER JOIN categoria_cnh h ON h.id_categoria_cnh = m.id_categoria_cnh INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista INNER JOIN pessoa_fisica f ON f.id_pessoa_fisica = m.id_pessoa_fisica INNER JOIN genero g ON g.id_genero = f.id_genero INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado WHERE m.id_motorista = '"+ funcionario +"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarPessoaFisicaId(self, motorista):
        try:
            _sql = "SELECT f.id_pessoa_fisica FROM pessoa_fisica f INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa WHERE p.id_pessoa = '" +str(motorista)+ "'"

            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaVeiculo(self, idMotorista, situacao):
        try:
            _sql = "SELECT id_veiculo FROM veiculo_motorista WHERE id_motorista = '" + idMotorista + "' AND  situacao = '" + situacao + "'"
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
            _sql = "SELECT * FROM telefone_motorista t INNER JOIN telefone l ON l.id_telefone = t.id_telefone INNER JOIN motorista c ON c.id_motorista = t.id_motorista WHERE t.id_telefone = '" + idTelefone + "' AND  t.id_motorista = '" + idFuncionario + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaEmailMotorista(self, idEmail, idFuncionario):
        try:
            _sql = "SELECT * FROM email_motorista t INNER JOIN email l ON l.id_email = t.id_email INNER JOIN motorista c ON c.id_motorista = t.id_motorista WHERE t.id_telefone = '" + idEmail + "' AND  t.id_motorista = '" + idFuncionario + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def atualizarMotorista(self, motorista):

        try:
            __sql = "UPDATE motorista SET  id_pessoa_fisica = %s, situacao = %s, observacao = %s, cnh = %s, pis = %s, id_categoria_cnh = %s, atualizado = %s WHERE  id_motorista = %s"
            _valores = (motorista.getIdPessoaFisica, motorista.getSituacao, motorista.getObservacao, motorista.getCnh, motorista.getPis, motorista.getCategoria, self.__dataHora, motorista.getIdMotorista)
            self.__cursor.execute(__sql, _valores)
            self.__conexao.conn.commit()
            QMessageBox.information(QWidget(), 'Mensagem', "Cadastro atualizado com sucesso")
            # self.__cursor.close()
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao atualizar as informações no banco de dados")
            self.__conexao.conn.rollback()
            return False

    def pesquisarTabelaNf(self, idMotorista):
        try:
            _sql = "SELECT * FROM notas_fiscais WHERE id_motorista = '" + str(idMotorista) + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def deletarMotorista(self, motorista):
        try:
            __sql = "DELETE FROM motorista WHERE id_motorista = '" + str(motorista) + "'"
            self.__cursor.execute(__sql)
            self.__conexao.conn.commit()
            # self.__cursor.close
            return True
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao deletar as informações no banco de dados")
            self.__conexao.conn.rollback()
            return False

    def alterarVeiculo(self, situacao, motorista):
        try:
            __sql = "UPDATE veiculo_motorista SET situacao = %s, atualizado = %s WHERE id_veiculo = %s"
            _valores = (situacao, self.__dataHora, motorista)

            self.__cursor.execute(__sql, _valores)
            self.__conexao.conn.commit()
            # self.__cursor.close()
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao deletar as informações no banco de dados")
            self.__conexao.conn.rollback()
            return False

    def deletarVeiculoMotorista(self, motorista):
        try:
            __sql = "DELETE FROM veiculo_motorista WHERE id_motorista = '" + str(motorista)+ "'"
            self.__cursor.execute(__sql)
            self.__conexao.conn.commit()
            # self.__cursor.close()
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao deletar as informações no banco de dados")
            self.__conexao.conn.rollback()
            return False
