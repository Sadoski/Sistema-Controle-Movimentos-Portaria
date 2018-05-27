import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from decimal import Decimal

from classes.classMensagemBox import MensagemBox
from classes.classValidator import Validator
from controller.getSetDescricaoProduto import DescricaoProduto
from controller.getSetFornecedor import Fornecedor
from controller.getSetMotorista import Motorista
from controller.getSetNotaFiscal import NotaFiscal
from controller.getSetPesquisaNotaFiscal import PesquisaNotaFiscal
from controller.getSetRomaneio import Romaneio
from dao.fornecedorDao import FornecedorDao
from dao.motoristaDao import MotoristaDao
from dao.notaFiscalRomaneioDao import NotaFiscalRomanieo
from dao.pesquisaEmpresa import PesquisaEmpresaDao
from dao.pesquisarFornecedor import PesquisarFornecedorDao
from dao.pesquisarMotorista import PesquisarMotoristaDao
from dao.pesquisarNotaFiscalRomaneioDao import PesquisarNotaFiscalRomaneioDao
from telas.frmEntradaNF import Ui_frmEntradaNF, _fromUtf8
from telas.frmEntradaNotasRomaneios import Ui_frmEntradaNotaRomaneios
from telas.frmPesquisarEmpresa import Ui_frmConsultarEmpresa
from telas.frmPesquisarFornecedor import Ui_frmPesquisarFornecedor
from telas.frmPesquisarMotorista import Ui_frmConsultarMotoristas
from telas.frmPesquisarNotasFiscais import Ui_frmConsultarNotasFiscais


