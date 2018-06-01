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

    def cadastrarNotaFiscal(self, nota):
            try:
                _sql = "INSERT INTO notas_fiscais(serie, numero_nota, data_emissao, data_entrada, valor_total, valor_icms, valor_ipi, alicota_icms, alicota_ipi, cadastrado, id_fornecedor, id_motorista, id_tipo_nf) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                _valores = (nota.getSerie, nota.getNumNotaFiscal, nota.getDataEmissao, nota.getDataEntrada, nota.getValorTotal, nota.getValorIcms, nota.getValorIpi, nota.getAlicotaIcms, nota.getAlicotaIpi, self.__dataHora, nota.getIdFornecedor, nota.getIdMotorista, nota.getIdTipoNf)
                self.__cursor.execute(_sql, _valores)
                self.__conexao.conn.commit()
                # self.__cursor.close()
                QMessageBox.information(QWidget(), 'Mensagem', "Cadastro realizado com sucesso")
            except mysql.connector.Error as e:
                w = QWidget()
                QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
                self.__conexao.conn.rollback()
                return False

    def cadastrarDescricaoProduto(self, descricao):
            try:
                _sql = "INSERT INTO descricao_produto_nota_fiscal(id_notas_fiscais, id_produto, ncm, cst, cfop, csosn, unidade_medida, quantidade, valor_unitario, valor_total, valor_icms, valor_ipi, alicota_icms, alicota_ipi) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                _valores = (descricao.getNotaFiscal, descricao.getIdProduto, descricao.getNcm, descricao.getCst, descricao.getCfop, descricao.getCsosn, descricao.getUn, descricao.getQtd, descricao.getValorUnitario, descricao.getValorTotal, descricao.getValorIcms, descricao.getValorIpi, descricao.getAlicotaIcms, descricao.getAlicotaIpi)
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

    def pesquisarNumNotaFiscal(self, pesquisa):
        try:
            _sql = "SELECT n.id_entrada_notas_fiscais, t.tipo, n.serie, n.numero_nota, n.data_emissao, n.data_entrada, n.valor_total, n.valor_icms, n.valor_ipi, n.alicota_icms, n.alicota_ipi FROM notas_fiscais n INNER JOIN tipo_nf t ON t.id_tipo_nf = n.id_tipo_nf INNER JOIN motorista m ON m.id_motorista = n.id_motorista INNER JOIN fornecedor r ON r.id_fornecedor = n.id_fornecedor WHERE n.numero_nota =  '"+pesquisa+"'"

            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarDataEmitido(self, pesquisa):
        try:
            _sql = "SELECT n.id_entrada_notas_fiscais, t.tipo, n.serie, n.numero_nota, n.data_emissao, n.data_entrada, n.valor_total, n.valor_icms, n.valor_ipi, n.alicota_icms, n.alicota_ipi FROM notas_fiscais n INNER JOIN tipo_nf t ON t.id_tipo_nf = n.id_tipo_nf INNER JOIN motorista m ON m.id_motorista = n.id_motorista INNER JOIN fornecedor r ON r.id_fornecedor = n.id_fornecedor WHERE n.data_emissao =  '"+pesquisa+"'"

            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarDataEntrada(self, pesquisa):
        try:
            _sql = "SELECT n.id_entrada_notas_fiscais, t.tipo, n.serie, n.numero_nota, n.data_emissao, n.data_entrada, n.valor_total, n.valor_icms, n.valor_ipi, n.alicota_icms, n.alicota_ipi FROM notas_fiscais n INNER JOIN tipo_nf t ON t.id_tipo_nf = n.id_tipo_nf INNER JOIN motorista m ON m.id_motorista = n.id_motorista INNER JOIN fornecedor r ON r.id_fornecedor = n.id_fornecedor WHERE n.data_entrada =  '"+pesquisa+"'"

            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarDataPeriodos(self, dataInicio, dataFinal):
        try:
            _sql = "SELECT n.id_entrada_notas_fiscais, t.tipo, n.serie, n.numero_nota, n.data_emissao, n.data_entrada, n.valor_total, n.valor_icms, n.valor_ipi, n.alicota_icms, n.alicota_ipi FROM notas_fiscais n INNER JOIN tipo_nf t ON t.id_tipo_nf = n.id_tipo_nf INNER JOIN motorista m ON m.id_motorista = n.id_motorista INNER JOIN fornecedor r ON r.id_fornecedor = n.id_fornecedor WHERE n.data_entrada > '"+dataInicio+"' AND n.data_entrada <= '"+dataFinal+"' "

            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            #self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarFornecedorNF(self, pesquisar):
        try:
            _sql = "SELECT n.id_fornecedor, p.nome_razao FROM notas_fiscais n INNER JOIN tipo_nf t ON t.id_tipo_nf = n.id_tipo_nf INNER JOIN fornecedor r ON r.id_fornecedor = n.id_fornecedor  LEFT OUTER JOIN pessoa_fisica f ON f.id_pessoa_fisica =  r.id_pessoa_fisica LEFT OUTER JOIN pessoa_juridica j ON j.id_pessoa_juridica = r.id_pessoa_juridica INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa OR p.id_pessoa = r.id_pessoa WHERE n.id_entrada_notas_fiscais = '" + pesquisar+ "' "

            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()[0]
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisarMotoristaNF(self, pesquisar):
        try:
            _sql = "SELECT n.id_motorista, p.nome_razao, p.sobrenome_fantasia FROM notas_fiscais n INNER JOIN tipo_nf t ON t.id_tipo_nf = n.id_tipo_nf INNER JOIN motorista m ON m.id_motorista = n.id_motorista INNER JOIN pessoa_fisica f ON f.id_pessoa_fisica = m.id_pessoa_fisica INNER JOIN pessoa p ON p.id_pessoa = f.id_pessoa WHERE n.id_entrada_notas_fiscais = '" + pesquisar+ "' "

            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()[0]
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def pesquisaDescricaoProduto(self, pesquisar):
        try:
            _sql = "SELECT d.id_desc_pro_nota, d.id_produto, p.descricao, d.ncm, d.cst, d.cfop, d.csosn, d.unidade_medida, d.quantidade, d.valor_unitario, d.valor_total, d.valor_icms, d.valor_ipi, d.alicota_icms, d.alicota_ipi FROM descricao_produto_nota_fiscal d INNER JOIN notas_fiscais n ON n.id_entrada_notas_fiscais = d.id_notas_fiscais INNER JOIN produto p ON p.id_produto = d.id_produto WHERE n.id_entrada_notas_fiscais = '" + pesquisar+ "' "

            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False

    def atualizarNotasFiscais(self, nota):

        try:
            __sql = "UPDATE notas_fiscais SET  serie = %s, numero_nota = %s, data_emissao = %s, data_entrada = %s, valor_total = %s, valor_icms = %s, valor_ipi = %s, alicota_icms = %s, alicota_ipi = %s, alterado = %s, id_fornecedor = %s, id_motorista = %s, id_tipo_nf = %s WHERE  id_entrada_notas_fiscais = %s"
            _valores = (nota.getSerie, nota.getNumNotaFiscal, nota.getDataEmissao, nota.getDataEntrada, nota.getValorTotal, nota.getValorIcms, nota.getValorIpi, nota.getAlicotaIcms, nota.getAlicotaIpi, self.__dataHora, nota.getIdFornecedor, nota.getIdMotorista, nota.getIdTipoNf, nota.getIdNotaFiscal)
            self.__cursor.execute(__sql, _valores)
            self.__conexao.conn.commit()
            QMessageBox.information(QWidget(), 'Mensagem', "Cadastro atualizado com sucesso")
            # self.__cursor.close()
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao atualizar as informações no banco de dados")
            self.__conexao.conn.rollback()
            return False

    def deletarDescricao(self, idDescricao, idNf):

        try:
            _sql = "DELETE FROM descricao_produto_nota_fiscal WHERE id_desc_pro_nota = '" + str(idDescricao) + "' AND id_notas_fiscais = '" + str(idNf )+ "'"
            self.__cursor.execute(_sql)
            self.__conexao.conn.commit()
            # self.__cursor.close()

        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False

    def deletarNF(self, idNf):

        try:
            _sql = "DELETE FROM notas_fiscais WHERE  	id_entrada_notas_fiscais = '" + str(idNf) + "'"
            self.__cursor.execute(_sql)
            self.__conexao.conn.commit()
            # self.__cursor.close()
            return True
        except mysql.connector.Error as e:
            w = QWidget()
            QMessageBox.warning(w, 'Erro', "Erro ao inserir as informações no banco de dados ")
            self.__conexao.conn.rollback()
            return False

    def pesquisarTabelaDescarregamento(self, pesquisar):
        try:
            _sql = "SELECT * FROM entrada_veiculo_descarregamento d INNER JOIN notas_fiscais f ON f.id_entrada_notas_fiscais = d.id_entrada_notas_fiscais WHERE f.id_entrada_notas_fiscais = '" + str(pesquisar) + "' "

            self.__cursor.execute(_sql)
            result = self.__cursor.fetchall()
            # self.__cursor.close()
            return result
        except BaseException as os:
            return False