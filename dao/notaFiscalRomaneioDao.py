import sys
import time
import datetime
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mysql.connector import Error
from conexao.conexao import ConexaoDb, mysql

class NotaFiscalRomanieo(object):
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

    def pesquisarNf(self):
        try:
            _sql = "SELECT * FROM tipo_nf"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarNcm(self):
        try:
            _sql = "SELECT * FROM ncm"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarCfop(self):
        try:
            _sql = "SELECT * FROM cfop"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarCsosn(self):
        try:
            _sql = "SELECT * FROM csosn"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarCst(self):
        try:
            _sql = "SELECT * FROM cst"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarTipoCarga(self):
        try:
            _sql = "SELECT * FROM tipo_carga"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False


    def pesquisarProduto(self):
        try:
            _sql = "SELECT * FROM produto"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarFornecedor(self, fornecedor):
        try:
            _sql = "SELECT f.id_fornecedor, f.razao_social, f.cnpj, f.inscricao_estadual FROM fornecedor f INNER JOIN cidade c ON c.id_cidade = f.id_cidades INNER JOIN estado s ON s.id_estado = c.id_estado INNER JOIN empresa e ON e.id_empresa = f.id_empresa WHERE f.fantasia = '"+fornecedor+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarMotorista(self, motorista):
        try:
            _sql = "SELECT m.id_motorista, m.rg, m.cpf, v.marca, v.modelo, v.placa FROM veiculo_motorista v INNER JOIN tipo_veiculo t ON t.id_tipo_veiculo = v.id_tipo_veiculo INNER JOIN motorista m On m.id_motorista = v.id_motorista INNER JOIN categoria_cnh n ON n.id_categoria_cnh = m.id_categoria_cnh INNER JOIN cidade c ON c.id_cidade = m.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado WHERE m.nome = '"+motorista+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def cadastrarNotaFiscal(self, nota):
            try:
                _sql = "INSERT INTO notas_fiscais(serie, modelo, numero_nota, data_emissao, data_entrada, valor_total, cadastrado, id_fornecedor, id_motorista, id_tipo_nf) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                _valores = (nota.getSerie, nota.getModelo, nota.getNumNotaFiscal, nota.getDataEmissao, nota.getDataEntrada, nota.getValorTotal, self.__dataHora, nota.getIdFornecedor, nota.getIdEmpresa, nota.getTipoNf)
                self.__cursor.execute(_sql, _valores)
                self.__conexao.conn.commit()
                # self.__cursor.close()
                return True
            except mysql.connector.Error as e:
                w = QWidget()
                QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
                self.__conexao.conn.rollback()
                return False

    def cadastrarDescricaoProduto(self, descricao):
            try:
                _sql = "INSERT INTO descricao_produto_nota_fiscal(id_notas_fiscais, id_produto, ncm, cst, cfop, csosn, unidade_medida, quantidade, valor_unitario, valor_total, valor_icms, valor_ipi, alicota_icms, alicota_ipi, qtd_total, ins_municipal, valor_total_servico, base_issqn, valor_issqn) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                _valores = (descricao.getIdNf, descricao.getProduto, descricao.getNcm, descricao.getCst, descricao.getCfop, descricao.getCsosn, descricao.getUnidade, descricao.getQuantidade, descricao.getValorUn, descricao.getValorTotal, descricao.getValorIcms, descricao.getValorIpi, descricao.getAlicotaIcms, descricao.getAlicotaIpi, descricao.getQtdTotal, descricao.getInsMunicipal, descricao.getValorTotalServico, descricao.getBaseIssqn, descricao.getValorIssqn)
                self.__cursor.execute(_sql, _valores)
                self.__conexao.conn.commit()
                # self.__cursor.close()
                return True
            except mysql.connector.Error as e:
                w = QWidget()
                QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
                self.__conexao.conn.rollback()
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

    def pesquisarMotorista(self, motorista):
        try:
            _sql = "SELECT m.id_motorista, p.nome_razao, p.sobrenome_fantasia, m.cnh, p.cpf_cnpj, p.rg_inscricao, f.expeditor, f.uf, m.pis, f.aniversario, g.sexo, f.mae, f.pai, p.endereco, p.numero, p.complemento, p.bairro, c.nome, e.nome, c.cep, t.descricao, v.marca, v.modelo, v.placa, m.observacao, m.situacao FROM motorista m INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista INNER JOIN categoria_cnh t ON t.id_categoria_cnh = m.id_categoria_cnh INNER JOIN pessoa_fisica f ON f.id_pessoa_fisica = m.id_pessoa_fisica INNER JOIN genero g ON g.id_genero = f.id_genero INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado WHERE m.id_motorista = '"+motorista+"' AND v.situacao = 1"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaFornecedor(self, pesquisa):
        try:
            _sql = "SELECT c.id_fornecedor, t.descricao, p.nome_razao, p.sobrenome_fantasia, p.cpf_cnpj, p.rg_inscricao, f.expeditor, f.uf, f.aniversario, p.endereco, p.numero, p.complemento, p.bairro, i.nome, e.nome, i.cep, j.site, c.observacao, c.situacao FROM fornecedor c LEFT OUTER JOIN pessoa_fisica f ON f.id_pessoa_fisica = c.id_pessoa_fisica LEFT OUTER JOIN pessoa_juridica j ON j.id_pessoa_juridica = c.id_pessoa_juridica INNER JOIN pessoa p ON p.id_pessoa = c.id_pessoa INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN cidade i ON i.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = i.id_estado WHERE c.id_fornecedor = '"+pesquisa+"' AND c.situacao = 1"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False
