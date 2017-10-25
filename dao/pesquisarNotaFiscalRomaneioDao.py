import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mysql.connector import Error
from conexao.conexao import ConexaoDb, mysql

class PesquisarNotaFiscalRomaneioDao(object):


    def __init__(self):
        self.__conexao = ConexaoDb()
        self.__cursor = self.__conexao.conn.cursor()

    def pesquisarNumeroNota(self, numero):
        try:
            _sql = "SELECT n.id_entrada_notas_fiscais, n.numero_nota, n.data_emissao, n.valor_total, f.id_fornecedor, f.fantasia, f.razao_social, f.cnpj, f.inscricao_estadual, e.id_empresa, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual, m.id_motorista, m.nome, m.rg, m.cpf, r.id_romaneios, r.numer_romaneio, r.certificada, q.descricao FROM romaneios r INNER JOIN notas_fiscais n ON n.id_entrada_notas_fiscais = r.id_entrada_notas_fiscais INNER JOIN fornecedor f ON f.id_fornecedor = n.id_fornecedor INNER JOIN empresa e ON e.id_empresa = n.id_empresa INNER JOIN motorista m ON m.id_motorista = n.id_motorista INNER JOIN metragem q ON q.id_metragem = r.id_metragem  where n.numero_nota = '"+numero+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarNumeroRomaneio(self, numero):
        try:
            _sql = "SELECT n.id_entrada_notas_fiscais, n.numero_nota, n.data_emissao, n.valor_total, f.id_fornecedor, f.fantasia, f.razao_social, f.cnpj, f.inscricao_estadual, e.id_empresa, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual, m.id_motorista, m.nome, m.rg, m.cpf, r.id_romaneios, r.numer_romaneio, r.certificada, q.descricao FROM romaneios r INNER JOIN notas_fiscais n ON n.id_entrada_notas_fiscais = r.id_entrada_notas_fiscais INNER JOIN fornecedor f ON f.id_fornecedor = n.id_fornecedor INNER JOIN empresa e ON e.id_empresa = n.id_empresa INNER JOIN motorista m ON m.id_motorista = n.id_motorista INNER JOIN metragem q ON q.id_metragem = r.id_metragem  where r.numer_romaneio = '" + numero + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarFantasiaEmit(self, fantasia):
        try:
            _sql = "SELECT n.id_entrada_notas_fiscais, n.numero_nota, n.data_emissao, n.valor_total, f.id_fornecedor, f.fantasia, f.razao_social, f.cnpj, f.inscricao_estadual, e.id_empresa, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual, m.id_motorista, m.nome, m.rg, m.cpf, r.id_romaneios, r.numer_romaneio, r.certificada, q.descricao FROM romaneios r INNER JOIN notas_fiscais n ON n.id_entrada_notas_fiscais = r.id_entrada_notas_fiscais INNER JOIN fornecedor f ON f.id_fornecedor = n.id_fornecedor INNER JOIN empresa e ON e.id_empresa = n.id_empresa INNER JOIN motorista m ON m.id_motorista = n.id_motorista INNER JOIN metragem q ON q.id_metragem = r.id_metragem  where f.fantasia = '" + fantasia + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarRozaoSocialEmit(self, razaoSocial):
        try:
            _sql = "SELECT n.id_entrada_notas_fiscais, n.numero_nota, n.data_emissao, n.valor_total, f.id_fornecedor, f.fantasia, f.razao_social, f.cnpj, f.inscricao_estadual, e.id_empresa, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual, m.id_motorista, m.nome, m.rg, m.cpf, r.id_romaneios, r.numer_romaneio, r.certificada, q.descricao FROM romaneios r INNER JOIN notas_fiscais n ON n.id_entrada_notas_fiscais = r.id_entrada_notas_fiscais INNER JOIN fornecedor f ON f.id_fornecedor = n.id_fornecedor INNER JOIN empresa e ON e.id_empresa = n.id_empresa INNER JOIN motorista m ON m.id_motorista = n.id_motorista INNER JOIN metragem q ON q.id_metragem = r.id_metragem  where f.razao_social = '" + razaoSocial + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarCnpjEmit(self, cnpj):
        try:
            _sql = "SELECT n.id_entrada_notas_fiscais, n.numero_nota, n.data_emissao, n.valor_total, f.id_fornecedor, f.fantasia, f.razao_social, f.cnpj, f.inscricao_estadual, e.id_empresa, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual, m.id_motorista, m.nome, m.rg, m.cpf, r.id_romaneios, r.numer_romaneio, r.certificada, q.descricao FROM romaneios r INNER JOIN notas_fiscais n ON n.id_entrada_notas_fiscais = r.id_entrada_notas_fiscais INNER JOIN fornecedor f ON f.id_fornecedor = n.id_fornecedor INNER JOIN empresa e ON e.id_empresa = n.id_empresa INNER JOIN motorista m ON m.id_motorista = n.id_motorista INNER JOIN metragem q ON q.id_metragem = r.id_metragem  where f.cnpj = '" + cnpj + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarInsEstadualEmit(self, inscricacao):
        try:
            _sql = "SELECT n.id_entrada_notas_fiscais, n.numero_nota, n.data_emissao, n.valor_total, f.id_fornecedor, f.fantasia, f.razao_social, f.cnpj, f.inscricao_estadual, e.id_empresa, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual, m.id_motorista, m.nome, m.rg, m.cpf, r.id_romaneios, r.numer_romaneio, r.certificada, q.descricao FROM romaneios r INNER JOIN notas_fiscais n ON n.id_entrada_notas_fiscais = r.id_entrada_notas_fiscais INNER JOIN fornecedor f ON f.id_fornecedor = n.id_fornecedor INNER JOIN empresa e ON e.id_empresa = n.id_empresa INNER JOIN motorista m ON m.id_motorista = n.id_motorista INNER JOIN metragem q ON q.id_metragem = r.id_metragem  where f.inscricao_estadual = '" + inscricacao + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False


    def pesquisarFantasiaDest(self, fantasia):
        try:
            _sql = "SELECT n.id_entrada_notas_fiscais, n.numero_nota, n.data_emissao, n.valor_total, f.id_fornecedor, f.fantasia, f.razao_social, f.cnpj, f.inscricao_estadual, e.id_empresa, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual, m.id_motorista, m.nome, m.rg, m.cpf, r.id_romaneios, r.numer_romaneio, r.certificada, q.descricao FROM romaneios r INNER JOIN notas_fiscais n ON n.id_entrada_notas_fiscais = r.id_entrada_notas_fiscais INNER JOIN fornecedor f ON f.id_fornecedor = n.id_fornecedor INNER JOIN empresa e ON e.id_empresa = n.id_empresa INNER JOIN motorista m ON m.id_motorista = n.id_motorista INNER JOIN metragem q ON q.id_metragem = r.id_metragem  where e.fantasia = '" + fantasia + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarRozaoSocialDest(self, razaoSocial):
        try:
            _sql = "SELECT n.id_entrada_notas_fiscais, n.numero_nota, n.data_emissao, n.valor_total, f.id_fornecedor, f.fantasia, f.razao_social, f.cnpj, f.inscricao_estadual, e.id_empresa, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual, m.id_motorista, m.nome, m.rg, m.cpf, r.id_romaneios, r.numer_romaneio, r.certificada, q.descricao FROM romaneios r INNER JOIN notas_fiscais n ON n.id_entrada_notas_fiscais = r.id_entrada_notas_fiscais INNER JOIN fornecedor f ON f.id_fornecedor = n.id_fornecedor INNER JOIN empresa e ON e.id_empresa = n.id_empresa INNER JOIN motorista m ON m.id_motorista = n.id_motorista INNER JOIN metragem q ON q.id_metragem = r.id_metragem  where e.razao_social = '" + razaoSocial + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarCnpjDest(self, cnpj):
        try:
            _sql = "SELECT n.id_entrada_notas_fiscais, n.numero_nota, n.data_emissao, n.valor_total, f.id_fornecedor, f.fantasia, f.razao_social, f.cnpj, f.inscricao_estadual, e.id_empresa, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual, m.id_motorista, m.nome, m.rg, m.cpf, r.id_romaneios, r.numer_romaneio, r.certificada, q.descricao FROM romaneios r INNER JOIN notas_fiscais n ON n.id_entrada_notas_fiscais = r.id_entrada_notas_fiscais INNER JOIN fornecedor f ON f.id_fornecedor = n.id_fornecedor INNER JOIN empresa e ON e.id_empresa = n.id_empresa INNER JOIN motorista m ON m.id_motorista = n.id_motorista INNER JOIN metragem q ON q.id_metragem = r.id_metragem  where e.cnpj = '" + cnpj + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarInsEstadualDest(self, inscricacao):
        try:
            _sql = "SELECT n.id_entrada_notas_fiscais, n.numero_nota, n.data_emissao, n.valor_total, f.id_fornecedor, f.fantasia, f.razao_social, f.cnpj, f.inscricao_estadual, e.id_empresa, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual, m.id_motorista, m.nome, m.rg, m.cpf, r.id_romaneios, r.numer_romaneio, r.certificada, q.descricao FROM romaneios r INNER JOIN notas_fiscais n ON n.id_entrada_notas_fiscais = r.id_entrada_notas_fiscais INNER JOIN fornecedor f ON f.id_fornecedor = n.id_fornecedor INNER JOIN empresa e ON e.id_empresa = n.id_empresa INNER JOIN motorista m ON m.id_motorista = n.id_motorista INNER JOIN metragem q ON q.id_metragem = r.id_metragem  where e.inscricao_estadual = '" + inscricacao + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarDataLancamento(self, data):
        try:
            _sql = "SELECT n.id_entrada_notas_fiscais, n.numero_nota, n.data_emissao, n.valor_total, f.id_fornecedor, f.fantasia, f.razao_social, f.cnpj, f.inscricao_estadual, e.id_empresa, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual, m.id_motorista, m.nome, m.rg, m.cpf, r.id_romaneios, r.numer_romaneio, r.certificada, q.descricao FROM romaneios r INNER JOIN notas_fiscais n ON n.id_entrada_notas_fiscais = r.id_entrada_notas_fiscais INNER JOIN fornecedor f ON f.id_fornecedor = n.id_fornecedor INNER JOIN empresa e ON e.id_empresa = n.id_empresa INNER JOIN motorista m ON m.id_motorista = n.id_motorista INNER JOIN metragem q ON q.id_metragem = r.id_metragem  where n.data_emissao = '" + data + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarDataPeriodo(self, dataIni, dataFim):
        try:
            _sql = "SELECT n.id_entrada_notas_fiscais, n.numero_nota, n.data_emissao, n.valor_total, f.id_fornecedor, f.fantasia, f.razao_social, f.cnpj, f.inscricao_estadual, e.id_empresa, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual, m.id_motorista, m.nome, m.rg, m.cpf, r.id_romaneios, r.numer_romaneio, r.certificada, q.descricao FROM romaneios r INNER JOIN notas_fiscais n ON n.id_entrada_notas_fiscais = r.id_entrada_notas_fiscais INNER JOIN fornecedor f ON f.id_fornecedor = n.id_fornecedor INNER JOIN empresa e ON e.id_empresa = n.id_empresa INNER JOIN motorista m ON m.id_motorista = n.id_motorista INNER JOIN metragem q ON q.id_metragem = r.id_metragem  where n.data_emissao > '"+ dataIni +"' AND n.data_emissao < '" + dataFim +"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarVeiculoMotorista(self, motorista, rg, cpf,):
        try:
            _sql = "SELECT v.marca, v.modelo, v.placa FROM veiculo_motorista v INNER JOIN tipo_veiculo t ON t.id_tipo_veiculo = v.id_tipo_veiculo INNER JOIN motorista m On m.id_motorista = v.id_motorista INNER JOIN categoria_cnh n ON n.id_categoria_cnh = m.id_categoria_cnh INNER JOIN cidade c ON c.id_cidade = m.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado WHERE m.nome = '"+motorista+"' AND  m.rg = '"+rg+"' AND m.cpf = '"+cpf+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            return result
            print(result)
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao pesquisar a cidade no banco de dados ")
            return False

    def pesquisarDescricaoProduto(self, num, data, valor,):
        try:
            _sql = "SELECT t.descricao, p.descricao, d.unidade_medida, d.quantidade, d.valor_unitario FROM descricao_produto_nota_fiscal d INNER JOIN notas_fiscais f ON f.id_entrada_notas_fiscais = d.id_notas_fiscais INNER JOIN carga_produto c ON c.id_carga_produto = d.id_carga_produto INNER JOIN tipo_carga t ON t.id_tipo_carga = c.id_tipo_carga INNER JOIN produto p ON p.id_produto = c.id_produto WHERE f.numero_nota = '"+num+"' AND f.data_emissao = '"+data+"' AND f.valor_total = '"+valor+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            return result
            print(result)
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao pesquisar a cidade no banco de dados ")
            return False