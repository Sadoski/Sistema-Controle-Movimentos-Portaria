from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from classes.CSV import RelatorioPessoaFisicaCSV
from classes.NotasFiscaisCSV import NotasFiscaisCSV
from classes.classValidator import Validator
from classes.clienteCSV import ClienteCSV
from classes.empresaCSV import EmpresaCSV
from classes.entSaiCarreCSV import EntSaiCarreCSV
from classes.entSaiDescaCSV import EntSaiDescaCSV
from classes.entSaiFuncCSV import EntSaiFuncCSV
from classes.fornecedorCSV import FornecedorCSV
from classes.funcionarioCSV import FuncionarioCSV
from classes.pessoaJuridicaCSV import RelatorioPessoaJuridicaCSV
from classes.usuarioCSV import UsuarioCSV
from dao.carregamentoSaidaDao import CarregamentoSaidaDao
from dao.clienteDao import ClienteDao
from dao.descarregamentoSaidaDao import DescarreSaidaDao
from dao.empresaDao import EmpresaDao
from dao.fornecedorDao import FornecedorDao
from dao.funcionarioDao import FuncionarioDao
from dao.notaFiscalRomaneioDao import NotaFiscalRomanieo
from dao.pesquisarPessoaFisicaDao import PesquisarPessoaFisicaDao
from dao.pesquisarPessoaJuridicaDao import PesquisarPessoaJuridicaDao
from dao.saidaFuncionarioDao import SaidaFuncionarioDao
from dao.usuarioPermissaoDao import UsuarioPermissaoDao
from telas.frmRelatorio import Ui_frmRelatorio


