import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from controller.getSetEntradaCarre import EntradaCarre
from dao.carregamentoEntradaDao import CarregamentoEntradaDao
from telas.frmEntradaVeiculosCarregamentos import Ui_frmEntradaVeiculosCarregamento

class CarregamentoEntrada(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmEntradaVeiculosCarregamento()
        self.ui.setupUi(self)

        self.ui.btnNovo.clicked.connect(self.botoesNovoCadastro)
        self.ui.btnSalvar.clicked.connect(self.cadastro)
        self.ui.btnCancelar.clicked.connect(self.cancelarCadastro)

        self.ui.txtNomeEmpresaOrigem.returnPressed.connect(self.pesquisarEmpresa)
        self.ui.txtNomeClienteDestinatario.returnPressed.connect(self.pesquisarCliente)
        self.ui.txtNomeMotorista.returnPressed.connect(self.pesquisarMotorista)

        self.ui.txtTipoCarga.currentIndexChanged.connect(self.pesquisaProduto)

    def pesquisarTiposCarga(self):
        __carrEntrada = CarregamentoEntradaDao()
        __carga = __carrEntrada.pesquisarTipoCarga()
        for i in __carga:
            self.ui.txtTipoCarga.addItem(i[0])

    def pesquisaProduto(self):
        __carrEntrada = CarregamentoEntradaDao()
        __produto = __carrEntrada.pesquisarProduto(str(self.ui.txtTipoCarga.currentText()))
        self.ui.txtProduto.clear()
        for i in __produto:
            self.ui.txtProduto.addItem(i[0])


    def pesquisarMotorista(self):
        __carrEntrada = CarregamentoEntradaDao()
        __motorista = __carrEntrada.pesquisarMotorista(str(self.ui.txtNomeMotorista.text()))
        if len(__motorista) == 0:
            self.limparCamposMotorista()
            QMessageBox.warning(QWidget(), 'Mensagem', "Informação de motorista esta incorreto")
        else:
            self.limparCamposMotorista()
            for i in __motorista:
                self.ui.txtidMotorista.setText(str(i[0]))
                self.ui.txtMarcaMotorista.setText(i[1])
                self.ui.txtModeloMotorista.setText(i[2])
                self.ui.txtPlacaMotorista.setText(i[3])
            self.ui.grbDadosClienteDestinatario.setEnabled(True)
            self.ui.txtNomeClienteDestinatario.setFocus()

    def pesquisarCliente(self):
        __carrEntrada = CarregamentoEntradaDao()
        __motorista = __carrEntrada.pesquisarCliente(str(self.ui.txtNomeClienteDestinatario.text()))
        if len(__motorista) == 0:
            self.limparCamposCliente()
            QMessageBox.warning(QWidget(), 'Mensagem', "Informação do cliente esta incorreto")
        else:
            self.limparCamposCliente()
            for i in __motorista:
                self.ui.txtIdClienteDestinatario.setText(str(i[0]))
                self.ui.txtRazaoSocialClienteDestinatario.setText(i[1])
                self.ui.txtCnpjClienteDestinatario.setText(i[2])
                self.ui.txtInscricaoEstaduaClienteDestinatario.setText(i[3])
            self.ui.grbDadosEmpresaOrigem.setEnabled(True)
            self.ui.txtNomeEmpresaOrigem.setFocus()

    def pesquisarEmpresa(self):
        __carrEntrada = CarregamentoEntradaDao()
        __fornecedor = __carrEntrada.pesquisarEmpresa(str(self.ui.txtNomeEmpresaOrigem.text()))
        if len(__fornecedor) == 0:
            self.limparCamposEmpresa()
            QMessageBox.warning(QWidget(), 'Mensagem', "Informação de destinatario esta incorreto")
        else:
            self.limparCamposEmpresa()
            for i in __fornecedor:
                self.ui.txtIdEmpresaOrigem.setText(str(i[0]))
                self.ui.txtRazaoSocialEmpresaOrigem.setText(i[1])
                self.ui.txtCnpjEmpresaOrigem.setText(i[2])
                self.ui.txtInscricaoEstaduaEmpresaOrigem.setText(i[3])

    def botoesNovoCadastro(self):

        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(True)
        self.ui.btnCancelar.setEnabled(True)
        self.ui.btnDeletar.setEnabled(False)
        self.ui.btnEditar.setEnabled(False)

        self.ui.grbDadosMotorista.setEnabled(True)
        self.ui.txtData.setFocus()
        self.ui.txtData.setEnabled(True)
        self.ui.txtHora.setEnabled(True)
        self.ui.txtTipoCarga.setEnabled(True)
        self.ui.txtProduto.setEnabled(True)
        self.pesquisarTiposCarga()

    def botoesCancelarCadastro(self):

        self.ui.btnNovo.setEnabled(True)
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(False)
        self.ui.btnDeletar.setEnabled(False)
        self.ui.btnEditar.setEnabled(False)

        self.ui.grbDadosMotorista.setEnabled(False)
        self.ui.grbDadosClienteDestinatario.setEnabled(False)
        self.ui.grbDadosEmpresaOrigem.setEnabled(False)
        self.ui.txtData.setEnabled(False)
        self.ui.txtHora.setEnabled(False)
        self.ui.txtTipoCarga.setEnabled(False)
        self.ui.txtProduto.setEnabled(False)

    def limparCamposMotorista(self):
        self.ui.txtidMotorista.clear()
        self.ui.txtModeloMotorista.clear()
        self.ui.txtMarcaMotorista.clear()
        self.ui.txtPlacaMotorista.clear()

    def limparCamposCliente(self):
        self.ui.txtIdClienteDestinatario.clear()
        self.ui.txtRazaoSocialClienteDestinatario.clear()
        self.ui.txtInscricaoEstaduaClienteDestinatario.clear()

    def limparCamposEmpresa(self):
        self.ui.txtIdEmpresaOrigem.clear()
        self.ui.txtRazaoSocialEmpresaOrigem.clear()
        self.ui.txtInscricaoEstaduaEmpresaOrigem.clear()

    def limparCampos(self):
        self.ui.txtData.setDate(QDate.currentDate())
        self.ui.txtHora.setTime(QTime.currentTime())
        self.ui.txtTipoCarga.clear()
        self.ui.txtProduto.clear()

        self.ui.txtidMotorista.clear()
        self.ui.txtNomeMotorista.clear()
        self.ui.txtModeloMotorista.clear()
        self.ui.txtMarcaMotorista.clear()
        self.ui.txtPlacaMotorista.clear()

        self.ui.txtIdClienteDestinatario.clear()
        self.ui.txtNomeClienteDestinatario.clear()
        self.ui.txtRazaoSocialClienteDestinatario.clear()
        self.ui.txtInscricaoEstaduaClienteDestinatario.clear()

        self.ui.txtIdEmpresaOrigem.clear()
        self.ui.txtNomeEmpresaOrigem.clear()
        self.ui.txtRazaoSocialEmpresaOrigem.clear()
        self.ui.txtInscricaoEstaduaEmpresaOrigem.clear()

    def cancelarCadastro(self):
        result = QMessageBox.question(QWidget(), 'Menssagem', "Tem certeza que deseja cancelar essa operação?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            self.botoesCancelarCadastro()
            self.limparCampos()


    def cadastro(self):
        if self.ui.txtidMotorista.text() and self.ui.txtNomeMotorista.text() and self.ui.txtMarcaMotorista.text() and self.ui.txtModeloMotorista.text() and self.ui.txtIdClienteDestinatario.text() and self.ui.txtNomeClienteDestinatario.text() and self.ui.txtRazaoSocialClienteDestinatario.text() and self.ui.txtInscricaoEstaduaClienteDestinatario and self.ui.txtIdEmpresaOrigem.text() and self.ui.txtNomeEmpresaOrigem.text() and self.ui.txtRazaoSocialEmpresaOrigem.text() and self.ui.txtInscricaoEstaduaEmpresaOrigem.text() != "":
            __entCarre = CarregamentoEntradaDao()
            data = self.formatarData(self.removerCaracter(self.ui.txtData.text()))
            hora = self.ui.txtHora.text()
            carga = self.ui.txtTipoCarga.currentText()
            produto = self.ui.txtProduto.currentText()
            cargaProduto = __entCarre.pesquisarIdCargaProduto(carga, produto)
            idMotorista = self.ui.txtidMotorista.text()
            idCliente = self.ui.txtIdClienteDestinatario.text()
            idEmpresa = self.ui.txtIdEmpresaOrigem.text()

            __dados = EntradaCarre(data, hora, cargaProduto, idMotorista, idCliente, idEmpresa)
            __cad = __entCarre.cadastrar(__dados)
            if __cad == True:
                self.limparCampos()
                self.botoesCancelarCadastro()

        else:
            QMessageBox.warning(QWidget(), 'Mensagem', "Por Favor preencha todos os campos!")

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
