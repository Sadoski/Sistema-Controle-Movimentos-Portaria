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
from dao.fornecedorDao import FornecedorDao
from dao.motoristaDao import MotoristaDao
from dao.notaFiscalRomaneioDao import NotaFiscalRomanieo
from dao.pesquisaEmpresa import PesquisaEmpresaDao
from telas.frmEntradaNF import Ui_frmEntradaNF
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
        self.idNf = int()
        self.idMotorista = int()
        self.idFornecedor = int()
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
        self.ui.btnSalvar.clicked.connect(self.cadastro)
        self.ui.btnCancelar.clicked.connect(self.cancelar)
        self.ui.btnEditar.clicked.connect(self.atualizar)
        self.ui.btnDeletar.clicked.connect(self.deletar)

        self.ui.btnPesquisarMotorista.clicked.connect(self.pesquisarMotoristas)
        self.ui.btnPesquisarFornecedor.clicked.connect(self.pesquisarFornecedores)

        self.ui.btnAdd.clicked.connect(self.addProdutos)
        self.ui.btnRemove.clicked.connect(self.delDescricao)

        self.ui.txtValorICMS.textChanged.connect(self.validatorChangedDoubleValorICMS)
        self.ui.txtValorIPI.textChanged.connect(self.validatorChangedDoubleValorIPI)
        self.ui.txtAlicotaICMS.textChanged.connect(self.validatorChangedDoubleAlicotaICMS)
        self.ui.txtAlicotaIPI.textChanged.connect(self.validatorChangedDoubleAlicotaIPI)
        self.ui.txtValorUnotario.textChanged.connect(self.validatorChangedDoubleValorUnitario)
        self.ui.txtValorTotal.textChanged.connect(self.validatorChangedDoubleValorTotal)
        self.ui.txtSomatoriaTotalValor.textChanged.connect(self.validatorChangedDoubleSomatoriaTotal)


        self.ui.txtCodig.textChanged.connect(self.numberCodigoFornecedor)
        self.ui.txtCodigoMotorista.textChanged.connect(self.numberCodigoMotorista)
        self.ui.txtSerie.textChanged.connect(self.numberSerie)
        self.ui.txtNumNF.textChanged.connect(self.numberNumNF)
        self.ui.txtQtd.textChanged.connect(self.numberQuantidade)

        self.ui.txtValorTotal.editingFinished.connect(self.setFloatDecimalValorTotal)
        self.ui.txtValorUnotario.editingFinished.connect(self.setFloatDecimalValorUni)
        self.ui.txtValorICMS.editingFinished.connect(self.setFloatDecimalValorIcms)
        self.ui.txtValorIPI.editingFinished.connect(self.setFloatDecimalValorIpi)
        self.ui.txtAlicotaICMS.editingFinished.connect(self.setFloatDecimalAlicotaIcms)
        self.ui.txtAlicotaIPI.editingFinished.connect(self.setFloatDecimalAlicotaIpi)

        self.ui.txtCodig.returnPressed.connect(self.setFornecedor)
        self.ui.txtCodigoMotorista.returnPressed.connect(self.setMotorista)

        self.ui.txtCodig.editingFinished.connect(self.setFornecedorFinish)
        self.ui.txtCodigoMotorista.editingFinished.connect(self.setMotoristaFinish)
        self.ui.txtValorUnotario.editingFinished.connect(self.somarUniValor)

    def somarUniValor(self):
        if self.ui.txtQtd.text() != '' and self.ui.txtValorUnotario.text() != '':
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
        self.ui.grbDescricaoProduto.setEnabled(False)

        self.ui.btnNovo.setEnabled(True)
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnEditar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(False)
        self.ui.btnDeletar.setEnabled(False)

    def botoesEditar(self):
        self.ui.grbFornecedor.setEnabled(True)
        self.ui.grbTransportadoraMotorista.setEnabled(True)
        self.ui.grbData.setEnabled(True)
        self.ui.grbDadosNF.setEnabled(True)
        self.ui.grbImpostos.setEnabled(True)
        self.ui.grbCalculoImposto.setEnabled(True)
        self.ui.grbDescricaoProduto.setEnabled(True)

        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnEditar.setEnabled(True)
        self.ui.btnCancelar.setEnabled(True)
        self.ui.btnDeletar.setEnabled(True)

        self.unidadeMedida()
        self.tiposNF()
        self.setNcm()
        self.setCfop()
        self.setCsosn()
        self.setCst()
        self.setProdutos()

    def validarCamposFlutuante(self):

        validarReal = QtGui.QDoubleValidator(0.00, 999999999.99, 2, self)
        validarReal.setNotation(QtGui.QDoubleValidator.StandardNotation)
        validarReal.setDecimals(2)

        listaObj = [self.ui.txtValorICMS, self.ui.txtValorIPI, self.ui.txtValorUnotario, self.ui.txtValorTotal]

        for objeto in listaObj:
            objeto.setValidator(validarReal)

    def validarCamposInteiro(self):

        validarReal = QtGui.QIntValidator(0, 999999999, self)

        listaObj = [self.ui.txtCodig, self.ui.txtCodigoMotorista, self.ui.txtSerie, self.ui.txtNumNF, self.ui.txtQtd]

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

    def alterarElevacao(self, i):
        i = i.replace('²', '')
        i = i.replace('³', '')

        return i

    def reformatar(self, i):
        i = i.replace(',', '.')
        return i


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

    def validatorChangedDoubleAlicotaICMS(self):
        ponto = self.alterarCaracterNum(self.ui.txtAlicotaICMS.text())

        if len(ponto) >1:
            self.ui.txtAlicotaICMS.backspace()
        elif len(ponto) == 1:
            self.ui.txtAlicotaICMS.setText(self.alterarCaracter(self.ui.txtAlicotaICMS.text()))
            numero = self.reformatar(self.ui.txtAlicotaICMS.text())
            formatar = str(numero).split('.')
            if len(formatar[1]) >2:
                self.ui.txtAlicotaICMS.backspace()

    def validatorChangedDoubleAlicotaIPI(self):
        ponto = self.alterarCaracterNum(self.ui.txtAlicotaIPI.text())

        if len(ponto) >1:
            self.ui.txtAlicotaIPI.backspace()
        elif len(ponto) == 1:
            self.ui.txtAlicotaIPI.setText(self.alterarCaracter(self.ui.txtAlicotaIPI.text()))
            numero = self.reformatar(self.ui.txtAlicotaIPI.text())
            formatar = str(numero).split('.')
            if len(formatar[1]) >2:
                self.ui.txtAlicotaIPI.backspace()

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

    def numberQuantidade(self):
        if self.ui.txtQtd.text().isnumeric() == False:
            self.ui.txtQtd.backspace()

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
        self.decricao.clear()
        self.desc.clear()
        self.ncm.clear()
        self.cfop.clear()
        self.csosn.clear()
        self.cst.clear()
        self.tipos.clear()
        self.produto.clear()
        self.decricao.clear()
        self.removeDescricao.clear()
        self.atuaDecricao.clear()
        self.deletarDescricaoProduto()
        self.ui.txtCodig.clear()
        self.ui.txtFornecedor.clear()
        self.ui.txtCodigoMotorista.clear()
        self.ui.txtMotorista.clear()
        self.ui.txtSerie.clear()
        self.ui.txtNumNF.clear()
        self.ui.dateDataEmissao.setDate(QDate.currentDate())
        self.ui.dateDataEntrada.setDate(QDate.currentDate())

        self.ui.txtValorICMS.clear()
        self.ui.txtValorIPI.clear()

        self.ui.txtQtd.clear()
        self.ui.txtValorUnotario.clear()
        self.ui.txtValorTotal.clear()

        self.ui.txtSomatoriaTotalValor.clear()


        self.ui.cBoxNcm.clear()
        self.ui.cBoxCfop.clear()
        self.ui.cBoxCsosn.clear()
        self.ui.cBoxCst.clear()
        self.ui.cBoxProduto.clear()
        self.ui.cBoxUn.clear()
        self.ui.cboxTipos.clear()

        self.editar = False

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
            cell = (self.ui.tabDescricaoProduto.item(row, x).text())
            lista.append(cell)
        a1 = lista[0]
        a2 = lista[1]
        a3 = lista[2]
        a4 = lista[3]
        a5 = lista[4]
        a6 = lista[5]
        a7 = lista[6]
        a8 = lista[7]
        a9 = lista[8]
        a10 = lista[9]
        a11 = lista[10]
        a12 = lista[11]
        a13 = lista[12]
        a14 = lista[13]

        return (a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14)

    def cellClickDescricao(self):
        index = self.ui.tabDescricaoProduto.currentRow()
        lista = self.tabDescricao()

        if lista in self.atuaDecricao:
            self.subtrairTotal(lista[9])
            self.atuaDecricao.remove(lista)
            self.ui.tabDescricaoProduto.removeRow(index)
        else:
            self.subtrairTotal(lista[9])
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

    def setFloatDecimalValorIcms(self):
        if self.ui.txtValorICMS.text() != '':
            self.ui.txtValorICMS.setText(self.ui.txtValorICMS.text()+self.setDecimal(self.ui.txtValorICMS.text()))

    def setFloatDecimalValorIpi(self):
        if self.ui.txtValorIPI.text() != '':
            self.ui.txtValorIPI.setText(self.ui.txtValorIPI.text()+self.setDecimal(self.ui.txtValorIPI.text()))

    def setFloatDecimalAlicotaIcms(self):
        if self.ui.txtValorICMS.text() != '':
            self.ui.txtAlicotaICMS.setText(self.ui.txtAlicotaICMS.text()+self.setDecimal(self.ui.txtAlicotaICMS.text()))

    def setFloatDecimalAlicotaIpi(self):
        if self.ui.txtAlicotaIPI.text() != '':
            self.ui.txtAlicotaIPI.setText(self.ui.txtAlicotaIPI.text()+self.setDecimal(self.ui.txtAlicotaIPI.text()))

    def setFloatDecimalValorTotal(self):
        self.ui.txtValorTotal.setText(self.ui.txtValorTotal.text()+self.setDecimal(self.ui.txtValorTotal.text()))

    def setFloatDecimalValorUni(self):
        if self.ui.txtValorUnotario.text() != '':
            self.ui.txtValorUnotario.setText(self.ui.txtValorUnotario.text() + self.setDecimal(self.ui.txtValorUnotario.text()))


    def setDecimal(self, flutuante):

        ponto = self.alterarCaracterNum(flutuante)

        if len(ponto) == 1:
            retorno = "00"
        elif len(ponto) == 0:
            retorno = ",00"

        return retorno

    def addProdutos(self):
        if self.ui.txtQtd.text() != "" and self.ui.txtValorUnotario.text() != "" and self.ui.txtValorTotal.text() != "":
            ncm = self.ui.cBoxNcm.currentText()
            cfop = self.ui.cBoxCfop.currentText()
            csosn = self.ui.cBoxCsosn.currentText()
            cst = self.ui.cBoxCst.currentText()
            if self.editar == False:
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
                uni = self.substituirCaracterMetros(self.ui.cBoxUn.currentText())
                qtd = self.ui.txtQtd.text()
                valUni = self.ui.txtValorUnotario.text()
                valTotal = self.ui.txtValorTotal.text()

                add = (str(idProduto), produto, ncm, cst,  cfop, csosn, uni, qtd, valUni, valTotal, valorIcms, valorIpi, alicotaIcms, alicotaIpi)
                self.inserirTabela([add])

                self.decricao.append(add)
                self.totalNf()
                self.ui.txtQtd.clear()
                self.ui.txtValorUnotario.clear()
                self.ui.txtValorTotal.clear()

            elif self.editar == True:
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
                uni = self.substituirCaracterMetros(self.ui.cBoxUn.currentText())
                qtd = self.ui.txtQtd.text()
                valUni = self.ui.txtValorUnotario.text()
                valTotal = self.ui.txtValorTotal.text()

                add = (str(idProduto), produto, ncm, cst, cfop, csosn, uni, qtd, valUni, valTotal, valorIcms, valorIpi,
                       alicotaIcms, alicotaIpi)
                self.inserirTabela([add])

                self.atuaDecricao.append(add)

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

    def getIndexTipoNf(self):
        index = self.ui.cboxTipos.currentIndex()

        for lista in self.tipos:
            a = lista[index]
        idTipo = int(a[0])

        return idTipo


    def formatarData(self, data):
        dia = data[:2]
        mes = data[3:5]
        ano = data[6:10]

        return ("%s%s%s" % (ano, mes, dia))

    def substituirVirgula(self, i):
        i = str(i)
        i = i.replace(',', '.')

        return i

    def cadastro(self):
        if self.ui.txtCodig.text() != '' and self.ui.txtFornecedor != '' and self.ui.txtCodigoMotorista.text() != '' and self.ui.txtMotorista.text() != '' and self.ui.txtSerie.text() != '' and self.ui.txtNumNF.text() != '' and self.ui.txtSomatoriaTotalValor.text() != '':
            nota = NotaFiscalRomanieo()
            if self.ui.txtValorICMS.text() == '':
                valorIcms = '0.00'
            else:
                valorIcms = self.substituirVirgula(self.ui.txtValorICMS.text())

            if self.ui.txtValorIPI.text() == '':
                valorIpi = '0.00'
            else:
                valorIpi = self.substituirVirgula(self.ui.txtValorIPI.text())

            if self.ui.txtAlicotaICMS.text() == '':
                alicotaIcms = '0.00'
            else:
                alicotaIcms = self.substituirVirgula(self.ui.txtAlicotaICMS.text())

            if self.ui.txtAlicotaIPI.text() == '':
                alicotaIpi = '0.00'
            else:
                alicotaIpi = self.substituirVirgula(self.ui.txtAlicotaIPI.text())

            nf = NotaFiscal(None, self.ui.txtCodig.text(), self.ui.txtFornecedor.text(), self.getIndexTipoNf(), self.ui.txtCodigoMotorista.text(), self.ui.txtMotorista.text(), self.ui.txtSerie.text(), self.ui.txtNumNF.text(), self.formatarData(self.ui.dateDataEmissao.text()), self.formatarData(self.ui.dateDataEntrada.text()), self.substituirVirgula(self.ui.txtSomatoriaTotalValor.text()), valorIcms, valorIpi, alicotaIcms, alicotaIpi)
            nota.cadastrarNotaFiscal(nf)
            self.idNf = nota.ultimoRegistro()
            self.cadastrarDescricaoProduto()

            self.cancelar()

        else:
            self.mensagem.warning( 'Atenção', "Preencha os campos obrigatorio")

    def cadastrarDescricaoProduto(self):
        nota = NotaFiscalRomanieo()
        i = 0
        for lista in self.decricao:
            a = self.decricao[i]


            idProduto = a[0]
            produto = a[1]
            ncm = a[2]
            cst = a[3]
            cfop = a[4]
            csosn = a[5]
            un = a[6]
            qtd = a[7]
            valUni = a[8]
            valTot = a[9]
            valIcms = a[10]
            valIpi = a[11]
            alicotaIcms = a[12]
            alicotaIpi = a[13]


            __descricao = DescricaoProduto(None, self.idNf, idProduto, produto, ncm, cst, cfop, csosn, un, qtd, valUni, valTot, valIcms, valIpi, alicotaIcms, alicotaIpi)
            nota.cadastrarDescricaoProduto(__descricao)

            i += 1

    def keyPressEvent(self, keyEvent):
        if keyEvent.key() == (QtCore.Qt.Key_F12):
            self.dialogNF = QDialog(self)
            self.__pesquisarNF = Ui_frmConsultarNotasFiscais()
            self.__pesquisarNF.setupUi(self.dialogNF)

            self.__pesquisarNF.txtPesquisar.setValidator(self.validator)

            self.__pesquisarNF.radBtnNumNotaFiscal.clicked.connect(self.ativarCampos)
            self.__pesquisarNF.radBtnDataEntrada.clicked.connect(self.ativarCampos)
            self.__pesquisarNF.radBtnDataEmitido.clicked.connect(self.ativarCampos)
            self.__pesquisarNF.radBtnDataPeriodos.clicked.connect(self.ativarCampos)

            self.__pesquisarNF.txtPesquisar.returnPressed.connect(self.pesquisar)

            self.__pesquisarNF.btnPesquisar.clicked.connect(self.pesquisar)

            self.__pesquisarNF.tabPesquisar.doubleClicked.connect(self.setarCampos)

            self.dialogNF.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            self.dialogNF.exec_()

    def ativarCampos(self):
        if self.__pesquisarNF.radBtnNumNotaFiscal.isChecked():
            self.__pesquisarNF.txtDataInicial.setEnabled(False)
            self.__pesquisarNF.txtDataFinal.setEnabled(False)
            self.__pesquisarNF.txtPesquisar.setEnabled(True)
            self.__pesquisarNF.btnPesquisar.setEnabled(True)

        elif self.__pesquisarNF.radBtnDataEntrada.isChecked():
            self.__pesquisarNF.txtDataInicial.setEnabled(True)
            self.__pesquisarNF.txtDataFinal.setEnabled(False)
            self.__pesquisarNF.txtPesquisar.setEnabled(False)
            self.__pesquisarNF.btnPesquisar.setEnabled(True)

        elif self.__pesquisarNF.radBtnDataEmitido.isChecked():
            self.__pesquisarNF.txtDataInicial.setEnabled(True)
            self.__pesquisarNF.txtDataFinal.setEnabled(False)
            self.__pesquisarNF.txtPesquisar.setEnabled(False)
            self.__pesquisarNF.btnPesquisar.setEnabled(True)

        elif self.__pesquisarNF.radBtnDataPeriodos.isChecked():
            self.__pesquisarNF.txtDataInicial.setEnabled(True)
            self.__pesquisarNF.txtDataFinal.setEnabled(True)
            self.__pesquisarNF.txtPesquisar.setEnabled(False)
            self.__pesquisarNF.btnPesquisar.setEnabled(True)

    def pesquisar(self):
        __pesDao = NotaFiscalRomanieo()
        if self.__pesquisarNF.radBtnNumNotaFiscal.isChecked():
                __codigo = self.__pesquisarNF.txtPesquisar.text()
                __retorno = __pesDao.pesquisarNumNotaFiscal(__codigo)
                self.setarTabelaPesquisaEditar(__retorno)

        elif self.__pesquisarNF.radBtnDataEmitido.isChecked():
                __dataInicial = self.formatarData(self.__pesquisarNF.txtDataInicial.text())
                __retorno = __pesDao.pesquisarDataEmitido(__dataInicial)
                self.setarTabelaPesquisaEditar(__retorno)

        elif self.__pesquisarNF.radBtnDataEntrada.isChecked():
                __dataInicial = self.formatarData(self.__pesquisarNF.txtDataInicial.text())
                __retorno = __pesDao.pesquisarDataEntrada(__dataInicial)
                self.setarTabelaPesquisaEditar(__retorno)

        elif self.__pesquisarNF.radBtnDataPeriodos.isChecked():
                __dataInicial = self.formatarData(self.__pesquisarNF.txtDataInicial.text())
                __dataFinal= self.formatarData(self.__pesquisarNF.txtDataFinal.text())
                __retorno = __pesDao.pesquisarDataPeriodos(__dataInicial, __dataFinal)
                self.setarTabelaPesquisaEditar(__retorno)

        else:
            self.mensagem.warning( 'Atenção', "Selecione uma das opções de pesquisa")

    def setarTabelaPesquisaEditar(self, __retorno):
        qtde_registros = len(__retorno)
        self.__pesquisarNF.tabPesquisar.setRowCount(qtde_registros)

        linha = 0
        for pesqui in __retorno:
            # capturando os dados da tupla

            codigo = pesqui[0]
            tipo = pesqui[1]
            serie = pesqui[2]
            numNf = pesqui[3]
            dataEmissao = pesqui[4]
            dataEntrada = pesqui[5]
            valorTotal = pesqui[6]
            valorIcms = pesqui[7]
            valorIpi = pesqui[8]
            alicotaIcms = pesqui[9]
            alicotaIpi = pesqui[10]

            # preenchendo o grid de pesquisa
            self.__pesquisarNF.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
            self.__pesquisarNF.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(tipo)))
            self.__pesquisarNF.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(serie)))
            self.__pesquisarNF.tabPesquisar.setItem(linha, 3, QtGui.QTableWidgetItem(str(numNf)))
            self.__pesquisarNF.tabPesquisar.setItem(linha, 4, QtGui.QTableWidgetItem(str(dataEmissao)))
            self.__pesquisarNF.tabPesquisar.setItem(linha, 5, QtGui.QTableWidgetItem(str(dataEntrada)))
            self.__pesquisarNF.tabPesquisar.setItem(linha, 6, QtGui.QTableWidgetItem(str(valorTotal)))
            self.__pesquisarNF.tabPesquisar.setItem(linha, 7, QtGui.QTableWidgetItem(str(valorIcms)))
            self.__pesquisarNF.tabPesquisar.setItem(linha, 8, QtGui.QTableWidgetItem(str(valorIpi)))
            self.__pesquisarNF.tabPesquisar.setItem(linha, 9, QtGui.QTableWidgetItem(str(alicotaIcms)))
            self.__pesquisarNF.tabPesquisar.setItem(linha, 10, QtGui.QTableWidgetItem(str(alicotaIpi)))

            linha += 1

    def setarCampos(self):
        nfDao = NotaFiscalRomanieo()
        itens = []

        for item in self.__pesquisarNF.tabPesquisar.selectedItems():
            itens.append(item.text())

        codigo = itens[0]
        tipo = itens[1]
        serie = itens[2]
        numNf = itens[3]
        dataEmissao = itens[4]
        dataEntrada = itens[5]
        valorTotal = itens[6]
        valorIcms = itens[7]
        valorIpi = itens[8]
        alicotaIcms = itens[9]
        alicotaIpi = itens[10]

        forne = nfDao.pesquisarFornecedorNF(codigo)

        motor = nfDao.pesquisarMotoristaNF(codigo)

        __dados = NotaFiscal(codigo, forne[0], forne[1], tipo, motor[0], motor[1]+' '+motor[2], serie, numNf, dataEmissao, dataEntrada, valorTotal, valorIcms, valorIpi, alicotaIcms, alicotaIpi)
        self.botoesEditar()
        self.setCampos(__dados)
        self.pesquisarDesquicao(codigo)
        self.dialogNF.close()


    def setCampos(self, campos):
        self.ui.txtCodig.setEnabled(False)
        self.ui.txtCodigoMotorista.setEnabled(False)

        self.idNf = int(campos.getIdNotaFiscal)
        self.idMotorista = int(campos.getIdMotorista)
        self.idFornecedor = int(campos.getIdFornecedor)
        self.ui.txtCodig.setText(str(campos.getIdFornecedor))
        self.ui.txtFornecedor.setText(campos.getFornecedor)
        self.ui.txtCodigoMotorista.setText(str(campos.getIdMotorista))
        self.ui.txtMotorista.setText(campos.getMotorista)


        self.ui.txtSerie.setText(campos.getSerie)
        self.ui.txtNumNF.setText(campos.getNumNotaFiscal)
        self.ui.cboxTipos.setCurrentIndex(self.ui.cboxTipos.findText(campos.getIdTipoNf))

        self.ui.dateDataEmissao.setDate(self.formatarDataRetorno(campos.getDataEmissao))
        self.ui.dateDataEntrada.setDate(self.formatarDataRetorno(campos.getDataEntrada))
        self.ui.txtValorICMS.setText(campos.getValorIcms)
        self.ui.txtValorIPI.setText(campos.getValorIpi)
        self.ui.txtAlicotaICMS.setText(campos.getValorIcms)
        self.ui.txtAlicotaIPI.setText(campos.getAlicotaIpi)

        self.ui.txtSomatoriaTotalValor.setText(campos.getValorTotal)


        self.editar = True

    def pesquisarDesquicao(self, campos):
        nfDao = NotaFiscalRomanieo()
        id = nfDao.pesquisaDescricaoProduto(campos)

        if id != []:
            self.setTabelaDescricao(id)

    def setTabelaDescricao(self, __retorno):
        qtde_registros = len(__retorno)
        self.ui.tabDescricaoProduto.setRowCount(qtde_registros)

        linha = 0
        for pesqui in __retorno:
            idDescricao = str(pesqui[0])
            idProduto = pesqui[1]
            produto = pesqui[2]
            ncm = pesqui[3]
            cst = pesqui[4]
            cfop = pesqui[5]
            csosn = pesqui[6]
            un = pesqui[7]
            qtd = pesqui[8]
            valUni = pesqui[9]
            valTot = pesqui[10]
            valIcms = pesqui[11]
            valIpi = pesqui[12]
            alicotaIcms = pesqui[13]
            alicotaIpi = pesqui[14]


            self.ui.tabDescricaoProduto.setItem(linha, 0, QtGui.QTableWidgetItem(str(idProduto)))
            self.ui.tabDescricaoProduto.setItem(linha, 1, QtGui.QTableWidgetItem(str(produto)))
            self.ui.tabDescricaoProduto.setItem(linha, 2, QtGui.QTableWidgetItem(str(ncm)))
            self.ui.tabDescricaoProduto.setItem(linha, 3, QtGui.QTableWidgetItem(str(cst)))
            self.ui.tabDescricaoProduto.setItem(linha, 4, QtGui.QTableWidgetItem(str(cfop)))
            self.ui.tabDescricaoProduto.setItem(linha, 5, QtGui.QTableWidgetItem(str(csosn)))
            self.ui.tabDescricaoProduto.setItem(linha, 6, QtGui.QTableWidgetItem(str(un)))
            self.ui.tabDescricaoProduto.setItem(linha, 7, QtGui.QTableWidgetItem(str(qtd)))
            self.ui.tabDescricaoProduto.setItem(linha, 8, QtGui.QTableWidgetItem(str(valUni)))
            self.ui.tabDescricaoProduto.setItem(linha, 9, QtGui.QTableWidgetItem(str(valTot)))
            self.ui.tabDescricaoProduto.setItem(linha, 10, QtGui.QTableWidgetItem(str(valIcms)))
            self.ui.tabDescricaoProduto.setItem(linha, 11, QtGui.QTableWidgetItem(str(valIpi)))
            self.ui.tabDescricaoProduto.setItem(linha, 12, QtGui.QTableWidgetItem(str(alicotaIcms)))
            self.ui.tabDescricaoProduto.setItem(linha, 13, QtGui.QTableWidgetItem(str(alicotaIpi)))


            lista = (idDescricao, idProduto, produto, ncm, cst, cfop, csosn, un, qtd, valUni, valTot, valIcms, valIpi, alicotaIcms, alicotaIpi)
            self.decricao.append(lista)


            linha += 1

    def atualizar(self):
        if self.ui.txtCodig.text() != '' and self.ui.txtFornecedor != '' and self.ui.txtCodigoMotorista.text() != '' and self.ui.txtMotorista.text() != '' and self.ui.txtSerie.text() != '' and self.ui.txtNumNF.text() != '' and self.ui.txtSomatoriaTotalValor.text() != '':
            nota = NotaFiscalRomanieo()
            if self.ui.txtValorICMS.text() == '':
                valorIcms = '0.00'
            else:
                valorIcms = self.substituirVirgula(self.ui.txtValorICMS.text())

            if self.ui.txtValorIPI.text() == '':
                valorIpi = '0.00'
            else:
                valorIpi = self.substituirVirgula(self.ui.txtValorIPI.text())

            if self.ui.txtAlicotaICMS.text() == '':
                alicotaIcms = '0.00'
            else:
                alicotaIcms = self.substituirVirgula(self.ui.txtAlicotaICMS.text())

            if self.ui.txtAlicotaIPI.text() == '':
                alicotaIpi = '0.00'
            else:
                alicotaIpi = self.substituirVirgula(self.ui.txtAlicotaIPI.text())

            if self.removeDescricao  != []:
                self.deletarDescricao()

            if self.atuaDecricao != []:
                self.atualizaDescricao()


            nfDao = NotaFiscalRomanieo()
            nf = NotaFiscal(self.idNf, self.ui.txtCodig.text(), self.ui.txtFornecedor.text(), self.getIndexTipoNf(),self.ui.txtCodigoMotorista.text(), self.ui.txtMotorista.text(), self.ui.txtSerie.text(),self.ui.txtNumNF.text(), self.formatarData(self.ui.dateDataEmissao.text()),self.formatarData(self.ui.dateDataEntrada.text()),self.substituirVirgula(self.ui.txtSomatoriaTotalValor.text()), valorIcms, valorIpi,alicotaIcms, alicotaIpi)
            nfDao.atualizarNotasFiscais(nf)

            self.cancelar()
        else:
            self.mensagem.warning('Atenção', "Por Favor preencha os campos obrigatorios")

    def atualizaDescricao(self):
        nfDao = NotaFiscalRomanieo()
        i = 0
        for lista in self.atuaDecricao:
                a = self.atuaDecricao[i]

                idProduto = a[0]
                produto = a[1]
                ncm = a[2]
                cst = a[3]
                cfop = a[4]
                csosn = a[5]
                un = a[6]
                qtd = a[7]
                valUni = a[8]
                valTot = a[9]
                valIcms = a[10]
                valIpi = a[11]
                alicotaIcms = a[12]
                alicotaIpi = a[13]

                __descricao = DescricaoProduto(None, self.idNf, idProduto, produto, ncm, cst, cfop, csosn, un, qtd, valUni, valTot, valIcms, valIpi, alicotaIcms, alicotaIpi)
                nfDao.cadastrarDescricaoProduto(__descricao)

                i += 1

    def deletarDescricao(self):
        nfDao = NotaFiscalRomanieo()
        i = 0
        for lista in self.removeDescricao :
            a = self.removeDescricao[i]

            idDescricao = int(a[0])

            nfDao.deletarDescricao(idDescricao, self.idNf)

            i += 1

    def deletarDescricaoFrom(self):
        nfDao = NotaFiscalRomanieo()
        i = 0
        for lista in self.decricao :
            a = self.decricao[i]

            idDescricao = int(a[0])

            nfDao.deletarDescricao(idDescricao, self.idNf)

            i += 1

    def deletar(self):
        nfDao = NotaFiscalRomanieo()
        carre = nfDao.pesquisarTabelaDescarregamento(self.idNf)

        if carre == []:
            try:
                _fromUtf8 = QtCore.QString.fromUtf8
            except AttributeError:
                def _fromUtf8(s):
                    return s

            self.msgBox = QtGui.QMessageBox()
            self.msgBox.setWindowTitle('Menssagem')
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/question.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.msgBox.setWindowIcon(icon)
            self.msgBox.setIconPixmap(QtGui.QPixmap(_fromUtf8("./imagens/icon-question.png")))
            self.msgBox.setText("Tem certeza que deseja excluir esse registro")
            btnSim = QtGui.QPushButton('Sim')
            self.msgBox.addButton(btnSim, QtGui.QMessageBox.YesRole)
            btnNao = QtGui.QPushButton('Não')
            self.msgBox.addButton(btnNao, QtGui.QMessageBox.NoRole)
            btnSim.clicked.connect(self.simDeletar)
            btnNao.clicked.connect(self.fechar)
            btnNao.setFocus()
            self.msgBox.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            self.msgBox.exec_()
        else:
            MensagemBox().warning('Atenção', 'Impossivel fazer essa operação, pois essa pessoa esta relacionada com outro formulario')

    def simDeletar(self):
            nfDao = NotaFiscalRomanieo()
            codigo = self.idNf
            a = nfDao.deletarNF(codigo)
            self.deletarDescricaoProd()

            if self.decricao != []:
                self.deletarDescricaoFrom()

            if self.removeDescricao != []:
                self.deletarDescricao()

            if a  == True :
                MensagemBox().informacao('Mensagem', 'Cadastro deletar com sucesso!')
            else:
                MensagemBox().critico('Erro', 'Erro ao deletar as informações no banco de dados')

            self.cancelar()
            self.msgBox.close()

    def fechar(self):
        self.msgBox.close()

    def deletarDescricaoProd(self):
        nfDao = NotaFiscalRomanieo()

        index = 0
        for lista in self.produto:
            a = lista[index]
            nfDao.deletarDescricao(a[0], self.idNf)
            index+=1