class Relatorio(QtGui.QDialog):
    def __init__(self, gerCvs, gerHtml):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmRelatorio()
        self.ui.setupUi(self)
        self.validator = Validator()
        self.gerCvs = gerCvs
        self.gerHtml = gerHtml

        self.ui.btnGerarCsv.setEnabled(self.gerCvs)
        self.ui.btnGerarHtml.setEnabled(self.gerHtml)

        self.ui.radBtnPessoaFisica.clicked.connect(self.ativarTab)
        self.ui.radBtnPessoaJuridica.clicked.connect(self.ativarTab)
        self.ui.radBtnEmpresa.clicked.connect(self.ativarTab)
        self.ui.radBtnFuncionario.clicked.connect(self.ativarTab)
        self.ui.radBtnCliente.clicked.connect(self.ativarTab)
        self.ui.radBtnFornecedor.clicked.connect(self.ativarTab)
        self.ui.radBtnUsuarios.clicked.connect(self.ativarTab)
        self.ui.radBtnNf.clicked.connect(self.ativarTab)
        self.ui.radBtnEntSaiCarregamento.clicked.connect(self.ativarTab)
        self.ui.radBtnEntSaiDescarregamento.clicked.connect(self.ativarTab)
        self.ui.radBtnEntSaiFuncionario.clicked.connect(self.ativarTab)

        self.ui.txtPesquisar.returnPressed.connect(self.pesquisar)
        self.ui.btnPesquisar.clicked.connect(self.pesquisar)

        self.ui.btnGerarCsv.clicked.connect(self.gerarCsv)
        self.ui.btnGerarHtml.clicked.connect(self.gerarHtml)

    def removerColuna(self):
        self.ui.tabPesquisar.horizontalHeader().hide()
        self.ui.tabPesquisar.verticalHeader().hide()


    def rowTab(self):
        if self.ui.radBtnPessoaFisica.isChecked():
            self.removerColuna()
            self.ui.tabPesquisar.setColumnCount(18)
            self.ui.tabPesquisar.setRowCount(0)
        elif self.ui.radBtnPessoaJuridica.isChecked():
            self.removerColuna()
            self.ui.tabPesquisar.setColumnCount(13)
            self.ui.tabPesquisar.setRowCount(0)
        elif self.ui.radBtnEmpresa.isChecked():
            self.removerColuna()
            self.ui.tabPesquisar.setColumnCount(16)
            self.ui.tabPesquisar.setRowCount(0)
        elif self.ui.radBtnFuncionario.isChecked():
            self.removerColuna()
            self.ui.tabPesquisar.setColumnCount(33)
            self.ui.tabPesquisar.setRowCount(0)
        elif self.ui.radBtnCliente.isChecked():
            self.removerColuna()
            self.ui.tabPesquisar.setColumnCount(19)
            self.ui.tabPesquisar.setRowCount(0)
        elif self.ui.radBtnFornecedor.isChecked():
            self.removerColuna()
            self.ui.tabPesquisar.setColumnCount(19)
            self.ui.tabPesquisar.setRowCount(0)
        elif self.ui.radBtnUsuarios.isChecked():
            self.removerColuna()
            self.ui.tabPesquisar.setColumnCount(5)
            self.ui.tabPesquisar.setRowCount(0)
        elif self.ui.radBtnNf.isChecked():
            self.removerColuna()
            self.ui.tabPesquisar.setColumnCount(14)
            self.ui.tabPesquisar.setRowCount(0)
        elif self.ui.radBtnEntSaiCarregamento.isChecked():
            self.removerColuna()
            self.ui.tabPesquisar.setColumnCount(12)
            self.ui.tabPesquisar.setRowCount(0)
        elif self.ui.radBtnEntSaiDescarregamento.isChecked():
            self.removerColuna()
            self.ui.tabPesquisar.setColumnCount(12)
            self.ui.tabPesquisar.setRowCount(0)
        elif self.ui.radBtnEntSaiFuncionario.isChecked():
            self.removerColuna()
            self.ui.tabPesquisar.setColumnCount(8)
            self.ui.tabPesquisar.setRowCount(0)


    def limparRad(self):
        self.ui.radBtn1.setText("")
        self.ui.radBtn2.setText("")
        self.ui.radBtn3.setText("")
        self.ui.radBtn4.setText("")
        self.ui.radBtn5.setText("")
        self.ui.radBtn6.setText("")

    def camposAtivar(self, btn1, btn2, btn3, btn4, btn5, btn6):
        self.ui.grbPesquisaRelatorio.setEnabled(True)
        self.ui.txtPesquisar.setEnabled(True)
        self.ui.btnPesquisar.setEnabled(True)
        self.ui.btnGerarCsv.setEnabled(True)
        self.ui.btnGerarHtml.setEnabled(True)
        self.ui.tabPesquisar.setEnabled(True)
        self.limparRad()
        self.ui.radBtn1.setText(btn1)
        self.ui.radBtn2.setText(btn2)
        self.ui.radBtn3.setText(btn3)
        self.ui.radBtn4.setText(btn4)
        if btn5 == False:
            self.ui.radBtn5.setEnabled(btn5)
        else:
            self.ui.radBtn5.setEnabled(True)
            self.ui.radBtn5.setText(btn5)
        if btn6 == False:
            self.ui.radBtn6.setEnabled(btn6)
        else:
            self.ui.radBtn6.setEnabled(True)
            self.ui.radBtn6.setText(btn6)
        self.rowTab()

    def ativarTab(self):
        if self.ui.radBtnPessoaFisica.isChecked():
            self.camposAtivar("Codigo", "Nome", "Sobrenome", "CPF", "RG", False)
        elif self.ui.radBtnPessoaJuridica.isChecked():
            self.camposAtivar("Codigo", "Razão Social", "Fantasia", "CNPJ", "Ins. Estadual", False)
        elif self.ui.radBtnEmpresa.isChecked():
            self.camposAtivar("Codigo", "Razão Social", "Fantasia", "CNPJ", "Ins. Estadual", "Ins. Municipal")
        elif self.ui.radBtnFuncionario.isChecked():
            self.camposAtivar("Codigo", "Nome", "CPJ", "RG", "Nº Carteira", "PIS/PASEP")
        elif self.ui.radBtnCliente.isChecked():
            self.camposAtivar("Codigo", "Nome/Razão Social", "Sobrenome/Fantasia", "CPF/CNPJ", "RG/Ins. Estadual", False)
        elif self.ui.radBtnFornecedor.isChecked():
            self.camposAtivar("Codigo", "Nome/Razão Social", "Sobrenome/Fantasia", "CPF/CNPJ", "RG/Ins. Estadual", False)
        elif self.ui.radBtnUsuarios.isChecked():
            self.camposAtivar("Codigo", "Nome", "Setor", "Cargo", "Login", False)
        elif self.ui.radBtnNf.isChecked():
            self.camposAtivar("Codigo", "Nº NF", "Fornecedor", "Motorista", "Produto", False)
        elif self.ui.radBtnEntSaiCarregamento.isChecked():
            self.camposAtivar("Codigo", "Motorista", "Placa Veiculo", "Carga", "Produto", 'Cliente')
        elif self.ui.radBtnEntSaiDescarregamento.isChecked():
            self.camposAtivar("Codigo", "Nº NF", "Produto", "Motorista", "Placa Veiculo", 'Fornecedor')
        elif self.ui.radBtnEntSaiFuncionario.isChecked():
            self.camposAtivar("Codigo", "Funcionario", "Setor", "Cargo", False, False)




    def pesquisar(self):
        if self.ui.radBtnPessoaFisica.isChecked():

            fisicaDao = PesquisarPessoaFisicaDao()

            if self.ui.radBtn1.isChecked():
                dados = fisicaDao.pesquisaCodigo(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn2.isChecked():
                dados = fisicaDao.pesquisaNome(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn3.isChecked():
                dados = fisicaDao.pesquisaApelido(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn4.isChecked():
                dados = fisicaDao.pesquisaCpf(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn5.isChecked():
                dados = fisicaDao.pesquisaRg(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn6.isChecked():
                pass

        elif self.ui.radBtnPessoaJuridica.isChecked():

            jurDao = PesquisarPessoaJuridicaDao()

            if self.ui.radBtn1.isChecked():
                dados = jurDao.pesquisaCodigo(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn2.isChecked():
                dados = jurDao.pesquisaRazaoSocial(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn3.isChecked():
                dados = jurDao.pesquisaFantasia(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn4.isChecked():
                dados = jurDao.pesquisaCnpj(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn5.isChecked():
                dados = jurDao.pesquisaInsEstadual(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn6.isChecked():
                pass

        elif self.ui.radBtnEmpresa.isChecked():

            empDao = EmpresaDao()

            if self.ui.radBtn1.isChecked():
                dados = empDao.pesquisaCodigo(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn2.isChecked():
                dados = empDao.pesquisaRazaoSocial(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn3.isChecked():
                dados = empDao.pesquisaFantasia(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn4.isChecked():
                dados = empDao.pesquisaCnpj(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn5.isChecked():
                dados = empDao.pesquisaInscEstadual(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn6.isChecked():
                dados = empDao.pesquisaInscMunicipal(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)

        elif self.ui.radBtnFuncionario.isChecked():

            funDao = FuncionarioDao()

            if self.ui.radBtn1.isChecked():
                dados = funDao.pesquisarFuncionarioCodigo(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn2.isChecked():
                dados = funDao.pesquisarFuncionarioNome(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn3.isChecked():
                dados = funDao.pesquisarFuncionarioCPF(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn4.isChecked():
                dados = funDao.pesquisarFuncionarioRg(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn5.isChecked():
                dados = funDao.pesquisarFuncionarioNumCarteira(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn6.isChecked():
                dados = funDao.pesquisarFuncionarioPis(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)

        elif self.ui.radBtnCliente.isChecked():

            cliDao = ClienteDao()

            if self.ui.radBtn1.isChecked():
                dados = cliDao.pesquisaCodigoFisica(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn2.isChecked():
                dados = cliDao.pesquisarNomeFisica(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn3.isChecked():
                dados = cliDao.pesquisaApelidoFisica(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn4.isChecked():
                dados = cliDao.pesquisaCpfFisica(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn5.isChecked():
                dados = cliDao.pesquisaRgFisica(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn6.isChecked():
                pass

        elif self.ui.radBtnFornecedor.isChecked():

            forDao = FornecedorDao()

            if self.ui.radBtn1.isChecked():
                dados = forDao.pesquisaCodigoFisica(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn2.isChecked():
                dados = forDao.pesquisarNomeFisica(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn3.isChecked():
                dados = forDao.pesquisaApelidoFisica(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn4.isChecked():
                dados = forDao.pesquisaCpfFisica(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn5.isChecked():
                dados = forDao.pesquisaRgFisica(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn6.isChecked():
                pass

        elif self.ui.radBtnUsuarios.isChecked():

            usuDao = UsuarioPermissaoDao()

            if self.ui.radBtn1.isChecked():
                dados = usuDao.pesquisaCodigoUsuario(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn2.isChecked():
                dados = usuDao.pesquisarNomeFuncionario(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn3.isChecked():
                dados = usuDao.pesquisaSetor(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn4.isChecked():
                dados = usuDao.pesquisaCargo(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn5.isChecked():
                dados = usuDao.pesquisaLogin(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn6.isChecked():
                pass

        elif self.ui.radBtnNf.isChecked():

            nfDao = NotaFiscalRomanieo()

            if self.ui.radBtn1.isChecked():
                dados = nfDao.pesquisarCodNfRel(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn2.isChecked():
                dados = nfDao.pesquisarNumNfRel(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn3.isChecked():
                dados = nfDao.pesquisarForNfRel(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn4.isChecked():
                dados = nfDao.pesquisarMotoNfRel(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn5.isChecked():
                dados = nfDao.pesquisarProNfRel(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn6.isChecked():
                pass

        elif self.ui.radBtnEntSaiCarregamento.isChecked():

            entSaiDao = CarregamentoSaidaDao()

            if self.ui.radBtn1.isChecked():
                dados = entSaiDao.pesquisarCodCarreRel(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn2.isChecked():
                dados = entSaiDao.pesquisarMotoCarreRel(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn3.isChecked():
                dados = entSaiDao.pesquisarPlacaCarreRel(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn4.isChecked():
                dados = entSaiDao.pesquisarCargaCarreRel(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn5.isChecked():
                dados = entSaiDao.pesquisarProdCarreRel(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn6.isChecked():
                dados = entSaiDao.pesquisarClieCarreRel(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)

        elif self.ui.radBtnEntSaiDescarregamento.isChecked():

            entSaiDao = DescarreSaidaDao()

            if self.ui.radBtn1.isChecked():
                dados = entSaiDao.pesquisarCodDescaRel(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn2.isChecked():
                dados = entSaiDao.pesquisarNumNfDescaRel(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn3.isChecked():
                dados = entSaiDao.pesquisarProdutoDescaRel(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn4.isChecked():
                dados = entSaiDao.pesquisarMotoDescaRel(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn5.isChecked():
                dados = entSaiDao.pesquisarPlacaDescaRel(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn6.isChecked():
                dados = entSaiDao.pesquisarFornDescaRel(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)

        elif self.ui.radBtnEntSaiFuncionario.isChecked():

            entSaiDao = SaidaFuncionarioDao()

            if self.ui.radBtn1.isChecked():
                dados = entSaiDao.pesquisarCodFuncRel(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn2.isChecked():
                dados = entSaiDao.pesquisarFuncioFuncRel(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn3.isChecked():
                dados = entSaiDao.pesquisarSetorFuncRel(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn4.isChecked():
                dados = entSaiDao.pesquisarCargoFuncRel(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn5.isChecked():
                pass
            elif self.ui.radBtn6.isChecked():
                pass

    def setarTabelaPesquisa(self, __retorno):
        if self.ui.radBtnPessoaFisica.isChecked():
            qtde_registros = len(__retorno)
            self.ui.tabPesquisar.setRowCount(qtde_registros)

            linha = 0
            for pesqui in __retorno:
                # capturando os dados da tupla

                codigo = pesqui[0]
                nome = pesqui[1]
                sobrenome = pesqui[2]
                cpf = pesqui[3]
                rg = pesqui[4]
                expeditor = pesqui[5]
                uf = pesqui[6]
                data = pesqui[7]
                sexo = pesqui[8]
                mae = pesqui[9]
                pai = pesqui[10]
                endereco = pesqui[11]
                numero = pesqui[12]
                complemento = pesqui[13]
                bairro = pesqui[14]
                cidade = pesqui[15]
                estado = pesqui[16]
                cep = pesqui[17]


                # preenchendo o grid de pesquisa
                self.ui.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.ui.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(nome)))
                self.ui.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(sobrenome)))
                self.ui.tabPesquisar.setItem(linha, 3, QtGui.QTableWidgetItem(str(cpf)))
                self.ui.tabPesquisar.setItem(linha, 4, QtGui.QTableWidgetItem(str(rg)))
                self.ui.tabPesquisar.setItem(linha, 5, QtGui.QTableWidgetItem(str(expeditor)))
                self.ui.tabPesquisar.setItem(linha, 6, QtGui.QTableWidgetItem(str(uf)))
                self.ui.tabPesquisar.setItem(linha, 7, QtGui.QTableWidgetItem(str(data)))
                self.ui.tabPesquisar.setItem(linha, 8, QtGui.QTableWidgetItem(str(sexo)))
                self.ui.tabPesquisar.setItem(linha, 9, QtGui.QTableWidgetItem(str(mae)))
                self.ui.tabPesquisar.setItem(linha, 10, QtGui.QTableWidgetItem(str(pai)))
                self.ui.tabPesquisar.setItem(linha, 11, QtGui.QTableWidgetItem(str(endereco)))
                self.ui.tabPesquisar.setItem(linha, 12, QtGui.QTableWidgetItem(str(numero)))
                self.ui.tabPesquisar.setItem(linha, 13, QtGui.QTableWidgetItem(str(complemento)))
                self.ui.tabPesquisar.setItem(linha, 14, QtGui.QTableWidgetItem(str(bairro)))
                self.ui.tabPesquisar.setItem(linha, 15, QtGui.QTableWidgetItem(str(cidade)))
                self.ui.tabPesquisar.setItem(linha, 16, QtGui.QTableWidgetItem(str(estado)))
                self.ui.tabPesquisar.setItem(linha, 17, QtGui.QTableWidgetItem(str(cep)))

                linha += 1

        elif self.ui.radBtnPessoaJuridica.isChecked():
            qtde_registros = len(__retorno)
            self.ui.tabPesquisar.setRowCount(qtde_registros)

            linha = 0
            for pesqui in __retorno:
                # capturando os dados da tupla

                codigo = pesqui[0]
                razao = pesqui[1]
                fantasia = pesqui[2]
                cnpj = pesqui[3]
                inscricao = pesqui[4]
                endereco = pesqui[5]
                numero = pesqui[6]
                complemento = pesqui[7]
                bairro = pesqui[8]
                cidade = pesqui[9]
                estado = pesqui[10]
                cep = pesqui[11]
                site = pesqui[12]

                # preenchendo o grid de pesquisa
                self.ui.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.ui.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(razao)))
                self.ui.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(fantasia)))
                self.ui.tabPesquisar.setItem(linha, 3, QtGui.QTableWidgetItem(str(cnpj)))
                self.ui.tabPesquisar.setItem(linha, 4, QtGui.QTableWidgetItem(str(inscricao)))
                self.ui.tabPesquisar.setItem(linha, 5, QtGui.QTableWidgetItem(str(endereco)))
                self.ui.tabPesquisar.setItem(linha, 6, QtGui.QTableWidgetItem(str(numero)))
                self.ui.tabPesquisar.setItem(linha, 7, QtGui.QTableWidgetItem(str(complemento)))
                self.ui.tabPesquisar.setItem(linha, 8, QtGui.QTableWidgetItem(str(bairro)))
                self.ui.tabPesquisar.setItem(linha, 9, QtGui.QTableWidgetItem(str(cidade)))
                self.ui.tabPesquisar.setItem(linha, 10, QtGui.QTableWidgetItem(str(estado)))
                self.ui.tabPesquisar.setItem(linha, 11, QtGui.QTableWidgetItem(str(cep)))
                self.ui.tabPesquisar.setItem(linha, 12, QtGui.QTableWidgetItem(str(site)))

                linha += 1

        elif self.ui.radBtnEmpresa.isChecked():
            qtde_registros = len(__retorno)
            self.ui.tabPesquisar.setRowCount(qtde_registros)

            linha = 0
            for pesqui in __retorno:
                # capturando os dados da tupla

                codigo = pesqui[0]
                razao = pesqui[1]
                fantasia = pesqui[2]
                cnpj = pesqui[3]
                insEstadual = pesqui[4]
                insMunicipal = pesqui[5]
                tipoEmpresa = pesqui[6]
                endereco = pesqui[7]
                numero = pesqui[8]
                complemento = pesqui[9]
                bairro = pesqui[10]
                cidade = pesqui[11]
                estado = pesqui[12]
                cep = pesqui[13]
                if pesqui[14] == 1:
                    situacao = 'ATIVA'
                else:
                    situacao = 'Desativa'
                subclasse = pesqui[15]

                # preenchendo o grid de pesquisa
                self.ui.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.ui.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(razao)))
                self.ui.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(fantasia)))
                self.ui.tabPesquisar.setItem(linha, 3, QtGui.QTableWidgetItem(str(cnpj)))
                self.ui.tabPesquisar.setItem(linha, 4, QtGui.QTableWidgetItem(str(insEstadual)))
                self.ui.tabPesquisar.setItem(linha, 5, QtGui.QTableWidgetItem(str(insMunicipal)))
                self.ui.tabPesquisar.setItem(linha, 6, QtGui.QTableWidgetItem(str(tipoEmpresa)))
                self.ui.tabPesquisar.setItem(linha, 7, QtGui.QTableWidgetItem(str(endereco)))
                self.ui.tabPesquisar.setItem(linha, 8, QtGui.QTableWidgetItem(str(numero)))
                self.ui.tabPesquisar.setItem(linha, 9, QtGui.QTableWidgetItem(str(complemento)))
                self.ui.tabPesquisar.setItem(linha, 10, QtGui.QTableWidgetItem(str(bairro)))
                self.ui.tabPesquisar.setItem(linha, 11, QtGui.QTableWidgetItem(str(cidade)))
                self.ui.tabPesquisar.setItem(linha, 12, QtGui.QTableWidgetItem(str(estado)))
                self.ui.tabPesquisar.setItem(linha, 13, QtGui.QTableWidgetItem(str(cep)))
                self.ui.tabPesquisar.setItem(linha, 14, QtGui.QTableWidgetItem(str(situacao)))
                self.ui.tabPesquisar.setItem(linha, 15, QtGui.QTableWidgetItem(subclasse))

                linha += 1

        elif self.ui.radBtnFuncionario.isChecked():
            qtde_registros = len(__retorno)
            self.ui.tabPesquisar.setRowCount(qtde_registros)

            linha = 0
            for pesqui in __retorno:
                # capturando os dados da tupla

                codigo = pesqui[0]
                nome = pesqui[1]
                segundoNome = pesqui[2]
                cpf = pesqui[3]
                rg = pesqui[4]
                expeditor = pesqui[5]
                uf = pesqui[6]
                data = pesqui[7]
                sexo = pesqui[8]
                endereco = pesqui[9]
                numero = pesqui[10]
                complemento = pesqui[11]
                bairro = pesqui[12]
                mae = pesqui[13]
                pai = pesqui[14]
                cidade = pesqui[15]
                estado = pesqui[16]
                cep = pesqui[17]
                admissao = pesqui[18]
                demissao = pesqui[19]
                carteira = pesqui[20]
                serie = pesqui[21]
                uff = pesqui[22]
                emissao = pesqui[23]
                pis = pesqui[24]
                civil = pesqui[25]
                deficiencia = pesqui[26]
                categoria = pesqui[27]
                setor = pesqui[28]
                cargo = pesqui[29]
                obs = pesqui[30]
                jornada = pesqui[31]
                if pesqui[32] == 1:
                    situacao = "Ativo"
                else:
                    situacao = "Desativo"

                # preenchendo o grid de pesquisa
                self.ui.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.ui.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(nome)))
                self.ui.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(segundoNome)))
                self.ui.tabPesquisar.setItem(linha, 3, QtGui.QTableWidgetItem(str(cpf)))
                self.ui.tabPesquisar.setItem(linha, 4, QtGui.QTableWidgetItem(str(rg)))
                self.ui.tabPesquisar.setItem(linha, 5, QtGui.QTableWidgetItem(str(expeditor)))
                self.ui.tabPesquisar.setItem(linha, 6, QtGui.QTableWidgetItem(str(uf)))
                self.ui.tabPesquisar.setItem(linha, 7, QtGui.QTableWidgetItem(str(data)))
                self.ui.tabPesquisar.setItem(linha, 8, QtGui.QTableWidgetItem(str(endereco)))
                self.ui.tabPesquisar.setItem(linha, 9, QtGui.QTableWidgetItem(str(numero)))
                self.ui.tabPesquisar.setItem(linha, 10, QtGui.QTableWidgetItem(str(complemento)))
                self.ui.tabPesquisar.setItem(linha, 11, QtGui.QTableWidgetItem(str(bairro)))
                self.ui.tabPesquisar.setItem(linha, 12, QtGui.QTableWidgetItem(str(cidade)))
                self.ui.tabPesquisar.setItem(linha, 13, QtGui.QTableWidgetItem(str(estado)))
                self.ui.tabPesquisar.setItem(linha, 14, QtGui.QTableWidgetItem(str(cep)))
                self.ui.tabPesquisar.setItem(linha, 15, QtGui.QTableWidgetItem(str(sexo)))
                self.ui.tabPesquisar.setItem(linha, 16, QtGui.QTableWidgetItem(str(mae)))
                self.ui.tabPesquisar.setItem(linha, 17, QtGui.QTableWidgetItem(str(pai)))
                self.ui.tabPesquisar.setItem(linha, 18, QtGui.QTableWidgetItem(str(admissao)))
                self.ui.tabPesquisar.setItem(linha, 19, QtGui.QTableWidgetItem(str(demissao)))
                self.ui.tabPesquisar.setItem(linha, 20, QtGui.QTableWidgetItem(str(carteira)))
                self.ui.tabPesquisar.setItem(linha, 21, QtGui.QTableWidgetItem(str(serie)))
                self.ui.tabPesquisar.setItem(linha, 22, QtGui.QTableWidgetItem(str(uff)))
                self.ui.tabPesquisar.setItem(linha, 23, QtGui.QTableWidgetItem(str(emissao)))
                self.ui.tabPesquisar.setItem(linha, 24, QtGui.QTableWidgetItem(str(pis)))
                self.ui.tabPesquisar.setItem(linha, 25, QtGui.QTableWidgetItem(str(civil)))
                self.ui.tabPesquisar.setItem(linha, 26, QtGui.QTableWidgetItem(str(deficiencia)))
                self.ui.tabPesquisar.setItem(linha, 27, QtGui.QTableWidgetItem(str(categoria)))
                self.ui.tabPesquisar.setItem(linha, 28, QtGui.QTableWidgetItem(str(cargo)))
                self.ui.tabPesquisar.setItem(linha, 29, QtGui.QTableWidgetItem(str(setor)))
                self.ui.tabPesquisar.setItem(linha, 30, QtGui.QTableWidgetItem(str(obs)))
                self.ui.tabPesquisar.setItem(linha, 31, QtGui.QTableWidgetItem(str(jornada)))
                self.ui.tabPesquisar.setItem(linha, 32, QtGui.QTableWidgetItem(str(situacao)))

                linha += 1
        elif self.ui.radBtnCliente.isChecked():
            qtde_registros = len(__retorno)
            self.ui.tabPesquisar.setRowCount(qtde_registros)

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
                self.ui.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.ui.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(tipo)))
                self.ui.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(nome)))
                self.ui.tabPesquisar.setItem(linha, 3, QtGui.QTableWidgetItem(str(apelido)))
                self.ui.tabPesquisar.setItem(linha, 4, QtGui.QTableWidgetItem(str(cpf)))
                self.ui.tabPesquisar.setItem(linha, 5, QtGui.QTableWidgetItem(str(rg)))
                self.ui.tabPesquisar.setItem(linha, 6, QtGui.QTableWidgetItem(str(expeditor)))
                self.ui.tabPesquisar.setItem(linha, 7, QtGui.QTableWidgetItem(str(uf)))
                self.ui.tabPesquisar.setItem(linha, 8, QtGui.QTableWidgetItem(str(aniversario)))
                self.ui.tabPesquisar.setItem(linha, 9, QtGui.QTableWidgetItem(str(endereco)))
                self.ui.tabPesquisar.setItem(linha, 10, QtGui.QTableWidgetItem(str(numero)))
                self.ui.tabPesquisar.setItem(linha, 11, QtGui.QTableWidgetItem(str(complemento)))
                self.ui.tabPesquisar.setItem(linha, 12, QtGui.QTableWidgetItem(str(bairro)))
                self.ui.tabPesquisar.setItem(linha, 13, QtGui.QTableWidgetItem(str(cidade)))
                self.ui.tabPesquisar.setItem(linha, 14, QtGui.QTableWidgetItem(str(estado)))
                self.ui.tabPesquisar.setItem(linha, 15, QtGui.QTableWidgetItem(str(cep)))
                self.ui.tabPesquisar.setItem(linha, 16, QtGui.QTableWidgetItem(str(site)))
                self.ui.tabPesquisar.setItem(linha, 17, QtGui.QTableWidgetItem(str(obs)))
                self.ui.tabPesquisar.setItem(linha, 18, QtGui.QTableWidgetItem(str(situacao)))

                linha += 1

        elif self.ui.radBtnFornecedor.isChecked():
            qtde_registros = len(__retorno)
            self.ui.tabPesquisar.setRowCount(qtde_registros)

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
                self.ui.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.ui.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(tipo)))
                self.ui.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(nome)))
                self.ui.tabPesquisar.setItem(linha, 3, QtGui.QTableWidgetItem(str(apelido)))
                self.ui.tabPesquisar.setItem(linha, 4, QtGui.QTableWidgetItem(str(cpf)))
                self.ui.tabPesquisar.setItem(linha, 5, QtGui.QTableWidgetItem(str(rg)))
                self.ui.tabPesquisar.setItem(linha, 6, QtGui.QTableWidgetItem(str(expeditor)))
                self.ui.tabPesquisar.setItem(linha, 7, QtGui.QTableWidgetItem(str(uf)))
                self.ui.tabPesquisar.setItem(linha, 8, QtGui.QTableWidgetItem(str(aniversario)))
                self.ui.tabPesquisar.setItem(linha, 9, QtGui.QTableWidgetItem(str(endereco)))
                self.ui.tabPesquisar.setItem(linha, 10, QtGui.QTableWidgetItem(str(numero)))
                self.ui.tabPesquisar.setItem(linha, 11, QtGui.QTableWidgetItem(str(complemento)))
                self.ui.tabPesquisar.setItem(linha, 12, QtGui.QTableWidgetItem(str(bairro)))
                self.ui.tabPesquisar.setItem(linha, 13, QtGui.QTableWidgetItem(str(cidade)))
                self.ui.tabPesquisar.setItem(linha, 14, QtGui.QTableWidgetItem(str(estado)))
                self.ui.tabPesquisar.setItem(linha, 15, QtGui.QTableWidgetItem(str(cep)))
                self.ui.tabPesquisar.setItem(linha, 16, QtGui.QTableWidgetItem(str(site)))
                self.ui.tabPesquisar.setItem(linha, 17, QtGui.QTableWidgetItem(str(obs)))
                self.ui.tabPesquisar.setItem(linha, 18, QtGui.QTableWidgetItem(str(situacao)))

                linha += 1

        elif self.ui.radBtnUsuarios.isChecked():
            qtde_registros = len(__retorno)
            self.ui.tabPesquisar.setRowCount(qtde_registros)

            linha = 0
            for pesqui in __retorno:
                # capturando os dados da tupla

                codigo = pesqui[0]
                nome = pesqui[1]
                sobrenome = pesqui[2]
                setor = pesqui[3]
                cargo = pesqui[4]
                login = pesqui[5]

                # preenchendo o grid de pesquisa
                self.ui.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.ui.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(nome + ' ' + sobrenome)))
                self.ui.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(setor)))
                self.ui.tabPesquisar.setItem(linha, 3, QtGui.QTableWidgetItem(str(cargo)))
                self.ui.tabPesquisar.setItem(linha, 4, QtGui.QTableWidgetItem(str(login)))

                linha += 1

        elif self.ui.radBtnNf.isChecked():
            qtde_registros = len(__retorno)
            self.ui.tabPesquisar.setRowCount(qtde_registros)

            nf = NotaFiscalRomanieo()
            linha = 0
            for pesqui in __retorno:
                # capturando os dados da tupla

                codigo = pesqui[0]
                tipo = pesqui[1]
                serie = pesqui[2]
                numNf = pesqui[3]
                fornecedor = nf.pesquisarForneRel(pesqui[4])
                motorista = nf.pesquisarMotoRel(pesqui[5])
                dataEmissao = pesqui[6]
                dataEntrada = pesqui[7]
                valorTotal = pesqui[8]
                valorIcms = pesqui[9]
                valorIpi = pesqui[10]
                alicotaIcms = pesqui[11]
                alicotaIpi = pesqui[12]
                produtos = nf.pesquisarProdRel(str(codigo))

                # preenchendo o grid de pesquisa
                self.ui.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.ui.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(tipo)))
                self.ui.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(serie)))
                self.ui.tabPesquisar.setItem(linha, 3, QtGui.QTableWidgetItem(str(numNf)))
                self.ui.tabPesquisar.setItem(linha, 4, QtGui.QTableWidgetItem(str(fornecedor)))
                self.ui.tabPesquisar.setItem(linha, 5, QtGui.QTableWidgetItem(str(motorista)))
                self.ui.tabPesquisar.setItem(linha, 6, QtGui.QTableWidgetItem(str(dataEmissao)))
                self.ui.tabPesquisar.setItem(linha, 7, QtGui.QTableWidgetItem(str(dataEntrada)))
                self.ui.tabPesquisar.setItem(linha, 8, QtGui.QTableWidgetItem(str(valorTotal)))
                self.ui.tabPesquisar.setItem(linha, 9, QtGui.QTableWidgetItem(str(valorIcms)))
                self.ui.tabPesquisar.setItem(linha, 10, QtGui.QTableWidgetItem(str(valorIpi)))
                self.ui.tabPesquisar.setItem(linha, 11, QtGui.QTableWidgetItem(str(alicotaIcms)))
                self.ui.tabPesquisar.setItem(linha, 12, QtGui.QTableWidgetItem(str(alicotaIpi)))
                self.ui.tabPesquisar.setItem(linha, 13, QtGui.QTableWidgetItem(str(produtos)))

                linha += 1

        elif self.ui.radBtnEntSaiCarregamento.isChecked():
            qtde_registros = len(__retorno)
            self.ui.tabPesquisar.setRowCount(qtde_registros)

            entSaiDao = CarregamentoSaidaDao()
            linha = 0
            for pesqui in __retorno:
                # capturando os dados da tupla

                codigo = pesqui[0]
                dataEnt = pesqui[1]
                horaEnt = pesqui[2]
                dataSai = pesqui[3]
                horaSai = pesqui[4]
                carga = pesqui[5]
                produto = pesqui[6]
                motorista = entSaiDao.pesquisarMotoristaCarreRel(pesqui[7])
                marca = pesqui[8]
                modelo = pesqui[9]
                placa = pesqui[10]
                cliente = entSaiDao.pesquisarClienteCarreRel(pesqui[11])


                # preenchendo o grid de pesquisa
                self.ui.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.ui.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(dataEnt)))
                self.ui.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(horaEnt)))
                self.ui.tabPesquisar.setItem(linha, 3, QtGui.QTableWidgetItem(str(dataSai)))
                self.ui.tabPesquisar.setItem(linha, 4, QtGui.QTableWidgetItem(str(horaSai)))
                self.ui.tabPesquisar.setItem(linha, 5, QtGui.QTableWidgetItem(str(carga)))
                self.ui.tabPesquisar.setItem(linha, 6, QtGui.QTableWidgetItem(str(produto)))
                self.ui.tabPesquisar.setItem(linha, 7, QtGui.QTableWidgetItem(str(motorista)))
                self.ui.tabPesquisar.setItem(linha, 8, QtGui.QTableWidgetItem(str(marca)))
                self.ui.tabPesquisar.setItem(linha, 9, QtGui.QTableWidgetItem(str(modelo)))
                self.ui.tabPesquisar.setItem(linha, 10, QtGui.QTableWidgetItem(str(placa)))
                self.ui.tabPesquisar.setItem(linha, 11, QtGui.QTableWidgetItem(str(cliente)))

                linha += 1

        elif self.ui.radBtnEntSaiDescarregamento.isChecked():
            qtde_registros = len(__retorno)
            self.ui.tabPesquisar.setRowCount(qtde_registros)

            entDao = DescarreSaidaDao()

            linha = 0
            for pesqui in __retorno:
                # capturando os dados da tupla

                codigo = pesqui[0]
                data = pesqui[1]
                hora = pesqui[2]
                dataSai = pesqui[3]
                horaSai = pesqui[4]
                numNf = pesqui[5]
                produto = pesqui[6]
                motorista = entDao.pesquisarMotoristaDescaRel(pesqui[7])
                marca = pesqui[8]
                modelo = pesqui[9]
                placa = pesqui[10]
                fornecedor = entDao.pesquisarFornecedorDescaRel(pesqui[11])

                # preenchendo o grid de pesquisa
                self.ui.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.ui.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(data)))
                self.ui.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(hora)))
                self.ui.tabPesquisar.setItem(linha, 3, QtGui.QTableWidgetItem(str(dataSai)))
                self.ui.tabPesquisar.setItem(linha, 4, QtGui.QTableWidgetItem(str(horaSai)))
                self.ui.tabPesquisar.setItem(linha, 5, QtGui.QTableWidgetItem(str(numNf)))
                self.ui.tabPesquisar.setItem(linha, 6, QtGui.QTableWidgetItem(str(produto)))
                self.ui.tabPesquisar.setItem(linha, 7, QtGui.QTableWidgetItem(str(motorista)))
                self.ui.tabPesquisar.setItem(linha, 8, QtGui.QTableWidgetItem(str(marca)))
                self.ui.tabPesquisar.setItem(linha, 9, QtGui.QTableWidgetItem(str(modelo)))
                self.ui.tabPesquisar.setItem(linha, 10, QtGui.QTableWidgetItem(str(placa)))
                self.ui.tabPesquisar.setItem(linha, 11, QtGui.QTableWidgetItem(str(fornecedor)))


                linha += 1

        elif self.ui.radBtnEntSaiFuncionario.isChecked():
            qtde_registros = len(__retorno)
            self.ui.tabPesquisar.setRowCount(qtde_registros)

            entDao = DescarreSaidaDao()

            linha = 0
            for pesqui in __retorno:
                # capturando os dados da tupla

                codigo = pesqui[0]
                data = pesqui[1]
                hora = pesqui[2]
                dataSai = pesqui[3]
                horaSai = pesqui[4]
                funcionario = pesqui[5]
                setor = pesqui[6]
                cargo = pesqui[7]

                # preenchendo o grid de pesquisa
                self.ui.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.ui.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(data)))
                self.ui.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(hora)))
                self.ui.tabPesquisar.setItem(linha, 3, QtGui.QTableWidgetItem(str(dataSai)))
                self.ui.tabPesquisar.setItem(linha, 4, QtGui.QTableWidgetItem(str(horaSai)))
                self.ui.tabPesquisar.setItem(linha, 5, QtGui.QTableWidgetItem(str(funcionario)))
                self.ui.tabPesquisar.setItem(linha, 6, QtGui.QTableWidgetItem(str(setor)))
                self.ui.tabPesquisar.setItem(linha, 7, QtGui.QTableWidgetItem(str(cargo)))


                linha += 1


    def gerarCsv(self):
        if self.ui.radBtnPessoaFisica.isChecked():

            fisicaDao = PesquisarPessoaFisicaDao()

            if self.ui.radBtn1.isChecked():
                dados = fisicaDao.pesquisaCodigo(self.ui.txtPesquisar.text())
                if dados != []:
                    RelatorioPessoaFisicaCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn2.isChecked():
                dados = fisicaDao.pesquisaNome(self.ui.txtPesquisar.text())
                if dados != []:
                    RelatorioPessoaFisicaCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn3.isChecked():
                dados = fisicaDao.pesquisaApelido(self.ui.txtPesquisar.text())
                if dados != []:
                    RelatorioPessoaFisicaCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn4.isChecked():
                dados = fisicaDao.pesquisaCpf(self.ui.txtPesquisar.text())
                if dados != []:
                    RelatorioPessoaFisicaCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn5.isChecked():
                dados = fisicaDao.pesquisaRg(self.ui.txtPesquisar.text())
                if dados != []:
                    RelatorioPessoaFisicaCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn6.isChecked():
                pass

        elif self.ui.radBtnPessoaJuridica.isChecked():

            jurDao = PesquisarPessoaJuridicaDao()

            if self.ui.radBtn1.isChecked():
                dados = jurDao.pesquisaCodigo(self.ui.txtPesquisar.text())
                if dados != []:
                    RelatorioPessoaJuridicaCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn2.isChecked():
                dados = jurDao.pesquisaRazaoSocial(self.ui.txtPesquisar.text())
                if dados != []:
                    RelatorioPessoaJuridicaCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn3.isChecked():
                dados = jurDao.pesquisaFantasia(self.ui.txtPesquisar.text())
                if dados != []:
                    RelatorioPessoaJuridicaCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn4.isChecked():
                dados = jurDao.pesquisaCnpj(self.ui.txtPesquisar.text())
                if dados != []:
                    RelatorioPessoaJuridicaCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn5.isChecked():
                dados = jurDao.pesquisaInsEstadual(self.ui.txtPesquisar.text())
                if dados != []:
                    RelatorioPessoaJuridicaCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn6.isChecked():
                pass

        elif self.ui.radBtnEmpresa.isChecked():

            empDao = EmpresaDao()

            if self.ui.radBtn1.isChecked():
                dados = empDao.pesquisaCodigo(self.ui.txtPesquisar.text())
                if dados != []:
                    EmpresaCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn2.isChecked():
                dados = empDao.pesquisaRazaoSocial(self.ui.txtPesquisar.text())
                if dados != []:
                    EmpresaCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn3.isChecked():
                dados = empDao.pesquisaFantasia(self.ui.txtPesquisar.text())
                if dados != []:
                    EmpresaCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn4.isChecked():
                dados = empDao.pesquisaCnpj(self.ui.txtPesquisar.text())
                if dados != []:
                    EmpresaCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn5.isChecked():
                dados = empDao.pesquisaInscEstadual(self.ui.txtPesquisar.text())
                if dados != []:
                    EmpresaCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn6.isChecked():
                dados = empDao.pesquisaInscMunicipal(self.ui.txtPesquisar.text())
                if dados != []:
                    EmpresaCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")

        elif self.ui.radBtnFuncionario.isChecked():

            funDao = FuncionarioDao()

            if self.ui.radBtn1.isChecked():
                dados = funDao.pesquisarFuncionarioCodigo(self.ui.txtPesquisar.text())
                if dados != []:
                    FuncionarioCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn2.isChecked():
                dados = funDao.pesquisarFuncionarioNome(self.ui.txtPesquisar.text())
                if dados != []:
                    FuncionarioCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn3.isChecked():
                dados = funDao.pesquisarFuncionarioCPF(self.ui.txtPesquisar.text())
                if dados != []:
                    FuncionarioCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn4.isChecked():
                dados = funDao.pesquisarFuncionarioRg(self.ui.txtPesquisar.text())
                if dados != []:
                    FuncionarioCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn5.isChecked():
                dados = funDao.pesquisarFuncionarioNumCarteira(self.ui.txtPesquisar.text())
                if dados != []:
                    FuncionarioCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn6.isChecked():
                dados = funDao.pesquisarFuncionarioPis(self.ui.txtPesquisar.text())
                if dados != []:
                    FuncionarioCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")

        elif self.ui.radBtnCliente.isChecked():

            cliDao = ClienteDao()

            if self.ui.radBtn1.isChecked():
                dados = cliDao.pesquisaCodigoFisica(self.ui.txtPesquisar.text())
                if dados != []:
                    ClienteCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn2.isChecked():
                dados = cliDao.pesquisarNomeFisica(self.ui.txtPesquisar.text())
                if dados != []:
                    ClienteCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn3.isChecked():
                dados = cliDao.pesquisaApelidoFisica(self.ui.txtPesquisar.text())
                if dados != []:
                    ClienteCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn4.isChecked():
                dados = cliDao.pesquisaCpfFisica(self.ui.txtPesquisar.text())
                if dados != []:
                    ClienteCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn5.isChecked():
                dados = cliDao.pesquisaRgFisica(self.ui.txtPesquisar.text())
                if dados != []:
                    ClienteCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn6.isChecked():
                pass

        elif self.ui.radBtnFornecedor.isChecked():

            forDao = FornecedorDao()

            if self.ui.radBtn1.isChecked():
                dados = forDao.pesquisaCodigoFisica(self.ui.txtPesquisar.text())
                if dados != []:
                    FornecedorCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn2.isChecked():
                dados = forDao.pesquisarNomeFisica(self.ui.txtPesquisar.text())
                if dados != []:
                    FornecedorCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn3.isChecked():
                dados = forDao.pesquisaApelidoFisica(self.ui.txtPesquisar.text())
                if dados != []:
                    FornecedorCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn4.isChecked():
                dados = forDao.pesquisaCpfFisica(self.ui.txtPesquisar.text())
                if dados != []:
                    FornecedorCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn5.isChecked():
                dados = forDao.pesquisaRgFisica(self.ui.txtPesquisar.text())
                if dados != []:
                    FornecedorCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn6.isChecked():
                pass

        elif self.ui.radBtnUsuarios.isChecked():

            usuDao = UsuarioPermissaoDao()

            if self.ui.radBtn1.isChecked():
                dados = usuDao.pesquisaCodigoUsuario(self.ui.txtPesquisar.text())
                if dados != []:
                    UsuarioCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn2.isChecked():
                dados = usuDao.pesquisarNomeFuncionario(self.ui.txtPesquisar.text())
                if dados != []:
                    UsuarioCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn3.isChecked():
                dados = usuDao.pesquisaSetor(self.ui.txtPesquisar.text())
                if dados != []:
                    UsuarioCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn4.isChecked():
                dados = usuDao.pesquisaCargo(self.ui.txtPesquisar.text())
                if dados != []:
                    UsuarioCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn5.isChecked():
                dados = usuDao.pesquisaLogin(self.ui.txtPesquisar.text())
                if dados != []:
                    UsuarioCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn6.isChecked():
                pass

        elif self.ui.radBtnNf.isChecked():

            nf = NotaFiscalRomanieo()

            if self.ui.radBtn1.isChecked():
                dados = nf.pesquisarCodNfRel(self.ui.txtPesquisar.text())
                if dados != []:
                    NotasFiscaisCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn2.isChecked():
                dados = nf.pesquisarNumNfRel(self.ui.txtPesquisar.text())
                if dados != []:
                    NotasFiscaisCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn3.isChecked():
                dados = nf.pesquisarForNfRel(self.ui.txtPesquisar.text())
                if dados != []:
                    NotasFiscaisCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn4.isChecked():
                dados = nf.pesquisarMotoNfRel(self.ui.txtPesquisar.text())
                if dados != []:
                    NotasFiscaisCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn5.isChecked():
                dados = nf.pesquisarProNfRel(self.ui.txtPesquisar.text())
                if dados != []:
                    NotasFiscaisCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn6.isChecked():
                pass

        elif self.ui.radBtnEntSaiCarregamento.isChecked():

            entSaiDao = CarregamentoSaidaDao()

            if self.ui.radBtn1.isChecked():
                dados = entSaiDao.pesquisarCodCarreRel(self.ui.txtPesquisar.text())
                if dados != []:
                    EntSaiCarreCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn2.isChecked():
                dados = entSaiDao.pesquisarMotoCarreRel(self.ui.txtPesquisar.text())
                if dados != []:
                    EntSaiCarreCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn3.isChecked():
                dados = entSaiDao.pesquisarPlacaCarreRel(self.ui.txtPesquisar.text())
                if dados != []:
                    EntSaiCarreCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn4.isChecked():
                dados = entSaiDao.pesquisarCargaCarreRel(self.ui.txtPesquisar.text())
                if dados != []:
                    NotasFiscaisCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn5.isChecked():
                dados = entSaiDao.pesquisarProdCarreRel(self.ui.txtPesquisar.text())
                if dados != []:
                    EntSaiCarreCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn6.isChecked():
                dados = entSaiDao.pesquisarClieCarreRel(self.ui.txtPesquisar.text())
                if dados != []:
                    EntSaiCarreCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")

        elif self.ui.radBtnEntSaiDescarregamento.isChecked():

            entSaiDao = DescarreSaidaDao()

            if self.ui.radBtn1.isChecked():
                dados = entSaiDao.pesquisarCodDescaRel(self.ui.txtPesquisar.text())
                if dados != []:
                    EntSaiDescaCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn2.isChecked():
                dados = entSaiDao.pesquisarNumNfDescaRel(self.ui.txtPesquisar.text())
                if dados != []:
                    EntSaiDescaCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn3.isChecked():
                dados = entSaiDao.pesquisarProdutoDescaRel(self.ui.txtPesquisar.text())
                if dados != []:
                    EntSaiDescaCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn4.isChecked():
                dados = entSaiDao.pesquisarMotoDescaRel(self.ui.txtPesquisar.text())
                if dados != []:
                    EntSaiDescaCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn5.isChecked():
                dados = entSaiDao.pesquisarPlacaDescaRel(self.ui.txtPesquisar.text())
                if dados != []:
                    EntSaiDescaCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn6.isChecked():
                dados = entSaiDao.pesquisarFornDescaRel(self.ui.txtPesquisar.text())
                if dados != []:
                    EntSaiDescaCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")

        elif self.ui.radBtnEntSaiFuncionario.isChecked():

            entSaiDao = SaidaFuncionarioDao()

            if self.ui.radBtn1.isChecked():
                dados = entSaiDao.pesquisarCodFuncRel(self.ui.txtPesquisar.text())
                if dados != []:
                    EntSaiFuncCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn2.isChecked():
                dados = entSaiDao.pesquisarFuncioFuncRel(self.ui.txtPesquisar.text())
                if dados != []:
                    EntSaiFuncCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn3.isChecked():
                dados = entSaiDao.pesquisarSetorFuncRel(self.ui.txtPesquisar.text())
                if dados != []:
                    EntSaiFuncCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn4.isChecked():
                dados = entSaiDao.pesquisarCargoFuncRel(self.ui.txtPesquisar.text())
                if dados != []:
                    EntSaiFuncCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn5.isChecked():
                pass
            elif self.ui.radBtn6.isChecked():
                pass

    def gerarHtml(self):
        if self.ui.radBtnPessoaFisica.isChecked():

            fisicaDao = PesquisarPessoaFisicaDao()
            from classes.HTML import TAG

            if self.ui.radBtn1.isChecked():
                dados = fisicaDao.pesquisaCodigo(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn2.isChecked():
                dados = fisicaDao.pesquisaNome(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn3.isChecked():
                dados = fisicaDao.pesquisaApelido(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn4.isChecked():
                dados = fisicaDao.pesquisaCpf(self.ui.txtPesquisar.text())
                if dados != "":
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn5.isChecked():
                dados = fisicaDao.pesquisaRg(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn6.isChecked():
                pass

        elif self.ui.radBtnPessoaJuridica.isChecked():

            jurDao = PesquisarPessoaJuridicaDao()
            from classes.pessoaJuridicaHTML import TAG

            if self.ui.radBtn1.isChecked():
                dados = jurDao.pesquisaCodigo(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn2.isChecked():
                dados = jurDao.pesquisaRazaoSocial(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn3.isChecked():
                dados = jurDao.pesquisaFantasia(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn4.isChecked():
                dados = jurDao.pesquisaCnpj(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn5.isChecked():
                dados = jurDao.pesquisaInsEstadual(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn6.isChecked():
                pass

        elif self.ui.radBtnEmpresa.isChecked():

            empDao = EmpresaDao()
            from classes.empresaHTML import TAG

            if self.ui.radBtn1.isChecked():
                dados = empDao.pesquisaCodigo(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn2.isChecked():
                dados = empDao.pesquisaRazaoSocial(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn3.isChecked():
                dados = empDao.pesquisaFantasia(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn4.isChecked():
                dados = empDao.pesquisaCnpj(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn5.isChecked():
                dados = empDao.pesquisaInscEstadual(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn6.isChecked():
                dados = empDao.pesquisaInscMunicipal(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")

        elif self.ui.radBtnFuncionario.isChecked():

            funDao = FuncionarioDao()
            from classes.funcionarioHTML import TAG

            if self.ui.radBtn1.isChecked():
                dados = funDao.pesquisarFuncionarioCodigo(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn2.isChecked():
                dados = funDao.pesquisarFuncionarioNome(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn3.isChecked():
                dados = funDao.pesquisarFuncionarioCPF(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn4.isChecked():
                dados = funDao.pesquisarFuncionarioRg(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn5.isChecked():
                dados = funDao.pesquisarFuncionarioNumCarteira(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn6.isChecked():
                dados = funDao.pesquisarFuncionarioPis(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")

        elif self.ui.radBtnCliente.isChecked():

            cliDao = ClienteDao()
            from classes.clienteHTML import TAG

            if self.ui.radBtn1.isChecked():
                dados = cliDao.pesquisaCodigoFisica(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn2.isChecked():
                dados = cliDao.pesquisarNomeFisica(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn3.isChecked():
                dados = cliDao.pesquisaApelidoFisica(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn4.isChecked():
                dados = cliDao.pesquisaCpfFisica(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn5.isChecked():
                dados = cliDao.pesquisaRgFisica(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn6.isChecked():
               pass

        elif self.ui.radBtnFornecedor.isChecked():

            forDao = FornecedorDao()
            from classes.fornecedorHTML import TAG

            if self.ui.radBtn1.isChecked():
                dados = forDao.pesquisaCodigoFisica(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn2.isChecked():
                dados = forDao.pesquisarNomeFisica(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn3.isChecked():
                dados = forDao.pesquisaApelidoFisica(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn4.isChecked():
                dados = forDao.pesquisaCpfFisica(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn5.isChecked():
                dados = forDao.pesquisaRgFisica(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn6.isChecked():
               pass

        elif self.ui.radBtnUsuarios.isChecked():

            usuDao = UsuarioPermissaoDao()
            from classes.usuarioHTML import TAG

            if self.ui.radBtn1.isChecked():
                dados = usuDao.pesquisaCodigoUsuario(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn2.isChecked():
                dados = usuDao.pesquisarNomeFuncionario(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn3.isChecked():
                dados = usuDao.pesquisaSetor(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn4.isChecked():
                dados = usuDao.pesquisaCargo(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn5.isChecked():
                dados = usuDao.pesquisaLogin(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn6.isChecked():
               pass

        elif self.ui.radBtnNf.isChecked():

            nfDao = NotaFiscalRomanieo()
            from classes.notasFiscaisHTML import TAG

            if self.ui.radBtn1.isChecked():
                dados = nfDao.pesquisarCodNfRel(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn2.isChecked():
                dados = nfDao.pesquisarNumNfRel(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn3.isChecked():
                dados = nfDao.pesquisarForNfRel(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn4.isChecked():
                dados = nfDao.pesquisarMotoNfRel(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn5.isChecked():
                dados = nfDao.pesquisarProNfRel(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn6.isChecked():
               pass

        elif self.ui.radBtnEntSaiCarregamento.isChecked():

            entSaiDao = CarregamentoSaidaDao()
            from classes.entSaiCarreHTML import TAG

            if self.ui.radBtn1.isChecked():
                dados = entSaiDao.pesquisarCodCarreRel(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn2.isChecked():
                dados = entSaiDao.pesquisarMotoCarreRel(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn3.isChecked():
                dados = entSaiDao.pesquisarPlacaCarreRel(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn4.isChecked():
                dados = entSaiDao.pesquisarCargaCarreRel(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn5.isChecked():
                dados = entSaiDao.pesquisarProdCarreRel(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn6.isChecked():
                dados = entSaiDao.pesquisarClieCarreRel(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")

        elif self.ui.radBtnEntSaiDescarregamento.isChecked():

            entSaiDao = DescarreSaidaDao()
            from classes.entSaiDescaHTML import TAG

            if self.ui.radBtn1.isChecked():
                dados = entSaiDao.pesquisarCodDescaRel(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn2.isChecked():
                dados = entSaiDao.pesquisarNumNfDescaRel(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn3.isChecked():
                dados = entSaiDao.pesquisarProdutoDescaRel(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn4.isChecked():
                dados = entSaiDao.pesquisarMotoDescaRel(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn5.isChecked():
                dados = entSaiDao.pesquisarPlacaDescaRel(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn6.isChecked():
                dados = entSaiDao.pesquisarFornDescaRel(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")

        elif self.ui.radBtnEntSaiFuncionario.isChecked():

            entSaiDao = SaidaFuncionarioDao()
            from classes.entSaiFuncHTML import TAG

            if self.ui.radBtn1.isChecked():
                dados = entSaiDao.pesquisarCodFuncRel(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn2.isChecked():
                dados = entSaiDao.pesquisarFuncioFuncRel(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn3.isChecked():
                dados = entSaiDao.pesquisarSetorFuncRel(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn4.isChecked():
                dados = entSaiDao.pesquisarCargoFuncRel(self.ui.txtPesquisar.text())
                if dados != []:
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn5.isChecked():
                pass
            elif self.ui.radBtn6.isChecked():
                pass