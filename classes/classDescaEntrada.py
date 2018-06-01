import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from classes.classMensagemBox import MensagemBox
from classes.classValidator import Validator
from controller.getSetFornecedor import Fornecedor
from controller.getSetMotorista import Motorista
from controller.getSetNotaFiscal import NotaFiscal
from dao.descarregamentoEntradaDao import DescarreEntradaDao
from dao.fornecedorDao import FornecedorDao
from dao.motoristaDao import MotoristaDao
from dao.notaFiscalRomaneioDao import NotaFiscalRomanieo
from telas.frmEntradaVeiculosDescarregamento import Ui_frmEntradaVeiculosDescarregamento
from telas.frmPesquisarFornecedor import Ui_frmPesquisarFornecedor
from telas.frmPesquisarMotorista import Ui_frmConsultarMotoristas
from telas.frmPesquisarNotasFiscais import Ui_frmConsultarNotasFiscais


class DescaEntrada(QtGui.QDialog):

    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmEntradaVeiculosDescarregamento()
        self.ui.setupUi(self)
        self.validator = Validator()
        self.mensagem = MensagemBox()

        self.ui.btnNovo.clicked.connect(self.novo)
        self.ui.btnCancelar.clicked.connect(self.cancelar)

        self.ui.btnPesquisarNotaFiscal.clicked.connect(self.pesquisarNf)
        self.ui.btnPesquisarFornecedor.clicked.connect(self.pesquisarFornecedor)
        self.ui.btnPesquisarMotorista.clicked.connect(self.pesquisarMotor)

        self.ui.txtidMotorista.returnPressed.connect(self.setMotorista)
        self.ui.txtIdFornecedor.returnPressed.connect(self.setFornecedor)
        self.ui.txtCodigo.returnPressed.connect(self.setNf)

        self.ui.txtidMotorista.editingFinished.connect(self.setMotoristaFinish)
        self.ui.txtIdFornecedor.editingFinished.connect(self.setFornecedorFinish)
        self.ui.txtCodigo.editingFinished.connect(self.setNfFinish)


    def novo(self):
        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(True)
        self.ui.btnCancelar.setEnabled(True)
        self.ui.grbNotaFiscal.setEnabled(True)
        self.ui.grbDadosFornecedor.setEnabled(True)
        self.ui.grbDadosMotorista.setEnabled(True)
        self.ui.txtData.setEnabled(True)
        self.ui.txtHora.setEnabled(True)

    def cancelar(self):
        self.ui.btnNovo.setEnabled(True)
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(False)

        self.desativarCampos()


    def desativarCampos(self):
        self.ui.btnPesquisarNotaFiscal.setEnabled(False)

        self.ui.txtData.setEnabled(False)
        self.ui.txtHora.setEnabled(False)

        self.ui.grbNotaFiscal.setEnabled(False)
        self.ui.grbDadosFornecedor.setEnabled(False)
        self.ui.grbDadosMotorista.setEnabled(False)

        self.limparNotasFiscal()
        self.limparFornecedor()
        self.limparMotorista()

    def ativarCampos(self):
        self.limparPesquisa()
        self.ui.btnPesquisarNotaFiscal.setEnabled(False)


        self.limparNotasFiscal()

        self.ui.txtData.setEnabled(True)
        self.ui.txtHora.setEnabled(True)

        self.ui.grbNotaFiscal.setEnabled(True)
        self.ui.grbDadosFornecedor.setEnabled(True)
        self.ui.grbDadosMotorista.setEnabled(True)


    def limparNotasFiscal(self):
        self.ui.txtNumeroNotaFiscal.clear()
        self.ui.txtProduto.clear()

    def limparFornecedor(self):
        self.ui.txtIdFornecedor.clear()
        self.ui.txtNomeFornecedor.clear()
        self.ui.txtRazaoSocialFornecedor.clear()
        self.ui.txtCnpjFornecedor.clear()
        self.ui.txtInscricaoEstaduaFornecedor.clear()
        self.ui.txtEnderecoFornecedor.clear()
        self.ui.txtNumeroFornecedor.clear()
        self.ui.txtComplementoFornecedor.clear()
        self.ui.txtBairroFornecedor.clear()
        self.ui.txtCidadeFornecedor.clear()
        self.ui.txtEstadoFornecedor.clear()
        self.ui.txtCepFornecedor.clear()


    def limparMotorista(self):
        self.ui.txtidMotorista.clear()
        self.ui.txtNomeMotorista.clear()
        self.ui.txtModeloMotorista.clear()
        self.ui.txtMarcaMotorista.clear()
        self.ui.txtPlacaMotorista.clear()

    def pesquisarMotorista(self):
            self.dialog = QDialog(self)
            self.__pesquisarMotorista = Ui_frmConsultarMotoristas()
            self.__pesquisarMotorista.setupUi(self.dialog)

            self.__pesquisarMotorista.txtPesquisar.setValidator(self.validator)

            self.__pesquisarMotorista.txtPesquisar.returnPressed.connect(self.pesquisarMotor)

            self.__pesquisarMotorista.btnPesquisar.clicked.connect(self.pesquisarMotor)

            self.__pesquisarMotorista.tabPesquisar.doubleClicked.connect(self.setarCamposMotor)

            self.dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            self.dialog.exec_()

    def pesquisarMotor(self):
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
                self.setarTabelaPesquisaEditar(__retorno)

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

    def setarCamposMotor(self):
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
        self.dialog.close()

    def setCamposMotorista(self, campos):
        self.ui.txtidMotorista.setText(campos.getIdMotorista)
        self.ui.txtNomeMotorista.setText(campos.getNome + " " + campos.getSobrenome)
        self.ui.txtModeloMotorista.setText(campos.getModelo)
        self.ui.txtMarcaMotorista.setText(campos.getMarca)
        self.ui.txtPlacaMotorista.setText(campos.getPlaca)

    def pesquisarFornecedor(self):
            self.dialog = QDialog(self)
            self.__pesquisarFornecedor = Ui_frmPesquisarFornecedor()
            self.__pesquisarFornecedor.setupUi(self.dialog)

            self.__pesquisarFornecedor.txtPesquisar.setValidator(self.validator)

            self.__pesquisarFornecedor.txtPesquisar.returnPressed.connect(self.pesquisarForn)

            self.__pesquisarFornecedor.btnPesquisar.clicked.connect(self.pesquisarForn)

            self.__pesquisarFornecedor.tabPesquisar.doubleClicked.connect(self.setarCamposForn)

            self.dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            self.dialog.exec_()

    def pesquisarForn(self):
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
            self.setarTabelaPesquisaEditarFornecedor(__retorno)

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

    def setarCamposForn(self):
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
        self.setCamposFornecedor(__dados, endereco, numero, complemento, bairro, cidade, estado, cep)
        self.dialog.close()

    def setCamposFornecedor(self, campos, ende, num, comp, bai, cid, est, cep):
        self.ui.txtIdFornecedor.setText(campos.getIdFornecedor)
        self.ui.txtNomeFornecedor.setText(campos.getFantasia            )
        self.ui.txtRazaoSocialFornecedor.setText(campos.getRazaoSocial)
        self.ui.txtInscricaoEstaduaFornecedor.setText(campos.getInscricaoEstadual)
        self.ui.txtCnpjFornecedor.setText(campos.getCnpj)
        self.ui.txtEnderecoFornecedor.setText(ende)
        self.ui.txtNumeroFornecedor.setText(num)
        self.ui.txtComplementoFornecedor.setText(comp)
        self.ui.txtBairroFornecedor.setText(bai)
        self.ui.txtCidadeFornecedor.setText(cid)
        self.ui.txtEstadoFornecedor.setText(est)
        self.ui.txtCepFornecedor.setText(cep)

    def pesquisarNf(self):
            self.dialogNF = QDialog(self)
            self.__pesquisarNF = Ui_frmConsultarNotasFiscais()
            self.__pesquisarNF.setupUi(self.dialogNF)

            self.__pesquisarNF.txtPesquisar.setValidator(self.validator)

            self.__pesquisarNF.radBtnNumNotaFiscal.clicked.connect(self.ativarCamposNf)
            self.__pesquisarNF.radBtnDataEntrada.clicked.connect(self.ativarCamposNf)
            self.__pesquisarNF.radBtnDataEmitido.clicked.connect(self.ativarCamposNf)
            self.__pesquisarNF.radBtnDataPeriodos.clicked.connect(self.ativarCamposNf)

            self.__pesquisarNF.txtPesquisar.returnPressed.connect(self.pesquisarNotasFiscais)

            self.__pesquisarNF.btnPesquisar.clicked.connect(self.pesquisarNotasFiscais)

            self.__pesquisarNF.tabPesquisar.doubleClicked.connect(self.setarCamposNf)

            self.dialogNF.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            self.dialogNF.exec_()

    def ativarCamposNf(self):
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

    def pesquisarNotasFiscais(self):
        __pesDao = NotaFiscalRomanieo()
        if self.__pesquisarNF.radBtnNumNotaFiscal.isChecked():
                __codigo = self.__pesquisarNF.txtPesquisar.text()
                __retorno = __pesDao.pesquisarNumNotaFiscal(__codigo)
                self.setarTabelaPesquisaEditarNotasFiscais(__retorno)

        elif self.__pesquisarNF.radBtnDataEmitido.isChecked():
                __dataInicial = self.formatarData(self.__pesquisarNF.txtDataInicial.text())
                __retorno = __pesDao.pesquisarDataEmitido(__dataInicial)
                self.setarTabelaPesquisaEditarNotasFiscais(__retorno)

        elif self.__pesquisarNF.radBtnDataEntrada.isChecked():
                __dataInicial = self.formatarData(self.__pesquisarNF.txtDataInicial.text())
                __retorno = __pesDao.pesquisarDataEntrada(__dataInicial)
                self.setarTabelaPesquisaEditarNotasFiscais(__retorno)

        elif self.__pesquisarNF.radBtnDataPeriodos.isChecked():
                __dataInicial = self.formatarData(self.__pesquisarNF.txtDataInicial.text())
                __dataFinal= self.formatarData(self.__pesquisarNF.txtDataFinal.text())
                __retorno = __pesDao.pesquisarDataPeriodos(__dataInicial, __dataFinal)
                self.setarTabelaPesquisaEditarNotasFiscais(__retorno)

        else:
            self.mensagem.warning( 'Atenção', "Selecione uma das opções de pesquisa")

    def setarTabelaPesquisaEditarNotasFiscais(self, __retorno):
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

    def setarCamposNf(self):
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
        desDao = DescarreEntradaDao()
        produto = desDao.pesquisarProduto(codigo)
        self.setCamposNotasFiscais(__dados, produto)
        self.dialogNF.close()


    def setCamposNotasFiscais(self, campos, produto):
        self.ui.txtNumeroNotaFiscal.setText(campos.getNumNotaFiscal)
        self.ui.txtProduto.setText(str(produto))


    def setNf(self):
        moto = DescarreEntradaDao()
        emp = moto.pesquisarNumNotaFiscal(self.ui.txtCodigo.text())
        produto = moto.pesquisarProduto(self.ui.txtCodigo.text())

        if emp == []:
            MensagemBox().warning('Mensagem', "Atenção não existe nenhum cadastro deste NF")
            self.ui.txtNumeroNotaFiscal.clear()
            self.ui.txtProduto.clear()
        else:
            for empres in emp:
                self.ui.txtNumeroNotaFiscal.setText(str(empres[3]))
                self.ui.txtProduto.setText(produto)


    def setNfFinish(self):
        moto = DescarreEntradaDao()
        emp = moto.pesquisarNumNotaFiscal(self.ui.txtCodigo.text())
        produto = moto.pesquisarProduto(self.ui.txtCodigo.text())

        if emp == []:
            self.ui.txtNumeroNotaFiscal.clear()
            self.ui.txtProduto.clear()

        else:
            for empres in emp:
                self.ui.txtNumeroNotaFiscal.setText(str(empres[3]))
                self.ui.txtProduto.setText(produto)

    def setFornecedor(self):
        moto = DescarreEntradaDao()
        emp = moto.pesquisarFornecedor(self.ui.txtIdFornecedor.text())

        if emp == []:
            MensagemBox().warning('Mensagem', "Atenção não existe nenhum cadastro deste fornecedor ou esta inativo")
            self.ui.txtNomeFornecedor.clear()
            self.ui.txtRazaoSocialFornecedor.clear()
            self.ui.txtInscricaoEstaduaFornecedor.clear()
            self.ui.txtCnpjFornecedor.clear()
            self.ui.txtEnderecoFornecedor.clear()
            self.ui.txtNumeroFornecedor.clear()
            self.ui.txtComplementoFornecedor.clear()
            self.ui.txtBairroFornecedor.clear()
            self.ui.txtCidadeFornecedor.clear()
            self.ui.txtEstadoFornecedor.clear()
            self.ui.txtCepFornecedor.clear()
        else:
            for empres in emp:
                self.ui.txtNomeFornecedor.setText(empres[3])
                self.ui.txtRazaoSocialFornecedor.setText(empres[2])
                self.ui.txtInscricaoEstaduaFornecedor.setText(empres[5])
                self.ui.txtCnpjFornecedor.setText(empres[4])
                self.ui.txtEnderecoFornecedor.setText(empres[9])
                self.ui.txtNumeroFornecedor.setText(empres[10])
                self.ui.txtComplementoFornecedor.setText(empres[11])
                self.ui.txtBairroFornecedor.setText(empres[12])
                self.ui.txtCidadeFornecedor.setText(empres[13])
                self.ui.txtEstadoFornecedor.setText(empres[14])
                self.ui.txtCepFornecedor.setText(empres[15])


    def setFornecedorFinish(self):
        moto = DescarreEntradaDao()
        emp = moto.pesquisarFornecedor(self.ui.txtIdFornecedor.text())

        if emp == []:
            self.ui.txtNomeFornecedor.clear()
            self.ui.txtRazaoSocialFornecedor.clear()
            self.ui.txtInscricaoEstaduaFornecedor.clear()
            self.ui.txtCnpjFornecedor.clear()
            self.ui.txtEnderecoFornecedor.clear()
            self.ui.txtNumeroFornecedor.clear()
            self.ui.txtComplementoFornecedor.clear()
            self.ui.txtBairroFornecedor.clear()
            self.ui.txtCidadeFornecedor.clear()
            self.ui.txtEstadoFornecedor.clear()
            self.ui.txtCepFornecedor.clear()

        else:
            for empres in emp:
                self.ui.txtNomeFornecedor.setText(empres[3])
                self.ui.txtRazaoSocialFornecedor.setText(empres[2])
                self.ui.txtInscricaoEstaduaFornecedor.setText(empres[5])
                self.ui.txtCnpjFornecedor.setText(empres[4])
                self.ui.txtEnderecoFornecedor.setText(empres[9])
                self.ui.txtNumeroFornecedor.setText(empres[10])
                self.ui.txtComplementoFornecedor.setText(empres[11])
                self.ui.txtBairroFornecedor.setText(empres[12])
                self.ui.txtCidadeFornecedor.setText(empres[13])
                self.ui.txtEstadoFornecedor.setText(empres[14])
                self.ui.txtCepFornecedor.setText(empres[15])



    def setMotorista(self):
        moto = DescarreEntradaDao()
        emp = moto.pesquisarMotorista(self.ui.txtidMotorista.text())

        if emp == []:
            MensagemBox().warning('Mensagem', "Atenção não existe nenhum cadastro deste motorista ou esta inativo")
            self.ui.txtNomeMotorista.clear()
            self.ui.txtModeloMotorista.clear()
            self.ui.txtMarcaMotorista.clear()
            self.ui.txtPlacaMotorista.clear()
        else:
            for empres in emp:
                self.ui.txtNomeMotorista.setText(empres[1] + " " +empres[2])
                self.ui.txtModeloMotorista.setText(empres[21])
                self.ui.txtMarcaMotorista.setText(empres[22])
                self.ui.txtPlacaMotorista.setText(empres[23])


    def setMotoristaFinish(self):
        forne = DescarreEntradaDao()

        emp = forne.pesquisarMotorista(self.ui.txtidMotorista.text())

        if emp == []:
            self.ui.txtNomeMotorista.clear()
            self.ui.txtModeloMotorista.clear()
            self.ui.txtMarcaMotorista.clear()
            self.ui.txtPlacaMotorista.clear()

        else:
            for empres in emp:
                self.ui.txtNomeMotorista.setText(empres[1] + " " + empres[2])
                self.ui.txtModeloMotorista.setText(empres[21])
                self.ui.txtMarcaMotorista.setText(empres[22])
                self.ui.txtPlacaMotorista.setText(empres[23])

