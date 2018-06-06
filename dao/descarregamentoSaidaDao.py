import sys
import time
import datetime
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mysql.connector import Error
from conexao.conexao import ConexaoDb, mysql


class DescarreSaidaDao(object):
    def __init__(self):
        self.__conexao = ConexaoDb()
        self.__cursor = self.__conexao.conn.cursor()
        self.__ts = time.time()
        self.__dataHora = datetime.datetime.fromtimestamp(self.__ts).strftime('%Y-%m-%d %H:%M:%S')

    def pesquisarIdMotorista(self, pesquisar):
        try:
            _sql = "SELECT m.id_motorista FROM entrada_veiculo_descarregamento e INNER JOIN motorista m ON m.id_motorista = e.id_motorista INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista INNER JOIN pessoa_fisica f ON f.id_pessoa_fisica =m.id_pessoa_fisica INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa WHERE e.id_entrada_vei_desc = '"+pesquisar+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarEntrada(self):
        try:
            _sql = "SELECT e.id_entrada_vei_desc, e.data, e.hora, p.nome_razao, p.sobrenome_fantasia, v.marca, v.modelo, v.placa FROM entrada_veiculo_descarregamento e INNER JOIN motorista m ON m.id_motorista = e.id_motorista INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista INNER JOIN pessoa_fisica f ON f.id_pessoa_fisica =m.id_pessoa_fisica INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa WHERE e.status = 'Aberto'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def cadastrar(self, campos):
        try:
            _sql = "INSERT INTO saida_veiculos_descarregamento (data, hora, id_entrada_vei_desc) VALUES (%s, %s, %s)"
            _valores = (campos.getData, campos.getHora, campos.getIdEntrada)

            self.__cursor.execute(_sql, _valores)
            self.__cursor.execute("UPDATE entrada_veiculo_descarregamento set status = 'Fechado' WHERE id_entrada_vei_desc = '"+campos.getIdEntrada+"'")
            self.__conexao.conn.commit()
            #self.__cursor.close()
            QMessageBox.information(QWidget(), 'Mensagem', "Saida realizado com sucesso!")
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados")
            self.__conexao.conn.rollback()
            return False

    def pesquisarMotoristaDescaRel(self, pesquisar):
        try:
            _sql = "SELECT p.nome_razao FROM entrada_veiculo_descarregamento e LEFT OUTER JOIN saida_veiculos_descarregamento d ON d.id_entrada_vei_desc = e.id_entrada_vei_desc  INNER JOIN notas_fiscais n ON n.id_entrada_notas_fiscais = e.id_entrada_notas_fiscais INNER JOIN descricao_produto_nota_fiscal r ON r.id_notas_fiscais = n.id_entrada_notas_fiscais INNER JOIN produto o on o.id_produto = r.id_produto INNER JOIN motorista m ON m.id_motorista = e.id_motorista INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista INNER JOIN pessoa_fisica f ON f.id_pessoa_fisica = m.id_pessoa_fisica INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa_fisica WHERE  e.id_motorista = '" + str(pesquisar )+ "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarFornecedorDescaRel(self, pesquisar):
        try:
            _sql = "SELECT p.nome_razao FROM entrada_veiculo_descarregamento e LEFT OUTER JOIN saida_veiculos_descarregamento d ON d.id_entrada_vei_desc = e.id_entrada_vei_desc  INNER JOIN notas_fiscais n ON n.id_entrada_notas_fiscais = e.id_entrada_notas_fiscais INNER JOIN descricao_produto_nota_fiscal r ON r.id_notas_fiscais = n.id_entrada_notas_fiscais INNER JOIN produto o on o.id_produto = r.id_produto INNER JOIN fornecedor c ON c.id_fornecedor = e.id_fornecedor INNER JOIN motorista m ON m.id_motorista = e.id_motorista INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista LEFT OUTER JOIN pessoa_fisica f ON f.id_pessoa_fisica = c.id_pessoa_fisica LEFT OUTER JOIN pessoa_juridica j ON j.id_pessoa_juridica = c.id_pessoa_juridica INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa_fisica or p.id_pessoa = j.id_pessoa_juridica WHERE e.id_fornecedor = '" + str(pesquisar) + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarCodDescaRel(self, pesquisar):
        try:
            _sql = "SELECT e.id_entrada_vei_desc, e.data, e.hora, d.data, d.hora, n.numero_nota, o.descricao, e.id_motorista, v.marca, v.modelo, v.placa, e.id_fornecedor FROM entrada_veiculo_descarregamento e LEFT OUTER JOIN saida_veiculos_descarregamento d ON d.id_entrada_vei_desc = e.id_entrada_vei_desc  INNER JOIN notas_fiscais n ON n.id_entrada_notas_fiscais = e.id_entrada_notas_fiscais INNER JOIN descricao_produto_nota_fiscal r ON r.id_notas_fiscais = n.id_entrada_notas_fiscais INNER JOIN produto o on o.id_produto = r.id_produto INNER JOIN fornecedor c ON c.id_fornecedor = e.id_fornecedor INNER JOIN motorista m ON m.id_motorista = e.id_motorista INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista WHERE e.id_entrada_vei_desc = '"+pesquisar+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarNumNfDescaRel(self, pesquisar):
        try:
            _sql = "SELECT e.id_entrada_vei_desc, e.data, e.hora, d.data, d.hora, n.numero_nota, o.descricao, e.id_motorista, v.marca, v.modelo, v.placa, e.id_fornecedor FROM entrada_veiculo_descarregamento e LEFT OUTER JOIN saida_veiculos_descarregamento d ON d.id_entrada_vei_desc = e.id_entrada_vei_desc  INNER JOIN notas_fiscais n ON n.id_entrada_notas_fiscais = e.id_entrada_notas_fiscais INNER JOIN descricao_produto_nota_fiscal r ON r.id_notas_fiscais = n.id_entrada_notas_fiscais INNER JOIN produto o on o.id_produto = r.id_produto INNER JOIN fornecedor c ON c.id_fornecedor = e.id_fornecedor INNER JOIN motorista m ON m.id_motorista = e.id_motorista INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista WHERE n.numero_nota = '"+pesquisar+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarProdutoDescaRel(self, pesquisar):
        try:
            _sql = "SELECT e.id_entrada_vei_desc, e.data, e.hora, d.data, d.hora, n.numero_nota, o.descricao, e.id_motorista, v.marca, v.modelo, v.placa, e.id_fornecedor FROM entrada_veiculo_descarregamento e LEFT OUTER JOIN saida_veiculos_descarregamento d ON d.id_entrada_vei_desc = e.id_entrada_vei_desc  INNER JOIN notas_fiscais n ON n.id_entrada_notas_fiscais = e.id_entrada_notas_fiscais INNER JOIN descricao_produto_nota_fiscal r ON r.id_notas_fiscais = n.id_entrada_notas_fiscais INNER JOIN produto o on o.id_produto = r.id_produto INNER JOIN fornecedor c ON c.id_fornecedor = e.id_fornecedor INNER JOIN motorista m ON m.id_motorista = e.id_motorista INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista WHERE o.descricao LIKE '%" + pesquisar + "%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarMotoDescaRel(self, pesquisar):
        try:
            _sql = "SELECT e.id_entrada_vei_desc, e.data, e.hora, d.data, d.hora, n.numero_nota, o.descricao, e.id_motorista, v.marca, v.modelo, v.placa, e.id_fornecedor FROM entrada_veiculo_descarregamento e LEFT OUTER JOIN saida_veiculos_descarregamento d ON d.id_entrada_vei_desc = e.id_entrada_vei_desc  INNER JOIN notas_fiscais n ON n.id_entrada_notas_fiscais = e.id_entrada_notas_fiscais INNER JOIN descricao_produto_nota_fiscal r ON r.id_notas_fiscais = n.id_entrada_notas_fiscais INNER JOIN produto o on o.id_produto = r.id_produto INNER JOIN motorista m ON m.id_motorista = e.id_motorista INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista INNER JOIN pessoa_fisica f ON f.id_pessoa_fisica = m.id_pessoa_fisica INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa_fisica WHERE p.nome_razao LIKE '%" + pesquisar + "%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarPlacaDescaRel(self, pesquisar):
        try:
            _sql = "SELECT e.id_entrada_vei_desc, e.data, e.hora, d.data, d.hora, n.numero_nota, o.descricao, e.id_motorista, v.marca, v.modelo, v.placa, e.id_fornecedor FROM entrada_veiculo_descarregamento e LEFT OUTER JOIN saida_veiculos_descarregamento d ON d.id_entrada_vei_desc = e.id_entrada_vei_desc  INNER JOIN notas_fiscais n ON n.id_entrada_notas_fiscais = e.id_entrada_notas_fiscais INNER JOIN descricao_produto_nota_fiscal r ON r.id_notas_fiscais = n.id_entrada_notas_fiscais INNER JOIN produto o on o.id_produto = r.id_produto INNER JOIN fornecedor c ON c.id_fornecedor = e.id_fornecedor INNER JOIN motorista m ON m.id_motorista = e.id_motorista INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista WHERE v.placa = '" + pesquisar + "'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarFornDescaRel(self, pesquisar):
        try:
            _sql = "SELECT e.id_entrada_vei_desc, e.data, e.hora, d.data, d.hora, n.numero_nota, o.descricao, e.id_motorista, v.marca, v.modelo, v.placa, e.id_fornecedor FROM entrada_veiculo_descarregamento e LEFT OUTER JOIN saida_veiculos_descarregamento d ON d.id_entrada_vei_desc = e.id_entrada_vei_desc  INNER JOIN notas_fiscais n ON n.id_entrada_notas_fiscais = e.id_entrada_notas_fiscais INNER JOIN descricao_produto_nota_fiscal r ON r.id_notas_fiscais = n.id_entrada_notas_fiscais INNER JOIN produto o on o.id_produto = r.id_produto INNER JOIN fornecedor c ON c.id_fornecedor = e.id_fornecedor INNER JOIN motorista m ON m.id_motorista = e.id_motorista INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista LEFT OUTER JOIN pessoa_fisica f ON f.id_pessoa_fisica = c.id_pessoa_fisica LEFT OUTER JOIN pessoa_juridica j ON j.id_pessoa_juridica = c.id_pessoa_juridica INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa_fisica or p.id_pessoa = j.id_pessoa_juridica WHERE p.nome_razao LIKE '%" + pesquisar + "%'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False