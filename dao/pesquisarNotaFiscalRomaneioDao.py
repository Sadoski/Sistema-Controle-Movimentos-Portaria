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
            _sql = "SELECT n.id_entrada_notas_fiscais, n.numero_nota, n.data_emissao, n.valor_total, f.id_fornecedor, f.fantasia, f.razao_social, f.cnpj, f.inscricao_estadual, e.id_empresa, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual, m.id_motorista, m.nome, m.rg, m.cpf, r.id_romaneios, r.numer_romaneio, r.certificada, q.descricao FROM romaneios r INNER JOIN notas_fiscais n ON n.id_entrada_notas_fiscais = r.id_entrada_notas_fiscais INNER JOIN fornecedor f ON f.id_fornecedor = n.id_fornecedor INNER JOIN empresa e ON e.id_empresa = n.id_empresa INNER JOIN motorista m ON m.id_motorista = n.id_motorista INNER JOIN metragem q ON q.id_metragem = r.id_metragem  where f.inscricao_estadual = '" + cnpj + "'"
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
            _sql = "SELECT n.id_entrada_notas_fiscais, n.numero_nota, n.data_emissao, n.valor_total, f.id_fornecedor, f.fantasia, f.razao_social, f.cnpj, f.inscricao_estadual, e.id_empresa, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual, m.id_motorista, m.nome, m.rg, m.cpf, r.id_romaneios, r.numer_romaneio, r.certificada, q.descricao FROM romaneios r INNER JOIN notas_fiscais n ON n.id_entrada_notas_fiscais = r.id_entrada_notas_fiscais INNER JOIN fornecedor f ON f.id_fornecedor = n.id_fornecedor INNER JOIN empresa e ON e.id_empresa = n.id_empresa INNER JOIN motorista m ON m.id_motorista = n.id_motorista INNER JOIN metragem q ON q.id_metragem = r.id_metragem  where e.inscricao_estadual = '" + cnpj + "'"
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