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
            _sql = "INSERT INTO telefone_funcionario (id_telefone, id_funcionario) VALUES (%s, %s)"
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
            _sql = "INSERT INTO email_funcionario (id_email, id_funcionario) VALUES (%s, %s)"
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
            _sql = "INSERT INTO funcionario (id_pessoa_fisica, situacao, observacao, data_demissao, data_admissao, num_carteira, serie, uf, data_emissao, pis_pasep, id_civil, id_deficiencia, id_categoria_trabalho, id_setores, id_cargo, id_jornada_trabalho, cadastrado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            _valores = (funcionario.getIdPessoaFisica, funcionario.getSituacao, funcionario.getObservacao, funcionario.getDemissao, funcionario.getAdmissao, funcionario.getNumCarteira,  funcionario.setSerie, funcionario.getUf, funcionario.getEmissao, funcionario.getPis, funcionario.getCivil, funcionario.getDeficiencia, funcionario.getCategoria, funcionario.getSetor, funcionario.getCargo, funcionario.getJornada, self.__dataHora)

            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            # self.__cursor.close()
            QMessageBox.information(QWidget(), 'Mensagem', "Cadastro realizado com sucesso!")

        except mysql.connector.Error as e:
            QMessageBox.warning(QWidget(), 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False

    def cadastrarHorarios(self, semana, inicio, iniIntervalo, fimIntervalo, termino, jornada, idFuncionario):
        try:
            _sql = "INSERT INTO horario_jornada (dia, hora_entrada, hora_ini_intervalo, hora_fim_intervalo, hora_saida, id_jornada_trabalho, id_funcionario) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            _valores = (semana, inicio, iniIntervalo, fimIntervalo, termino, jornada, idFuncionario)
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            # self.__cursor.close()
        except mysql.connector.Error as e:
            QMessageBox.warning(QWidget(), 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False

    def pesquisarFuncionarioCodigo(self, funcionario):
        try:
            _sql = "SELECT f.id_funcionario, p.nome_razao, p.sobrenome_fantasia, p.cpf_cnpj, p.rg_inscricao, s.expeditor, s.uf, s.aniversario, g.sexo, p.endereco, p.numero, p.complemento, p.bairro, s.mae, s.pai, c.nome, e.nome, c.cep, f.data_admissao, f.data_demissao, f.num_carteira, f.serie, f.uf, f.data_emissao, f.pis_pasep, i.descricao, d.descricao, r.descricao, t.descricao,  o.descricao, f.observacao, b.descricao, f.situacao  FROM funcionario f INNER JOIN civil i ON i.id_civil = f.id_civil INNER JOIN deficiencia d ON d.id_deficiencia = f.id_deficiencia INNER JOIN categoria_trabalho r ON r.id_categoria_trabalho = f.id_categoria_trabalho INNER JOIN setores t ON t.id_setores = f.id_setores INNER JOIN cargo o ON o.id_cargo = f.id_cargo INNER JOIN jornada_trabalho b ON b.id_jornada_trabalho = f.id_jornada_trabalho INNER JOIN pessoa_fisica s ON s.id_pessoa_fisica = f.id_pessoa_fisica INNER JOIN genero g ON g.id_genero = s.id_genero INNER JOIN pessoa p ON p.id_pessoa = s.id_pessoa INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado  WHERE f.id_funcionario = '"+ funcionario +"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False


    def pesquisarFuncionarioNome(self, funcionario):
        try:
            _sql = "SELECT f.id_funcionario, p.nome_razao, p.sobrenome_fantasia, p.cpf_cnpj, p.rg_inscricao, s.expeditor, s.uf, s.aniversario, g.sexo, p.endereco, p.numero, p.complemento, p.bairro, s.mae, s.pai, c.nome, e.nome, c.cep, f.data_admissao, f.data_demissao, f.num_carteira, f.serie, f.uf, f.data_emissao, f.pis_pasep, i.descricao, d.descricao, r.descricao, t.descricao,  o.descricao, f.observacao, b.descricao, f.situacao  FROM funcionario f INNER JOIN civil i ON i.id_civil = f.id_civil INNER JOIN deficiencia d ON d.id_deficiencia = f.id_deficiencia INNER JOIN categoria_trabalho r ON r.id_categoria_trabalho = f.id_categoria_trabalho INNER JOIN setores t ON t.id_setores = f.id_setores INNER JOIN cargo o ON o.id_cargo = f.id_cargo INNER JOIN jornada_trabalho b ON b.id_jornada_trabalho = f.id_jornada_trabalho INNER JOIN pessoa_fisica s ON s.id_pessoa_fisica = f.id_pessoa_fisica INNER JOIN genero g ON g.id_genero = s.id_genero INNER JOIN pessoa p ON p.id_pessoa = s.id_pessoa INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado  WHERE p.nome_razao LIKE '%"+ funcionario +"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarFuncionarioCPF(self, funcionario):
        try:
            _sql = "SELECT f.id_funcionario, p.nome_razao, p.sobrenome_fantasia, p.cpf_cnpj, p.rg_inscricao, s.expeditor, s.uf, s.aniversario, g.sexo, p.endereco, p.numero, p.complemento, p.bairro, s.mae, s.pai, c.nome, e.nome, c.cep, f.data_admissao, f.data_demissao, f.num_carteira, f.serie, f.uf, f.data_emissao, f.pis_pasep, i.descricao, d.descricao, r.descricao, t.descricao,  o.descricao, f.observacao, b.descricao, f.situacao  FROM funcionario f INNER JOIN civil i ON i.id_civil = f.id_civil INNER JOIN deficiencia d ON d.id_deficiencia = f.id_deficiencia INNER JOIN categoria_trabalho r ON r.id_categoria_trabalho = f.id_categoria_trabalho INNER JOIN setores t ON t.id_setores = f.id_setores INNER JOIN cargo o ON o.id_cargo = f.id_cargo INNER JOIN jornada_trabalho b ON b.id_jornada_trabalho = f.id_jornada_trabalho INNER JOIN pessoa_fisica s ON s.id_pessoa_fisica = f.id_pessoa_fisica INNER JOIN genero g ON g.id_genero = s.id_genero INNER JOIN pessoa p ON p.id_pessoa = s.id_pessoa INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado  WHERE p.cpf_cnpj = '"+ funcionario +"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False


    def pesquisarFuncionarioRg(self, funcionario):
        try:
            _sql = "SELECT f.id_funcionario, p.nome_razao, p.sobrenome_fantasia, p.cpf_cnpj, p.rg_inscricao, s.expeditor, s.uf, s.aniversario, g.sexo, p.endereco, p.numero, p.complemento, p.bairro, s.mae, s.pai, c.nome, e.nome, c.cep, f.data_admissao, f.data_demissao, f.num_carteira, f.serie, f.uf, f.data_emissao, f.pis_pasep, i.descricao, d.descricao, r.descricao, t.descricao,  o.descricao, f.observacao, b.descricao, f.situacao  FROM funcionario f INNER JOIN civil i ON i.id_civil = f.id_civil INNER JOIN deficiencia d ON d.id_deficiencia = f.id_deficiencia INNER JOIN categoria_trabalho r ON r.id_categoria_trabalho = f.id_categoria_trabalho INNER JOIN setores t ON t.id_setores = f.id_setores INNER JOIN cargo o ON o.id_cargo = f.id_cargo INNER JOIN jornada_trabalho b ON b.id_jornada_trabalho = f.id_jornada_trabalho INNER JOIN pessoa_fisica s ON s.id_pessoa_fisica = f.id_pessoa_fisica INNER JOIN genero g ON g.id_genero = s.id_genero INNER JOIN pessoa p ON p.id_pessoa = s.id_pessoa INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado  WHERE p.rg_inscricao = '"+ funcionario +"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarFuncionarioNumCarteira(self, funcionario):
        try:
            _sql = "SELECT f.id_funcionario, p.nome_razao, p.sobrenome_fantasia, p.cpf_cnpj, p.rg_inscricao, s.expeditor, s.uf, s.aniversario, g.sexo, p.endereco, p.numero, p.complemento, p.bairro, s.mae, s.pai, c.nome, e.nome, c.cep, f.data_admissao, f.data_demissao, f.num_carteira, f.serie, f.uf, f.data_emissao, f.pis_pasep, i.descricao, d.descricao, r.descricao, t.descricao,  o.descricao, f.observacao, b.descricao, f.situacao  FROM funcionario f INNER JOIN civil i ON i.id_civil = f.id_civil INNER JOIN deficiencia d ON d.id_deficiencia = f.id_deficiencia INNER JOIN categoria_trabalho r ON r.id_categoria_trabalho = f.id_categoria_trabalho INNER JOIN setores t ON t.id_setores = f.id_setores INNER JOIN cargo o ON o.id_cargo = f.id_cargo INNER JOIN jornada_trabalho b ON b.id_jornada_trabalho = f.id_jornada_trabalho INNER JOIN pessoa_fisica s ON s.id_pessoa_fisica = f.id_pessoa_fisica INNER JOIN genero g ON g.id_genero = s.id_genero INNER JOIN pessoa p ON p.id_pessoa = s.id_pessoa INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado  WHERE f.num_carteira = '"+ funcionario +"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarFuncionarioPis(self, funcionario):
        try:
            _sql = "SELECT f.id_funcionario, p.nome_razao, p.sobrenome_fantasia, p.cpf_cnpj, p.rg_inscricao, s.expeditor, s.uf, s.aniversario, g.sexo, p.endereco, p.numero, p.complemento, p.bairro, s.mae, s.pai, c.nome, e.nome, c.cep, f.data_admissao, f.data_demissao, f.num_carteira, f.serie, f.uf, f.data_emissao, f.pis_pasep, i.descricao, d.descricao, r.descricao, t.descricao,  o.descricao, f.observacao, b.descricao, f.situacao  FROM funcionario f INNER JOIN civil i ON i.id_civil = f.id_civil INNER JOIN deficiencia d ON d.id_deficiencia = f.id_deficiencia INNER JOIN categoria_trabalho r ON r.id_categoria_trabalho = f.id_categoria_trabalho INNER JOIN setores t ON t.id_setores = f.id_setores INNER JOIN cargo o ON o.id_cargo = f.id_cargo INNER JOIN jornada_trabalho b ON b.id_jornada_trabalho = f.id_jornada_trabalho INNER JOIN pessoa_fisica s ON s.id_pessoa_fisica = f.id_pessoa_fisica INNER JOIN genero g ON g.id_genero = s.id_genero INNER JOIN pessoa p ON p.id_pessoa = s.id_pessoa INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado  WHERE f.pis_pasep = '"+ funcionario +"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarPessoaCodigo(self, funcionario):
        try:
            _sql = "SELECT p.id_pessoa FROM funcionario f INNER JOIN civil v ON v.id_civil = f.id_civil INNER JOIN deficiencia d ON d.id_deficiencia = f.id_deficiencia INNER JOIN categoria_trabalho t ON t.id_categoria_trabalho = f.id_categoria_trabalho INNER JOIN setores s ON s.id_setores = f.id_setores INNER JOIN cargo g ON g.id_cargo = f.id_cargo INNER JOIN jornada_trabalho j ON j.id_jornada_trabalho = f.id_jornada_trabalho INNER JOIN pessoa_fisica i ON i.id_pessoa_fisica = f.id_pessoa_fisica INNER JOIN genero n ON n.id_genero = i.id_genero INNER JOIN pessoa p ON p.id_pessoa = i.id_pessoa INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado WHERE f.id_funcionario = '"+ funcionario +"'"
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
            _sql = "SELECT t.id_telefone, l.contato, l.telefone FROM telefone_funcionario t INNER JOIN telefone l ON l.id_telefone = t.id_telefone INNER JOIN funcionario c ON c.id_funcionario = t.id_funcionario WHERE t.id_funcionario = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaEmail(self, pesquisa):
        try:
            _sql = "SELECT t.id_email, l.contato, l.email FROM email_funcionario t INNER JOIN email l ON l.id_email = t.id_email INNER JOIN funcionario c ON c.id_funcionario = t.id_funcionario WHERE t.id_funcionario  = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaHorarios(self, pesquisa):
        try:
            _sql = "SELECT h.dia, h.hora_entrada, h.hora_ini_intervalo, h.hora_fim_intervalo, h.hora_saida FROM horario_jornada h INNER JOIN funcionario f ON f.id_funcionario = h.id_funcionario WHERE f.id_funcionario  = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def deletarFuncionario(self, funcionario):
        try:
            __sql = "DELETE FROM funcionario WHERE id_funcionario = '" + str(funcionario) + "'"
            self.__cursor.execute(__sql)
            self.__conexao.conn.commit()
            # self.__cursor.close()

            return True
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao deletar as informações no banco de dados")
            self.__conexao.conn.rollback()
            return False

    def deletarHorario(self, funcionario):
        try:
            __sql = "DELETE FROM horario_jornada WHERE id_funcionario = '" + str(funcionario) + "'"
            self.__cursor.execute(__sql)
            self.__conexao.conn.commit()
            # self.__cursor.close()

            return True
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

    def deletarTelefone(self, idTelefone, idCliente):

        try:
            _sql = "DELETE FROM telefone_funcionario WHERE id_telefone = %s AND id_funcionario = %s"
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
            _sql = "DELETE FROM email_funcionario WHERE id_email = %s AND id_funcionario = %s"
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

    def pesquisaTelefoneFuncionario(self, idTelefone, idFuncionario):
        try:
            _sql = "SELECT * FROM telefone_funcionario t INNER JOIN telefone l ON l.id_telefone = t.id_telefone INNER JOIN funcionario c ON c.id_funcionario = t.id_funcionario WHERE t.id_telefone = '"+idTelefone+"' AND  t.id_funcionario = '"+idFuncionario+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaEmailFuncionario(self, idEmail, idFuncionario):
        try:
            _sql = "SELECT * FROM email_funcionario t INNER JOIN email l ON l.id_email = t.id_email INNER JOIN funcionario c ON c.id_funcionario = t.id_funcionario WHERE t.id_telefone = '"+idEmail+"' AND  t.id_funcionario = '"+idFuncionario+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def atualizarFuncionario(self, funcionario):

        try:
            __sql = "UPDATE funcionario SET  id_pessoa_fisica = %s, situacao = %s, observacao = %s, data_demissao = %s, data_admissao = %s, num_carteira = %s, serie = %s, uf = %s, data_emissao = %s, pis_pasep = %s, id_civil = %s, id_deficiencia = %s, id_categoria_trabalho = %s, id_setores = %s, id_cargo = %s, id_jornada_trabalho = %s, atualizado = %s WHERE  id_funcionario = %s"
            _valores = (funcionario.getIdPessoaFisica, funcionario.getSituacao, funcionario.getObservacao, funcionario.getDemissao, funcionario.getAdmissao, funcionario.getNumCarteira,  funcionario.setSerie, funcionario.getUf, funcionario.getEmissao, funcionario.getPis, funcionario.getCivil, funcionario.getDeficiencia, funcionario.getCategoria, funcionario.getSetor, funcionario.getCargo, funcionario.getJornada, self.__dataHora, funcionario.getIdFuncionario)

            self.__cursor.execute(__sql, _valores)
            self.__conexao.conn.commit()
            QMessageBox.information(QWidget(), 'Mensagem', "Cadastro atualizado com sucesso")
            # self.__cursor.close()
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao atualizar as informações no banco de dados")
            self.__conexao.conn.rollback()
            return False

    def atualizarHorarios(self, semana, inicio, iniIntervalo, fimIntervalo, termino, jornada, idFuncionario):

        try:
            __sql = "UPDATE horario_jornada SET hora_entrada = %s, hora_ini_intervalo = %s, hora_fim_intervalo = %s, hora_saida = %s, id_jornada_trabalho = %s WHERE dia = %s AND  id_funcionario = %s"
            _valores = (inicio, iniIntervalo, fimIntervalo, termino, jornada, semana, idFuncionario)

            self.__cursor.execute(__sql, _valores)
            self.__conexao.conn.commit()
            # self.__cursor.close()
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao atualizar as informações no banco de dados")
            self.__conexao.conn.rollback()
            return False

    def pesquisarTabelaUsuario(self, idFuncionario):
        try:
            _sql = "SELECT * FROM usuarios u INNER JOIN funcionario f ON f.id_funcionario = u.id_funcionario WHERE u.id_funcionario = '"+str(idFuncionario)+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False