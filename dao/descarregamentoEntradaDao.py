import sys
import time
import datetime
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mysql.connector import Error
from conexao.conexao import ConexaoDb, mysql


class DescarreEntradaDao(object):
    def __init__(self):
        self.__conexao = ConexaoDb()
        self.__cursor = self.__conexao.conn.cursor()
        self.__ts = time.time()
        self.__dataHora = datetime.datetime.fromtimestamp(self.__ts).strftime('%Y-%m-%d %H:%M:%S')

    def pesquisarNumNotaFiscal(self, pesquisa):
        try:
            _sql = "SELECT n.id_entrada_notas_fiscais, t.tipo, n.serie, n.numero_nota, n.data_emissao, n.data_entrada, n.valor_total, n.valor_icms, n.valor_ipi, n.alicota_icms, n.alicota_ipi FROM notas_fiscais n INNER JOIN tipo_nf t ON t.id_tipo_nf = n.id_tipo_nf INNER JOIN motorista m ON m.id_motorista = n.id_motorista INNER JOIN fornecedor r ON r.id_fornecedor = n.id_fornecedor WHERE n.id_entrada_notas_fiscais = '"+pesquisa+"'"

            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
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

    def pesquisarProduto(self, pesquisar):
        try:
            _sql = "SELECT p.descricao FROM descricao_produto_nota_fiscal d INNER JOIN notas_fiscais n ON n.id_entrada_notas_fiscais = d.id_notas_fiscais INNER JOIN produto p ON p.id_produto = d.id_produto WHERE n.id_entrada_notas_fiscais = '" + pesquisar+ "' "

            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarFornecedor(self, pesquisa):
        try:
            _sql = "SELECT c.id_fornecedor, t.descricao, p.nome_razao, p.sobrenome_fantasia, p.cpf_cnpj, p.rg_inscricao, f.expeditor, f.uf, f.aniversario, p.endereco, p.numero, p.complemento, p.bairro, i.nome, e.nome, i.cep, j.site, c.observacao, c.situacao FROM fornecedor c LEFT OUTER JOIN pessoa_fisica f ON f.id_pessoa_fisica = c.id_pessoa_fisica LEFT OUTER JOIN pessoa_juridica j ON j.id_pessoa_juridica = c.id_pessoa_juridica INNER JOIN pessoa p ON p.id_pessoa = c.id_pessoa INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN cidade i ON i.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = i.id_estado WHERE c.id_fornecedor  = '"+pesquisa+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def cadastrar(self, campos):
        try:
            _sql = "INSERT INTO entrada_veiculo_descarregamento (data, hora, id_entrada_notas_fiscais, id_fornecedor, id_motorista, status) VALUES (%s, %s, %s, %s, %s, %s)"
            _valores = (campos.getData, campos.getHora, campos.getIdNf, campos.getIdFornecedor, campos.getIdMotorista, 'Aberto')
            self.__cursor.execute(_sql, _valores)
            self.__conexao.conn.commit()
            #self.__cursor.close()
            QMessageBox.information(QWidget(), 'Mensagem', "Cadastro realizado com sucesso!")
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados  email")
            self.__conexao.conn.rollback()
            return False