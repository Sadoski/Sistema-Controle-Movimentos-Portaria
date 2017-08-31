import sys
import time
import datetime
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mysql.connector import Error
from conexao.conexao import ConexaoDb, mysql

class CarregamentoSaidaDao(object):
    def __init__(self):
        self.__conexao = ConexaoDb()
        self.__cursor = self.__conexao.conn.cursor()

    def pesquisarTipoCarga(self):
        try:
            _sql = "SELECT descricao FROM tipo_carga"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
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

    def pesquisarNomeMotoristaVazio(self, nome):
        try:
            _sql = "SELECT c.id_entrada_vei_carre, m.id_motorista, m.nome, v.marca, v.modelo, v.placa, c.data, c.hora, i.descricao, o.descricao, l.id_cliente, l.fantasia, l.razao_social, l.cnpj, l.inscricao_estadual, e.id_empresa, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual FROM entrada_veiculo_carregamento c INNER JOIN motorista m ON m.id_motorista = c.id_motorista INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista INNER JOIN carga_produto a ON a.id_carga_produto = c.id_carga_produto INNER JOIN tipo_carga i On i.id_tipo_carga = a.id_tipo_carga INNER JOIN produto o ON o.id_produto = a.id_produto INNER JOIN cliente l ON l.id_cliente = c.id_cliente INNER JOIN empresa e ON e.id_empresa = c.id_empresa INNER JOIN carga_produto p ON p.id_carga_produto = c.id_carga_produto WHERE m.nome LIKE '%"+nome+"%' AND c.status = 'Aberto'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarMarcaVazio(self, marca):
        try:
            _sql = "SELECT c.id_entrada_vei_carre, m.id_motorista, m.nome, v.marca, v.modelo, v.placa, c.data, c.hora, i.descricao, o.descricao, l.id_cliente, l.fantasia, l.razao_social, l.cnpj, l.inscricao_estadual, e.id_empresa, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual FROM entrada_veiculo_carregamento c INNER JOIN motorista m ON m.id_motorista = c.id_motorista INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista INNER JOIN carga_produto a ON a.id_carga_produto = c.id_carga_produto INNER JOIN tipo_carga i On i.id_tipo_carga = a.id_tipo_carga INNER JOIN produto o ON o.id_produto = a.id_produto INNER JOIN cliente l ON l.id_cliente = c.id_cliente INNER JOIN empresa e ON e.id_empresa = c.id_empresa INNER JOIN carga_produto p ON p.id_carga_produto = c.id_carga_produto WHERE v.marca = '%"+marca+"%' AND c.status = 'Aberto'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarModeloVazio(self, modelo):
        try:
            _sql = "SELECT c.id_entrada_vei_carre, m.id_motorista, m.nome, v.marca, v.modelo, v.placa, c.data, c.hora, i.descricao, o.descricao, l.id_cliente, l.fantasia, l.razao_social, l.cnpj, l.inscricao_estadual, e.id_empresa, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual FROM entrada_veiculo_carregamento c INNER JOIN motorista m ON m.id_motorista = c.id_motorista INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista INNER JOIN carga_produto a ON a.id_carga_produto = c.id_carga_produto INNER JOIN tipo_carga i On i.id_tipo_carga = a.id_tipo_carga INNER JOIN produto o ON o.id_produto = a.id_produto INNER JOIN cliente l ON l.id_cliente = c.id_cliente INNER JOIN empresa e ON e.id_empresa = c.id_empresa INNER JOIN carga_produto p ON p.id_carga_produto = c.id_carga_produto WHERE v.modelo = '%"+modelo+"%' AND c.status = 'Aberto'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarPlacaVazio(self, placa):
        try:
            _sql = "SELECT c.id_entrada_vei_carre, m.id_motorista, m.nome, v.marca, v.modelo, v.placa, c.data, c.hora, i.descricao, o.descricao, l.id_cliente, l.fantasia, l.razao_social, l.cnpj, l.inscricao_estadual, e.id_empresa, e.fantasia, e.razao_social, e.cnpj, e.inscricao_estadual FROM entrada_veiculo_carregamento c INNER JOIN motorista m ON m.id_motorista = c.id_motorista INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista INNER JOIN carga_produto a ON a.id_carga_produto = c.id_carga_produto INNER JOIN tipo_carga i On i.id_tipo_carga = a.id_tipo_carga INNER JOIN produto o ON o.id_produto = a.id_produto INNER JOIN cliente l ON l.id_cliente = c.id_cliente INNER JOIN empresa e ON e.id_empresa = c.id_empresa INNER JOIN carga_produto p ON p.id_carga_produto = c.id_carga_produto WHERE v.placa = '%"+placa+"%' AND c.status = 'Aberto'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarNomeMotoristaCarregado(self, nome):
        try:
            _sql = "SELECT c.id_entrada_vei_desc, m.id_motorista, m.nome, v.marca, v.modelo, v.placa, c.data, c.hora FROM entrada_veiculo_descarregamento c INNER JOIN motorista m ON m.id_motorista = c.id_motorista INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista WHERE m.nome LIKE '%"+nome+"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarMarcaCarregado(self, marca):
        try:
            _sql = "SELECT c.id_entrada_vei_desc, m.id_motorista, m.nome, v.marca, v.modelo, v.placa, c.data, c.hora FROM entrada_veiculo_descarregamento c INNER JOIN motorista m ON m.id_motorista = c.id_motorista INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista WHERE v.marca = '%"+marca+"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarModeloCarregado(self, modelo):
        try:
            _sql = "SELECT c.id_entrada_vei_desc, m.id_motorista, m.nome, v.marca, v.modelo, v.placa, c.data, c.hora FROM entrada_veiculo_descarregamento c INNER JOIN motorista m ON m.id_motorista = c.id_motorista INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista WHERE v.modelo = '%"+modelo+"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarPlacaCarregado(self, placa):
        try:
            _sql = "SELECT c.id_entrada_vei_desc, m.id_motorista, m.nome, v.marca, v.modelo, v.placa, c.data, c.hora FROM entrada_veiculo_descarregamento c INNER JOIN motorista m ON m.id_motorista = c.id_motorista INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista WHERE v.placa = '%"+placa+"%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def cadastrarVazio(self, entrada):
        try:
            _sql = "INSERT INTO saida_veiculos_caregamento (id_entrada_vei_carre, data, hora, status) VALUES (%s, %s, %s, %s)"
            _valores = (entrada.getIdEntrada, entrada.getData, entrada.getHora, 'Entrou Vazio')
            print(_valores)
            self.__cursor.execute(_sql, _valores)
            self.__cursor.execute("UPDATE entrada_veiculo_carregamento set status = 'Fechado' WHERE id_entrada_vei_carre = '"+entrada.getIdEntrada+"'")
            self.__conexao.conn.commit()
            # self.__cursor.close()
            QMessageBox.warning(QWidget(), 'Mensagem', "Cadastro realizado com sucesso!")
            return  True
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False