class CadastroNotaFiscal(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmEntradaNF()
        self.ui.setupUi(self)
        self.validator = Validator()
        self.mensagem = MensagemBox()
        self.validarCamposFlutuante()
        self.editar = False
        self.desc = []
        self.ncm = []
        self.cfop = []
        self.csosn = []
        self.cst = []
        self.tipos = []
        self.produto = []
        self.decricao = []
        self.removeDescricao = []
        self.atuaDecricao = []

        self.ui.btnNovo.clicked.connect(self.novo)
        #self.ui.btnSalvar.clicked.connect(self.cadastrar)
        self.ui.btnCancelar.clicked.connect(self.cancelar)
        #self.ui.btnEditar.clicked.connect(self.atualizar)
        #self.ui.btnDeletar.clicked.connect(self.deletar)

        self.ui.btnPesquisarMotorista.clicked.connect(self.pesquisarMotoristas)
        self.ui.btnPesquisarFornecedor.clicked.connect(self.pesquisarFornecedores)

        self.ui.btnAdd.clicked.connect(self.addProdutos)
        self.ui.btnRemove.clicked.connect(self.delDescricao)

        self.ui.txtBaseICMS.textChanged.connect(self.validatorChangedDoubleBaseICMS)
        self.ui.txtValorICMS.textChanged.connect(self.validatorChangedDoubleValorICMS)
        self.ui.txtBaseICMSST.textChanged.connect(self.validatorChangedDoubleBaseICMSST)
        self.ui.txtValorICMSSub.textChanged.connect(self.validatorChangedDoubleValorICMSSubs)
        self.ui.txtValorPIS.textChanged.connect(self.validatorChangedDoubleValorPIS)
        self.ui.txtValorConfins.textChanged.connect(self.validatorChangedDoubleValorConfins)
        self.ui.txtValorFrete.textChanged.connect(self.validatorChangedDoubleValorFrete)
        self.ui.txtValorSeguro.textChanged.connect(self.validatorChangedDoubleValorSeguro)
        self.ui.txtValorDesconto.textChanged.connect(self.validatorChangedDoubleValorDesconto)
        self.ui.txtOutrasDespesas.textChanged.connect(self.validatorChangedDoubleOutrasDespesas)
        self.ui.txtValorIPI.textChanged.connect(self.validatorChangedDoubleValorIPI)
        self.ui.txtValorTotalServico.textChanged.connect(self.validatorChangedDoubleValorTotalServico)
        self.ui.txtBaseIssqn.textChanged.connect(self.validatorChangedDoubleBaseIssqn)
        self.ui.txtValorIssqn.textChanged.connect(self.validatorChangedDoubleValorIssqn)
        self.ui.txtValorUnotario.textChanged.connect(self.validatorChangedDoubleValorUnitario)
        self.ui.txtValorTotal.textChanged.connect(self.validatorChangedDoubleValorTotal)
        self.ui.txtSomatoriaTotalValor.textChanged.connect(self.validatorChangedDoubleSomatoriaTotal)


        self.ui.txtCodig.textChanged.connect(self.numberCodigoFornecedor)
        self.ui.txtCodigoMotorista.textChanged.connect(self.numberCodigoMotorista)
        self.ui.txtSerie.textChanged.connect(self.numberSerie)
        self.ui.txtModelo.textChanged.connect(self.numberModelo)
        self.ui.txtNumNF.textChanged.connect(self.numberNumNF)
        self.ui.txtQtd.textChanged.connect(self.numberQuantidade)
        self.ui.txtInsMunicipal.textChanged.connect(self.numberInsMunicipal)

        self.ui.txtValorTotal.editingFinished.connect(self.setFloatDecimalValorTotal)
        self.ui.txtValorUnotario.editingFinished.connect(self.setFloatDecimalValorUni)

        self.ui.txtCodig.returnPressed.connect(self.setFornecedor)
        self.ui.txtCodigoMotorista.returnPressed.connect(self.setMotorista)

        self.ui.txtCodig.editingFinished.connect(self.setFornecedorFinish)
        self.ui.txtCodigoMotorista.editingFinished.connect(self.setMotoristaFinish)
        self.ui.txtValorUnotario.editingFinished.connect(self.somarUniValor)

    def somarUniValor(self):

        self.ui.txtValorTotal.setText(str(int(self.ui.txtQtd.text())*float(self.reformatar(self.ui.txtValorUnotario.text()))))

    def totalNf(self):
        if self.ui.txtSomatoriaTotalValor.text() == "":
            total = 0
        else:
            total = float(self.reformatar(self.ui.txtSomatoriaTotalValor.text()))

        soma = int(self.ui.txtQtd.text()) * float(self.reformatar(self.ui.txtValorUnotario.text()))

        result = total+soma

        self.ui.txtSomatoriaTotalValor.setText(str(self.alterarCaracter(str(result)+self.setDecimal(str(result)))))

    def subtrairTotal(self, soma):
        total = float(self.reformatar(self.ui.txtSomatoriaTotalValor.text()))

        result = total - float(self.reformatar(soma))

        self.ui.txtSomatoriaTotalValor.setText(str(self.alterarCaracter(str(result)+self.setDecimal(str(result)))))

    def novo(self):
        self.ui.grbFornecedor.setEnabled(True)
        self.ui.grbTransportadoraMotorista.setEnabled(True)
        self.ui.grbData.setEnabled(True)
        self.ui.grbDadosNF.setEnabled(True)
        self.ui.grbImpostos.setEnabled(True)
        self.ui.grbCalculoImposto.setEnabled(True)
        self.ui.grbIssqn.setEnabled(True)
        self.ui.grbDescricaoProduto.setEnabled(True)

        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(True)
        self.ui.btnEditar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(True)
        self.ui.btnDeletar.setEnabled(False)

        self.unidadeMedida()
        self.tiposNF()
        self.setNcm()
        self.setCfop()
        self.setCsosn()
        self.setCst()
        self.setProdutos()

    def cancelar(self):
        self.limparCampos()
        self.ui.grbFornecedor.setEnabled(False)
        self.ui.grbTransportadoraMotorista.setEnabled(False)
        self.ui.grbData.setEnabled(False)
        self.ui.grbDadosNF.setEnabled(False)
        self.ui.grbImpostos.setEnabled(False)
        self.ui.grbCalculoImposto.setEnabled(False)
        self.ui.grbIssqn.setEnabled(False)
        self.ui.grbDescricaoProduto.setEnabled(False)

        self.ui.btnNovo.setEnabled(True)
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnEditar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(False)
        self.ui.btnDeletar.setEnabled(False)

    def validarCamposFlutuante(self):

        validarReal = QtGui.QDoubleValidator(0.00, 999999999.99, 2, self)
        validarReal.setNotation(QtGui.QDoubleValidator.StandardNotation)
        validarReal.setDecimals(2)

        listaObj = [self.ui.txtBaseICMS,  self.ui.txtValorICMS, self.ui.txtBaseICMSST,
                    self.ui.txtValorICMSSub, self.ui.txtValorPIS, self.ui.txtValorConfins, self.ui.txtValorFrete,
                    self.ui.txtValorSeguro, self.ui.txtValorDesconto, self.ui.txtOutrasDespesas, self.ui.txtValorIPI,
                    self.ui.txtValorUnotario, self.ui.txtValorTotal, self.ui.txtValorTotalServico, self.ui.txtBaseIssqn, self.ui.txtValorIssqn]

        for objeto in listaObj:
            objeto.setValidator(validarReal)

    def validarCamposInteiro(self):

        validarReal = QtGui.QIntValidator(0, 999999999, self)

        listaObj = [self.ui.txtCodig, self.ui.txtCodigoMotorista, self.ui.txtSerie, self.ui.txtNumNF, self.ui.txtModelo,
                    self.ui.txtQtd, self.ui.txtInsMunicipal]

        for objeto in listaObj:
            objeto.setValidator(validarReal)

    def alterarCaracterNum(self, i):
        i = i.replace('0', '')
        i = i.replace('1', '')
        i = i.replace('2', '')
        i = i.replace('3', '')
        i = i.replace('4', '')
        i = i.replace('5', '')
        i = i.replace('6', '')
        i = i.replace('7', '')
        i = i.replace('8', '')
        i = i.replace('9', '')

        return  i

    def alterarCaracter(self, i):
        i = i.replace('-', '')
        i = i.replace('+', '')
        i = i.replace('.', ',')

        return i

    def reformatar(self, i):
        i = i.replace(',', '.')
        return i


    def validatorChangedDoubleBaseICMS(self):
        ponto = self.alterarCaracterNum(self.ui.txtBaseICMS.text())

        if len(ponto) >1:
            self.ui.txtBaseICMS.backspace()
        elif len(ponto) == 1:
            self.ui.txtBaseICMS.setText(self.alterarCaracter(self.ui.txtBaseICMS.text()))
            numero = self.reformatar(self.ui.txtBaseICMS.text())
            formatar = str(numero).split('.')
            if len(formatar[1]) >2:
                self.ui.txtBaseICMS.backspace()

    def validatorChangedDoubleValorICMS(self):
        ponto = self.alterarCaracterNum(self.ui.txtValorICMS.text())

        if len(ponto) >1:
            self.ui.txtValorICMS.backspace()
        elif len(ponto) == 1:
            self.ui.txtValorICMS.setText(self.alterarCaracter(self.ui.txtValorICMS.text()))
            numero = self.reformatar(self.ui.txtValorICMS.text())
            formatar = str(numero).split('.')
            if len(formatar[1]) >2:
                self.ui.txtValorICMS.backspace()

    def validatorChangedDoubleBaseICMSST(self):
        ponto = self.alterarCaracterNum(self.ui.txtBaseICMSST.text())

        if len(ponto) >1:
            self.ui.txtBaseICMSST.backspace()
        elif len(ponto) == 1:
            self.ui.txtBaseICMSST.setText(self.alterarCaracter(self.ui.txtBaseICMSST.text()))
            numero = self.reformatar(self.ui.txtBaseICMSST.text())
            formatar = str(numero).split('.')
            if len(formatar[1]) >2:
                self.ui.txtBaseICMSST.backspace()

    def validatorChangedDoubleValorICMSSubs(self):
        ponto = self.alterarCaracterNum(self.ui.txtValorICMSSub.text())

        if len(ponto) >1:
            self.ui.txtValorICMSSub.backspace()
        elif len(ponto) == 1:
            self.ui.txtValorICMSSub.setText(self.alterarCaracter(self.ui.txtValorICMSSub.text()))
            numero = self.reformatar(self.ui.txtValorICMSSub.text())
            formatar = str(numero).split('.')
            if len(formatar[1]) >2:
                self.ui.txtValorICMSSub.backspace()

    def validatorChangedDoubleValorPIS(self):
        ponto = self.alterarCaracterNum(self.ui.txtValorPIS.text())

        if len(ponto) >1:
            self.ui.txtValorPIS.backspace()
        elif len(ponto) == 1:
            self.ui.txtValorPIS.setText(self.alterarCaracter(self.ui.txtValorPIS.text()))
            numero = self.reformatar(self.ui.txtValorPIS.text())
            formatar = str(numero).split('.')
            if len(formatar[1]) >2:
                self.ui.txtValorPIS.backspace()

    def validatorChangedDoubleValorConfins(self):
        ponto = self.alterarCaracterNum(self.ui.txtValorConfins.text())

        if len(ponto) >1:
            self.ui.txtValorConfins.backspace()
        elif len(ponto) == 1:
            self.ui.txtValorConfins.setText(self.alterarCaracter(self.ui.txtValorConfins.text()))
            numero = self.reformatar(self.ui.txtValorConfins.text())
            formatar = str(numero).split('.')
            if len(formatar[1]) >2:
                self.ui.txtValorConfins.backspace()

    def validatorChangedDoubleValorFrete(self):
        ponto = self.alterarCaracterNum(self.ui.txtValorFrete.text())

        if len(ponto) >1:
            self.ui.txtValorFrete.backspace()
        elif len(ponto) == 1:
            self.ui.txtValorFrete.setText(self.alterarCaracter(self.ui.txtValorFrete.text()))
            numero = self.reformatar(self.ui.txtValorFrete.text())
            formatar = str(numero).split('.')
            if len(formatar[1]) >2:
                self.ui.txtValorFrete.backspace()

    def validatorChangedDoubleValorSeguro(self):
        ponto = self.alterarCaracterNum(self.ui.txtValorSeguro.text())

        if len(ponto) >1:
            self.ui.txtValorSeguro.backspace()
        elif len(ponto) == 1:
            self.ui.txtValorSeguro.setText(self.alterarCaracter(self.ui.txtValorSeguro.text()))
            numero = self.reformatar(self.ui.txtValorSeguro.text())
            formatar = str(numero).split('.')
            if len(formatar[1]) >2:
                self.ui.txtValorSeguro.backspace()

    def validatorChangedDoubleValorDesconto(self):
        ponto = self.alterarCaracterNum(self.ui.txtValorDesconto.text())

        if len(ponto) >1:
            self.ui.txtValorDesconto.backspace()
        elif len(ponto) == 1:
            self.ui.txtValorDesconto.setText(self.alterarCaracter(self.ui.txtValorDesconto.text()))
            numero = self.reformatar(self.ui.txtValorDesconto.text())
            formatar = str(numero).split('.')
            if len(formatar[1]) >2:
                self.ui.txtValorDesconto.backspace()

    def validatorChangedDoubleOutrasDespesas(self):
        ponto = self.alterarCaracterNum(self.ui.txtOutrasDespesas.text())

        if len(ponto) >1:
            self.ui.txtOutrasDespesas.backspace()
        elif len(ponto) == 1:
            self.ui.txtOutrasDespesas.setText(self.alterarCaracter(self.ui.txtOutrasDespesas.text()))
            numero = self.reformatar(self.ui.txtOutrasDespesas.text())
            formatar = str(numero).split('.')
            if len(formatar[1]) >2:
                self.ui.txtOutrasDespesas.backspace()

    def validatorChangedDoubleValorIPI(self):
        ponto = self.alterarCaracterNum(self.ui.txtValorIPI.text())

        if len(ponto) >1:
            self.ui.txtValorIPI.backspace()
        elif len(ponto) == 1:
            self.ui.txtValorIPI.setText(self.alterarCaracter(self.ui.txtValorIPI.text()))
            numero = self.reformatar(self.ui.txtValorIPI.text())
            formatar = str(numero).split('.')
            if len(formatar[1]) >2:
                self.ui.txtValorIPI.backspace()

    def validatorChangedDoubleValorTotalServico(self):
        ponto = self.alterarCaracterNum(self.ui.txtValorTotalServico.text())

        if len(ponto) >1:
            self.ui.txtValorTotalServico.backspace()
        elif len(ponto) == 1:
            self.ui.txtValorTotalServico.setText(self.alterarCaracter(self.ui.txtValorTotalServico.text()))
            numero = self.reformatar(self.ui.txtValorTotalServico.text())
            formatar = str(numero).split('.')
            if len(formatar[1]) >2:
                self.ui.txtValorTotalServico.backspace()

    def validatorChangedDoubleBaseIssqn(self):
        ponto = self.alterarCaracterNum(self.ui.txtBaseIssqn.text())

        if len(ponto) >1:
            self.ui.txtBaseIssqn.backspace()
        elif len(ponto) == 1:
            self.ui.txtBaseIssqn.setText(self.alterarCaracter(self.ui.txtBaseIssqn.text()))
            numero = self.reformatar(self.ui.txtBaseIssqn.text())
            formatar = str(numero).split('.')
            if len(formatar[1]) >2:
                self.ui.txtBaseIssqn.backspace()

    def validatorChangedDoubleValorIssqn(self):
        ponto = self.alterarCaracterNum(self.ui.txtValorIssqn.text())

        if len(ponto) >1:
            self.ui.txtValorIssqn.backspace()
        elif len(ponto) == 1:
            self.ui.txtValorIssqn.setText(self.alterarCaracter(self.ui.txtValorIssqn.text()))
            numero = self.reformatar(self.ui.txtValorIssqn.text())
            formatar = str(numero).split('.')
            if len(formatar[1]) >2:
                self.ui.txtValorIssqn.backspace()

    def validatorChangedDoubleValorUnitario(self):
        ponto = self.alterarCaracterNum(self.ui.txtValorUnotario.text())

        if len(ponto) >1:
            self.ui.txtValorUnotario.backspace()
        elif len(ponto) == 1:
            self.ui.txtValorUnotario.setText(self.alterarCaracter(self.ui.txtValorUnotario.text()))
            numero = self.reformatar(self.ui.txtValorUnotario.text())
            formatar = str(numero).split('.')
            if len(formatar[1]) >2:
                self.ui.txtValorUnotario.backspace()

    def validatorChangedDoubleValorTotal(self):
        ponto = self.alterarCaracterNum(self.ui.txtValorTotal.text())

        if len(ponto) >1:
            self.ui.txtValorTotal.backspace()
        elif len(ponto) == 1:
            self.ui.txtValorTotal.setText(self.alterarCaracter(self.ui.txtValorTotal.text()))
            numero = self.reformatar(self.ui.txtValorTotal.text())
            formatar = str(numero).split('.')
            if len(formatar[1]) >2:
                self.ui.txtValorTotal.backspace()

    def validatorChangedDoubleSomatoriaTotal(self):
        ponto = self.alterarCaracterNum(self.ui.txtSomatoriaTotalValor.text())

        if len(ponto) >1:
            self.ui.txtSomatoriaTotalValor.backspace()
        elif len(ponto) == 1:
            self.ui.txtSomatoriaTotalValor.setText(self.alterarCaracter(self.ui.txtSomatoriaTotalValor.text()))
            numero = self.reformatar(self.ui.txtSomatoriaTotalValor.text())
            formatar = str(numero).split('.')
            if len(formatar[1]) >2:
                self.ui.txtSomatoriaTotalValor.backspace()

    def numberCodigoFornecedor(self):
        if self.ui.txtCodig.text().isnumeric() == False:
            self.ui.txtCodig.backspace()

    def numberCodigoMotorista(self):
        if self.ui.txtCodigoMotorista.text().isnumeric() == False:
            self.ui.txtCodigoMotorista.backspace()

    def numberSerie(self):
        if self.ui.txtSerie.text().isnumeric() == False:
            self.ui.txtSerie.backspace()

    def numberNumNF(self):
        if self.ui.txtNumNF.text().isnumeric() == False:
            self.ui.txtNumNF.backspace()

    def numberModelo(self):
        if self.ui.txtModelo.text().isnumeric() == False:
            self.ui.txtModelo.backspace()

    def numberQuantidade(self):
        if self.ui.txtQtd.text().isnumeric() == False:
            self.ui.txtQtd.backspace()

    def numberInsMunicipal(self):
        if self.ui.txtInsMunicipal.text().isnumeric() == False:
            self.ui.txtInsMunicipal.backspace()

    def unidadeMedida(self):
        lista = ["UN", "KM", "HM", "DAM", "M", "M²", "M³", "DM", "CM", "MM", "KM²", "HM²", "DAM²", "DM²", "CM²", "MM²", "MM³", "KM³", "HM³", "DAM³", "DM³", "CM³", "MM³", "T", "KG", "HG", "DAG", "G", "DG", "CG", "MG", "KL", "HL", "DAL", "L", "DL", "CL", "ML", "ST"]
        #lista = ["UN", "M", "M²", "M³", "T", "ST", "L"]

        for i in lista:
            self.ui.cBoxUn.addItem(i)

    def tiposNF(self):
        nf = NotaFiscalRomanieo()
        tipo = nf.pesquisarNf()
        for i in tipo:
            self.ui.cboxTipos.addItem(str(i[1]))
        self.tipos.append(tipo)

    def setNcm(self):
        nf = NotaFiscalRomanieo()
        ncm = nf.pesquisarNcm()
        for i in ncm:
            self.ui.cBoxNcm.addItem(str(i[1]))
        self.ncm.append(ncm)

    def setCfop(self):
        nf = NotaFiscalRomanieo()
        cfop = nf.pesquisarCfop()
        for i in cfop:
            self.ui.cBoxCfop.addItem(str(i[0]))
        self.cfop.append(cfop)

    def setCsosn(self):
        nf = NotaFiscalRomanieo()
        csosn = nf.pesquisarCsosn()
        for i in csosn:
            self.ui.cBoxCsosn.addItem(str(i[1]))
        self.csosn.append(csosn)

    def setCst(self):
        nf = NotaFiscalRomanieo()
        cst = nf.pesquisarCst()
        for i in cst:
            self.ui.cBoxCst.addItem(str(i[1]))
        self.cst.append(cst)

    def setProdutos(self):
        nf = NotaFiscalRomanieo()
        produto = nf.pesquisarProduto()
        for i in produto:
            self.ui.cBoxProduto.addItem(str(i[1]))
        self.produto.append(produto)

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

    def formataData(self, data):
        dia = data[:2]
        mes = data[2:4]
        ano = data[4:8]

        return ("%s%s%s" % (ano, mes, dia))

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

    def removerCaracterDin(self, i):
        i = str(i)
        i = i.replace('.', '')
        i = i.replace('R', '')
        i = i.replace('$', '')
        i = i.replace(',', '')
        i = i.replace(' ', '')
        return i

    def limparCampos(self):
        self.ui.txtCodig.clear()
        self.ui.txtFornecedor.clear()
        self.ui.txtCodigoMotorista.clear()
        self.ui.txtMotorista.clear()
        self.ui.txtSerie.clear()
        self.ui.txtModelo.clear()
        self.ui.txtNumNF.clear()
        self.ui.dateDataEmissao.setDate(QDate.currentDate())
        self.ui.dateDataEntrada.setDate(QDate.currentDate())

        self.ui.txtBaseICMS.clear()
        self.ui.txtValorICMS.clear()
        self.ui.txtBaseICMSST.clear()
        self.ui.txtValorICMSSub.clear()
        self.ui.txtValorPIS.clear()
        self.ui.txtValorConfins.clear()
        self.ui.txtValorFrete.clear()
        self.ui.txtValorSeguro.clear()
        self.ui.txtValorDesconto.clear()
        self.ui.txtOutrasDespesas.clear()
        self.ui.txtValorIPI.clear()

        self.ui.txtQtd.clear()
        self.ui.txtValorUnotario.clear()
        self.ui.txtValorTotal.clear()

        self.ui.txtSomatoriaTotalValor.clear()

        self.ui.txtInsMunicipal.clear()
        self.ui.txtValorTotalServico.clear()
        self.ui.txtBaseIssqn.clear()
        self.ui.txtValorIssqn.clear()

        self.ui.cBoxNcm.clear()
        self.ui.cBoxCfop.clear()
        self.ui.cBoxCsosn.clear()
        self.ui.cBoxCst.clear()
        self.ui.cBoxProduto.clear()
        self.ui.cBoxUn.clear()
        self.ui.cboxTipos.clear()

    def pesquisarMotoristas(self):
            self.dialogMotoristas = QDialog(self)
            self.__pesquisarMotorista = Ui_frmConsultarMotoristas()
            self.__pesquisarMotorista.setupUi(self.dialogMotoristas)

            self.__pesquisarMotorista.txtPesquisar.setValidator(self.validator)

            self.__pesquisarMotorista.txtPesquisar.returnPressed.connect(self.pesquisarMotorista)

            self.__pesquisarMotorista.btnPesquisar.clicked.connect(self.pesquisarMotorista)

            self.__pesquisarMotorista.tabPesquisar.doubleClicked.connect(self.setarCamposMotorista)

            self.dialogMotoristas.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            self.dialogMotoristas.exec_()

    def pesquisarMotorista(self):
        __pesDao = MotoristaDao()
        if self.__pesquisarMotorista.radBtnCodigo.isChecked():
                __codigo = self.__pesquisarMotorista.txtPesquisar.text()
                __retorno = __pesDao.pesquisaCodigoFisica(__codigo)
                self.setarTabelaPesquisaEditarMotorista(__retorno)

        elif self.__pesquisarMotorista.radBtnNome.isChecked():
                __razao = self.__pesquisarMotorista.txtPesquisar.text()
                __retorno = __pesDao.pesquisarNomeFisica(__razao)
                self.setarTabelaPesquisaEditarMotorista(__retorno)

        elif self.__pesquisarMotorista.radBtnCpf.isChecked():
                __fantasia = self.__pesquisarMotorista.txtPesquisar.text()
                __retorno = __pesDao.pesquisaCpfFisica(__fantasia)
                self.setarTabelaPesquisaEditarMotorista(__retorno)

        elif self.__pesquisarMotorista.radBtnRg.isChecked():
                __cnpj = self.__pesquisarMotorista.txtPesquisar.text()
                __retorno = __pesDao.pesquisaRgFisica(__cnpj)
                self.setarTabelaPesquisaEditarMotorista(__retorno)

        elif self.__pesquisarMotorista.radBtnNumCarteira.isChecked():
                __inscricao = self.__pesquisarMotorista.txtPesquisar.text()
                __retorno = __pesDao.pesquisaNumCarteira(__inscricao)
                self.setarTabelaPesquisaEditarMotorista(__retorno)

        elif self.__pesquisarMotorista.radBtnPis.isChecked():
                __inscricao = self.__pesquisarMotorista.txtPesquisar.text()
                __retorno = __pesDao.pesquisaPis(__inscricao)
                self.setarTabelaPesquisaEditarMotorista(__retorno)

        else:
            self.mensagem.warning( 'Atenção', "Selecione uma das opções de pesquisa")

    def setarTabelaPesquisaEditarMotorista(self, __retorno):
        qtde_registros = len(__retorno)
        self.__pesquisarMotorista.tabPesquisar.setRowCount(qtde_registros)

        linha = 0
        for pesqui in __retorno:
            # capturando os dados da tupla

            codigo = pesqui[0]
            nome = pesqui[1]
            apelido = pesqui[2]
            cnh = pesqui[3]
            cpf = pesqui[4]
            rg = pesqui[5]
            expeditor = pesqui[6]
            uf = pesqui[7]
            pis = pesqui[8]
            aniversario = pesqui[9]
            genero = pesqui[10]
            mae = pesqui[11]
            pai = pesqui[12]
            endereco = pesqui[13]
            numero = pesqui[14]
            complemento = pesqui[15]
            bairro = pesqui[16]
            cidade = pesqui[17]
            estado = pesqui[18]
            cep = pesqui[19]
            categoria = pesqui[20]
            marca = pesqui[21]
            modelo = pesqui[22]
            placa = pesqui[23]
            obs = pesqui[24]
            if pesqui[25] == 1:
                situacao = "Ativo"
            else:
                situacao = "Inativo"


            # preenchendo o grid de pesquisa
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(nome)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(apelido)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 3, QtGui.QTableWidgetItem(str(cnh)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 4, QtGui.QTableWidgetItem(str(cpf)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 5, QtGui.QTableWidgetItem(str(rg)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 6, QtGui.QTableWidgetItem(str(expeditor)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 7, QtGui.QTableWidgetItem(str(uf)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 8, QtGui.QTableWidgetItem(str(pis)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 9, QtGui.QTableWidgetItem(str(aniversario)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 10, QtGui.QTableWidgetItem(str(genero)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 11, QtGui.QTableWidgetItem(str(mae)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 12, QtGui.QTableWidgetItem(str(pai)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 13, QtGui.QTableWidgetItem(str(endereco)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 14, QtGui.QTableWidgetItem(str(numero)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 15, QtGui.QTableWidgetItem(str(complemento)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 16, QtGui.QTableWidgetItem(str(bairro)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 17, QtGui.QTableWidgetItem(str(cidade)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 18, QtGui.QTableWidgetItem(str(estado)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 19, QtGui.QTableWidgetItem(str(cep)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 20, QtGui.QTableWidgetItem(str(categoria)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 21, QtGui.QTableWidgetItem(str(marca)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 22, QtGui.QTableWidgetItem(str(modelo)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 23, QtGui.QTableWidgetItem(str(placa)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 24, QtGui.QTableWidgetItem(str(obs)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 25, QtGui.QTableWidgetItem(str(situacao)))

            linha += 1

    def setarCamposMotorista(self):
        motoDao = MotoristaDao()
        itens = []

        for item in self.__pesquisarMotorista.tabPesquisar.selectedItems():
            itens.append(item.text())

        codigo = itens[0]
        nome = itens[1]
        sobrenome = itens[2]
        cnh = itens[3]
        cpf = itens[4]
        rg = itens[5]
        expeditor = itens[6]
        uf = itens[7]
        pis = itens[8]
        data = itens[9]
        sexo = itens[10]
        mae = itens[11]
        pai = itens[12]
        endereco = itens[13]
        numero = itens[14]
        complemento = itens[15]
        bairro = itens[16]
        cidade = itens[17]
        estado = itens[18]
        cep = itens[19]
        categoria = itens[20]
        marca = itens[21]
        modelo = itens[22]
        placa = itens[23]
        obs = itens[24]
        if itens[25] == 'Ativo':
            situacao = True
        else:
            situacao = False


        __dados = Motorista(codigo, None, None, nome, sobrenome, rg, cpf, pis, cnh, categoria, marca, modelo, placa, obs, situacao)
        self.setCamposMotorista(__dados)
        self.dialogMotoristas.close()


    def setCamposMotorista(self, campos):
        self.ui.txtCodigoMotorista.setText(campos.getIdMotorista)
        self.ui.txtMotorista.setText(campos.getNome + " " + campos.getSobrenome)

    def pesquisarFornecedores(self):
        self.dialogFornecedores = QDialog(self)
        self.__pesquisarFornecedor = Ui_frmPesquisarFornecedor()
        self.__pesquisarFornecedor.setupUi(self.dialogFornecedores)

        self.__pesquisarFornecedor.txtPesquisar.setValidator(self.validator)

        self.__pesquisarFornecedor.txtPesquisar.returnPressed.connect(self.pesquisarFornecedor)

        self.__pesquisarFornecedor.btnPesquisar.clicked.connect(self.pesquisarFornecedor)

        self.__pesquisarFornecedor.tabPesquisar.doubleClicked.connect(self.setarCamposFornecedor)

        self.dialogFornecedores.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.dialogFornecedores.exec_()

    def pesquisarFornecedor(self):
        __pesDao = FornecedorDao()
        if self.__pesquisarFornecedor.radBtnCodigo.isChecked():
            __codigo = self.__pesquisarFornecedor.txtPesquisar.text()
            __retorno = __pesDao.pesquisaCodigoFisica(__codigo)
            self.setarTabelaPesquisaEditarFornecedor(__retorno)

        elif self.__pesquisarFornecedor.radBtnRazaoSocial.isChecked():
            __razao = self.__pesquisarFornecedor.txtPesquisar.text()
            __retorno = __pesDao.pesquisarNomeFisica(__razao)
            self.setarTabelaPesquisaEditarFornecedor(__retorno)

        elif self.__pesquisarFornecedor.radBtnFantasia.isChecked():
            __fantasia = self.__pesquisarFornecedor.txtPesquisar.text()
            __retorno = __pesDao.pesquisaApelidoFisica(__fantasia)
            self.setarTabelaPesquisaEditarFornecedor(__retorno)

        elif self.__pesquisarFornecedor.radBtnCnpj.isChecked():
            __cnpj = self.__pesquisarFornecedor.txtPesquisar.text()
            __retorno = __pesDao.pesquisaCpfFisica(__cnpj)
            self.setarTabelaPesquisaEditar(__retorno)

        elif self.__pesquisarFornecedor.radBtnInsEstadual.isChecked():
            __inscricao = self.__pesquisarFornecedor.txtPesquisar.text()
            __retorno = __pesDao.pesquisaRgFisica(__inscricao)
            self.setarTabelaPesquisaEditarFornecedor(__retorno)

        else:
            self.mensagem.warning('Atenção', "Selecione uma das opções de pesquisa")

    def setarTabelaPesquisaEditarFornecedor(self, __retorno):
        qtde_registros = len(__retorno)
        self.__pesquisarFornecedor.tabPesquisar.setRowCount(qtde_registros)

        linha = 0
        for pesqui in __retorno:
            # capturando os dados da tupla

            codigo = pesqui[0]
            tipo = pesqui[1]
            nome = pesqui[2]
            apelido = pesqui[3]
            cpf = pesqui[4]
            rg = pesqui[5]
            expeditor = pesqui[6]
            uf = pesqui[7]
            aniversario = pesqui[8]
            endereco = pesqui[9]
            numero = pesqui[10]
            complemento = pesqui[11]
            bairro = pesqui[12]
            cidade = pesqui[13]
            estado = pesqui[14]
            cep = pesqui[15]
            site = pesqui[16]
            obs = pesqui[17]
            if pesqui[18] == 1:
                situacao = "Ativo"
            else:
                situacao = "Inativo"


            # preenchendo o grid de pesquisa
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(tipo)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(nome)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 3, QtGui.QTableWidgetItem(str(apelido)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 4, QtGui.QTableWidgetItem(str(cpf)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 5, QtGui.QTableWidgetItem(str(rg)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 6, QtGui.QTableWidgetItem(str(expeditor)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 7, QtGui.QTableWidgetItem(str(uf)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 8, QtGui.QTableWidgetItem(str(aniversario)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 9, QtGui.QTableWidgetItem(str(endereco)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 10, QtGui.QTableWidgetItem(str(numero)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 11, QtGui.QTableWidgetItem(str(complemento)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 12, QtGui.QTableWidgetItem(str(bairro)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 13, QtGui.QTableWidgetItem(str(cidade)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 14, QtGui.QTableWidgetItem(str(estado)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 15, QtGui.QTableWidgetItem(str(cep)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 16, QtGui.QTableWidgetItem(str(site)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 17, QtGui.QTableWidgetItem(str(obs)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 18, QtGui.QTableWidgetItem(str(situacao)))

            linha += 1

    def setarCamposFornecedor(self):
        itens = []

        for item in self.__pesquisarFornecedor.tabPesquisar.selectedItems():
            itens.append(item.text())

        codigo = str(itens[0])
        tipo = str(itens[1])
        razao = str(itens[2])
        fantasia = str(itens[3])
        cnpj = str(itens[4])
        insEstadual = str(itens[5])
        expeditor = str(itens[6])
        uf = str(itens[7])
        aniversario = str(itens[8])
        endereco = str(itens[9])
        numero = str(itens[10])
        complemento = str(itens[11])
        bairro = str(itens[12])
        cidade = str(itens[13])
        estado = str(itens[14])
        cep = str(itens[15])
        site = str(itens[16])
        obs = str(itens[17])
        if itens[18] == 'Ativo':
            situacao = True
        else:
            situacao = False

        __dados = Fornecedor(codigo, None, None, None, cnpj, insEstadual, fantasia, razao, obs, situacao, tipo)
        self.setCamposFornecedor(__dados)
        self.dialogFornecedores.close()

    def setCamposFornecedor(self, campos):
        self.ui.txtCodig.setText(campos.getIdFornecedor)
        self.ui.txtFornecedor.setText(campos.getRazaoSocial)

    def setFornecedor(self):
        forne = NotaFiscalRomanieo()
        emp = forne.pesquisaFornecedor(self.ui.txtCodig.text())

        if emp == []:
            MensagemBox().warning('Mensagem', "Atenção não existe nenhum cadastro desta fornecedor ou esta inativo")
            self.ui.txtFornecedor.clear()

        else:
            for empres in emp:
                self.ui.txtFornecedor.setText(str(empres[2]))


    def setFornecedorFinish(self):
        forne = NotaFiscalRomanieo()
        emp = forne.pesquisaFornecedor(self.ui.txtCodig.text())

        if emp == []:
            self.ui.txtFornecedor.clear()

        else:
            for empres in emp:
                self.ui.txtFornecedor.setText(str(empres[2]))

    def setMotorista(self):
        moto = NotaFiscalRomanieo()
        emp = moto.pesquisarMotorista(self.ui.txtCodigoMotorista.text())
        if emp == []:
            MensagemBox().warning('Mensagem', "Atenção não existe nenhum cadastro deste motorista ou esta inativo")
            self.ui.txtMotorista.clear()
        else:
            for empres in emp:
                self.ui.txtMotorista.setText(empres[1] + " " +empres[2])


    def setMotoristaFinish(self):
        forne = NotaFiscalRomanieo()

        emp = forne.pesquisarMotorista(self.ui.txtCodigoMotorista.text())

        if emp == []:
            self.ui.txtMotorista.clear()

        else:
            for empres in emp:
                self.ui.txtMotorista.setText(empres[1] + " " +empres[2])

    def tabDescricao(self):
        lista = []
        columcount = self.ui.tabDescricaoProduto.columnCount()
        row = self.ui.tabDescricaoProduto.currentItem().row()
        for x in range(0, columcount, 1):
            cell = self.ui.tabDescricaoProduto.item(row, x).text()
            lista.append(cell)
        return lista

    def cellClickDescricao(self):
        index = self.ui.tabDescricaoProduto.currentRow()

        lista = self.tabDescricao()
        if lista in self.atuaDecricao:
            self.atuaDecricao.remove(list)
            self.ui.tabDescricaoProduto.removeRow(index)
        else:
            self.ui.tabDescricaoProduto.removeRow(index)
            if index >= 0:
                self.removeDescricao.append(self.decricao[index])
                del self.decricao[index]
            else:
                MensagemBox().warning( 'Mensagem',"Impossivel realizar essa ação, por favor selecione um item da lista para excluir")


    def delDescricao(self):
        index = self.ui.tabDescricaoProduto.currentRow()

        if self.editar == False:

            if index >= 0:
                self.subtrairTotal(self.tabDescricao()[9])
                del self.decricao[index]
                self.ui.tabDescricaoProduto.removeRow(index)
            else:
                MensagemBox().warning('Mensagem', "Impossivel realizar essa ação, por favor selecione um item da lista para excluir")
        elif self.editar == True:
            self.cellClickDescricao()

    def deletarDescricaoProduto(self):
        for i in reversed(range(self.ui.tabDescricaoProduto.rowCount())):
            self.ui.tabDescricaoProduto.removeRow(i)

    def setFloatDecimalValorTotal(self):
        self.ui.txtValorTotal.setText(self.ui.txtValorTotal.text()+self.setDecimal(self.ui.txtValorTotal.text()))

    def setFloatDecimalValorUni(self):
        self.ui.txtValorUnotario.setText(self.ui.txtValorUnotario.text() + self.setDecimal(self.ui.txtValorUnotario.text()))


    def setDecimal(self, flutuante):

        ponto = self.alterarCaracterNum(flutuante)

        if len(ponto) == 1:
            retorno = "0"
        elif len(ponto) == 0:
            retorno = ",00"

        return retorno

    def addProdutos(self):
        if self.ui.txtQtd.text() != "" and self.ui.txtValorUnotario.text() != "" and self.ui.txtValorTotal.text() != "":
            ncm = self.ui.cBoxNcm.currentText()
            cfop = self.ui.cBoxCfop.currentText()
            csosn = self.ui.cBoxCsosn.currentText()
            cst = self.ui.cBoxCst.currentText()

            valorIcms = self.ui.txtValorICMS.text()
            if valorIcms == "":
                valorIcms = 0
            valorIpi = self.ui.txtValorIPI.text()
            if valorIpi == "":
                valorIpi = 0
            alicotaIcms = self.ui.txtAlicotaICMS.text()
            if alicotaIcms == "":
                alicotaIcms = 0
            alicotaIpi = self.ui.txtAlicotaIPI.text()
            if alicotaIpi == "":
                alicotaIpi = 0

            idProduto = self.getIndexProduto()
            produto = self.ui.cBoxProduto.currentText()
            uni = self.ui.cBoxUn.currentText()
            qtd = self.ui.txtQtd.text()
            valUni = self.ui.txtValorUnotario.text()
            valTotal = self.ui.txtValorTotal.text()

            add = [(idProduto, produto, ncm, cst,  cfop, csosn, uni, qtd, valUni, valTotal, valorIcms, valorIpi, alicotaIcms, alicotaIpi)]
            self.inserirTabela(add)

            self.decricao.append(add)
            self.totalNf()
            self.ui.txtQtd.clear()
            self.ui.txtValorUnotario.clear()
            self.ui.txtValorTotal.clear()
        else:
            MensagemBox().warning('Mensagem', "Atenção prencha todos os campos obrigatorio")

    def inserirTabela(self, dado):

        linha = self.ui.tabDescricaoProduto.rowCount()
        for info in dado:
            self.ui.tabDescricaoProduto.insertRow(linha)
            idProduto = info[0]
            produto = info[1]
            ncm = info[2]
            cst = info[3]
            cfop = info[4]
            csosn = info[5]
            uni = info[6]
            qtd = info[7]
            valUni = info[8]
            valTotal = info[9]
            valorIcms = info[10]
            valorIpi = info[11]
            alicotaIcms = info[12]
            alicotaIpi = info[13]

            self.ui.tabDescricaoProduto.setItem(linha, 0, QtGui.QTableWidgetItem(str(idProduto)))
            self.ui.tabDescricaoProduto.setItem(linha, 1, QtGui.QTableWidgetItem(str(produto)))
            self.ui.tabDescricaoProduto.setItem(linha, 2, QtGui.QTableWidgetItem(str(ncm)))
            self.ui.tabDescricaoProduto.setItem(linha, 3, QtGui.QTableWidgetItem(str(cst)))
            self.ui.tabDescricaoProduto.setItem(linha, 4, QtGui.QTableWidgetItem(str(cfop)))
            self.ui.tabDescricaoProduto.setItem(linha, 5, QtGui.QTableWidgetItem(str(csosn)))
            self.ui.tabDescricaoProduto.setItem(linha, 6, QtGui.QTableWidgetItem(str(uni)))
            self.ui.tabDescricaoProduto.setItem(linha, 7, QtGui.QTableWidgetItem(str(qtd)))
            self.ui.tabDescricaoProduto.setItem(linha, 8, QtGui.QTableWidgetItem(str(valUni)))
            self.ui.tabDescricaoProduto.setItem(linha, 9, QtGui.QTableWidgetItem(str(valTotal)))
            self.ui.tabDescricaoProduto.setItem(linha, 10, QtGui.QTableWidgetItem(str(valorIcms)))
            self.ui.tabDescricaoProduto.setItem(linha, 11, QtGui.QTableWidgetItem(str(valorIpi)))
            self.ui.tabDescricaoProduto.setItem(linha, 12, QtGui.QTableWidgetItem(str(alicotaIcms)))
            self.ui.tabDescricaoProduto.setItem(linha, 13, QtGui.QTableWidgetItem(str(alicotaIpi)))

            linha += 1

    def getIndexProduto(self):
        index = self.ui.cBoxProduto.currentIndex()

        for lista in self.produto:
            a = lista[index]
        idProduto = int(a[0])

        return idProduto

    def cadastro(self):
            if self.ui.txtCodig.text() != '' and self.ui.txtFornecedor != '' and self.ui.txtCodigoMotorista.text() != '' and self.ui.txtMotorista.text() != '' and self.ui.txtSerie.text() != '' and self.ui.txtModelo.text() != '' and self.ui.txtNumNF.text() != '':
                pass












                '''
                empresa = Empresas(None, self.ui.txtCodigo.text(), self.ui.cBoxTipoEmpresa.currentText(),
                                   self.ui.txtInscricaoMunicipal.text())
                empresaDao = EmpresaDao()
                empresaDao.cadastroEmpresa(empresa)

                registroGeral = RegistroGeralDao()
                self.idEmpresa = registroGeral.ultimoRegistro()

                if self.contatoAdd != []:
                    i = 0
                    for lista in self.desc:
                        a = self.contatoAdd[i]

                        __notaFiscal = a[0]
                        __codigoNosso = a[1]
                        __codigoProduto = a[2]
                        __produto = a[3]
                        __ncm = a[4]
                        __cst = a[5]
                        __cfop = a[6]
                        __un = a[7]
                        __qtd = a[8]
                        __valorUnitario = a[9]
                        __valorTotal = a[10]
                        __valorIcms = a[11]
                        __valorIpi = a[12]
                        __alicotaIcms = a[13]
                        __alicotaIpi = a[14]

                        __descricao = DescricaoProduto(None, __notaFiscal, __codigoNosso, __codigoProduto, __produto,
                                                       __ncm, __cst, __cfop, __un, __qtd, __valorUnitario, __valorTotal,
                                                       __valorIcms, __valorIpi, __alicotaIcms, __alicotaIpi)
                        #__notaFiscalRomaneio.cadastrarDescricaoProduto(__descricao)

                        i += 1

        self.ui.txtNomeEmitente.editingFinished.connect(self.pesquisarFornecedor)
        self.ui.txtFantasiaDestinatario.editingFinished.connect(self.pesquisarEmpresa)
        self.ui.txtNomeMotorista.editingFinished.connect(self.pesquisarMotorista)

        self.ui.txtNomeEmitente.textChanged.connect(self.upperCaseEmitente)
        self.ui.txtFantasiaDestinatario.textChanged.connect(self.upperCaseDestinatario)
        self.ui.txtNomeMotorista.textChanged.connect(self.upperCaseMotorista)

        self.ui.txtNomeEmitente.returnPressed.connect(self.focusEmpresa)
        self.ui.txtFantasiaDestinatario.returnPressed.connect(self.focusMotorista)
        self.ui.txtNomeMotorista.returnPressed.connect(self.focusNumNota)
        self.ui.txtNumeroNotaFiscal.returnPressed.connect(self.focusDataEmissao)
        self.ui.txtValorTotal.returnPressed.connect(self.focusNumRomaneio)
        self.ui.txtNumeroRomaneio.returnPressed.connect(self.focusMetragem)
        self.ui.txtQuantidade.returnPressed.connect(self.focusValorUnitario)

        self.ui.txtValorTotal.cursorPositionChanged.connect(self.positionCursor)
        self.ui.txtValorTotal.textChanged.connect(self.positionCursor)

        self.ui.btnPesquisarDestinatario.clicked.connect(self.consultarEmpresa)
        self.ui.btnPesquisarEmitente.clicked.connect(self.consultarFornecedor)
        self.ui.btnPesquisarMotorista.clicked.connect(self.consultarMotorista)

        self.ui.btnAdicionar.clicked.connect(self.addDescricaoProduto)
        self.ui.btnExcluir.clicked.connect(self.delDescricaoProduto)

        self.ui.txtTipoCargaServico.currentIndexChanged.connect(self.pesquisaProduto)

        self.ui.btnNovo.clicked.connect(self.botoesNovo)
        self.ui.btnSalvar.clicked.connect(self.cadastrar)
        self.ui.btnCancelar.clicked.connect(self.cancelarCad)

        
    def positionCursor(self):
        texto = self.removerCaracterDin(self.ui.txtValorTotal.text())
        if texto == '' or texto != '':
            self.ui.txtValorTotal.setCursorPosition(14)

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
        if self.ui.txtQuantidade.text() != "" and self.ui.txtValorUnitario.text() != "":
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
        else:
            QMessageBox.warning(QWidget(), 'Mensagem', "Por favor preencha os campos de quantidade e valor unitario")

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
        a = self.ui.tbProduto.removeRow(index)
        if index >= 0:
            del self.desc[index]
        else:
            QMessageBox.warning(QWidget(), 'Mensagem', "Impossivel realizar essa ação, por favor selecione um item da lista para excluir")


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
        self.ui.txtNomeEmitente.clear()
        self.limparCamposDestinatario()
        self.ui.txtFantasiaDestinatario.clear()
        self.limparCamposMotorista()
        self.ui.txtNomeMotorista.clear()
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

        self.desc.clear()
        self.deletarDescricaoProduto()

   

    def keyPressEvent(self, keyEvent):
        if keyEvent.key() == (QtCore.Qt.Key_F12):
            self.dialog = QDialog(self)
            self.__pesquisar = Ui_frmConsultarNotasFiscais()
            self.__pesquisar.setupUi(self.dialog)

            self.__pesquisar.txtPesquisar.returnPressed.connect(self.pesquisar)
            self.__pesquisar.radBtnDataLanamento.clicked.connect(self.ativarDataLancamento)
            self.__pesquisar.radBtnDataPeriodos.clicked.connect(self.ativarData)
            self.__pesquisar.radBtnFantasiaEmitente.clicked.connect(self.ativarPesquisa)
            self.__pesquisar.radBtnRazaoSocialEmitente.clicked.connect(self.ativarPesquisa)
            self.__pesquisar.radBtnCnpjEmitente.clicked.connect(self.ativarPesquisa)
            self.__pesquisar.radBtnIncrisaoEstadualEmitente.clicked.connect(self.ativarPesquisa)
            self.__pesquisar.radBtnFantasiaDestinatario.clicked.connect(self.ativarPesquisa)
            self.__pesquisar.radBtnRazaoSocialDestinatario.clicked.connect(self.ativarPesquisa)
            self.__pesquisar.radBtnCnpjDestinatario.clicked.connect(self.ativarPesquisa)
            self.__pesquisar.radBtnIncrisaoEstadualDestinatario.clicked.connect(self.ativarPesquisa)
            self.__pesquisar.radBtnNumNotaFiscal.clicked.connect(self.ativarPesquisa)
            self.__pesquisar.radBtnRomaneio.clicked.connect(self.ativarPesquisa)

            self.__pesquisar.btnPesquisar.clicked.connect(self.pesquisar)

            self.__pesquisar.tabPesquisar.doubleClicked.connect(self.setarCampos)
            self.dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            self.dialog.exec_()


    def ativarDataLancamento(self):
        self.pesquisar.txtDataInicial.setEnabled(True)
        self.__pesquisar.txtDataFinal.setEnabled(False)

        self.__pesquisar.txtPesquisar.setEnabled(False)
        self.__pesquisar.btnPesquisar.setEnabled(True)


    def ativarData(self):
        self.__pesquisar.txtDataInicial.setEnabled(True)
        self.__pesquisar.txtDataFinal.setEnabled(True)

        self.__pesquisar.txtPesquisar.setEnabled(False)

        self.__pesquisar.btnPesquisar.setEnabled(True)


    def ativarPesquisa(self):
        self.__pesquisar.txtDataInicial.setEnabled(False)
        self.__pesquisar.txtDataFinal.setEnabled(False)

        self.__pesquisar.txtPesquisar.setEnabled(True)

        self.__pesquisar.btnPesquisar.setEnabled(True)


   


    def pesquisar(self):
        if self.__pesquisar.radBtnNumNotaFiscal.isChecked():
            __nunNota = self.__pesquisar.txtPesquisar.text()
            __pesDao = PesquisarNotaFiscalRomaneioDao()
            __retorno = __pesDao.pesquisarNumeroNota(__nunNota)

            self.setarTabelaPesquisa(__retorno)

        elif self.__pesquisar.radBtnRomaneio.isChecked():
            __numRomaneio = self.__pesquisar.txtPesquisar.text()
            __pesDao = PesquisarNotaFiscalRomaneioDao()
            __retorno = __pesDao.pesquisarNumeroRomaneio(__numRomaneio)

            self.setarTabelaPesquisa(__retorno)

        elif self.__pesquisar.radBtnFantasiaDestinatario.isChecked():
            __fantasiaDestinatario = self.__pesquisar.txtPesquisar.text()
            __pesDao = PesquisarNotaFiscalRomaneioDao()
            __retorno = __pesDao.pesquisarFantasiaDest(__fantasiaDestinatario)

            self.setarTabelaPesquisa(__retorno)

        elif self.__pesquisar.radBtnRazaoSocialDestinatario.isChecked():
            __razaoSocialDestinatario = self.__pesquisar.txtPesquisar.text()
            __pesDao = PesquisarNotaFiscalRomaneioDao()
            __retorno = __pesDao.pesquisarRozaoSocialDest(__razaoSocialDestinatario)

            self.setarTabelaPesquisa(__retorno)

        elif self.__pesquisar.radBtnCnpjDestinatario.isChecked():
            __cnpjDestinatario = self.__pesquisar.txtPesquisar.text()
            __pesDao = PesquisarNotaFiscalRomaneioDao()
            __retorno = __pesDao.pesquisarCnpjDest(__cnpjDestinatario)

            self.setarTabelaPesquisa(__retorno)

        elif self.__pesquisar.radBtnIncrisaoEstadualDestinatario.isChecked():
            __insDestinatario = self.__pesquisar.txtPesquisar.text()
            __pesDao = PesquisarNotaFiscalRomaneioDao()
            __retorno = __pesDao.pesquisarInsEstadualDest(__insDestinatario)

            self.setarTabelaPesquisa(__retorno)

        elif self.__pesquisar.radBtnFantasiaEmitente.isChecked():
            __fantasiaEmitente = self.__pesquisar.txtPesquisar.text()
            __pesDao = PesquisarNotaFiscalRomaneioDao()
            __retorno = __pesDao.pesquisarFantasiaEmit(__fantasiaEmitente)

            self.setarTabelaPesquisa(__retorno)

        elif self.__pesquisar.radBtnRazaoSocialEmitente.isChecked():
            __razaoSocialEmitente = self.__pesquisar.txtPesquisar.text()
            __pesDao = PesquisarNotaFiscalRomaneioDao()
            __retorno = __pesDao.pesquisarRozaoSocialEmit(__razaoSocialEmitente)

            self.setarTabelaPesquisa(__retorno)

        elif self.__pesquisar.radBtnCnpjEmitente.isChecked():
            __cnpjEmitente = self.__pesquisar.txtPesquisar.text()
            __pesDao = PesquisarNotaFiscalRomaneioDao()
            __retorno = __pesDao.pesquisarCnpjEmit(__cnpjEmitente)

            self.setarTabelaPesquisa(__retorno)

        elif self.__pesquisar.radBtnIncrisaoEstadualEmitente.isChecked():
            __insEmitente = self.__pesquisar.txtPesquisar.text()
            __pesDao = PesquisarNotaFiscalRomaneioDao()
            __retorno = __pesDao.pesquisarInsEstadualEmit(__insEmitente)

            self.setarTabelaPesquisa(__retorno)

        elif self.__pesquisar.radBtnDataLanamento.isChecked():
            __dataLancamento = self.formatarData(self.removerCaracter(self.__pesquisar.txtDataInicial.text()))
            __pesDao = PesquisarNotaFiscalRomaneioDao()
            __retorno = __pesDao.pesquisarDataLancamento(__dataLancamento)

            self.setarTabelaPesquisa(__retorno)

        elif self.__pesquisar.radBtnDataPeriodos.isChecked():
            __dataIni = self.formatarData(self.removerCaracter(self.__pesquisar.txtDataInicial.text()))
            __dataFim = self.formatarData(self.removerCaracter(self.__pesquisar.txtDataFinal.text()))
            __pesDao = PesquisarNotaFiscalRomaneioDao()
            __retorno = __pesDao.pesquisarDataPeriodo(__dataIni, __dataFim)

            self.setarTabelaPesquisa(__retorno)
        else:
            QMessageBox.warning(QWidget(), 'Atenção', "Selecione uma das opções de pesquisa")


    def setarTabelaPesquisa(self, __retorno):
        qtde_registros = len(__retorno)
        self.__pesquisar.tabPesquisar.setRowCount(qtde_registros)

        linha = 0
        for pesqui in __retorno:
            # capturando os dados da tupla

            codigo = pesqui[0]
            numNotaFiscal = pesqui[1]
            data = pesqui[2]
            valorTotal = pesqui[3]
            codFornecedor = pesqui[4]
            forneFantasia = pesqui[5]
            forneRazaoSocial = pesqui[6]
            forneCnpj = pesqui[7]
            forneInsEstadual = pesqui[8]
            codEmpresa = pesqui[9]
            emprFantasia = pesqui[10]
            emprRazaoSocial = pesqui[11]
            emprCnpj = pesqui[12]
            emprInsEstadual = pesqui[13]
            codMotorista = pesqui[14]
            nomeMotorista = pesqui[15]
            rg = pesqui[16]
            cpf = pesqui[17]
            codRomaneio = pesqui[18]
            numRomaneio = pesqui[19]
            if pesqui[20] == 1:
                certificada = "Certificada"
            else:
                certificada = "Não Certificada"
            metragem = pesqui[21]

            # preenchendo o grid de pesquisa
            self.__pesquisar.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
            self.__pesquisar.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(numNotaFiscal)))
            self.__pesquisar.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(data)))
            self.__pesquisar.tabPesquisar.setItem(linha, 3, QtGui.QTableWidgetItem(str(valorTotal)))
            self.__pesquisar.tabPesquisar.setItem(linha, 4, QtGui.QTableWidgetItem(str(codFornecedor)))
            self.__pesquisar.tabPesquisar.setItem(linha, 5, QtGui.QTableWidgetItem(str(forneFantasia)))
            self.__pesquisar.tabPesquisar.setItem(linha, 6, QtGui.QTableWidgetItem(str(forneRazaoSocial)))
            self.__pesquisar.tabPesquisar.setItem(linha, 7, QtGui.QTableWidgetItem(str(forneCnpj)))
            self.__pesquisar.tabPesquisar.setItem(linha, 8, QtGui.QTableWidgetItem(str(forneInsEstadual)))
            self.__pesquisar.tabPesquisar.setItem(linha, 9, QtGui.QTableWidgetItem(str(codEmpresa)))
            self.__pesquisar.tabPesquisar.setItem(linha, 10, QtGui.QTableWidgetItem(str(emprFantasia)))
            self.__pesquisar.tabPesquisar.setItem(linha, 11, QtGui.QTableWidgetItem(str(emprRazaoSocial)))
            self.__pesquisar.tabPesquisar.setItem(linha, 12, QtGui.QTableWidgetItem(str(emprCnpj)))
            self.__pesquisar.tabPesquisar.setItem(linha, 13, QtGui.QTableWidgetItem(str(emprInsEstadual)))
            self.__pesquisar.tabPesquisar.setItem(linha, 14, QtGui.QTableWidgetItem(str(codMotorista)))
            self.__pesquisar.tabPesquisar.setItem(linha, 15, QtGui.QTableWidgetItem(str(nomeMotorista)))
            self.__pesquisar.tabPesquisar.setItem(linha, 16, QtGui.QTableWidgetItem(str(rg)))
            self.__pesquisar.tabPesquisar.setItem(linha, 17, QtGui.QTableWidgetItem(str(cpf)))
            self.__pesquisar.tabPesquisar.setItem(linha, 18, QtGui.QTableWidgetItem(str(codRomaneio)))
            self.__pesquisar.tabPesquisar.setItem(linha, 19, QtGui.QTableWidgetItem(str(numRomaneio)))
            self.__pesquisar.tabPesquisar.setItem(linha, 20, QtGui.QTableWidgetItem(str(certificada)))
            self.__pesquisar.tabPesquisar.setItem(linha, 21, QtGui.QTableWidgetItem(str(metragem)))

            linha += 1

    def formatarDataRetorno(self, data):
        dia = data[8:10]
        mes = data[5:7]
        ano = data[:4]

        return QtCore.QDate(int(ano), int(mes), int(dia))


    def setarCampos(self):
        itens = []

        for item in self.__pesquisar.tabPesquisar.selectedItems():
            itens.append(item.text())

        codNotaFiscal = str(itens[0])
        numeroNotaFiscal = str(itens[1])
        dataNota = self.formatarDataRetorno(itens[2])
        valorTotl = str(itens[3])
        codEmitente = str(itens[4])
        fantasiaEmitente = itens[5]
        razaoSocialEmitente = itens[6]
        cnpjEmitente = str(itens[7])
        insEstadualEmitente = str(itens[8])
        codDestinatario = str(itens[9])
        fantasiaDestinatario = itens[10]
        razaoSocialDestinatario = itens[11]
        cnpjDestinatario = str(itens[12])
        insEstadualDestinatario = str(itens[13])
        codMotorista = str(itens[14])
        nomeMotorista = itens[15]
        rg = str(itens[16])
        cpf = str(itens[17])
        codRomaneio = str(itens[18])
        numRomaneio = str(itens[19])
        if itens[20] == 'Certificada':
            certificada = True
        elif itens[20] == 'Não Certificada':
            certificada = False
        else:
            return None
        metragem = itens[21]

        __dados = PesquisaNotaFiscal(codNotaFiscal, numeroNotaFiscal, dataNota, valorTotl, codEmitente,
                                     fantasiaEmitente, razaoSocialEmitente, cnpjEmitente, insEstadualEmitente,
                                     codDestinatario, fantasiaDestinatario, razaoSocialDestinatario, cnpjDestinatario,
                                     insEstadualDestinatario, codMotorista, nomeMotorista, rg, cpf, codRomaneio,
                                     numRomaneio, certificada, metragem)
        self.setCampos(__dados)
        self.botoesEditar()
        self.dialog.close()

    def setCampos(self, campos):
        self.unidadeMedida()
        self.pesquisarTiposCarga()
        self.botoesNovo
        self.ui.txtIdEmitente.setText(str(campos.getCodEmitente))
        self.ui.txtNomeEmitente.setText(campos.getFantasiaEmitente)
        self.ui.txtRazaoSocialEmitente.setText(campos.getRazaoSocialEmitente)
        self.ui.txtCnpjEmitente.setText(str(campos.getCnpjEmitente))
        self.ui.txtInscricaoEstaduaEmitente.setText(str(campos.getInsEstadualEmitente))
        self.ui.txtIdDestinatario.setText(str(campos.getCodDestinatario))
        self.ui.txtFantasiaDestinatario.setText(campos.getFantasiaDestinatario)
        self.ui.txtRazaoSocialDestinatario.setText(campos.getRazaoSocialDestinatario)
        self.ui.txtCnpjDestinatario.setText(campos.getCnpjDestinatario)
        self.ui.txtInscricaoEstaduaDestinatario.setText(str(campos.getInsEstadualDestinatario))
        self.ui.txtidMotorista.setText(str(campos.getCodMotorista))
        self.ui.txtNomeMotorista.setText(campos.getNomeMotorista)
        self.ui.txtRg.setText(str(campos.getRg))
        self.ui.txtCpf.setText(str(campos.getCpf))
        self.ui.txtNumeroNotaFiscal.setText(str(campos.getNumNotaFiscal))
        self.codRomaneio = campos.getCodRomaneio
        self.ui.txtNumeroRomaneio.setText(str(campos.getNumRomaneio))
        self.ui.txtMetragemMadeira.addItem(campos.getMetragem)
        self.ui.txtCertificada.setCheckable(campos.getCetificada)
        self.ui.txtDataEmissao.setDate(campos.getData)
        self.ui.txtValorTotal.setText(campos.getValorTotal)
        if campos.getCetificada == True:
            self.ui.txtCertificada.setChecked(True)
        elif campos.getCetificada == False:
            self.ui.txtCertificada.setChecked(False)


        data = self.formatarData(self.removerCaracter(self.ui.txtDataEmissao.text()))

        dao = PesquisarNotaFiscalRomaneioDao()
        a = dao.pesquisarVeiculoMotorista(campos.getNomeMotorista, campos.getRg, campos.getCpf)
        b = dao.pesquisarDescricaoProduto(campos.getNumNotaFiscal, data, campos.getValorTotal)
        self.setCamposDescricao(b)
        for i in a:
            self.ui.txtMarca.setText(str(i[0]))
            self.ui.txtModelo.setText(str(i[1]))
            self.ui.txtPlaca.setText(str(i[2]))

    def setCamposDescricao(self, campos):

        qtde_registros = len(campos)
        self.ui.tbProduto.setRowCount(qtde_registros)

        linha = 0
        for pesqui in campos:
            # capturando os dados da tupla

            carga = pesqui[0]
            produto= pesqui[1]
            unidade = pesqui[2]
            qtd = pesqui[3]
            valor = pesqui[4]


            # preenchendo o grid de pesquisa
            self.ui.tbProduto.setItem(linha, 0, QtGui.QTableWidgetItem(str(carga)))
            self.ui.tbProduto.setItem(linha, 1, QtGui.QTableWidgetItem(str(produto)))
            self.ui.tbProduto.setItem(linha, 2, QtGui.QTableWidgetItem(str(unidade)))
            self.ui.tbProduto.setItem(linha, 3, QtGui.QTableWidgetItem(str(qtd)))
            self.ui.tbProduto.setItem(linha, 4, QtGui.QTableWidgetItem(str(valor)))

            linha += 1

    def consultarEmpresa(self):
        self.dialogEmp = QDialog(self)
        self.__pesEmp = Ui_frmConsultarEmpresa()
        self.__pesEmp.setupUi(self.dialogEmp)

        self.__pesEmp.txtPesquisar.returnPressed.connect(self.pesquisarEmpresas)
        self.__pesEmp.btnPesquisar.clicked.connect(self.pesquisarEmpresas)
        self.__pesEmp.tabPesquisar.doubleClicked.connect(self.setarEmpresa)

        self.dialogEmp.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.dialogEmp.exec_()

    def pesquisarEmpresas(self):

        if self.__pesEmp.radBtnCodigo.isChecked():
            dao = PesquisaEmpresaDao()
            empresa = dao.pesquisaCodigo(self.__pesEmp.txtPesquisar.text())
            self.setarTabelaPesquisaEmp(empresa)

        elif self.__pesEmp.radBtnFantasia.isChecked():
            dao = PesquisaEmpresaDao()
            empresa = dao.pesquisaFantasia(self.__pesEmp.txtPesquisar.text())
            self.setarTabelaPesquisaEmp(empresa)

        elif self.__pesEmp.radBtnRazaoSocial.isChecked():
            dao = PesquisaEmpresaDao()
            empresa = dao.pesquisaRazaoSocial(self.__pesEmp.txtPesquisar.text())
            self.setarTabelaPesquisaEmp(empresa)

        elif self.__pesEmp.radBtnCnpj.isChecked():
            dao = PesquisaEmpresaDao()
            empresa = dao.pesquisaCnpj(self.__pesEmp.txtPesquisar.text())
            self.setarTabelaPesquisaEmp(empresa)

        elif self.__pesEmp.radBtnIncrisaoEstadual.isChecked():
            dao = PesquisaEmpresaDao()
            empresa = dao.pesquisaInscEstadual(self.__pesEmp.txtPesquisar.text())
            self.setarTabelaPesquisaEmp(empresa)
        else:
            QMessageBox.warning(QWidget(), 'Atenção', "Selecione uma das opções de pesquisa")


    def setarTabelaPesquisaEmp(self, empresa):
        qtde_registros = len(empresa)
        self.__pesEmp.tabPesquisar.setRowCount(qtde_registros)

        linha = 0
        for pesqui in empresa:
            # capturando os dados da tupla

            cod = pesqui[0]
            fantasia = pesqui[1]
            razao = pesqui[2]
            cpnj = pesqui[3]
            inscricao = pesqui[4]
            tipo = pesqui[5]
            endereco = pesqui[6]
            numero = pesqui[7]
            bairro = pesqui[8]
            cidade = pesqui[9]
            estado = pesqui[10]
            cep = pesqui[11]

            # preenchendo o grid de pesquisa
            self.__pesEmp.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(cod)))
            self.__pesEmp.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(fantasia)))
            self.__pesEmp.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(razao)))
            self.__pesEmp.tabPesquisar.setItem(linha, 3, QtGui.QTableWidgetItem(str(cpnj)))
            self.__pesEmp.tabPesquisar.setItem(linha, 4, QtGui.QTableWidgetItem(str(inscricao)))
            self.__pesEmp.tabPesquisar.setItem(linha, 5, QtGui.QTableWidgetItem(str(tipo)))
            self.__pesEmp.tabPesquisar.setItem(linha, 6, QtGui.QTableWidgetItem(str(endereco)))
            self.__pesEmp.tabPesquisar.setItem(linha, 7, QtGui.QTableWidgetItem(str(numero)))
            self.__pesEmp.tabPesquisar.setItem(linha, 8, QtGui.QTableWidgetItem(str(bairro)))
            self.__pesEmp.tabPesquisar.setItem(linha, 9, QtGui.QTableWidgetItem(str(cidade)))
            self.__pesEmp.tabPesquisar.setItem(linha, 10, QtGui.QTableWidgetItem(str(estado)))
            self.__pesEmp.tabPesquisar.setItem(linha, 11, QtGui.QTableWidgetItem(str(cep)))

            linha += 1

    def setarEmpresa(self):
        itens = []
        for item in self.__pesEmp.tabPesquisar.selectedItems():
            itens.append(item.text())

        codEmpresa = str(itens[0])
        fantasia = str(itens[1])
        razao = str(itens[2])
        cpnj = str(itens[3])
        inscricao = str(itens[4])

        self.ui.txtIdDestinatario.setText(codEmpresa)
        self.ui.txtFantasiaDestinatario.setText(fantasia)
        self.ui.txtRazaoSocialDestinatario.setText(razao)
        self.ui.txtCnpjDestinatario.setText(cpnj)
        self.ui.txtInscricaoEstaduaDestinatario.setText(inscricao)

        self.dialogEmp.close()

    def consultarFornecedor(self):
        self.dialogFun = QDialog(self)
        self.__pesFun = Ui_frmConsultarFornecedores()
        self.__pesFun.setupUi(self.dialogFun)

        self.__pesFun.txtPesquisar.returnPressed.connect(self.pesquisarFornecedo)
        self.__pesFun.btnPesquisar.clicked.connect(self.pesquisarFornecedo)
        self.__pesFun.tabPesquisar.doubleClicked.connect(self.setarFornecedor)

        self.dialogFun.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.dialogFun.exec_()

    def pesquisarFornecedo(self):
        dao = PesquisarFornecedorDao()
        if self.__pesFun.radBtnCodigo.isChecked():
            fornecedor = dao.pesquisaCodigo(self.__pesFun.txtPesquisar.text())
            self.setarTabelaPesquisaFun(fornecedor)

        elif self.__pesFun.radBtnFantasia.isChecked():
            fornecedor = dao.pesquisaFantasia(self.__pesFun.txtPesquisar.text())
            self.setarTabelaPesquisaFun(fornecedor)

        elif self.__pesFun.radBtnRazaoSocial.isChecked():
            fornecedor = dao.pesquisaRazaoSocial(self.__pesFun.txtPesquisar.text())
            self.setarTabelaPesquisaFun(fornecedor)

        elif self.__pesFun.radBtnCnpj.isChecked():
            fornecedor = dao.pesquisaCnpj(self.__pesFun.txtPesquisar.text())
            self.setarTabelaPesquisaFun(fornecedor)

        elif self.__pesFun.radBtnIncrisaoEstadual.isChecked():
            fornecedor = dao.pesquisaInscEstadual(self.__pesFun.txtPesquisar.text())
            self.setarTabelaPesquisaFun(fornecedor)
        else:
            QMessageBox.warning(QWidget(), 'Atenção', "Selecione uma das opções de pesquisa")

    def setarTabelaPesquisaFun(self, empresa):
        qtde_registros = len(empresa)
        self.__pesFun.tabPesquisar.setRowCount(qtde_registros)

        linha = 0
        for pesqui in empresa:
            # capturando os dados da tupla

            cod = pesqui[0]
            fantasia = pesqui[1]
            razao = pesqui[2]
            cpnj = pesqui[3]
            inscricao = pesqui[4]
            endereco = pesqui[5]
            numero = pesqui[6]
            bairro = pesqui[7]
            cidade = pesqui[8]
            estado = pesqui[9]
            cep = pesqui[10]

            # preenchendo o grid de pesquisa
            self.__pesFun.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(cod)))
            self.__pesFun.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(fantasia)))
            self.__pesFun.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(razao)))
            self.__pesFun.tabPesquisar.setItem(linha, 3, QtGui.QTableWidgetItem(str(cpnj)))
            self.__pesFun.tabPesquisar.setItem(linha, 4, QtGui.QTableWidgetItem(str(inscricao)))
            self.__pesFun.tabPesquisar.setItem(linha, 5, QtGui.QTableWidgetItem(str(endereco)))
            self.__pesFun.tabPesquisar.setItem(linha, 6, QtGui.QTableWidgetItem(str(numero)))
            self.__pesFun.tabPesquisar.setItem(linha, 7, QtGui.QTableWidgetItem(str(bairro)))
            self.__pesFun.tabPesquisar.setItem(linha, 8, QtGui.QTableWidgetItem(str(cidade)))
            self.__pesFun.tabPesquisar.setItem(linha, 9, QtGui.QTableWidgetItem(str(estado)))
            self.__pesFun.tabPesquisar.setItem(linha, 10, QtGui.QTableWidgetItem(str(cep)))

            linha += 1

    def setarFornecedor(self):
        itens = []
        for item in self.__pesFun.tabPesquisar.selectedItems():
            itens.append(item.text())

        codEmpresa = str(itens[0])
        fantasia = str(itens[1])
        razao = str(itens[2])
        cpnj = str(itens[3])
        inscricao = str(itens[4])

        self.ui.txtIdEmitente.setText(codEmpresa)
        self.ui.txtNomeEmitente.setText(fantasia)
        self.ui.txtRazaoSocialEmitente.setText(razao)
        self.ui.txtCnpjEmitente.setText(cpnj)
        self.ui.txtInscricaoEstaduaEmitente.setText(inscricao)

        self.dialogFun.close()


    def consultarMotorista(self):
        self.dialogMot = QDialog(self)
        self.__pesMot = Ui_frmConsultarMotoristas()
        self.__pesMot.setupUi(self.dialogMot)

        self.__pesMot.txtPesquisar.returnPressed.connect(self.pesquisarMotoristas)
        self.__pesMot.btnPesquisar.clicked.connect(self.pesquisarMotoristas)
        self.__pesMot.tabPesquisar.doubleClicked.connect(self.setarMotorista)

        self.dialogMot.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.dialogMot.exec_()

    def pesquisarMotoristas(self):
        dao = PesquisarMotoristaDao()

        if self.__pesMot.radBtnNome.isChecked():
            motorista = dao.pesquisarNomeMotorista(self.__pesMot.txtPesquisar.text())
            self.setarTabelaPesquisaMot(motorista)

        elif self.__pesMot.radBtnRg.isChecked():
            motorista = dao.pesquisarRgMotorista(self.__pesMot.txtPesquisar.text())
            self.setarTabelaPesquisaMot(motorista)

        elif self.__pesMot.radBtnCpf.isChecked():
            motorista = dao.pesquisarCpfMotorista(self.__pesMot.txtPesquisar.text())
            self.setarTabelaPesquisaMot(motorista)

        elif self.__pesMot.radBtnNumCarteira.isChecked():
            motorista = dao.pesquisarCnhMotorista(self.__pesMot.txtPesquisar.text())
            self.setarTabelaPesquisaMot(motorista)
        else:
            QMessageBox.warning(QWidget(), 'Atenção', "Selecione uma das opções de pesquisa")


    def setarTabelaPesquisaMot(self, empresa):
        qtde_registros = len(empresa)
        self.__pesMot.tabPesquisar.setRowCount(qtde_registros)

        linha = 0
        for pesqui in empresa:
            # capturando os dados da tupla

            cod = pesqui[0]
            nome = pesqui[1]
            rg = pesqui[2]
            cpf = pesqui[3]
            endereco = pesqui[4]
            numero = pesqui[5]
            bairro = pesqui[6]
            cidade = pesqui[7]
            estado = pesqui[8]
            cep = pesqui[9]
            marca = pesqui[10]
            modelo = pesqui[11]
            placa = pesqui[12]

            # preenchendo o grid de pesquisa
            self.__pesMot.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(cod)))
            self.__pesMot.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(nome)))
            self.__pesMot.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(rg)))
            self.__pesMot.tabPesquisar.setItem(linha, 3, QtGui.QTableWidgetItem(str(cpf)))
            self.__pesMot.tabPesquisar.setItem(linha, 4, QtGui.QTableWidgetItem(str(endereco)))
            self.__pesMot.tabPesquisar.setItem(linha, 5, QtGui.QTableWidgetItem(str(numero)))
            self.__pesMot.tabPesquisar.setItem(linha, 6, QtGui.QTableWidgetItem(str(bairro)))
            self.__pesMot.tabPesquisar.setItem(linha, 7, QtGui.QTableWidgetItem(str(cidade)))
            self.__pesMot.tabPesquisar.setItem(linha, 8, QtGui.QTableWidgetItem(str(estado)))
            self.__pesMot.tabPesquisar.setItem(linha, 9, QtGui.QTableWidgetItem(str(cep)))
            self.__pesMot.tabPesquisar.setItem(linha, 10, QtGui.QTableWidgetItem(str(marca)))
            self.__pesMot.tabPesquisar.setItem(linha, 11, QtGui.QTableWidgetItem(str(modelo)))
            self.__pesMot.tabPesquisar.setItem(linha, 12, QtGui.QTableWidgetItem(str(placa)))


            linha += 1

    def setarMotorista(self):
        itens = []
        for item in self.__pesMot.tabPesquisar.selectedItems():
            itens.append(item.text())

        cod = itens[0]
        nome = itens[1]
        rg = itens[2]
        cpf = itens[3]
        endereco = itens[4]
        numero = itens[5]
        bairro = itens[6]
        cidade = itens[7]
        estado = itens[8]
        cep = itens[9]
        marca = itens[10]
        modelo = itens[11]
        placa = itens[12]


        self.ui.txtidMotorista.setText(cod)
        self.ui.txtNomeMotorista.setText(nome)
        self.ui.txtRg.setText(rg)
        self.ui.txtCpf.setText(cpf)
        self.ui.txtMarca.setText(marca)
        self.ui.txtModelo.setText(modelo)
        self.ui.txtPlaca.setText(placa)

        self.dialogMot.close()
        '''