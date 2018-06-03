import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from classes.classMensagemBox import MensagemBox
from classes.classValidator import Validator
from controller.getSetCliente import Cliente
from controller.getSetEntradaCarre import EntradaCarre
from controller.getSetMotorista import Motorista
from dao.carregamentoEntradaDao import CarregamentoEntradaDao
from dao.clienteDao import ClienteDao
from dao.motoristaDao import MotoristaDao
from telas.frmEntradaVeiculosCarregamentos import Ui_frmEntradaVeiculosCarregamento
from telas.frmPesquisarClientes import Ui_frmPesquisarCliente
from telas.frmPesquisarMotorista import Ui_frmConsultarMotoristas


class CarregamentoEntrada(QtGui.QDialog):
    def __init__(self, cadatra, cancela ):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmEntradaVeiculosCarregamento()
        self.ui.setupUi(self)
        self.validator = Validator()
        self.mensagem = MensagemBox()
        self.idCarregamento = int()
        self.produto = []
        self.carga = []
        self.cada = cadatra
        self.canc = cancela

        self.ui.btnNovo.setEnabled(self.cada)

        self.ui.btnNovo.clicked.connect(self.botoesNovoCadastro)
        self.ui.btnSalvar.clicked.connect(self.cadastro)
        self.ui.btnCancelar.clicked.connect(self.cancelarCadastro)

        self.ui.btnPesquisarClienteDestinatario.clicked.connect(self.pesquisarCliente)
        self.ui.btnPesquisarMotorista.clicked.connect(self.pesquisarMotorista)

        self.ui.txtidMotorista.returnPressed.connect(self.setMotorista)
        self.ui.txtIdClienteDestinatario.returnPressed.connect(self.setCliente)

        self.ui.txtidMotorista.editingFinished.connect(self.setMotoristaFinish)
        self.ui.txtIdClienteDestinatario.editingFinished.connect(self.setClienteFinish)


    def pesquisarTiposCarga(self):
        __carrEntrada = CarregamentoEntradaDao()
        __carga = __carrEntrada.pesquisarTipoCarga()
        for i in __carga:
            self.ui.txtTipoCarga.addItem(i[1])

        self.carga.append(__carga)

    def pesquisaProduto(self):
        __carrEntrada = CarregamentoEntradaDao()
        __produto = __carrEntrada.pesquisarProduto()
        self.ui.txtProduto.clear()
        for i in  __produto:
            self.ui.txtProduto.addItem(i[1])
        self.produto.append( __produto)


    def botoesNovoCadastro(self):

        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(self.cada)
        self.ui.btnCancelar.setEnabled(self.canc)

        self.ui.grbDadosMotorista.setEnabled(self.cada)
        self.ui.grbDadosClienteDestinatario.setEnabled(self.cada)
        self.ui.txtData.setFocus()
        self.ui.txtData.setEnabled(self.cada)
        self.ui.txtHora.setEnabled(self.cada)
        self.ui.txtTipoCarga.setEnabled(self.cada)
        self.ui.txtProduto.setEnabled(self.cada)
        self.ui.txtData.setDate(QDate.currentDate())
        self.ui.txtHora.setTime(QTime.currentTime())
        self.pesquisarTiposCarga()
        self.pesquisaProduto()

    def botoesCancelarCadastro(self):

        self.ui.btnNovo.setEnabled(self.cada)
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(False)

        self.ui.grbDadosMotorista.setEnabled(False)
        self.ui.grbDadosClienteDestinatario.setEnabled(False)
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
        self.ui.txtEndereco.clear()
        self.ui.txtNumero.clear()
        self.ui.txtComplemento.clear()
        self.ui.txtBairro.clear()
        self.ui.txtCidade.clear()
        self.ui.txtEstado.clear()
        self.ui.txtCep.clear()


    def cancelarCadastro(self):
        result = QMessageBox.question(QWidget(), 'Menssagem', "Tem certeza que deseja cancelar essa operação?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            self.botoesCancelarCadastro()
            self.limparCampos()

    def getIndexProduto(self):
        index = self.ui.txtProduto.currentIndex()

        for lista in self.produto:
            a = lista[index]
        idProduto = int(a[0])

        return idProduto

    def getIndexCarga(self):
        index = self.ui.txtTipoCarga.currentIndex()

        for lista in self.carga:
            a = lista[index]
        idCarga = int(a[0])

        return idCarga

    def cadastro(self):
        if self.ui.txtidMotorista.text() != '' and self.ui.txtNomeMotorista.text() != '' and self.ui.txtMarcaMotorista.text() != '' and self.ui.txtModeloMotorista.text() != '' and self.ui.txtIdClienteDestinatario.text() != '' and self.ui.txtNomeClienteDestinatario.text() != '' and self.ui.txtRazaoSocialClienteDestinatario.text() != '' and self.ui.txtInscricaoEstaduaClienteDestinatario.text()  != '' :
            __entCarre = CarregamentoEntradaDao()
            data = self.formatarData(self.removerCaracter(self.ui.txtData.text()))
            hora = self.ui.txtHora.text()
            produto = self.getIndexProduto()
            carga = self.getIndexCarga()
            idMotorista = self.ui.txtidMotorista.text()
            idVeiculo = __entCarre.pesquisarVeiculo(str(idMotorista), self.ui.txtMarcaMotorista.text(), self.ui.txtModeloMotorista.text(), self.removerCaracter(self.ui.txtPlacaMotorista.text()))
            idCliente = self.ui.txtIdClienteDestinatario.text()

            __dados = EntradaCarre(data, hora, carga, produto, idMotorista, idVeiculo, idCliente)
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

    def pesquisarCliente(self):
            self.dialog = QDialog(self)
            self.__pesquisarCliente = Ui_frmPesquisarCliente()
            self.__pesquisarCliente.setupUi(self.dialog)

            self.__pesquisarCliente.txtPesquisar.setValidator(self.validator)

            self.__pesquisarCliente.txtPesquisar.returnPressed.connect(self.pesquisarCli)

            self.__pesquisarCliente.btnPesquisar.clicked.connect(self.pesquisarCli)

            self.__pesquisarCliente.tabPesquisar.doubleClicked.connect(self.setarCamposCli)

            self.dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            self.dialog.exec_()

    def pesquisarCli(self):
        __pesDao = ClienteDao()
        if self.__pesquisarCliente.radBtnCodigo.isChecked():
                __codigo = self.__pesquisarCliente.txtPesquisar.text()
                __retorno = __pesDao.pesquisaCodigoFisica(__codigo)
                self.setarTabelaPesquisaEditarCliente(__retorno)

        elif self.__pesquisarCliente.radBtnRazaoSocial.isChecked():
                __razao = self.__pesquisarCliente.txtPesquisar.text()
                __retorno = __pesDao.pesquisarNomeFisica(__razao)
                self.setarTabelaPesquisaEditarCliente(__retorno)

        elif self.__pesquisarCliente.radBtnFantasia.isChecked():
                __fantasia = self.__pesquisarCliente.txtPesquisar.text()
                __retorno = __pesDao.pesquisaApelidoFisica(__fantasia)
                self.setarTabelaPesquisaEditarCliente(__retorno)

        elif self.__pesquisarCliente.radBtnCnpj.isChecked():
                __cnpj = self.__pesquisarCliente.txtPesquisar.text()
                __retorno = __pesDao.pesquisaCpfFisica(__cnpj)
                self.setarTabelaPesquisaEditarCliente(__retorno)

        elif self.__pesquisarCliente.radBtnInsEstadual.isChecked():
                __inscricao = self.__pesquisarCliente.txtPesquisar.text()
                __retorno = __pesDao.pesquisaRgFisica(__inscricao)
                self.setarTabelaPesquisaEditarCliente(__retorno)

        else:
            self.mensagem.warning( 'Atenção', "Selecione uma das opções de pesquisa")

    def setarTabelaPesquisaEditarCliente(self, __retorno):
        qtde_registros = len(__retorno)
        self.__pesquisarCliente.tabPesquisar.setRowCount(qtde_registros)

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
            self.__pesquisarCliente.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
            self.__pesquisarCliente.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(tipo)))
            self.__pesquisarCliente.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(nome)))
            self.__pesquisarCliente.tabPesquisar.setItem(linha, 3, QtGui.QTableWidgetItem(str(apelido)))
            self.__pesquisarCliente.tabPesquisar.setItem(linha, 4, QtGui.QTableWidgetItem(str(cpf)))
            self.__pesquisarCliente.tabPesquisar.setItem(linha, 5, QtGui.QTableWidgetItem(str(rg)))
            self.__pesquisarCliente.tabPesquisar.setItem(linha, 6, QtGui.QTableWidgetItem(str(expeditor)))
            self.__pesquisarCliente.tabPesquisar.setItem(linha, 7, QtGui.QTableWidgetItem(str(uf)))
            self.__pesquisarCliente.tabPesquisar.setItem(linha, 8, QtGui.QTableWidgetItem(str(aniversario)))
            self.__pesquisarCliente.tabPesquisar.setItem(linha, 9, QtGui.QTableWidgetItem(str(endereco)))
            self.__pesquisarCliente.tabPesquisar.setItem(linha, 10, QtGui.QTableWidgetItem(str(numero)))
            self.__pesquisarCliente.tabPesquisar.setItem(linha, 11, QtGui.QTableWidgetItem(str(complemento)))
            self.__pesquisarCliente.tabPesquisar.setItem(linha, 12, QtGui.QTableWidgetItem(str(bairro)))
            self.__pesquisarCliente.tabPesquisar.setItem(linha, 13, QtGui.QTableWidgetItem(str(cidade)))
            self.__pesquisarCliente.tabPesquisar.setItem(linha, 14, QtGui.QTableWidgetItem(str(estado)))
            self.__pesquisarCliente.tabPesquisar.setItem(linha, 15, QtGui.QTableWidgetItem(str(cep)))
            self.__pesquisarCliente.tabPesquisar.setItem(linha, 16, QtGui.QTableWidgetItem(str(site)))
            self.__pesquisarCliente.tabPesquisar.setItem(linha, 17, QtGui.QTableWidgetItem(str(obs)))
            self.__pesquisarCliente.tabPesquisar.setItem(linha, 18, QtGui.QTableWidgetItem(str(situacao)))

            linha += 1

    def setarCamposCli(self):
        clienteDao = ClienteDao()
        itens = []

        for item in self.__pesquisarCliente.tabPesquisar.selectedItems():
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

        __dados = Cliente(codigo, None, None, None, cnpj, insEstadual, fantasia, razao, obs, situacao, tipo)
        self.setCamposCliente(__dados, endereco, numero, complemento, bairro, cidade, estado, cep)
        self.dialog.close()

    def setCamposCliente(self, campos, ende, num, comp, bai, cid, est, cep):
        self.ui.txtIdClienteDestinatario.setText(campos.getIdCliente)
        self.ui.txtNomeClienteDestinatario.setText(campos.getFantasia)
        self.ui.txtRazaoSocialClienteDestinatario.setText(campos.getRazaoSocial)
        self.ui.txtInscricaoEstaduaClienteDestinatario.setText(campos.getInscricaoEstadual)
        self.ui.txtCnpjClienteDestinatario.setText(campos.getCnpj)
        self.ui.txtEndereco.setText(ende)
        self.ui.txtNumero.setText(num)
        self.ui.txtComplemento.setText(comp)
        self.ui.txtBairro.setText(bai)
        self.ui.txtCidade.setText(cid)
        self.ui.txtEstado.setText(est)
        self.ui.txtCep.setText(cep)

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

    def setMotorista(self):
        moto = CarregamentoEntradaDao()
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
        forne = CarregamentoEntradaDao()

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


    def setCliente(self):
        moto = CarregamentoEntradaDao()
        emp = moto.pesquisarCliente(self.ui.txtIdClienteDestinatario.text())

        if emp == []:
            MensagemBox().warning('Mensagem', "Atenção não existe nenhum cadastro deste motorista ou esta inativo")
            self.ui.txtNomeClienteDestinatario.clear()
            self.ui.txtRazaoSocialClienteDestinatario.clear()
            self.ui.txtInscricaoEstaduaClienteDestinatario.clear()
            self.ui.txtCnpjClienteDestinatario.clear()
            self.ui.txtEndereco.clear()
            self.ui.txtNumero.clear()
            self.ui.txtComplemento.clear()
            self.ui.txtBairro.clear()
            self.ui.txtCidade.clear()
            self.ui.txtEstado.clear()
            self.ui.txtCep.clear()
        else:
            for empres in emp:
                self.ui.txtNomeClienteDestinatario.setText(empres[3])
                self.ui.txtRazaoSocialClienteDestinatario.setText(empres[2])
                self.ui.txtInscricaoEstaduaClienteDestinatario.setText(empres[5])
                self.ui.txtCnpjClienteDestinatario.setText(empres[4])
                self.ui.txtEndereco.setText(empres[9])
                self.ui.txtNumero.setText(empres[10])
                self.ui.txtComplemento.setText(empres[11])
                self.ui.txtBairro.setText(empres[12])
                self.ui.txtCidade.setText(empres[13])
                self.ui.txtEstado.setText(empres[14])
                self.ui.txtCep.setText(empres[15])


    def setClienteFinish(self):
        forne = CarregamentoEntradaDao()

        emp = forne.pesquisarCliente(self.ui.txtIdClienteDestinatario.text())

        if emp == []:
            self.ui.txtNomeClienteDestinatario.clear()
            self.ui.txtRazaoSocialClienteDestinatario.clear()
            self.ui.txtInscricaoEstaduaClienteDestinatario.clear()
            self.ui.txtCnpjClienteDestinatario.clear()
            self.ui.txtCnpjClienteDestinatario.clear()
            self.ui.txtEndereco.clear()
            self.ui.txtNumero.clear()
            self.ui.txtComplemento.clear()
            self.ui.txtBairro.clear()
            self.ui.txtCidade.clear()
            self.ui.txtEstado.clear()
            self.ui.txtCep.clear()

        else:
            for empres in emp:
                self.ui.txtNomeClienteDestinatario.setText(empres[3])
                self.ui.txtRazaoSocialClienteDestinatario.setText(empres[2])
                self.ui.txtInscricaoEstaduaClienteDestinatario.setText(empres[5])
                self.ui.txtCnpjClienteDestinatario.setText(empres[4])
                self.ui.txtEndereco.setText(empres[9])
                self.ui.txtNumero.setText(empres[10])
                self.ui.txtComplemento.setText(empres[11])
                self.ui.txtBairro.setText(empres[12])
                self.ui.txtCidade.setText(empres[13])
                self.ui.txtEstado.setText(empres[14])
                self.ui.txtCep.setText(empres[15])