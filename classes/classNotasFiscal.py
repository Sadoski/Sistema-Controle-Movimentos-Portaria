import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from decimal import Decimal

from controller.getSetDescricaoProduto import DescricaoProduto
from controller.getSetNotaFiscal import NotaFiscal
from controller.getSetRomaneio import Romaneio
from dao.notaFiscalRomaneioDao import NotaFiscalRomanieo
from telas.frmEntradaNotasRomaneios import Ui_frmEntradaNotaRomaneios

class CadastroEmpresa(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmEntradaNotaRomaneios()
        self.ui.setupUi(self)
        self.desc = []

        self.ui.txtNomeEmitente.editingFinished.connect(self.pesquisarFornecedor)
        self.ui.txtFantasiaDestinatario.editingFinished.connect(self.pesquisarEmpresa)
        self.ui.txtNomeMotorista.editingFinished.connect(self.pesquisarMotorista)

        self.ui.txtNomeEmitente.returnPressed.connect(self.focusEmpresa)
        self.ui.txtFantasiaDestinatario.returnPressed.connect(self.focusMotorista)
        self.ui.txtNomeMotorista.returnPressed.connect(self.focusNumNota)
        self.ui.txtNumeroNotaFiscal.returnPressed.connect(self.focusDataEmissao)
        self.ui.txtValorTotal.returnPressed.connect(self.focusNumRomaneio)
        self.ui.txtNumeroRomaneio.returnPressed.connect(self.focusMetragem)
        self.ui.txtQuantidade.returnPressed.connect(self.focusValorUnitario)

        self.ui.btnAdicionar.clicked.connect(self.addDescricaoProduto)
        self.ui.btnExcluir.clicked.connect(self.delDescricaoProduto)

        self.ui.txtTipoCargaServico.currentIndexChanged.connect(self.pesquisaProduto)

        self.ui.btnNovo.clicked.connect(self.botoesNovo)
        self.ui.btnSalvar.clicked.connect(self.cadastrar)
        self.ui.btnCancelar.clicked.connect(self.cancelarCad)

    def focusEmpresa(self):
        self.ui.txtFantasiaDestinatario.setFocus()

    def focusMotorista(self):
        self.ui.txtNomeMotorista.setFocus()

    def focusNumNota(self):
        self.ui.txtNumeroNotaFiscal.setFocus()

    def focusDataEmissao(self):
        self.ui.txtDataEmissao.setFocus()

    def focusValorTotal(self):
        self.ui.txtValorTotal.setFocus()

    def focusNumRomaneio(self):
        self.ui.txtNumeroRomaneio.setFocus()

    def focusMetragem(self):
        self.ui.txtMetragemMadeira.setFocus()

    def focusQuantidade(self):
        self.ui.txtQuantidade.setFocus()

    def focusValorUnitario(self):
        self.ui.txtValorUnitario.setFocus()


    def unidadeMedida(self):
        #lista = ["UN", "KM", "HM", "DAM", "M", "DM", "CM", "MM", "KM²", "HM²", "DAM²", "M²", "DM²", "CM²", "MM²", "KM³", "HM³", "DAM³", "M³", "DM³", "CM³", "MM³", "T", "KG", "HG", "DAG", "G", "DG", "CG", "MG", "KL", "HL", "DAL", "L", "DL", "CL", "ML"]
        lista = ["UN", "M", "M²", "M³", "T", "ST", "L"]
        for i in lista:
            self.ui.txtUn.addItem(i)

    def pesquisarTiposCarga(self):
        __notaRomaneio = NotaFiscalRomanieo()
        __cargo = __notaRomaneio.pesquisarTipoCarga()
        for i in __cargo:
            self.ui.txtTipoCargaServico.addItem(i[0])

    def pesquisarMetragem(self):
        __notaRomaneio = NotaFiscalRomanieo()
        __cargo = __notaRomaneio.pesquisarMetragem()
        for i in __cargo:
            self.ui.txtMetragemMadeira.addItem(i[0])

    def pesquisaProduto(self):
        __notaRomaneio = NotaFiscalRomanieo()
        __produto = __notaRomaneio.pesquisarProduto(str(self.ui.txtTipoCargaServico.currentText()))
        self.ui.txtTipoProdutoServico.clear()
        for i in __produto:
            self.ui.txtTipoProdutoServico.addItem(i[0])

    def limparCamposEmitente(self):
        self.ui.txtIdEmitente.clear()
        self.ui.txtRazaoSocialEmitente.clear()
        self.ui.txtCnpjEmitente.clear()
        self.ui.txtInscricaoEstaduaEmitente.clear()

    def pesquisarFornecedor(self):
        __notaRomaneio = NotaFiscalRomanieo()
        __fornecedor = __notaRomaneio.pesquisarFornecedor(str(self.ui.txtNomeEmitente.text()))
        if len(__fornecedor) == 0:
            self.limparCamposEmitente()
            QMessageBox.warning(QWidget(), 'Mensagem', "Informação de emitente esta incorreto")
        else:
            self.limparCamposEmitente()
            for i in __fornecedor:
                self.ui.txtIdEmitente.setText(str(i[0]))
                self.ui.txtRazaoSocialEmitente.setText(i[1])
                self.ui.txtCnpjEmitente.setText(i[2])
                self.ui.txtInscricaoEstaduaEmitente.setText(i[3])

    def limparCamposDestinatario(self):
        self.ui.txtIdDestinatario.clear()
        self.ui.txtRazaoSocialDestinatario.clear()
        self.ui.txtCnpjDestinatario.clear()
        self.ui.txtInscricaoEstaduaDestinatario.clear()

    def pesquisarEmpresa(self):
        __notaRomaneio = NotaFiscalRomanieo()
        __fornecedor = __notaRomaneio.pesquisarEmpresa(str(self.ui.txtFantasiaDestinatario.text()))
        if len(__fornecedor) == 0:
            self.limparCamposDestinatario()
            QMessageBox.warning(QWidget(), 'Mensagem', "Informação de destinatario esta incorreto")
        else:
            self.limparCamposDestinatario()
            for i in __fornecedor:
                self.ui.txtIdDestinatario.setText(str(i[0]))
                self.ui.txtRazaoSocialDestinatario.setText(i[1])
                self.ui.txtCnpjDestinatario.setText(i[2])
                self.ui.txtInscricaoEstaduaDestinatario.setText(i[3])

    def limparCamposMotorista(self):
        self.ui.txtidMotorista.clear()
        self.ui.txtRg.clear()
        self.ui.txtCpf.clear()
        self.ui.txtMarca.clear()
        self.ui.txtModelo.clear()
        self.ui.txtPlaca.clear()


    def pesquisarMotorista(self):
        __notaRomaneio = NotaFiscalRomanieo()
        __motorista = __notaRomaneio.pesquisarMotorista(str(self.ui.txtNomeMotorista.text()))
        if len(__motorista) == 0:
            self.limparCamposMotorista()
            QMessageBox.warning(QWidget(), 'Mensagem', "Informação de motorista esta incorreto")
        else:
            self.limparCamposMotorista()
            for i in __motorista:
                self.ui.txtidMotorista.setText(str(i[0]))
                self.ui.txtRg.setText(i[1])
                self.ui.txtCpf.setText(i[2])
                self.ui.txtMarca.setText(i[3])
                self.ui.txtModelo.setText(i[4])
                self.ui.txtPlaca.setText(i[5])

    def removerCaracterDinheiro(self, i):
        i = str(i)
        i = i.replace('.', '')
        i = i.replace('R', '')
        i = i.replace('$', '')
        i = i.replace(',', '.')
        i = i.replace(' ', '')
        return i

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

    def addDescricaoProduto(self):
        __carga = str(self.ui.txtTipoCargaServico.currentText())
        __produto = str(self.ui.txtTipoProdutoServico.currentText())
        __un = str(self.ui.txtUn.currentText())
        __qtd = str(self.ui.txtQuantidade.text())
        __valorUni = str(self.removerCaracterDinheiro(self.ui.txtValorUnitario.text()))


        add = [(__carga, __produto, __un, __qtd, __valorUni)]
        self.desc.append([__carga, __produto, __un, __qtd, __valorUni])
        self.inserirTabela(add)

        self.ui.txtQuantidade.clear()
        self.ui.txtValorUnitario.clear()

        self.ui.txtTipoCargaServico.setFocus()

    def inserirTabela(self, dado):

        linha = self.ui.tbProduto.rowCount()
        for info in dado:

            self.ui.tbProduto.insertRow(linha)
            __carga = info[0]
            __produto = info[1]
            __uni = info[2]
            __qtd = info[3]
            __valorUni = info[4]

            self.ui.tbProduto.setItem(linha, 0, QtGui.QTableWidgetItem(str(__carga)))
            self.ui.tbProduto.setItem(linha, 1, QtGui.QTableWidgetItem(str(__produto)))
            self.ui.tbProduto.setItem(linha, 2, QtGui.QTableWidgetItem(str(__uni)))
            self.ui.tbProduto.setItem(linha, 3, QtGui.QTableWidgetItem(str(__qtd)))
            self.ui.tbProduto.setItem(linha, 4, QtGui.QTableWidgetItem(str(__valorUni)))

            linha += 1

    def delDescricaoProduto(self):
        index = self.ui.tbProduto.currentRow()
        self.ui.tbProduto.removeRow(index)
        del self.desc[index]


    def cadastrarNotaFiscal(self):
        __notaFiscal = NotaFiscalRomanieo()
        __idFornecedor = self.ui.txtIdEmitente.text()
        __idEmpresa = self.ui.txtIdDestinatario.text()
        __idMotorista = self.ui.txtidMotorista.text()
        __numeroNotaFiscal = self.ui.txtNumeroNotaFiscal.text()
        __data = self.removerCaracter(self.ui.txtDataEmissao.text())
        __dataEmissao = self.formatarData(__data)
        __valorTotal = self.removerCaracterDinheiro(self.ui.txtValorTotal.text())

        __dadosNota = NotaFiscal(None, __idFornecedor, __idEmpresa, __idMotorista, __numeroNotaFiscal, __dataEmissao, __valorTotal)
        __notaFiscal.cadastrarNotaFiscal(__dadosNota)


    def cadastrarRomaneio(self):
        __notaFiscalRomaneio = NotaFiscalRomanieo()
        __idFornecedor = self.ui.txtIdEmitente.text()
        __idEmpresa = self.ui.txtIdDestinatario.text()
        __idMotorista = self.ui.txtidMotorista.text()
        __numeroNotaFiscal = str(self.ui.txtNumeroNotaFiscal.text())
        __data = self.removerCaracter(self.ui.txtDataEmissao.text())
        __dataEmissao = str(self.formatarData(__data))
        __valorTotal = self.removerCaracterDinheiro(self.ui.txtValorTotal.text())

        __dadosNota = NotaFiscal(None, __idFornecedor, __idEmpresa, __idMotorista, __numeroNotaFiscal, __dataEmissao, __valorTotal)


        __idNotaFiscal = __notaFiscalRomaneio.pesquisarIdNotaFiscal(__dadosNota)
        __numeroRomaneio = self.ui.txtNumeroRomaneio.text()
        __metragem = __notaFiscalRomaneio.pesquisarIdMetragem(self.ui.txtMetragemMadeira.currentText())
        if self.ui.txtCertificada.isChecked():
            __certificada = 1
        else:
            __certificada = 0


        __dadosRomaneio = Romaneio(None, __idNotaFiscal, __numeroRomaneio, __metragem, __certificada)
        __notaFiscalRomaneio.cadastrarRomaneio(__dadosRomaneio)

    def cadastrarDescricaoProduto(self):
        __notaFiscalRomaneio = NotaFiscalRomanieo()
        __idFornecedor = self.ui.txtIdEmitente.text()
        __idEmpresa = self.ui.txtIdDestinatario.text()
        __idMotorista = self.ui.txtidMotorista.text()
        __numeroNotaFiscal = str(self.ui.txtNumeroNotaFiscal.text())
        __data = self.removerCaracter(self.ui.txtDataEmissao.text())
        __dataEmissao = str(self.formatarData(__data))
        __valorTotal = self.removerCaracterDinheiro(self.ui.txtValorTotal.text())

        __dadosNota = NotaFiscal(None, __idFornecedor, __idEmpresa, __idMotorista, __numeroNotaFiscal, __dataEmissao, __valorTotal)

        __idNotaFiscal = __notaFiscalRomaneio.pesquisarIdNotaFiscal(__dadosNota)

        i = 0
        for lista in self.desc:
            a = self.desc[i]

            __carga = __notaFiscalRomaneio.pesquisarIdTipoCarga(a[0])
            __produto = __notaFiscalRomaneio.pesquisarIdProduto(a[1])
            __idCargaProduto = __notaFiscalRomaneio.pesquisarIdCargaProduto(__carga, __produto)
            __unidade = self.substituirCaracterMetros(a[2])
            __qtd = a[3]
            __valor = a[4]

            __descricao = DescricaoProduto(None, __idCargaProduto, __idNotaFiscal, __unidade, __qtd, __valor)
            __notaFiscalRomaneio.cadastrarDescricaoProduto(__descricao)

            i+=1

    def substituirCaracterMetros(self, i):
        i = str(i)
        i = i.replace('²', '2')
        i = i.replace('³', '3')

        return i

    def formatarDataRetorno(self, data):
        dia = data[8:10]
        mes = data[5:7]
        ano = data[:4]

        return QtCore.QDate(int(ano), int(mes), int(dia))

    def formatarData(self, data):
        dia = data[:2]
        mes = data[2:4]
        ano = data[4:8]

        return ("%s-%s-%s" % (ano, mes, dia))

    def limparCamposNotafical(self):
        self.ui.txtNumeroNotaFiscal.clear()
        self.ui.txtDataEmissao.setDate(QDate.currentDate())
        self.ui.txtValorTotal.clear()

    def limparCamposRomaneio(self):
        self.ui.txtNumeroRomaneio.clear()
        self.ui.txtMetragemMadeira.clear()
        self.ui.txtCertificada.setChecked(False)

    def limparCamposDescricao(self):
        self.ui.txtTipoCargaServico.clear()
        self.ui.txtTipoProdutoServico.clear()
        self.ui.txtUn.clear()
        self.ui.txtQuantidade.clear()
        self.ui.txtValorUnitario.clear()

    def cadastrar(self):
        if self.ui.txtIdEmitente.text() != "" and self.ui.txtNomeEmitente.text() != "" and self.ui.txtCnpjEmitente.text() != "" and self.ui.txtCnpjEmitente.text() != "" and self.ui.txtInscricaoEstaduaEmitente.text() != "" and self.ui.txtIdDestinatario.text() != "" and self.ui.txtFantasiaDestinatario.text() != "" and self.ui.txtRazaoSocialDestinatario.text() != "" and self.ui.txtCnpjDestinatario.text() != "" and self.ui.txtInscricaoEstaduaDestinatario.text() != "" and self.ui.txtNomeMotorista.text() != "" and self.ui.txtCpf.text() != "" and self.ui.txtRg.text() != "" and self.ui.txtNumeroRomaneio.text() != "" :

            __valiUnidade = self.calUnidade()
            if __valiUnidade == True:
                __nota = self.cadastrarNotaFiscal()
                __romaneio = self.cadastrarRomaneio()
                __desc = self.cadastrarDescricaoProduto()
                if __nota and __romaneio and __desc == True:
                    QMessageBox.warning(QWidget(), 'Mensagem', "Cadastro realizado com sucesso!")
                    self.limparCamposEmitente()
                    self.limparCamposDestinatario()
                    self.limparCamposMotorista()
                    self.limparCamposNotafical()
                    self.limparCamposRomaneio()
                    self.limparCamposDescricao()
                    self.botoesCancelar()


    def calUnidade(self):
        __valTotal = 0
        i = 0
        for lista in self.desc:
            a = self.desc[i]
            __qtd = int(a[3])
            __valor = Decimal(a[4])
            __valTotal += (__qtd * __valor)

            i += 1
        if __valTotal == Decimal(self.removerCaracterDinheiro(self.ui.txtValorTotal.text())):
            return True
        else:
            QMessageBox.warning(QWidget(), 'Mensagem', "O valor descriminado não confere com o valor total!")
            return False

    def unidadeMedidaCalculo(self):
        if self.ui.txtUn.currentText() == "UN":
            self.calUnidade()
        elif self.ui.txtUn.currentText() == "M":
            self.calUnidade()
        elif self.ui.txtUn.currentText() == "M²":
            self.calUnidade()
        elif self.ui.txtUn.currentText() == "M³":
            self.calUnidade()
        elif self.ui.txtUn.currentText() == "T":
            self.calUnidade()
        elif self.ui.txtUn.currentText() == "ST":
            self.calUnidade()
        elif self.ui.txtUn.currentText() == "L":
            self.calUnidade()
        else:
            QMessageBox.warning(QWidget(), 'Mensagem', "Erro ao calcular unidade e valor")

    def cancelarCad(self):
        self.limparCamposEmitente()
        self.limparCamposDestinatario()
        self.limparCamposMotorista()
        self.limparCamposNotafical()
        self.limparCamposRomaneio()
        self.limparCamposDescricao()
        self.botoesCancelar()

    def botoesNovo(self):
        self.ui.btnNovo.setEnabled(False)

        self.ui.grbDadosDestinatario.setEnabled(True)
        self.ui.grbDadosEmitente.setEnabled(True)
        self.ui.grbDadosMotorista.setEnabled(True)
        self.ui.grbDadosNotaFiscal.setEnabled(True)
        self.ui.grbDadosRomaneio.setEnabled(True)
        self.ui.grbDadosProduto.setEnabled(True)
        self.ui.btnSalvar.setEnabled(True)
        self.ui.btnEditar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(True)
        self.ui.btnDeletar.setEnabled(False)

        self.unidadeMedida()
        self.pesquisarTiposCarga()
        self.pesquisarMetragem()

    def botoesEditar(self):
        self.ui.btnNovo.setEnabled(False)

        self.ui.grbDadosDestinatario.setEnabled(True)
        self.ui.grbDadosEmitente.setEnabled(True)
        self.ui.grbDadosMotorista.setEnabled(True)
        self.ui.grbDadosNotaFiscal.setEnabled(True)
        self.ui.grbDadosRomaneio.setEnabled(True)
        self.ui.grbDadosProduto.setEnabled(True)
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnEditar.setEnabled(True)
        self.ui.btnCancelar.setEnabled(True)
        self.ui.btnDeletar.setEnabled(True)

    def botoesCancelar(self):
        self.ui.btnNovo.setEnabled(True)

        self.ui.grbDadosDestinatario.setEnabled(False)
        self.ui.grbDadosEmitente.setEnabled(False)
        self.ui.grbDadosMotorista.setEnabled(False)
        self.ui.grbDadosNotaFiscal.setEnabled(False)
        self.ui.grbDadosRomaneio.setEnabled(False)
        self.ui.grbDadosProduto.setEnabled(False)
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnEditar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(False)
        self.ui.btnDeletar.setEnabled(False)