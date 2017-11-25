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

    def pesquisarTipoCarga(self):
        try:
            _sql = "SELECT descricao FROM tipo_carga"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarMetragem(self):
        try:
            _sql = "SELECT descricao FROM metragem"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarIdMetragem(self, metragem):
        try:
            _sql = "SELECT id_metragem FROM metragem WHERE descricao = '"+metragem+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarIdTipoCarga(self, carga):
        try:
            _sql = "SELECT id_tipo_carga FROM tipo_carga WHERE descricao = '"+carga+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarIdProduto(self, produto):
        try:
            _sql = "SELECT id_produto FROM produto WHERE descricao = '"+produto+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarIdCargaProduto(self, carga, produto):
        try:
            _sql = "SELECT a.id_carga_produto FROM carga_produto a INNER JOIN tipo_carga c ON c.id_tipo_carga = a.id_tipo_carga INNER JOIN produto p ON p.id_produto = a.id_produto WHERE a.id_produto = %s AND a.id_tipo_carga = %s"
            _valores = (produto,carga)
            print(_valores)
            self.__cursor.execute(_sql, _valores)
            result = self.__cursor.fetchone()[0]
            print(result)
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarProduto(self, produto):
        try:
            _sql = "SELECT p.descricao FROM carga_produto a INNER JOIN tipo_carga c ON c.id_tipo_carga = a.id_tipo_carga INNER JOIN produto p ON p.id_produto = a.id_produto WHERE c.descricao = '"+produto+"'"
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

    def pesquisarEmpresa(self, empresa):
        try:
            _sql = "SELECT e.id_empresa, e.razao_social, e.cnpj, e.inscricao_estadual FROM empresa e INNER JOIN cidade c on c.id_cidade = e.id_cidades INNER JOIN estado d on d.id_estado = c.id_estado INNER JOIN tipo_empresa t on t.id_tipo_empresa = e.id_tipo_empresa where  e.fantasia = '"+empresa+"'"
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

    def removerCaracter(self, i):
        i = str(i)
        i = i.replace('.', '')
        i = i.replace(',', '')
        i = i.replace('/', '')
        i = i.replace('-', '')
        i = i.replace('(', '')
        i = i.replace(')', '')
        i = i.replace('\\', '')
        return i

    def pesquisarIdNotaFiscal(self, nota):
        try:
            _sql = "SELECT n.id_entrada_notas_fiscais FROM notas_fiscais n INNER JOIN fornecedor f ON f.id_fornecedor = n.id_fornecedor INNER JOIN empresa e ON e.id_empresa = n.id_empresa INNER JOIN motorista m ON m.id_motorista = n.id_motorista WHERE n.numero_nota = %s AND n.data_emissao = %s AND n.valor_total = %s AND n.id_fornecedor = %s AND n.id_empresa = %s AND n.id_motorista = %s"
            _valores = (nota.getNumNotaFiscal, self.removerCaracter(nota.getDataEmissao), nota.getValorTotal, nota.getIdFornecedor, nota.getIdEmpresa, nota.getIdEmpresa)
            self.__cursor.execute(_sql, _valores)
            result = self.__cursor.fetchone()[0]
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def cadastrarNotaFiscal(self, nota):
            try:
                _sql = "INSERT INTO notas_fiscais(numero_nota,data_emissao,valor_total,cadastrado,id_fornecedor,id_empresa,id_motorista) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                _valores = (nota.getNumNotaFiscal, nota.getDataEmissao, nota.getValorTotal, self.__dataHora, nota.getIdFornecedor, nota.getIdEmpresa, nota.getIdEmpresa)
                self.__cursor.execute(_sql, _valores)
                self.__conexao.conn.commit()
                # self.__cursor.close()
                return True
            except mysql.connector.Error as e:
                w = QWidget()
                QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
                self.__conexao.conn.rollback()
                return False

    def cadastrarRomaneio(self, romaneio):
            try:
                _sql = "INSERT INTO romaneios(numer_romaneio, certificada, cadastrado, id_entrada_notas_fiscais, id_metragem) VALUES (%s, %s, %s, %s, %s)"
                _valores = (romaneio.getNumRomaneio, romaneio.getCertifica, self.__dataHora, romaneio.getIdNotaFiscal, romaneio.getIdMetragem)
                self.__cursor.execute(_sql, _valores)
                self.__conexao.conn.commit()
                # self.__cursor.close()
                QMessageBox.warning(QWidget(), 'Mensagem', "Cadastro realizado com sucesso!")
                return True
            except mysql.connector.Error as e:
                w = QWidget()
                QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
                self.__conexao.conn.rollback()
                return False

    def cadastrarDescricaoProduto(self, descricao):
            try:
                _sql = "INSERT INTO descricao_produto_nota_fiscal(id_notas_fiscais, id_produto, ncm, cst, cfop, unidade_medida, quantidade, valor_unitario, valor_total, valor_icms, valor_ipi, alicota_icms, alicota_ipi) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                _valores = (descricao.getCargaProduto, descricao.getNotaFiscal, descricao.getUnidade, descricao.getQuantidade, descricao.getValor)
                self.__cursor.execute(_sql, _valores)
                self.__conexao.conn.commit()
                # self.__cursor.close()
                return True
            except mysql.connector.Error as e:
                w = QWidget()
                QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
                self.__conexao.conn.rollback()
                return False
