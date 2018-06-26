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

    def pesquisarEntradaCarregamento(self):
        try:
            _sql = "SELECT e.id_entrada_vei_carre, e.data, e.hora, g.descricao, t.descricao, m.id_motorista, v.marca, v.modelo, v.placa, c.id_cliente FROM entrada_veiculo_carregamento e INNER JOIN tipo_carga g on g.id_tipo_carga = e.id_tipo_carga INNER JOIN produto t ON t.id_produto = e.id_produto INNER JOIN motorista m ON m.id_motorista = e.id_motorista INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista INNER JOIN cliente c ON c.id_cliente = e.id_cliente  WHERE e.status = 'Aberto'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarIdMotorista(self, pesquisar):
        try:
            _sql = "SELECT e.id_motorista FROM entrada_veiculo_carregamento e INNER JOIN tipo_carga g on g.id_tipo_carga = e.id_tipo_carga INNER JOIN produto t ON t.id_produto = e.id_produto INNER JOIN motorista m ON m.id_motorista = e.id_motorista INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista INNER JOIN cliente c ON c.id_cliente = e.id_cliente LEFT OUTER JOIN pessoa_fisica f ON f.id_pessoa_fisica = m.id_pessoa_fisica OR f.id_pessoa_fisica = c.id_pessoa_fisica LEFT OUTER JOIN pessoa_juridica j ON j.id_pessoa_juridica = c.id_pessoa_juridica WHERE e.id_entrada_vei_carre = '"+pesquisar+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarIdCliente(self, pesquisar):
        try:
            _sql = "SELECT e.id_cliente FROM entrada_veiculo_carregamento e INNER JOIN tipo_carga g on g.id_tipo_carga = e.id_tipo_carga INNER JOIN produto t ON t.id_produto = e.id_produto INNER JOIN motorista m ON m.id_motorista = e.id_motorista INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista INNER JOIN cliente c ON c.id_cliente = e.id_cliente LEFT OUTER JOIN pessoa_fisica f ON f.id_pessoa_fisica = m.id_pessoa_fisica OR f.id_pessoa_fisica = c.id_pessoa_fisica LEFT OUTER JOIN pessoa_juridica j ON j.id_pessoa_juridica = c.id_pessoa_juridica WHERE e.id_entrada_vei_carre = '"+pesquisar+"'"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaCodigoMotorista(self, pesquisa):
        try:
            _sql = "SELECT m.id_motorista, p.nome_razao, p.sobrenome_fantasia, m.cnh, p.cpf_cnpj, p.rg_inscricao, f.expeditor, f.uf, m.pis, f.aniversario, g.sexo, f.mae, f.pai, p.endereco, p.numero, p.complemento, p.bairro, c.nome, e.nome, c.cep, t.descricao, v.marca, v.modelo, v.placa, m.observacao, m.situacao FROM motorista m INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista INNER JOIN categoria_cnh t ON t.id_categoria_cnh = m.id_categoria_cnh INNER JOIN pessoa_fisica f ON f.id_pessoa_fisica = m.id_pessoa_fisica INNER JOIN genero g ON g.id_genero = f.id_genero INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa INNER JOIN cidade c ON c.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = c.id_estado  WHERE m.id_motorista = '"+pesquisa+"' AND v.situacao = 1"
            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaCodigoCliente(self, pesquisa):
        try:
            _sql = "SELECT c.id_cliente, p.nome_razao, p.sobrenome_fantasia, p.cpf_cnpj, p.rg_inscricao, f.expeditor, f.uf, f.aniversario, p.endereco, p.numero, p.complemento, p.bairro, i.nome, e.nome, i.cep, j.site, c.observacao, c.situacao FROM cliente c LEFT OUTER JOIN pessoa_fisica f ON f.id_pessoa_fisica = c.id_pessoa_fisica LEFT OUTER JOIN pessoa_juridica j ON j.id_pessoa_juridica = c.id_pessoa_juridica INNER JOIN pessoa p ON p.id_pessoa = c.id_pessoa INNER JOIN tipo_pessoa t ON t.id_tipo_pessoa = p.id_tipo_pessoa INNER JOIN cidade i ON i.id_cidade = p.id_cidade INNER JOIN estado e ON e.id_estado = i.id_estado WHERE c.id_cliente = '"+pesquisa+"'"

            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def cadastrar(self, entrada):
        try:
            _sql = "INSERT saida_veiculos_caregamento (id_entrada_vei_carre, data, hora) VALUES (%s, %s, %s)"
            _valores = (entrada.getIdEntrada, entrada.getData, entrada.getHora)

            self.__cursor.execute(_sql, _valores)
            self.__cursor.execute("UPDATE entrada_veiculo_carregamento set status = 'Fechado' WHERE id_entrada_vei_carre = '"+entrada.getIdEntrada+"'")
            self.__conexao.conn.commit()
            # self.__cursor.close()
            QMessageBox.information(QWidget(), 'Mensagem', "Saida realizado com sucesso!")
            return  True
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False

    def pesquisarMotoristaCarreRel(self, pesquisa):
        try:
            _sql = "SELECT p.nome_razao FROM entrada_veiculo_carregamento e INNER JOIN tipo_carga g on g.id_tipo_carga = e.id_tipo_carga INNER JOIN produto t ON t.id_produto = e.id_produto INNER JOIN motorista m ON m.id_motorista = e.id_motorista INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista INNER JOIN cliente c ON c.id_cliente = e.id_cliente LEFT OUTER JOIN pessoa_fisica f ON f.id_pessoa_fisica = m.id_pessoa_fisica LEFT OUTER JOIN pessoa_juridica j ON j.id_pessoa_juridica = c.id_pessoa_juridica INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa LEFT OUTER JOIN saida_veiculos_caregamento i ON i.id_entrada_vei_carre = e.id_entrada_vei_carre WHERE e.id_motorista = '"+str(pesquisa)+"'"

            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarClienteCarreRel(self, pesquisa):
        try:
            _sql = "SELECT p.nome_razao FROM entrada_veiculo_carregamento e INNER JOIN tipo_carga g on g.id_tipo_carga = e.id_tipo_carga INNER JOIN produto t ON t.id_produto = e.id_produto INNER JOIN motorista m ON m.id_motorista = e.id_motorista INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista INNER JOIN cliente c ON c.id_cliente = e.id_cliente LEFT OUTER JOIN pessoa_fisica f ON f.id_pessoa_fisica = c.id_pessoa_fisica LEFT OUTER JOIN pessoa_juridica j ON j.id_pessoa_juridica = c.id_pessoa_juridica INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa OR p.id_pessoa = j.id_pessoa LEFT OUTER JOIN saida_veiculos_caregamento i ON i.id_entrada_vei_carre = e.id_entrada_vei_carre WHERE e.id_cliente = '"+str(pesquisa)+"'"

            self.__cursor.execute(_sql)
            result = self.__cursor.fetchone()[0]
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarCodCarreRel(self, pesquisa):
        try:
            _sql = "SELECT e.id_entrada_vei_carre, e.data, e.hora, i.data, i.hora, g.descricao, t.descricao, m.id_motorista, v.marca, v.modelo, v.placa, c.id_cliente FROM entrada_veiculo_carregamento e INNER JOIN tipo_carga g on g.id_tipo_carga = e.id_tipo_carga INNER JOIN produto t ON t.id_produto = e.id_produto INNER JOIN motorista m ON m.id_motorista = e.id_motorista INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista INNER JOIN cliente c ON c.id_cliente = e.id_cliente LEFT OUTER JOIN pessoa_fisica f ON f.id_pessoa_fisica = m.id_pessoa_fisica OR f.id_pessoa_fisica = c.id_pessoa_fisica LEFT OUTER JOIN pessoa_juridica j ON j.id_pessoa_juridica = c.id_pessoa_juridica  LEFT OUTER JOIN saida_veiculos_caregamento i ON i.id_entrada_vei_carre = e.id_entrada_vei_carre WHERE e.id_entrada_vei_carre = '"+pesquisa+"'"

            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarMotoCarreRel(self, pesquisa):
        try:
            _sql = "SELECT e.id_entrada_vei_carre, e.data, e.hora, i.data, i.hora, g.descricao, t.descricao, m.id_motorista, v.marca, v.modelo, v.placa, c.id_cliente FROM entrada_veiculo_carregamento e INNER JOIN tipo_carga g on g.id_tipo_carga = e.id_tipo_carga INNER JOIN produto t ON t.id_produto = e.id_produto INNER JOIN motorista m ON m.id_motorista = e.id_motorista INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista INNER JOIN cliente c ON c.id_cliente = e.id_cliente LEFT OUTER JOIN pessoa_fisica f ON f.id_pessoa_fisica = m.id_pessoa_fisica LEFT OUTER JOIN pessoa_juridica j ON j.id_pessoa_juridica = c.id_pessoa_juridica INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa LEFT OUTER JOIN saida_veiculos_caregamento i ON i.id_entrada_vei_carre = e.id_entrada_vei_carre WHERE p.nome_razao LIKE '%"+pesquisa+"%'"

            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarPlacaCarreRel(self, pesquisa):
        try:
            _sql = "SELECT e.id_entrada_vei_carre, e.data, e.hora, i.data, i.hora, g.descricao, t.descricao, m.id_motorista, v.marca, v.modelo, v.placa, c.id_cliente FROM entrada_veiculo_carregamento e INNER JOIN tipo_carga g on g.id_tipo_carga = e.id_tipo_carga INNER JOIN produto t ON t.id_produto = e.id_produto INNER JOIN motorista m ON m.id_motorista = e.id_motorista INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista INNER JOIN cliente c ON c.id_cliente = e.id_cliente LEFT OUTER JOIN pessoa_fisica f ON f.id_pessoa_fisica = m.id_pessoa_fisica OR f.id_pessoa_fisica = c.id_pessoa_fisica LEFT OUTER JOIN pessoa_juridica j ON j.id_pessoa_juridica = c.id_pessoa_juridica  LEFT OUTER JOIN saida_veiculos_caregamento i ON i.id_entrada_vei_carre = e.id_entrada_vei_carre WHERE v.placa LIKE '%"+pesquisa+"%'"

            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarCargaCarreRel(self, pesquisa):
        try:
            _sql = "SELECT e.id_entrada_vei_carre, e.data, e.hora, i.data, i.hora, g.descricao, t.descricao, m.id_motorista, v.marca, v.modelo, v.placa, c.id_cliente FROM entrada_veiculo_carregamento e INNER JOIN tipo_carga g on g.id_tipo_carga = e.id_tipo_carga INNER JOIN produto t ON t.id_produto = e.id_produto INNER JOIN motorista m ON m.id_motorista = e.id_motorista INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista INNER JOIN cliente c ON c.id_cliente = e.id_cliente LEFT OUTER JOIN pessoa_fisica f ON f.id_pessoa_fisica = m.id_pessoa_fisica OR f.id_pessoa_fisica = c.id_pessoa_fisica LEFT OUTER JOIN pessoa_juridica j ON j.id_pessoa_juridica = c.id_pessoa_juridica  LEFT OUTER JOIN saida_veiculos_caregamento i ON i.id_entrada_vei_carre = e.id_entrada_vei_carre WHERE g.descricao LIKE '%"+pesquisa+"%'"

            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarProdCarreRel(self, pesquisa):
        try:
            _sql = "SELECT e.id_entrada_vei_carre, e.data, e.hora, i.data, i.hora, g.descricao, t.descricao, m.id_motorista, v.marca, v.modelo, v.placa, c.id_cliente FROM entrada_veiculo_carregamento e INNER JOIN tipo_carga g on g.id_tipo_carga = e.id_tipo_carga INNER JOIN produto t ON t.id_produto = e.id_produto INNER JOIN motorista m ON m.id_motorista = e.id_motorista INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista INNER JOIN cliente c ON c.id_cliente = e.id_cliente LEFT OUTER JOIN pessoa_fisica f ON f.id_pessoa_fisica = m.id_pessoa_fisica OR f.id_pessoa_fisica = c.id_pessoa_fisica LEFT OUTER JOIN pessoa_juridica j ON j.id_pessoa_juridica = c.id_pessoa_juridica  LEFT OUTER JOIN saida_veiculos_caregamento i ON i.id_entrada_vei_carre = e.id_entrada_vei_carre WHERE t.descricao LIKE '%"+pesquisa+"%'"

            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarClieCarreRel(self, pesquisa):
        try:
            _sql = "SELECT e.id_entrada_vei_carre, e.data, e.hora, i.data, i.hora, g.descricao, t.descricao, m.id_motorista, v.marca, v.modelo, v.placa, c.id_cliente FROM entrada_veiculo_carregamento e INNER JOIN tipo_carga g on g.id_tipo_carga = e.id_tipo_carga INNER JOIN produto t ON t.id_produto = e.id_produto INNER JOIN motorista m ON m.id_motorista = e.id_motorista INNER JOIN veiculo_motorista v ON v.id_motorista = m.id_motorista INNER JOIN cliente c ON c.id_cliente = e.id_cliente LEFT OUTER JOIN pessoa_fisica f ON f.id_pessoa_fisica = c.id_pessoa_fisica LEFT OUTER JOIN pessoa_juridica j ON j.id_pessoa_juridica = c.id_pessoa_juridica INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa OR p.id_pessoa = j.id_pessoa LEFT OUTER JOIN saida_veiculos_caregamento i ON i.id_entrada_vei_carre = e.id_entrada_vei_carre WHERE p.nome_razao LIKE '%"+pesquisa+"%'"

            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False