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


class EmpresaDao(object):
    def __init__(self):
        self.__conexao = ConexaoDb()
        self.__cursor = self.__conexao.conn.cursor()
        self.__ts = time.time()
        self.__dataHora = datetime.datetime.fromtimestamp(self.__ts).strftime('%Y-%m-%d %H:%M:%S')

    def tipoEmpresa(self):
        try:
            __sql = "select descricao from tipo_empresa"
            self.__cursor.execute(__sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao pesquisar o tipo de empresa no banco de dados ")
            return False

    def idTipoEmpresa(self, descricao):
        try:
            _sql = "select id_tipo_empresa from tipo_empresa where descricao = '"+descricao+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            return result
            #self.__cursor.close()
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao pesquisar o tipo de empresa no banco de dados ")
            return False

    def pesquisarEmpresaId(self, empresa):
        try:
            _sql = "SELECT * FROM pessoa p INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN pessoa_juridica j ON j.id_pessoa = p.id_pessoa  INNER JOIN empresa m ON m.id_pessoa_juridica = j.id_pessoa_juridica INNER JOIN endereco_pessoa e ON e.id_pessoa = p.id_pessoa INNER JOIN cidade c ON c.id_cidade = e.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE  t.descricao = 'PESSOA JURIDICA' AND p.id_pessoa = '"+ empresa +"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarPessoaJuridica(self, pessoaJuridica):
        try:
            _sql = "SELECT p.cpf_cnpj, p.rg_inscricao, p.nome_razao, p.sobrenome_fantasia FROM pessoa p INNER JOIN pessoa_juridica j ON j.id_pessoa = p.id_pessoa INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE  t.descricao = 'PESSOA JURIDICA' AND p.id_pessoa = '"+ pessoaJuridica +"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarEmpresaCodigo(self, empresa):
        try:
            _sql = "SELECT m.id_empresa FROM pessoa p INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN pessoa_juridica j ON j.id_pessoa = p.id_pessoa INNER JOIN empresa m ON m.id_pessoa_juridica = j.id_pessoa_juridica INNER JOIN endereco_pessoa e ON e.id_pessoa = p.id_pessoa INNER JOIN cidade c ON c.id_cidade = e.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE  t.descricao = 'PESSOA JURIDICA' AND p.id_pessoa  '"+ empresa +"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarPessoaJuridicaId(self, empresa):
        try:
            _sql = "SELECT j.id_pessoa_juridica FROM pessoa p INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN pessoa_juridica j ON j.id_pessoa = p.id_pessoa INNER JOIN endereco_pessoa e ON e.id_pessoa = p.id_pessoa INNER JOIN cidade c ON c.id_cidade = e.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE  t.descricao = 'PESSOA JURIDICA' AND p.id_pessoa  = '"+empresa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def ultimoRegistro(self):
        try:
            _sql = "SELECT LAST_INSERT_ID()"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()

            return result

        except BaseException as os:
            return False

    def cadastroEmpresa(self, empresa):

        try:
            _sql = "INSERT INTO empresa (id_pessoa_juridica, inscricao_municipal, cadastrado, id_tipo_empresa, situacao) VALUES (%s, %s, %s, %s, %s)"
            _valores = (empresa.getIdPessoaJuridica, empresa.getInscricaoMunicipal, self.__dataHora, empresa.getTipoEmpresa, empresa.getSituacao)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            #self.__cursor.close()
            return True
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados empresa")
            self.__conexao.conn.rollback()
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

    def cadastrarTelefoneEmpresa(self, idTelefone, idEmpresa):

        try:
            _sql = "INSERT INTO telefone_empresa (id_telefone, id_empresa) VALUES (%s, %s)"
            _valores = (idTelefone, idEmpresa)
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

    def cadastrarEmailEmpresa(self, idEmail, idEmpresa):

        try:
            _sql = "INSERT INTO email_empresa (id_email, id_empresa) VALUES (%s, %s)"
            _valores = (idEmail, idEmpresa)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            #self.__cursor.close()

        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados  email")
            self.__conexao.conn.rollback()
            return False

    def cadastrarSetor(self, setores):

        try:
            _sql = "INSERT INTO setores (descricao, id_empresa, cadastrado) VALUES (%s, %s, %s)"
            _valores = (setores.getSetor, setores.getIdEmpresa, self.__dataHora)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            #self.__cursor.close()

        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados setor ")
            self.__conexao.conn.rollback()
            return False

    def cadastrarCargo(self, setores):

        try:
            _sql = "INSERT INTO cargo (descricao, id_empresa, cadastrado) VALUES (%s, %s, %s)"
            _valores = (setores.getCargo, setores.getIdEmpresa, self.__dataHora)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            #self.__cursor.close()

        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados cargo")
            self.__conexao.conn.rollback()
            return False

    def atualizarEmpresa(self, empresa):

        try:
            __sql = "UPDATE empresa SET inscricao_municipal = %s, atualizado = %s, id_tipo_empresa = %s, situacao = %s where id_empresa = %s"
            _valores = (empresa.getInscricaoMunicipal, self.__dataHora, empresa.getTipoEmpresa, empresa.getSituacao, empresa.getIdEmpresa)
            self.__cursor.execute(__sql, _valores)
            self.__conexao.conn.commit()
            #self.__cursor.close()
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao atualizar as informações no banco de dados")
            self.__conexao.conn.rollback()
            return False


    def deletarTelefone(self, idTelefone, idEmpresa):

        try:
            _sql = "DELETE FROM telefone_empresa WHERE id_telefone = %s AND id_empresa = %s"
            __valor = (idTelefone, idEmpresa)
            self.__cursor.execute(_sql, __valor)
            self.__conexao.conn.commit()
            #self.__cursor.close()

        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False

    def deletarContatoTelefone(self, idTelefone, idEmpresa):

        try:
            _sql = "DELETE FROM telefone WHERE id_telefone = '"+idTelefone+"'"
            self.__cursor.execute(_sql)
            self.__conexao.conn.commit()
            #self.__cursor.close()

        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False

    def deletarEmail(self, idEmail, idEmpresa):

        try:
            _sql = "DELETE FROM email_empresa WHERE id_email = %s AND id_empresa = %s"
            __valor = (idEmail, idEmpresa)
            self.__cursor.execute(_sql, __valor)
            self.__conexao.conn.commit()
            #self.__cursor.close()

        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados email ")
            self.__conexao.conn.rollback()
            return False

    def deletarContatoEmail(self, idEmail):

        try:
            _sql = "DELETE FROM email WHERE id_email = '"+idEmail+"'"
            self.__cursor.execute(_sql)
            self.__conexao.conn.commit()
            #self.__cursor.close()

        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados email ")
            self.__conexao.conn.rollback()
            return False

    def deletarSetor(self, idSetor, idEmpresa):

        try:
            _sql = "DELETE FROM setores WHERE  id_setor = '"+idSetor+"' AND id_empresa = '"+idEmpresa+"'"
            self.__cursor.execute(_sql)
            self.__conexao.conn.commit()
            #self.__cursor.close()

        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados setor ")
            self.__conexao.conn.rollback()
            return False

    def deletarCargo(self, idCargo, idEmpresa):

        try:
            _sql = "DELETE FROM cargo WHERE id_Cargo = '"+idCargo+"' AND id_empresa = '"+idEmpresa+"'"
            self.__cursor.execute(_sql)
            self.__conexao.conn.commit()
            #self.__cursor.close()

        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados cargo")
            self.__conexao.conn.rollback()
            return False


    def deletarEmpresa(self, empresa):
        try:
            __sql = "DELETE FROM empresa WHERE id_empresa = '"+empresa+"'"
            self.__cursor.execute(__sql)
            self.__conexao.conn.commit()
            #self.__cursor.close()
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao deletar as informações no banco de dados")
            self.__conexao.conn.rollback()
            return False


    def pesquisarCidades(self, cep):
        _sql = "SELECT c.id_cidade, c.nome, e.nome from cidade c inner join estado e e.id_estado = c.id_estado where c.cep = '"+cep+"'"
        try:
            lista = []
            cursor = self.__cursor.execute(_sql)
            for (id, nome, estado) in cursor:
                novo = Cidades(id, nome, estado)
                lista.append(novo)
            self.__conexao.conn.close()
        except BaseException as os:
            return False

        return lista

    def pesquisaCodigo(self, pesquisa):
        try:
            _sql = "SELECT p.id_pessoa, p.nome_razao, p.sobrenome_fantasia, p.cpf_cnpj, p.rg_inscricao, p.endereco, p.numero, p.complemento, p.bairro, c.nome, s.nome, c.cep, j.site FROM  pessoa p INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN pessoa_juridica j ON j.id_pessoa = p.id_pessoa INNER JOIN empresa m ON m.id_pessoa_juridica = j.id_pessoa_juridica INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE  t.descricao = 'PESSOA JURIDICA' AND p.id_pessoa = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaFantasia(self, pesquisa):
        try:
            _sql = "SELECT p.id_pessoa, p.nome_razao, p.sobrenome_fantasia, p.cpf_cnpj, p.rg_inscricao, p.endereco, p.numero, p.complemento, p.bairro, c.nome, s.nome, c.cep, j.site FROM  pessoa p INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN pessoa_juridica j ON j.id_pessoa = p.id_pessoa INNER JOIN empresa m ON m.id_pessoa_juridica = j.id_pessoa_juridica INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE  t.descricao = 'PESSOA JURIDICA' AND p.fantasia LIKE '%"+pesquisa+"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaRazaoSocial(self, pesquisa):
        try:

            _sql = "SELECT p.id_pessoa, p.nome_razao, p.sobrenome_fantasia, p.cpf_cnpj, p.rg_inscricao, p.endereco, p.numero, p.complemento, p.bairro, c.nome, s.nome, c.cep, j.site FROM  pessoa p INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN pessoa_juridica j ON j.id_pessoa = p.id_pessoa INNER JOIN empresa m ON m.id_pessoa_juridica = j.id_pessoa_juridica INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE  t.descricao = 'PESSOA JURIDICA' AND p.nome_razao LIKE '%"+pesquisa+"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaCnpj(self, pesquisa):
        try:
            _sql = "SELECT p.id_pessoa, p.nome_razao, p.sobrenome_fantasia, p.cpf_cnpj, p.rg_inscricao, p.endereco, p.numero, p.complemento, p.bairro, c.nome, s.nome, c.cep, j.site FROM  pessoa p INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN pessoa_juridica j ON j.id_pessoa = p.id_pessoa INNER JOIN empresa m ON m.id_pessoa_juridica = j.id_pessoa_juridica INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE  t.descricao = 'PESSOA JURIDICA' AND p.cpf_cnpj = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaInscEstadual(self, pesquisa):
        try:
            _sql = "SELECT p.id_pessoa, p.nome_razao, p.sobrenome_fantasia, p.cpf_cnpj, p.rg_inscricao, p.endereco, p.numero, p.complemento, p.bairro, c.nome, s.nome, c.cep, j.site FROM  pessoa p INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN pessoa_juridica j ON j.id_pessoa = p.id_pessoa INNER JOIN empresa m ON m.id_pessoa_juridica = j.id_pessoa_juridica INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE  t.descricao = 'PESSOA JURIDICA' AND p.rg_inscricao = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaInscMunicipal(self, pesquisa):
        try:
            _sql = "SELECT p.id_pessoa, p.nome_razao, p.sobrenome_fantasia, p.cpf_cnpj, p.rg_inscricao, p.endereco, p.numero, p.complemento, p.bairro, c.nome, s.nome, c.cep, j.site FROM  pessoa p INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN pessoa_juridica j ON j.id_pessoa = p.id_pessoa INNER JOIN empresa m ON m.id_pessoa_juridica = j.id_pessoa_juridica INNER JOIN tipo_empresa i ON i.id_tipo_empresa = m.id_tipo_empresa INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE  t.descricao = 'PESSOA JURIDICA' AND m.inscricao_municipal = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaEmpresa(self, pesquisa):
        try:
            _sql = "SELECT m.id_empresa, p.nome_razao, p.cpf_cnpj, p.rg_inscricao FROM  pessoa p INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN pessoa_juridica j ON j.id_pessoa = p.id_pessoa INNER JOIN empresa m ON m.id_pessoa_juridica = j.id_pessoa_juridica INNER JOIN tipo_empresa i ON i.id_tipo_empresa = m.id_tipo_empresa INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE  t.descricao = 'PESSOA JURIDICA' AND p.sobrenome_fantasia  = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaEmpresaSetCar(self, pesquisa):
        try:
            _sql = "SELECT m.id_empresa, p.nome_razao, t.descricao, p.cpf_cnpj, p.rg_inscricao FROM  pessoa p INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN pessoa_juridica j ON j.id_pessoa = p.id_pessoa INNER JOIN empresa m ON m.id_pessoa_juridica = j.id_pessoa_juridica INNER JOIN tipo_empresa i ON i.id_tipo_empresa = m.id_tipo_empresa INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE  t.descricao = 'PESSOA JURIDICA' AND p.sobrenome_fantasia  = '"+pesquisa+"'"
            _sql = "SELECT e.id_empresa, e.razao_social, t.descricao,  e.cnpj, e.inscricao_estadual from empresa e INNER JOIN tipo_empresa t on t.id_tipo_empresa = e.id_tipo_empresa where  fantasia = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def confirmarEmpresa(self, setorCargo):
        try:
            _sql = "SELECT id_empresa FROM  pessoa p INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN pessoa_juridica j ON j.id_pessoa = p.id_pessoa INNER JOIN empresa m ON m.id_pessoa_juridica = j.id_pessoa_juridica INNER JOIN tipo_empresa i ON i.id_tipo_empresa = m.id_tipo_empresa INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado s ON s.id_estado = c.id_estado WHERE  p.sobrenome_fantasia = %s AND p.nome_razao = %s AND p.cpf_cnpj = %s AND p.rg_inscricao = %s AND m.id_empresa = %s"
            _valores = (setorCargo.getFantasia, setorCargo.getRazaoSocial, setorCargo.getCnpj, setorCargo.getInscricao, setorCargo.getIdEmpresa)
            self.__cursor.execute(_sql, _valores)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaTelefone(self, pesquisa):
        try:
            _sql = "SELECT t.id_telefone, l.contato, l.telefone FROM telefone_empresa t INNER JOIN telefone l ON l.id_telefone = t.id_telefone INNER JOIN empresa e ON e.id_empresa = t.id_empresa WHERE t.id_empresa = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaTelefoneEmpresa(self, idTelefone, idEmpresa):
        try:
            _sql = "SELECT * FROM telefone_empresa t INNER JOIN telefone l ON l.id_telefone = t.id_telefone INNER JOIN empresa e ON e.id_empresa = t.id_empresa WHERE t.id_telefone = '"+idTelefone+"' AND  t.id_empresa = '"+idEmpresa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaEmail(self, pesquisa):
        try:
            _sql = "SELECT t.id_email, l.contato, l.email FROM email_empresa t INNER JOIN email l ON l.id_email = t.id_email INNER JOIN empresa e ON e.id_empresa = t.id_empresa WHERE t.id_empresa = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaEmailEmpresa(self, idEmail, idEmpresa):
        try:
            _sql = "SELECT * FROM email_empresa t INNER JOIN email l ON l.id_email = t.id_email INNER JOIN empresa e ON e.id_empresa = t.id_empresa WHERE t.id_telefone = '"+idEmail+"' AND  t.id_empresa = '"+idEmpresa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaSetor(self, pesquisa):
        try:
            _sql = "SELECT l.id_setores, l.descricao FROM  setores l INNER JOIN empresa e ON e.id_empresa = l.id_empresa WHERE l.id_empresa = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaCargo(self, pesquisa):
        try:
            _sql = "SELECT l.id_cargo, l.descricao FROM  cargo l INNER JOIN empresa e ON e.id_empresa = l.id_empresa WHERE l.id_empresa = '" + pesquisa + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False