import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from decimal import Decimal


from controller.getSetDescricaoProduto import DescricaoProduto
from controller.getSetNotaFiscal import NotaFiscal
from controller.getSetPesquisaNotaFiscal import PesquisaNotaFiscal
from controller.getSetRomaneio import Romaneio
from dao.notaFiscalRomaneioDao import NotaFiscalRomanieo
from dao.pesquisaEmpresa import PesquisaEmpresaDao
from dao.pesquisarFornecedor import PesquisarFornecedorDao
from dao.pesquisarMotorista import PesquisarMotoristaDao
from dao.pesquisarNotaFiscalRomaneioDao import PesquisarNotaFiscalRomaneioDao
from telas.frmEntradaNF import Ui_frmEntradaNF, _fromUtf8
from telas.frmEntradaNotasRomaneios import Ui_frmEntradaNotaRomaneios
from telas.frmPesquisarEmpresa import Ui_frmConsultarEmpresa
from telas.frmPesquisarFornecedor import Ui_frmConsultarFornecedores
from telas.frmPesquisarMotorista import Ui_frmConsultarMotoristas
from telas.frmPesquisarNotasFiscais import Ui_frmConsultarNotasFiscais


class CadastroNotaFiscal(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmEntradaNF()
        self.ui.setupUi(self)
        self.validarCamposFlutuante()
        self.desc = []

        self.unidadeMedida()
        self.tiposNF()

        self.ui.txtBaseICMS.textChanged.connect(self.alterarCaracter)

        self.ui.txtCodig.textChanged.connect(self.numberCodigoFornecedor)
        self.ui.txtCodigoMotorista.textChanged.connect(self.numberCodigoMotorista)
        self.ui.txtSerie.textChanged.connect(self.numberSerie)
        self.ui.txtModelo.textChanged.connect(self.numberModelo)
        self.ui.txtNumNF.textChanged.connect(self.numberNumNF)
        self.ui.txtChaveAcessoNF.textChanged.connect(self.numberChaveAcessoNF)
        self.ui.txtProtocoloAuto.textChanged.connect(self.numberProtocoloAuto)
        self.ui.txtQtd.textChanged.connect(self.numberQuantidade)
        self.ui.txtInsMunicipal.textChanged.connect(self.numberInsMunicipal)

    def validarCamposFlutuante(self):

        validarReal = QtGui.QDoubleValidator(0, 99999, 0, self)
        validarReal.setDecimals(2)

        listaObj = [self.ui.txtIcmsPorcento, self.ui.txtBaseICMS, self.ui.txtICMSRed,  self.ui.txtValorICMS, self.ui.txtBaseICMSST,
                    self.ui.txtValorICMSSub, self.ui.txtValorPIS, self.ui.txtValorConfins, self.ui.txtValorProduto, self.ui.txtValorFrete,
                    self.ui.txtValorSeguro, self.ui.txtValorDesconto, self.ui.txtOutrasDespesas, self.ui.txtValorIPI, self.ui.txtValorNF,
                    self.ui.txtValorUnotario, self.ui.txtValorTotal, self.ui.txtValorTotalServico, self.ui.txtBaseIssqn, self.ui.txtValorIssqn]

        for objeto in listaObj:
            objeto.setValidator(validarReal)

    def keyPressEvent(self, QKeyEvent):
        pass

    def alterarCaracter(self):
        i = self.ui.txtBaseICMS.text()
        i = i.replace('.', ',')

        self.ui.txtBaseICMS.setText(i)

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

    def numberChaveAcessoNF(self):
        if self.ui.txtChaveAcessoNF.text().isnumeric() == False:
            self.ui.txtChaveAcessoNF.backspace()

    def numberProtocoloAuto(self):
        if self.ui.txtProtocoloAuto.text().isnumeric() == False:
            self.ui.txtProtocoloAuto.backspace()

    def numberQuantidade(self):
        if self.ui.txtQtd.text().isnumeric() == False:
            self.ui.txtQtd.backspace()

    def numberInsMunicipal(self):
        if self.ui.txtInsMunicipal.text().isnumeric() == False:
            self.ui.txtInsMunicipal.backspace()


    def upperCaseDestinatario(self):
        self.ui.txtFornecedor.setText(self.ui.txtFornecedor.text().upper())

    def upperCaseMotorista(self):
        self.ui.txtMotorista.setText(self.ui.txtMotorista.text().upper())

    def unidadeMedida(self):
        lista = ["UN", "KM", "HM", "DAM", "M", "DM", "CM", "MM", "KM²", "HM²", "DAM²", "M²", "DM²", "CM²", "MM²", "KM³", "HM³", "DAM³", "M³", "DM³", "CM³", "MM³", "T", "KG", "HG", "DAG", "G", "DG", "CG", "MG", "KL", "HL", "DAL", "L", "DL", "CL", "ML", "ST"]
        #lista = ["UN", "M", "M²", "M³", "T", "ST", "L"]
        for i in lista:
            self.ui.cBoxUn.addItem(i)

    def tiposNF(self):
        lista = ["NF", "NF-e", "NFC-e", "NFS-e", "CT-e", "DANFE"]
        for i in lista:
            self.ui.cboxTipos.addItem(i)

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

    def formatarData(self, data):
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
        self.ui.txtIcmsPorcento.clear()
        self.ui.txtICMSRed.clear()
        self.ui.txtChaveAcessoNF.clear()
        self.ui.txtProtocoloAuto.clear()
        self.ui.dateDataEmissao.setDate(QDate.currentDate())
        self.ui.dateDataEntrada.setDate(QDate.currentDate())

        self.ui.txtBaseICMS.clear()
        self.ui.txtValorICMS.clear()
        self.ui.txtBaseICMSST.clear()
        self.ui.txtValorICMSSub.clear()
        self.ui.txtValorPIS.clear()
        self.ui.txtValorConfins.clear()
        self.ui.txtValorProduto.clear()
        self.ui.txtValorFrete.clear()
        self.ui.txtValorSeguro.clear()
        self.ui.txtValorDesconto.clear()
        self.ui.txtOutrasDespesas.clear()
        self.ui.txtValorIPI.clear()
        self.ui.txtValorNF.clear()

        self.ui.txtQtd.clear()
        self.ui.txtValorUnotario.clear()
        self.ui.txtValorTotal.clear()

        self.ui.txtSomatoriaTotalValor.clear()
        self.ui.txtSomatoriaTotalQtd.clear()

        self.ui.txtInsMunicipal.clear()
        self.ui.txtValorTotalServico.clear()
        self.ui.txtBaseIssqn.clear()
        self.ui.txtValorIssqn.clear()

    def deletarDescricaoProduto(self):
        for i in reversed(range(self.ui.tabDescricaoProduto.rowCount())):
            self.ui.tabDescricaoProduto.removeRow(i)

        def cadastro(self):
            if self.ui.txtCodigo.text() != '' and self.ui.txtCnpj.text() != '' and self.ui.txtInscricaoEstadua.text() != '' and self.ui.txtFantasia.text() != '' and self.ui.txtRazaoSocial.text() != '':
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

        '''
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