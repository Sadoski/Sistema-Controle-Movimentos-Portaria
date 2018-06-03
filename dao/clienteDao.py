import sys
import time
import datetime
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mysql.connector import Error
from conexao.conexao import ConexaoDb, mysql

class ClienteDao(object):
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

    def cadastrarClienteFisico(self, cliente):
        try:
            _sql = "INSERT INTO cliente (id_pessoa, id_pessoa_fisica, situacao, observacao, cadastrado) VALUES (%s, %s, %s, %s, %s)"
            _valores = (cliente.getIdPessoa, cliente.getIdPessoaFisica, cliente.getSituacao, cliente.getObservacao, self.__dataHora)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            # self.__cursor.close()
            QMessageBox.information(QWidget(), 'Mensagem', "Cadastro realizado com sucesso!")

        except mysql.connector.Error as e:
            QMessageBox.warning(QWidget(), 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False

    def cadastrarClienteJuridica(self, cliente):
        try:
            _sql = "INSERT INTO cliente(id_pessoa, id_pessoa_juridica, situacao, observacao, cadastrado) VALUES (%s, %s, %s, %s, %s)"
            _valores = (cliente.getIdPessoa, cliente.getIdPessoaJuridica, cliente.getSituacao, cliente.getObservacao, self.__dataHora)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            # self.__cursor.close()
            QMessageBox.information(QWidget(), 'Mensagem', "Cadastro realizado com sucesso!")

        except mysql.connector.Error as e:
            QMessageBox.warning(QWidget(), 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False

    def atualizarCliente(self, cliente):

        try:
            __sql = "UPDATE cliente SET observacao = %s, situacao = %s WHERE id_cliente = %s"
            _valores = (cliente.getObservacao, cliente.getSituacao, cliente.getIdCliente)
            self.__cursor.execute(__sql, _valores)
            self.__conexao.conn.commit()
            # self.__cursor.close()
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao atualizar as informações no banco de dados")
            self.__conexao.conn.rollback()
            return False

    def deletarCliente(self, cliente):
        try:
            __sql = "DELETE FROM cliente WHERE id_cliente = '" + cliente + "'"
            self.__cursor.execute(__sql)
            self.__conexao.conn.commit()
            # self.__cursor.close()
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao deletar as informações no banco de dados")
            self.__conexao.conn.rollback()
            return False

    def pesquisaCodigoJuridica(self, pesquisa):
        try:
            _sql = "SELECT e.id_cliente, j.fantasia, j.razao_social, j.cnpj, j.ins_estadual, j.endereco, j.numero, j.complemento, j.bairro, c.nome, s.nome, c.cep, e.situacao FROM cliente e INNER JOIN pessoa_juridica j ON j.id_pessoa_juridica = e.id_pessoa_juridica INNER JOIN cidade c ON c.id_cidade = j.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE  e.id_cliente = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaFantasiaJuridica(self, pesquisa):
        try:
            _sql = "SELECT e.id_cliente, j.fantasia, j.razao_social, j.cnpj, j.ins_estadual, j.endereco, j.numero, j.complemento, j.bairro, c.nome, s.nome, c.cep, e.situacao FROM cliente e INNER JOIN pessoa_juridica j ON j.id_pessoa_juridica = e.id_pessoa_juridica INNER JOIN cidade c ON c.id_cidade = j.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE  e.fantasia LIKE '%"+pesquisa+"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaRazaoSocialJuridica(self, pesquisa):
        try:
            _sql = "SELECT e.id_cliente, j.fantasia, j.razao_social, j.cnpj, j.ins_estadual, j.endereco, j.numero, j.complemento, j.bairro, c.nome, s.nome, c.cep, e.situacao FROM cliente e INNER JOIN pessoa_juridica j ON j.id_pessoa_juridica = e.id_pessoa_juridica INNER JOIN cidade c ON c.id_cidade = j.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE  e.razao_social LIKE '%"+pesquisa+"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaCnpjJuridica(self, pesquisa):
        try:
            _sql = "SELECT e.id_cliente, j.fantasia, j.razao_social, j.cnpj, j.ins_estadual, j.endereco, j.numero, j.complemento, j.bairro, c.nome, s.nome, c.cep, e.situacao FROM cliente e INNER JOIN pessoa_juridica j ON j.id_pessoa_juridica = e.id_pessoa_juridica INNER JOIN cidade c ON c.id_cidade = j.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE  e.cnpj = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaInscEstadualJuridica(self, pesquisa):
        try:
            _sql = "SELECT e.id_cliente, j.fantasia, j.razao_social, j.cnpj, j.ins_estadual, j.endereco, j.numero, j.complemento, j.bairro, c.nome, s.nome, c.cep, e.situacao FROM cliente e INNER JOIN pessoa_juridica j ON j.id_pessoa_juridica = e.id_pessoa_juridica INNER JOIN cidade c ON c.id_cidade = j.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE  e.inscricao_estadual = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaCodigoFisica(self, pesquisa):
        try:
            _sql = "SELECT c.id_cliente, t.descricao, p.nome_razao, p.sobrenome_fantasia, p.cpf_cnpj, p.rg_inscricao, f.expeditor, f.uf, f.aniversario, p.endereco, p.numero, p.complemento, p.bairro, i.nome, e.nome, i.cep, j.site, c.observacao, c.situacao FROM cliente c LEFT OUTER JOIN pessoa_fisica f ON f.id_pessoa_fisica = c.id_pessoa_fisica LEFT OUTER JOIN pessoa_juridica j ON j.id_pessoa_juridica = c.id_pessoa_juridica INNER JOIN pessoa p ON p.id_pessoa = c.id_pessoa INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN cidade i ON i.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = i.id_estado WHERE c.id_cliente = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaApelidoFisica(self, pesquisa):
        try:
            _sql = "SELECT c.id_cliente, t.descricao, p.nome_razao, p.sobrenome_fantasia, p.cpf_cnpj, p.rg_inscricao, f.expeditor, f.uf, f.aniversario, p.endereco, p.numero, p.complemento, p.bairro, i.nome, e.nome, i.cep, j.site, c.observacao, c.situacao FROM cliente c LEFT OUTER JOIN pessoa_fisica f ON f.id_pessoa_fisica = c.id_pessoa_fisica LEFT OUTER JOIN pessoa_juridica j ON j.id_pessoa_juridica = c.id_pessoa_juridica INNER JOIN pessoa p ON p.id_pessoa = c.id_pessoa INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN cidade i ON i.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = i.id_estado WHERE p.sobrenome_fantasia LIKE '%"+pesquisa+"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarNomeFisica(self, pesquisa):
        try:
            _sql = "SELECT c.id_cliente, t.descricao, p.nome_razao, p.sobrenome_fantasia, p.cpf_cnpj, p.rg_inscricao, f.expeditor, f.uf, f.aniversario, p.endereco, p.numero, p.complemento, p.bairro, i.nome, e.nome, i.cep, j.site, c.observacao, c.situacao FROM cliente c LEFT OUTER JOIN pessoa_fisica f ON f.id_pessoa_fisica = c.id_pessoa_fisica LEFT OUTER JOIN pessoa_juridica j ON j.id_pessoa_juridica = c.id_pessoa_juridica INNER JOIN pessoa p ON p.id_pessoa = c.id_pessoa INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN cidade i ON i.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = i.id_estado WHERE p.nome_razao LIKE '%"+pesquisa+"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaCpfFisica(self, pesquisa):
        try:
            _sql = "SELECT c.id_cliente, t.descricao, p.nome_razao, p.sobrenome_fantasia, p.cpf_cnpj, p.rg_inscricao, f.expeditor, f.uf, f.aniversario, p.endereco, p.numero, p.complemento, p.bairro, i.nome, e.nome, i.cep, j.site, c.observacao, c.situacao FROM cliente c LEFT OUTER JOIN pessoa_fisica f ON f.id_pessoa_fisica = c.id_pessoa_fisica LEFT OUTER JOIN pessoa_juridica j ON j.id_pessoa_juridica = c.id_pessoa_juridica INNER JOIN pessoa p ON p.id_pessoa = c.id_pessoa INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN cidade i ON i.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = i.id_estado WHERE p.cpf_cnpj = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaRgFisica(self, pesquisa):
        try:
            _sql = "SELECT c.id_cliente, t.descricao, p.nome_razao, p.sobrenome_fantasia, p.cpf_cnpj, p.rg_inscricao, f.expeditor, f.uf, f.aniversario, p.endereco, p.numero, p.complemento, p.bairro, i.nome, e.nome, i.cep, j.site, c.observacao, c.situacao FROM cliente c LEFT OUTER JOIN pessoa_fisica f ON f.id_pessoa_fisica = c.id_pessoa_fisica LEFT OUTER JOIN pessoa_juridica j ON j.id_pessoa_juridica = c.id_pessoa_juridica INNER JOIN pessoa p ON p.id_pessoa = c.id_pessoa INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN cidade i ON i.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = i.id_estado WHERE p.rg_inscricao = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarClienteIdFisico(self, cliente):
        try:
            _sql = "SELECT * FROM cliente e INNER JOIN pessoa p ON p.id_pessoa = e.id_pessoa INNER JOIN pessoa_fisica f ON p.id_pessoa = f.id_pessoa WHERE f.id_pessoa_fisica = '"+ cliente +"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarClienteIdJuridico(self, cliente):
        try:
            _sql = "SELECT * FROM cliente e INNER JOIN pessoa p ON p.id_pessoa = e.id_pessoa INNER JOIN pessoa_juridica j ON p.id_pessoa = j.id_pessoa WHERE j.id_pessoa_juridica = '"+ cliente +"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
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

    def pesquisarPessoaJur(self, pessoaFisica):
        try:
            _sql = "SELECT p.id_pessoa FROM pessoa_juridica j INNER JOIN pessoa p ON p.id_pessoa = j.id_pessoa WHERE j.id_pessoa_juridica = '"+pessoaFisica+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
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

    def pesquisarPessoaJuridica(self, pessoaJuridica):
        try:
            _sql = "SELECT p.cpf_cnpj, p.rg_inscricao, p.nome_razao, p.sobrenome_fantasia FROM pessoa_juridica j INNER JOIN pessoa p ON p.id_pessoa = J.id_pessoa WHERE j.id_pessoa_juridica = '"+pessoaJuridica+"'"
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

    def cadastrarTelefoneCliente(self, idTelefone, idPessoa):

        try:
            _sql = "INSERT INTO telefone_cliente (id_telefone, id_cliente) VALUES (%s, %s)"
            _valores = (idTelefone, idPessoa)

            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            #self.__cursor.close()

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

    def cadastrarEmailCliente(self, idEmail, idPessoa):

        try:
            _sql = "INSERT INTO email_cliente (id_email, id_cliente) VALUES (%s, %s)"
            _valores = (idEmail, idPessoa)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            #self.__cursor.close()

        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados  email")
            self.__conexao.conn.rollback()
            return False

    def pesquisarPessoaCodigo(self, cliente):
        try:
            _sql = "SELECT p.id_pessoa FROM cliente c INNER JOIN pessoa p ON p.id_pessoa = c.id_pessoa INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa WHERE c.id_cliente = '" + cliente + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarPessoaFisicaId(self, cliente):
        try:
            _sql = "SELECT f.id_pessoa_fisica FROM pessoa_fisica f INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa WHERE p.id_pessoa = '" + cliente + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarPessoaJuridicaId(self, cliente):
        try:
            _sql = "SELECT j.id_pessoa_juridica FROM pessoa_juridica j INNER JOIN pessoa p ON p.id_pessoa = j.id_pessoa INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa WHERE p.id_pessoa = '" + cliente + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaTelefone(self, pesquisa):
        try:
            _sql = "SELECT t.id_telefone, l.contato, l.telefone FROM telefone_cliente t INNER JOIN telefone l ON l.id_telefone = t.id_telefone INNER JOIN cliente c ON c.id_cliente = t.id_cliente WHERE t.id_cliente  = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaEmail(self, pesquisa):
        try:
            _sql = "SELECT t.id_email, l.contato, l.email FROM email_cliente t INNER JOIN email l ON l.id_email = t.id_email INNER JOIN cliente c ON c.id_cliente = t.id_cliente WHERE t.id_cliente  = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaTelefoneCliente(self, idTelefone, idCliente):
        try:
            _sql = "SELECT * FROM telefone_cliente t INNER JOIN telefone l ON l.id_telefone = t.id_telefone INNER JOIN cliente c ON c.id_cliente = t.id_cliente WHERE t.id_telefone = '"+idTelefone+"' AND  t.id_cliente = '"+idCliente+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaEmailCliente(self, idEmail, idCliente):
        try:
            _sql = "SELECT * FROM email_cliente t INNER JOIN email l ON l.id_email = t.id_email INNER JOIN cliente c ON c.id_cliente = t.id_cliente WHERE t.id_telefone = '"+idEmail+"' AND  t.id_cliente = '"+idCliente+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def deletarTelefone(self, idTelefone, idCliente):

        try:
            _sql = "DELETE FROM telefone_cliente WHERE id_telefone = %s AND id_cliente = %s"
            __valor = (idTelefone, idCliente)
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

    def deletarEmail(self, idEmail, idCliente):

        try:
            _sql = "DELETE FROM email_cliente WHERE id_email = %s AND id_cliente = %s"
            __valor = (idEmail, idCliente)
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

    def pesquisarClientesFisico(self, empresa):
        try:
            _sql = "SELECT * FROM pessoa p INNER JOIN pessoa_fisica j ON j.id_pessoa = p.id_pessoa INNER JOIN cliente e ON e.id_pessoa_fisica = j.id_pessoa_fisica INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE  t.descricao = 'PESSOA FISÍCA' AND e.id_pessoa_fisica = '"+ empresa +"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarClientesJuridico(self, empresa):
        try:
            _sql = "SELECT * FROM pessoa p INNER JOIN pessoa_juridica j ON j.id_pessoa = p.id_pessoa INNER JOIN cliente e ON e.id_pessoa_juridica = j.id_pessoa_juridica INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE  t.descricao = 'PESSOA JURIDICA' AND e.id_pessoa_juridica = '"+ empresa +"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarTabelaCarreg(self, carrega):
        try:
            _sql = "SELECT * FROM entrada_veiculo_carregamento c INNER JOIN cliente l ON l.id_cliente = c.id_cliente WHERE c.id_cliente = '"+ carrega +"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False