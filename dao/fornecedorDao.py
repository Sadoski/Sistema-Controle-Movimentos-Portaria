import sys
import time
import datetime
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mysql.connector import Error
from conexao.conexao import ConexaoDb, mysql


class FornecedorDao(object):
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

    def pesquisarFornecedorIdFisico(self, fornecedor):
        try:
            _sql = "SELECT * FROM fornecedor e INNER JOIN pessoa p ON p.id_pessoa = e.id_pessoa INNER JOIN pessoa_fisica f ON p.id_pessoa = f.id_pessoa WHERE f.id_pessoa_fisica = '"+ fornecedor +"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarFornecedorIdJuridico(self, fornecedor):
        try:
            _sql = "SELECT * FROM fornecedor e INNER JOIN pessoa p ON p.id_pessoa = e.id_pessoa INNER JOIN pessoa_juridica j ON p.id_pessoa = j.id_pessoa WHERE j.id_pessoa_juridica = '"+ fornecedor +"'"
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

    def cadastrarTelefoneFornecedor(self, idTelefone, idPessoa):

        try:
            _sql = "INSERT INTO telefone_fornecedor (id_telefone, id_fornecedor) VALUES (%s, %s)"
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

    def cadastrarEmailFornecedor(self, idEmail, idPessoa):

        try:
            _sql = "INSERT INTO email_fornecedor (id_email, id_fornecedor) VALUES (%s, %s)"
            _valores = (idEmail, idPessoa)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            #self.__cursor.close()

        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados  email")
            self.__conexao.conn.rollback()
            return False

    def cadastrarFornecedorFisico(self, fornecedor):
        try:
            _sql = "INSERT INTO fornecedor (id_pessoa, id_pessoa_fisica, situacao, observacao, cadastrado) VALUES (%s, %s, %s, %s, %s)"
            _valores = (fornecedor.getIdPessoa, fornecedor.getIdPessoaFisica, fornecedor.getSituacao, fornecedor.getObservacao, self.__dataHora)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            # self.__cursor.close()
            QMessageBox.information(QWidget(), 'Mensagem', "Cadastro realizado com sucesso!")

        except mysql.connector.Error as e:
            QMessageBox.warning(QWidget(), 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False

    def cadastrarFornecedorJuridica(self, fornecedor):
        try:
            _sql = "INSERT INTO fornecedor(id_pessoa, id_pessoa_juridica, situacao, observacao, cadastrado) VALUES (%s, %s, %s, %s, %s)"
            _valores = (fornecedor.getIdPessoa, fornecedor.getIdPessoaJuridica, fornecedor.getSituacao, fornecedor.getObservacao, self.__dataHora)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            # self.__cursor.close()
            QMessageBox.information(QWidget(), 'Mensagem', "Cadastro realizado com sucesso!")

        except mysql.connector.Error as e:
            QMessageBox.warning(QWidget(), 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False

    def atualizarFornecedor(self, fornecedor):

        try:
            __sql = "UPDATE fornecedor SET observacao = %s, situacao = %s WHERE id_fornecedor = %s"
            _valores = (fornecedor.getObservacao, fornecedor.getSituacao, fornecedor.getIdFornecedor)
            self.__cursor.execute(__sql, _valores)
            self.__conexao.conn.commit()
            # self.__cursor.close()
            QMessageBox.information(QWidget(), 'Erro', "Cadastro atualizar com sucesso")
        except mysql.connector.Error as e:
            QMessageBox.warning(QWidget(), 'Erro', "Erro ao atualizar as informações no banco de dados")
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

    def pesquisarPessoaJur(self, pessoaFisica):
        try:
            _sql = "SELECT p.id_pessoa FROM pessoa_juridica j INNER JOIN pessoa p ON p.id_pessoa = j.id_pessoa WHERE j.id_pessoa_juridica = '"+pessoaFisica+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def deletarFornecedor(self, fornecedor):
        try:
            __sql = "DELETE FROM fornecedor WHERE id_fornecedor = '" + fornecedor + "'"
            self.__cursor.execute(__sql)
            self.__conexao.conn.commit()
            # self.__cursor.close()
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao deletar as informações no banco de dados")
            self.__conexao.conn.rollback()
            return False

    def pesquisaCodigo(self, pesquisa):
        try:
            _sql = " SELECT f.id_fornecedor, f.fantasia, f.razao_social, f.cnpj, f.inscricao_estadual, f.endereco, f.numero_endereco, f.complemento, f.bairro, f.telefone, f.site, f.email, c.cep, c.nome, s.nome, e.id_empresa, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual FROM fornecedor f INNER JOIN cidade c ON c.id_cidade = f.id_cidades INNER JOIN estado s ON s.id_estado = c.id_estado INNER JOIN empresa e ON e.id_empresa = f.id_empresa WHERE f.id_fornecedor = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaFantasia(self, pesquisa):
        try:
            _sql = " SELECT f.id_fornecedor, f.fantasia, f.razao_social, f.cnpj, f.inscricao_estadual, f.endereco, f.numero_endereco, f.complemento, f.bairro, f.telefone, f.site, f.email, c.cep, c.nome, s.nome, e.id_empresa, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual FROM fornecedor f INNER JOIN cidade c ON c.id_cidade = f.id_cidades INNER JOIN estado s ON s.id_estado = c.id_estado INNER JOIN empresa e ON e.id_empresa = f.id_empresa WHERE f.fantasia LIKE '%"+pesquisa+"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaRazaoSocial(self, pesquisa):
        try:
            _sql = " SELECT f.id_fornecedor, f.fantasia, f.razao_social, f.cnpj, f.inscricao_estadual, f.endereco, f.numero_endereco, f.complemento, f.bairro, f.telefone, f.site, f.email, c.cep, c.nome, s.nome, e.id_empresa, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual FROM fornecedor f INNER JOIN cidade c ON c.id_cidade = f.id_cidades INNER JOIN estado s ON s.id_estado = c.id_estado INNER JOIN empresa e ON e.id_empresa = f.id_empresa WHERE f.razao_social LIKE '%"+pesquisa+"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaCnpj(self, pesquisa):
        try:
            _sql = " SELECT f.id_fornecedor, f.fantasia, f.razao_social, f.cnpj, f.inscricao_estadual, f.endereco, f.numero_endereco, f.complemento, f.bairro, f.telefone, f.site, f.email, c.cep, c.nome, s.nome, e.id_empresa, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual FROM fornecedor f INNER JOIN cidade c ON c.id_cidade = f.id_cidades INNER JOIN estado s ON s.id_estado = c.id_estado INNER JOIN empresa e ON e.id_empresa = f.id_empresa WHERE f.cnpj = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaInscEstadual(self, pesquisa):
        try:
            _sql = " SELECT f.id_fornecedor, f.fantasia, f.razao_social, f.cnpj, f.inscricao_estadual, f.endereco, f.numero_endereco, f.complemento, f.bairro, f.telefone, f.site, f.email, c.cep, c.nome, s.nome, e.id_empresa, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual FROM fornecedor f INNER JOIN cidade c ON c.id_cidade = f.id_cidades INNER JOIN estado s ON s.id_estado = c.id_estado INNER JOIN empresa e ON e.id_empresa = f.id_empresa WHERE f.inscricao_estadual = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaCodigoFisica(self, pesquisa):
        try:
            _sql = "SELECT c.id_fornecedor, t.descricao, p.nome_razao, p.sobrenome_fantasia, p.cpf_cnpj, p.rg_inscricao, f.expeditor, f.uf, f.aniversario, p.endereco, p.numero, p.complemento, p.bairro, i.nome, e.nome, i.cep, j.site, c.observacao, c.situacao FROM fornecedor c LEFT OUTER JOIN pessoa_fisica f ON f.id_pessoa_fisica = c.id_pessoa_fisica LEFT OUTER JOIN pessoa_juridica j ON j.id_pessoa_juridica = c.id_pessoa_juridica INNER JOIN pessoa p ON p.id_pessoa = c.id_pessoa INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN cidade i ON i.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = i.id_estado WHERE c.id_fornecedor  = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaApelidoFisica(self, pesquisa):
        try:
            _sql = "SELECT c.id_fornecedor, t.descricao, p.nome_razao, p.sobrenome_fantasia, p.cpf_cnpj, p.rg_inscricao, f.expeditor, f.uf, f.aniversario, p.endereco, p.numero, p.complemento, p.bairro, i.nome, e.nome, i.cep, j.site, c.observacao, c.situacao FROM fornecedor c LEFT OUTER JOIN pessoa_fisica f ON f.id_pessoa_fisica = c.id_pessoa_fisica LEFT OUTER JOIN pessoa_juridica j ON j.id_pessoa_juridica = c.id_pessoa_juridica INNER JOIN pessoa p ON p.id_pessoa = c.id_pessoa INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN cidade i ON i.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = i.id_estado WHERE p.sobrenome_fantasia LIKE '%"+pesquisa+"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarNomeFisica(self, pesquisa):
        try:
            _sql = "SELECT c.id_fornecedor, t.descricao, p.nome_razao, p.sobrenome_fantasia, p.cpf_cnpj, p.rg_inscricao, f.expeditor, f.uf, f.aniversario, p.endereco, p.numero, p.complemento, p.bairro, i.nome, e.nome, i.cep, j.site, c.observacao, c.situacao FROM fornecedor c LEFT OUTER JOIN pessoa_fisica f ON f.id_pessoa_fisica = c.id_pessoa_fisica LEFT OUTER JOIN pessoa_juridica j ON j.id_pessoa_juridica = c.id_pessoa_juridica INNER JOIN pessoa p ON p.id_pessoa = c.id_pessoa INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN cidade i ON i.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = i.id_estado WHERE p.nome_razao LIKE '%"+pesquisa+"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaCpfFisica(self, pesquisa):
        try:
            _sql = "SELECT c.id_fornecedor, t.descricao, p.nome_razao, p.sobrenome_fantasia, p.cpf_cnpj, p.rg_inscricao, f.expeditor, f.uf, f.aniversario, p.endereco, p.numero, p.complemento, p.bairro, i.nome, e.nome, i.cep, j.site, c.observacao, c.situacao FROM fornecedor c LEFT OUTER JOIN pessoa_fisica f ON f.id_pessoa_fisica = c.id_pessoa_fisica LEFT OUTER JOIN pessoa_juridica j ON j.id_pessoa_juridica = c.id_pessoa_juridica INNER JOIN pessoa p ON p.id_pessoa = c.id_pessoa INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN cidade i ON i.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = i.id_estado WHERE p.cpf_cnpj = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaRgFisica(self, pesquisa):
        try:
            _sql = "SELECT c.id_fornecedor, t.descricao, p.nome_razao, p.sobrenome_fantasia, p.cpf_cnpj, p.rg_inscricao, f.expeditor, f.uf, f.aniversario, p.endereco, p.numero, p.complemento, p.bairro, i.nome, e.nome, i.cep, j.site, c.observacao, c.situacao FROM fornecedor c LEFT OUTER JOIN pessoa_fisica f ON f.id_pessoa_fisica = c.id_pessoa_fisica LEFT OUTER JOIN pessoa_juridica j ON j.id_pessoa_juridica = c.id_pessoa_juridica INNER JOIN pessoa p ON p.id_pessoa = c.id_pessoa INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN cidade i ON i.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = i.id_estado WHERE p.rg_inscricao = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarPessoaCodigo(self, fornecedor):
        try:
            _sql = "SELECT p.id_pessoa FROM fornecedor c INNER JOIN pessoa p ON p.id_pessoa = c.id_pessoa INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa WHERE c.id_fornecedor = '" + fornecedor + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarPessoaFisicaId(self, fornecedor):
        try:
            _sql = "SELECT f.id_pessoa_fisica FROM pessoa_fisica f INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa WHERE p.id_pessoa = '" + fornecedor + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarPessoaJuridicaId(self, fornecedor):
        try:
            _sql = "SELECT j.id_pessoa_juridica FROM pessoa_juridica j INNER JOIN pessoa p ON p.id_pessoa = j.id_pessoa INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa WHERE p.id_pessoa = '" + fornecedor + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaTelefone(self, pesquisa):
        try:
            _sql = "SELECT t.id_telefone, l.contato, l.telefone FROM telefone_fornecedor t INNER JOIN telefone l ON l.id_telefone = t.id_telefone INNER JOIN fornecedor c ON c.id_fornecedor = t.id_fornecedor WHERE t.id_fornecedor  = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaEmail(self, pesquisa):
        try:
            _sql = "SELECT t.id_email, l.contato, l.email FROM email_fornecedor t INNER JOIN email l ON l.id_email = t.id_email INNER JOIN fornecedor c ON c.id_fornecedor = t.id_fornecedor WHERE t.id_fornecedor  = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def deletarTelefone(self, idTelefone, idFornecedor):

        try:
            _sql = "DELETE FROM telefone_fornecedor WHERE id_telefone = %s AND id_fornecedor = %s"
            __valor = (idTelefone, idFornecedor)
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

    def deletarEmail(self, idEmail, idFornecedor):

        try:
            _sql = "DELETE FROM email_fornecedor WHERE id_email = %s AND id_fornecedor = %s"
            __valor = (idEmail, idFornecedor)
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

    def pesquisaTelefoneFornecedor(self, idTelefone, idFornecedor):
        try:
            _sql = "SELECT * FROM telefone_cliente t INNER JOIN telefone l ON l.id_telefone = t.id_telefone INNER JOIN cliente c ON c.id_cliente = t.id_cliente WHERE t.id_telefone = '"+idTelefone+"' AND  t.id_cliente = '"+idFornecedor+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaEmailFornecedor(self, idEmail, idFornecedor):
        try:
            _sql = "SELECT * FROM email_cliente t INNER JOIN email l ON l.id_email = t.id_email INNER JOIN cliente c ON c.id_cliente = t.id_cliente WHERE t.id_telefone = '"+idEmail+"' AND  t.id_cliente = '"+idFornecedor+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarFornecedoresFisico(self, empresa):
        try:
            _sql = "SELECT * FROM pessoa p INNER JOIN pessoa_fisica j ON j.id_pessoa = p.id_pessoa INNER JOIN fornecedor e ON e.id_pessoa_fisica = j.id_pessoa_fisica INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE  t.descricao = 'PESSOA FISÍCA' AND e.id_pessoa_fisica = '" + empresa + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarFornecedoresJuridico(self, empresa):
        try:
            _sql = "SELECT * FROM pessoa p INNER JOIN pessoa_juridica j ON j.id_pessoa = p.id_pessoa INNER JOIN fornecedor e ON e.id_pessoa_juridica = j.id_pessoa_juridica INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE  t.descricao = 'PESSOA JURIDICA' AND e.id_pessoa_juridica = '" + empresa + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarTabelaDesca(self, fornecedor):
        try:
            _sql = "SELECT * FROM entrada_veiculo_descarregamento d INNER JOIN fornecedor f ON f.id_fornecedor = d.id_fornecedor WHERE d.id_fornecedor = '" + str(fornecedor) + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarTabelaNf(self, fornecedor):
        try:
            _sql = "SELECT * FROM notas_fiscais WHERE id_fornecedor = '" + str(fornecedor) + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False