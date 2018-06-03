import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from classes.classMensagemBox import MensagemBox
from classes.classUsuario import Usuario
from classes.classValidator import Validator
from controller.getSetFuncionario import Funcionario
from controller.getSetUsuario import UsuarioGetSet
from dao.funcionarioDao import FuncionarioDao
from dao.usuarioDao import UsuarioDao
from dao.usuarioPermissaoDao import UsuarioPermissaoDao
from telas.frmCadUsuarios import Ui_frmCadastroUsuarios
from telas.frmPesquisarFuncionario import Ui_frmPesquisarFuncionario


class UsuarioPermissao(QtGui.QDialog):

    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmCadastroUsuarios()
        self.ui.setupUi(self)
        self.validator = Validator()
        self.mensagem = MensagemBox()
        self.idUsuario = int()

        self.ui.txtLoginFuncionario.setValidator(self.validator)
        self.ui.txtSenhaFuncionario.setValidator(self.validator)

        # inicio botoes usuario
        self.ui.btnNovo.clicked.connect(self.ativarPesquisaUsuario)
        self.ui.btnSalvar.clicked.connect(self.cadastrar)
        self.ui.btnCancelar.clicked.connect(self.cancelarUsuario)
        # fim botoes usuario

        # inicio botoes permissão
        self.ui.btnAvacarPg1.clicked.connect(self.avancarVoltarPg2)
        self.ui.btnAvacarPg2.clicked.connect(self.avancarVoltarPg1)

        self.ui.btnVoltarPg1.clicked.connect(self.avancarVoltarPg2)
        self.ui.btnVoltarPg2.clicked.connect(self.avancarVoltarPg1)
        # fim botoes permissão


        self.ui.btnPesquisar.clicked.connect(self.pesquiFuncionario)

        self.ui.txtidFuncionario.returnPressed.connect(self.pesquisarFuncionario)
        self.ui.txtidFuncionario.editingFinished.connect(self.pesquisarFuncionarioEditFinish)

        self.ui.cBoxPessoaFisica.clicked.connect(self.changeClic)
        self.ui.cBoxPessoaJuridicaAtivar.clicked.connect(self.changeClic)
        self.ui.cBoxEmpresaAtivar.clicked.connect(self.changeClic)
        self.ui.cBoxFuncionarioAtivar.clicked.connect(self.changeClic)
        self.ui.cBoxFornecedorAtivar.clicked.connect(self.changeClic)
        self.ui.cBoxClienteAtivar.clicked.connect(self.changeClic)
        self.ui.cBoxMotoristaAtivar.clicked.connect(self.changeClic)
        self.ui.cBoxUsuPermAtivar.clicked.connect(self.changeClic)
        self.ui.cBoxNotaFiscalAtivar.clicked.connect(self.changeClic)
        self.ui.cheBoxEntradaVeiculosDescarregamentoAtivar.clicked.connect(self.changeClic)
        self.ui.cheBoxSaidaVeiculosDescarregamentoAtivar.clicked.connect(self.changeClic)
        self.ui.cheBoxEntradaVeiculosCarregamentoAtivar.clicked.connect(self.changeClic)
        self.ui.cheBoxSaidaVeiculosCarregamentoAtivar.clicked.connect(self.changeClic)
        self.ui.cheBoxEntrdaFuncionarioAtivar.clicked.connect(self.changeClic)
        self.ui.cheBoxSaidaFuncionarioAtivar.clicked.connect(self.changeClic)
        self.ui.cBoxRelatorioAtivar.clicked.connect(self.changeClic)




    def avancarVoltarPg1(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def avancarVoltarPg2(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def avancarVoltarPg3(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def ativarPesquisaUsuario(self):
        self.ui.grbFuncionarioPesquisa.setEnabled(True)
        self.ui.tabwCadPermUsuario.setEnabled(True)
        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(True)
        self.ui.btnEditar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(True)
        self.ui.btnDeletar.setEnabled(False)

    def desativarPesquisaUsuario(self):
        self.ui.grbFuncionarioPesquisa.setEnabled(False)
        self.ui.tabwCadPermUsuario.setEnabled(False)
        self.ui.btnNovo.setEnabled(True)
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnEditar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(False)
        self.ui.btnDeletar.setEnabled(False)
        self.ui.tabwCadPermUsuario.setCurrentIndex(0)

    def limparCamposCheckBox(self):

        self.ui.cBoxPessoaFisica.setChecked(False)
        self.ui.cBoxPessoaFisicaCadastro.setChecked(False)
        self.ui.cBoxPessoaFisicaCancelar.setChecked(False)
        self.ui.cBoxPessoaFisicaDeletar.setChecked(False)
        self.ui.cBoxPessoaFisicaEditar.setChecked(False)

        self.ui.cBoxPessoaJuridicaAtivar.setChecked(False)
        self.ui.cBoxPessoaJuridicaCadastro.setChecked(False)
        self.ui.cBoxPessoaJuridicaCancelar.setChecked(False)
        self.ui.cBoxPessoaJuridicaDeletar.setChecked(False)
        self.ui.cBoxPessoaJuridicaEditar.setChecked(False)

        self.ui.cBoxClienteAtivar.setChecked(False)
        self.ui.cBoxClienteCadastro.setChecked(False)
        self.ui.cBoxClienteCancelar.setChecked(False)
        self.ui.cBoxClienteDeletar.setChecked(False)
        self.ui.cBoxClienteEditar.setChecked(False)

        self.ui.cBoxEmpresaAtivar.setChecked(False)
        self.ui.cBoxEmpresaCadastro.setChecked(False)
        self.ui.cBoxEmpresaCancelar.setChecked(False)
        self.ui.cBoxEmpresaDeletar.setChecked(False)
        self.ui.cBoxEmpresaEditar.setChecked(False)

        self.ui.cBoxFornecedorAtivar.setChecked(False)
        self.ui.cBoxFornecedorCadastro.setChecked(False)
        self.ui.cBoxFornecedorCancelar.setChecked(False)
        self.ui.cBoxFornecedorDeletar.setChecked(False)
        self.ui.cBoxFornecedorEditar.setChecked(False)

        self.ui.cBoxFuncionarioAtivar.setChecked(False)
        self.ui.cBoxFuncionarioCadastrar.setChecked(False)
        self.ui.cBoxFuncionarioCancelar.setChecked(False)
        self.ui.cBoxFuncionarioDeletar.setChecked(False)
        self.ui.cBoxFuncionarioEditar.setChecked(False)

        self.ui.cBoxMotoristaAtivar.setChecked(False)
        self.ui.cBoxMotoristaCadastro.setChecked(False)
        self.ui.cBoxMotoristaCancelar.setChecked(False)
        self.ui.cBoxMotoristaDeletar.setChecked(False)
        self.ui.cBoxMotoristaEditar.setChecked(False)

        self.ui.cBoxUsuPermAtivar.setChecked(False)
        self.ui.cBoxUsuPermCadastro.setChecked(False)
        self.ui.cBoxUsuPermCancelar.setChecked(False)
        self.ui.cBoxUsuPermDeletar.setChecked(False)
        self.ui.cBoxUsuPermEditar.setChecked(False)

        self.ui.cBoxNotaFiscalAtivar.setChecked(False)
        self.ui.cBoxNotaFiscalCadastro.setChecked(False)
        self.ui.cBoxNotaFiscalCancelar.setChecked(False)
        self.ui.cBoxNotaFiscalDeletar.setChecked(False)
        self.ui.cBoxNotaFiscalEditar.setChecked(False)

        self.ui.cheBoxEntradaVeiculosCarregamentoAtivar.setChecked(False)
        self.ui.cheBoxEntradaVeiculosCarregamentoCadastro.setChecked(False)
        self.ui.cheBoxEntradaVeiculosCarregamentoCancelar.setChecked(False)

        self.ui.cheBoxEntradaVeiculosDescarregamentoAtivar.setChecked(False)
        self.ui.cheBoxEntradaVeiculosDescarregamentoCadastro.setChecked(False)
        self.ui.cheBoxEntradaVeiculosDescarregamentoCancelar.setChecked(False)

        self.ui.cheBoxEntrdaFuncionarioAtivar.setChecked(False)
        self.ui.cheBoxEntrdaFuncionarioCadastro.setChecked(False)
        self.ui.cheBoxEntrdaFuncionarioCancelar.setChecked(False)

        self.ui.cheBoxSaidaFuncionarioAtivar.setChecked(False)
        self.ui.cheBoxSaidaFuncionarioCadastro.setChecked(False)
        self.ui.cheBoxSaidaFuncionarioCancelar.setChecked(False)

        self.ui.cheBoxSaidaVeiculosCarregamentoAtivar.setChecked(False)
        self.ui.cheBoxSaidaVeiculosCarregamentoCadastro.setChecked(False)
        self.ui.cheBoxSaidaVeiculosCarregamentoCancelar.setChecked(False)

        self.ui.cheBoxSaidaVeiculosDescarregamentoAtivar.setChecked(False)
        self.ui.cheBoxSaidaVeiculosDescarregamentoCadastro.setChecked(False)
        self.ui.cheBoxSaidaVeiculosDescarregamentoCancelar.setChecked(False)

        self.ui.cBoxRelatorioAtivar.setChecked(False)
        self.ui.cBoxRelatorioGerarCsv.setChecked(False)
        self.ui.cBoxRelatorioGerarHtml.setChecked(False)

    def changeClic(self):

        if self.ui.cBoxPessoaFisica.isChecked() == False:
            self.ui.cBoxPessoaFisicaCadastro.setChecked(False)
            self.ui.cBoxPessoaFisicaCancelar.setChecked(False)
            self.ui.cBoxPessoaFisicaDeletar.setChecked(False)
            self.ui.cBoxPessoaFisicaEditar.setChecked(False)

            self.ui.cBoxPessoaFisicaCadastro.setEnabled(False)
            self.ui.cBoxPessoaFisicaCancelar.setEnabled(False)
            self.ui.cBoxPessoaFisicaDeletar.setEnabled(False)
            self.ui.cBoxPessoaFisicaEditar.setEnabled(False)
        else:
            self.ui.cBoxPessoaFisicaCadastro.setEnabled(True)
            self.ui.cBoxPessoaFisicaCancelar.setEnabled(True)
            self.ui.cBoxPessoaFisicaDeletar.setEnabled(True)
            self.ui.cBoxPessoaFisicaEditar.setEnabled(True)

        if self.ui.cBoxPessoaJuridicaAtivar.isChecked() == False:
            self.ui.cBoxPessoaJuridicaCadastro.setChecked(False)
            self.ui.cBoxPessoaJuridicaCancelar.setChecked(False)
            self.ui.cBoxPessoaJuridicaDeletar.setChecked(False)
            self.ui.cBoxPessoaJuridicaEditar.setChecked(False)

            self.ui.cBoxPessoaJuridicaCadastro.setEnabled(False)
            self.ui.cBoxPessoaJuridicaCancelar.setEnabled(False)
            self.ui.cBoxPessoaJuridicaDeletar.setEnabled(False)
            self.ui.cBoxPessoaJuridicaEditar.setEnabled(False)
        else:
            self.ui.cBoxPessoaJuridicaCadastro.setEnabled(True)
            self.ui.cBoxPessoaJuridicaCancelar.setEnabled(True)
            self.ui.cBoxPessoaJuridicaDeletar.setEnabled(True)
            self.ui.cBoxPessoaJuridicaEditar.setEnabled(True)

        if self.ui.cBoxClienteAtivar.isChecked() == False:
            self.ui.cBoxClienteCadastro.setChecked(False)
            self.ui.cBoxClienteCancelar.setChecked(False)
            self.ui.cBoxClienteDeletar.setChecked(False)
            self.ui.cBoxClienteEditar.setChecked(False)

            self.ui.cBoxClienteCadastro.setEnabled(False)
            self.ui.cBoxClienteCancelar.setEnabled(False)
            self.ui.cBoxClienteDeletar.setEnabled(False)
            self.ui.cBoxClienteEditar.setEnabled(False)
        else:
            self.ui.cBoxClienteCadastro.setEnabled(True)
            self.ui.cBoxClienteCancelar.setEnabled(True)
            self.ui.cBoxClienteDeletar.setEnabled(True)
            self.ui.cBoxClienteEditar.setEnabled(True)

        if self.ui.cBoxEmpresaAtivar.isChecked() == False:
            self.ui.cBoxEmpresaCadastro.setChecked(False)
            self.ui.cBoxEmpresaCancelar.setChecked(False)
            self.ui.cBoxEmpresaDeletar.setChecked(False)
            self.ui.cBoxEmpresaEditar.setChecked(False)

            self.ui.cBoxEmpresaCadastro.setEnabled(False)
            self.ui.cBoxEmpresaCancelar.setEnabled(False)
            self.ui.cBoxEmpresaDeletar.setEnabled(False)
            self.ui.cBoxEmpresaEditar.setEnabled(False)
        else:
            self.ui.cBoxEmpresaCadastro.setEnabled(True)
            self.ui.cBoxEmpresaCancelar.setEnabled(True)
            self.ui.cBoxEmpresaDeletar.setEnabled(True)
            self.ui.cBoxEmpresaEditar.setEnabled(True)

        if self.ui.cBoxFornecedorAtivar.isChecked() == False:
            self.ui.cBoxFornecedorCadastro.setChecked(False)
            self.ui.cBoxFornecedorCancelar.setChecked(False)
            self.ui.cBoxFornecedorDeletar.setChecked(False)
            self.ui.cBoxFornecedorEditar.setChecked(False)

            self.ui.cBoxFornecedorCadastro.setEnabled(False)
            self.ui.cBoxFornecedorCancelar.setEnabled(False)
            self.ui.cBoxFornecedorDeletar.setEnabled(False)
            self.ui.cBoxFornecedorEditar.setEnabled(False)
        else:
            self.ui.cBoxFornecedorCadastro.setEnabled(True)
            self.ui.cBoxFornecedorCancelar.setEnabled(True)
            self.ui.cBoxFornecedorDeletar.setEnabled(True)
            self.ui.cBoxFornecedorEditar.setEnabled(True)

        if self.ui.cBoxFuncionarioAtivar.isChecked() == False:
            self.ui.cBoxFuncionarioCadastrar.setChecked(False)
            self.ui.cBoxFuncionarioCancelar.setChecked(False)
            self.ui.cBoxFuncionarioDeletar.setChecked(False)
            self.ui.cBoxFuncionarioEditar.setChecked(False)

            self.ui.cBoxFuncionarioCadastrar.setEnabled(False)
            self.ui.cBoxFuncionarioCancelar.setEnabled(False)
            self.ui.cBoxFuncionarioDeletar.setEnabled(False)
            self.ui.cBoxFuncionarioEditar.setEnabled(False)
        else:
            self.ui.cBoxFuncionarioCadastrar.setEnabled(True)
            self.ui.cBoxFuncionarioCancelar.setEnabled(True)
            self.ui.cBoxFuncionarioDeletar.setEnabled(True)
            self.ui.cBoxFuncionarioEditar.setEnabled(True)

        if self.ui.cBoxMotoristaAtivar.isChecked() == False:
            self.ui.cBoxMotoristaCadastro.setChecked(False)
            self.ui.cBoxMotoristaCancelar.setChecked(False)
            self.ui.cBoxMotoristaDeletar.setChecked(False)
            self.ui.cBoxMotoristaEditar.setChecked(False)

            self.ui.cBoxMotoristaCadastro.setEnabled(False)
            self.ui.cBoxMotoristaCancelar.setEnabled(False)
            self.ui.cBoxMotoristaDeletar.setEnabled(False)
            self.ui.cBoxMotoristaEditar.setEnabled(False)
        else:
            self.ui.cBoxMotoristaCadastro.setEnabled(True)
            self.ui.cBoxMotoristaCancelar.setEnabled(True)
            self.ui.cBoxMotoristaDeletar.setEnabled(True)
            self.ui.cBoxMotoristaEditar.setEnabled(True)

        if self.ui.cBoxUsuPermAtivar.isChecked() == False:
            self.ui.cBoxUsuPermCadastro.setChecked(False)
            self.ui.cBoxUsuPermCancelar.setChecked(False)
            self.ui.cBoxUsuPermDeletar.setChecked(False)
            self.ui.cBoxUsuPermEditar.setChecked(False)

            self.ui.cBoxUsuPermCadastro.setEnabled(False)
            self.ui.cBoxUsuPermCancelar.setEnabled(False)
            self.ui.cBoxUsuPermDeletar.setEnabled(False)
            self.ui.cBoxUsuPermEditar.setEnabled(False)
        else:
            self.ui.cBoxUsuPermCadastro.setEnabled(True)
            self.ui.cBoxUsuPermCancelar.setEnabled(True)
            self.ui.cBoxUsuPermDeletar.setEnabled(True)
            self.ui.cBoxUsuPermEditar.setEnabled(True)

        if self.ui.cBoxNotaFiscalAtivar.isChecked() == False:
            self.ui.cBoxNotaFiscalCadastro.setChecked(False)
            self.ui.cBoxNotaFiscalCancelar.setChecked(False)
            self.ui.cBoxNotaFiscalDeletar.setChecked(False)
            self.ui.cBoxNotaFiscalEditar.setChecked(False)

            self.ui.cBoxNotaFiscalCadastro.setEnabled(False)
            self.ui.cBoxNotaFiscalCancelar.setEnabled(False)
            self.ui.cBoxNotaFiscalDeletar.setEnabled(False)
            self.ui.cBoxNotaFiscalEditar.setEnabled(False)
        else:
            self.ui.cBoxNotaFiscalCadastro.setEnabled(True)
            self.ui.cBoxNotaFiscalCancelar.setEnabled(True)
            self.ui.cBoxNotaFiscalDeletar.setEnabled(True)
            self.ui.cBoxNotaFiscalEditar.setEnabled(True)

        if self.ui.cheBoxEntradaVeiculosCarregamentoAtivar.isChecked() == False:
            self.ui.cheBoxEntradaVeiculosCarregamentoCadastro.setChecked(False)
            self.ui.cheBoxEntradaVeiculosCarregamentoCancelar.setChecked(False)

            self.ui.cheBoxEntradaVeiculosCarregamentoCadastro.setEnabled(False)
            self.ui.cheBoxEntradaVeiculosCarregamentoCancelar.setEnabled(False)
        else:
            self.ui.cheBoxEntradaVeiculosCarregamentoCadastro.setEnabled(True)
            self.ui.cheBoxEntradaVeiculosCarregamentoCancelar.setEnabled(True)

        if self.ui.cheBoxEntradaVeiculosDescarregamentoAtivar.isChecked() == False:
            self.ui.cheBoxEntradaVeiculosDescarregamentoCadastro.setChecked(False)
            self.ui.cheBoxEntradaVeiculosDescarregamentoCancelar.setChecked(False)

            self.ui.cheBoxEntradaVeiculosDescarregamentoCadastro.setEnabled(False)
            self.ui.cheBoxEntradaVeiculosDescarregamentoCancelar.setEnabled(False)
        else:
            self.ui.cheBoxEntradaVeiculosDescarregamentoCadastro.setEnabled(True)
            self.ui.cheBoxEntradaVeiculosDescarregamentoCancelar.setEnabled(True)

        if self.ui.cheBoxEntrdaFuncionarioAtivar.isChecked() == False:
            self.ui.cheBoxEntrdaFuncionarioCadastro.setChecked(False)
            self.ui.cheBoxEntrdaFuncionarioCancelar.setChecked(False)

            self.ui.cheBoxEntrdaFuncionarioCadastro.setEnabled(False)
            self.ui.cheBoxEntrdaFuncionarioCancelar.setEnabled(False)
        else:
            self.ui.cheBoxEntrdaFuncionarioCadastro.setEnabled(True)
            self.ui.cheBoxEntrdaFuncionarioCancelar.setEnabled(True)

        if self.ui.cheBoxSaidaFuncionarioAtivar.isChecked() == False:
            self.ui.cheBoxSaidaFuncionarioCadastro.setChecked(False)
            self.ui.cheBoxSaidaFuncionarioCancelar.setChecked(False)

            self.ui.cheBoxSaidaFuncionarioCadastro.setEnabled(False)
            self.ui.cheBoxSaidaFuncionarioCancelar.setEnabled(False)
        else:
            self.ui.cheBoxSaidaFuncionarioCadastro.setEnabled(True)
            self.ui.cheBoxSaidaFuncionarioCancelar.setEnabled(True)

        if self.ui.cheBoxSaidaVeiculosCarregamentoAtivar.isChecked() == False:
            self.ui.cheBoxSaidaVeiculosCarregamentoCadastro.setChecked(False)
            self.ui.cheBoxSaidaVeiculosCarregamentoCancelar.setChecked(False)

            self.ui.cheBoxSaidaVeiculosCarregamentoCadastro.setEnabled(False)
            self.ui.cheBoxSaidaVeiculosCarregamentoCancelar.setEnabled(False)
        else:
            self.ui.cheBoxSaidaVeiculosCarregamentoCadastro.setEnabled(True)
            self.ui.cheBoxSaidaVeiculosCarregamentoCancelar.setEnabled(True)

        if self.ui.cheBoxSaidaVeiculosDescarregamentoAtivar.isChecked() == False:
            self.ui.cheBoxSaidaVeiculosDescarregamentoCadastro.setChecked(False)
            self.ui.cheBoxSaidaVeiculosDescarregamentoCancelar.setChecked(False)

            self.ui.cheBoxSaidaVeiculosDescarregamentoCadastro.setEnabled(False)
            self.ui.cheBoxSaidaVeiculosDescarregamentoCancelar.setEnabled(False)
        else:
            self.ui.cheBoxSaidaVeiculosDescarregamentoCadastro.setEnabled(True)
            self.ui.cheBoxSaidaVeiculosDescarregamentoCancelar.setEnabled(True)

        if self.ui.cBoxRelatorioAtivar.isChecked() == False:
            self.ui.cBoxRelatorioGerarCsv.setChecked(False)
            self.ui.cBoxRelatorioGerarHtml.setChecked(False)

            self.ui.cBoxRelatorioGerarCsv.setEnabled(False)
            self.ui.cBoxRelatorioGerarHtml.setEnabled(False)
        else:
            self.ui.cBoxRelatorioGerarCsv.setEnabled(True)
            self.ui.cBoxRelatorioGerarHtml.setEnabled(True)

    def limparCamposUsuario(self):
        self.idUsuario = int()
        self.ui.txtidFuncionario.clear()
        self.ui.txtNomeFuncionario.clear()
        self.ui.txtCargo.clear()
        self.ui.txtSetor.clear()
        self.ui.txtLoginFuncionario.clear()
        self.ui.txtSenhaFuncionario.clear()

    def cancelarUsuario(self):
        result = QMessageBox.question(QWidget(), 'Menssagem', "Deseja realmente cancelar a operação", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            self.limparCamposCheckBox()
            self.limparCamposUsuario()
            self.desativarPesquisaUsuario()

    def pesquiFuncionario(self):
            self.dialog = QDialog(self)
            self.__pesquisarPessoa = Ui_frmPesquisarFuncionario()
            self.__pesquisarPessoa.setupUi(self.dialog)

            self.__pesquisarPessoa.txtPesquisar.returnPressed.connect(self.pesquisar)

            self.__pesquisarPessoa.btnPesquisar.clicked.connect(self.pesquisar)

            self.__pesquisarPessoa.tabPesquisar.doubleClicked.connect(self.setarCampos)

            self.dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            self.dialog.exec_()

    def pesquisar(self):
        if self.__pesquisarPessoa.radBtnCodigo.isChecked():
            __nome = self.__pesquisarPessoa.txtPesquisar.text()
            __pesDao = FuncionarioDao()
            __retorno = __pesDao.pesquisarFuncionarioCodigo(__nome)

            self.setarTabelaPesquisa(__retorno)

        elif self.__pesquisarPessoa.radBtnNome.isChecked():
            __nome = self.__pesquisarPessoa.txtPesquisar.text()
            __pesDao = FuncionarioDao()
            __retorno = __pesDao.pesquisarFuncionarioNome(__nome)

            self.setarTabelaPesquisa(__retorno)

        elif self.__pesquisarPessoa.radBtncPF.isChecked():
            __cpf= self.__pesquisarPessoa.txtPesquisar.text()
            __pesDao = FuncionarioDao()
            __retorno = __pesDao.pesquisarFuncionarioCPF(__cpf)

            self.setarTabelaPesquisa(__retorno)

        elif self.__pesquisarPessoa.radBtnRg.isChecked():
            __rg = self.__pesquisarPessoa.txtPesquisar.text()
            __pesDao = FuncionarioDao()
            __retorno = __pesDao.pesquisarFuncionarioRg(__rg)

            self.setarTabelaPesquisa(__retorno)

        elif self.__pesquisarPessoa.radBtnNumCarteira.isChecked():
            __mae = self.__pesquisarPessoa.txtPesquisar.text()
            __pesDao = FuncionarioDao()
            __retorno = __pesDao.pesquisarFuncionarioNumCarteira(__mae)

            self.setarTabelaPesquisa(__retorno)

        elif self.__pesquisarPessoa.radBtnPis.isChecked():
            __pai = self.__pesquisarPessoa.txtPesquisar.text()
            __pesDao = FuncionarioDao()
            __retorno = __pesDao.pesquisarFuncionarioPis(__pai)

            self.setarTabelaPesquisa(__retorno)

        else:
            MensagemBox().warning('Atenção', "Selecione uma das opções de pesquisa")

    def setarTabelaPesquisa(self, __retorno):
        qtde_registros = len(__retorno)
        self.__pesquisarPessoa.tabPesquisar.setRowCount(qtde_registros)

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
            obs =pesqui[30]
            jornada = pesqui[31]
            if pesqui[32] == 1:
                situacao = "Ativo"
            else:
                situacao = "Desativo"



            # preenchendo o grid de pesquisa
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(nome)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(segundoNome)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 3, QtGui.QTableWidgetItem(str(cpf)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 4, QtGui.QTableWidgetItem(str(rg)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 5, QtGui.QTableWidgetItem(str(expeditor)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 6, QtGui.QTableWidgetItem(str(uf)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 7, QtGui.QTableWidgetItem(str(data)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 8, QtGui.QTableWidgetItem(str(endereco)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 9, QtGui.QTableWidgetItem(str(numero)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 10, QtGui.QTableWidgetItem(str(complemento)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 11, QtGui.QTableWidgetItem(str(bairro)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 12, QtGui.QTableWidgetItem(str(cidade)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 13, QtGui.QTableWidgetItem(str(estado)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 14, QtGui.QTableWidgetItem(str(cep)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 15, QtGui.QTableWidgetItem(str(sexo)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 16, QtGui.QTableWidgetItem(str(mae)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 17, QtGui.QTableWidgetItem(str(pai)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 18, QtGui.QTableWidgetItem(str(admissao)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 19, QtGui.QTableWidgetItem(str(demissao)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 20, QtGui.QTableWidgetItem(str(carteira)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 21, QtGui.QTableWidgetItem(str(serie)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 22, QtGui.QTableWidgetItem(str(uff)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 23, QtGui.QTableWidgetItem(str(emissao)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 24, QtGui.QTableWidgetItem(str(pis)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 25, QtGui.QTableWidgetItem(str(civil)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 26, QtGui.QTableWidgetItem(str(deficiencia)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 27, QtGui.QTableWidgetItem(str(categoria)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 28, QtGui.QTableWidgetItem(str(cargo)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 29, QtGui.QTableWidgetItem(str(setor)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 30, QtGui.QTableWidgetItem(str(obs)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 31, QtGui.QTableWidgetItem(str(jornada)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 32, QtGui.QTableWidgetItem(str(situacao)))

            linha += 1

    def setarCampos(self):
        itens = []

        for item in self.__pesquisarPessoa.tabPesquisar.selectedItems():
            itens.append(item.text())

        codigo = itens[0]
        nome = itens[1]
        sobrenome = itens[2]
        cpf = itens[3]
        rg = itens[4]
        expeditor = itens[5]
        uf = itens[6]
        data = itens[7]
        sexo = itens[8]
        endereco = itens[9]
        numero = itens[10]
        complemento = itens[11]
        bairro = itens[12]
        mae = itens[13]
        pai = itens[14]
        cidade = itens[15]
        estado = itens[16]
        cep = itens[17]
        admissao = itens[18]
        demissao = itens[19]
        carteira = itens[20]
        serie = itens[21]
        uff = itens[22]
        emissao = itens[23]
        pis = itens[24]
        civil = itens[25]
        deficiencia = itens[26]
        categoria = itens[27]
        setor = itens[28]
        cargo = itens[29]
        obs = itens[30]
        jornada = itens[31]
        if itens[32] == 'Ativo':
            situacao = True
        else:
            situacao = False


        __dados = Funcionario(codigo, None, None, cpf, rg, nome, sobrenome, obs, situacao, civil, deficiencia, categoria, setor, cargo, jornada, admissao, demissao, carteira, pis, serie, uf,  emissao)
        self.setCampos(__dados)
        self.dialog.close()


    def setCampos(self, campos):
        self.ui.txtidFuncionario.setText(str(campos.getIdFuncionario))
        self.ui.txtNomeFuncionario.setText(campos.getNome + ' ' + campos.getSobrenome)
        self.ui.txtSetor.setText(campos.getCargo)
        self.ui.txtCargo.setText(campos.getSetor)


    def pesquisarFuncionario(self):
        __nome = self.ui.txtidFuncionario.text()
        __funDao = UsuarioPermissaoDao()
        __resultada = __funDao.pesquisarFuncionario(__nome)
        if __resultada == False:
            self.ui.txtNomeFuncionario.clear()
            self.ui.txtSetor.clear()
            self.ui.txtCargo.clear()
            MensagemBox().warning('Mensagem', "Atenção não existe nenhum cadastro deste funcionario")
        else:
            self.limparCamposUsuario()
            for non in __resultada:
                self.ui.txtidFuncionario.setText(str(non[0]))
                self.ui.txtNomeFuncionario.setText(non[1] + ' ' + non[2])
                self.ui.txtSetor.setText(non[28])
                self.ui.txtCargo.setText(non[29])

    def pesquisarFuncionarioEditFinish(self):
        __nome = self.ui.txtidFuncionario.text()
        __funDao = UsuarioPermissaoDao()
        __resultada = __funDao.pesquisarFuncionario(__nome)
        if __resultada == False:
            self.ui.txtNomeFuncionario.clear()
            self.ui.txtSetor.clear()
            self.ui.txtCargo.clear()
        else:
            self.limparCamposUsuario()
            for non in __resultada:
                self.ui.txtidFuncionario.setText(str(non[0]))
                self.ui.txtNomeFuncionario.setText(non[1] + ' ' + non[2])
                self.ui.txtSetor.setText(non[28])
                self.ui.txtCargo.setText(non[29])

    def cadastrar(self):
        if self.ui.txtidFuncionario.text() != "" and self.ui.txtNomeFuncionario.text() != "" and self.ui.txtCargo.text() != "" and self.ui.txtSetor.text() != "" and self.ui.txtLoginFuncionario.text() != "" and self.ui.txtSenhaFuncionario.text() != "" :
            idFuncionario = self.ui.txtidFuncionario.text()
            login = self.ui.txtLoginFuncionario.text()
            senha = self.ui.txtSenhaFuncionario.text()
            __usuario = Usuario()
            __saltoCripto = __usuario.getSalto()
            salto = __saltoCripto.decode('utf-8')
            __senhaCripto = __usuario.criptografar(senha, salto)

            usu = UsuarioGetSet(idFuncionario, login, __senhaCripto, salto)
            usuDao = UsuarioPermissaoDao()
            usuDao.cadatrar(usu)
            self.idUsuario = usuDao.ultimoRegistro()
            self.cadastroPermissoes()

            self.limparCamposCheckBox()
            self.limparCamposUsuario()
            self.desativarPesquisaUsuario()
        else:
            MensagemBox().warning('Atenção', "Por favor preencha todos os campos")


    def cadastroPermissoes(self):
        usuDao = UsuarioPermissaoDao()
        permissoes = [('1', self.ui.cBoxEmpresaAtivar.isChecked(), self.ui.cBoxEmpresaCadastro.isChecked(), self.ui.cBoxEmpresaCancelar.isChecked(), self.ui.cBoxEmpresaDeletar.isChecked(), self.ui.cBoxEmpresaEditar.isChecked()),
                      ('2', self.ui.cBoxFuncionarioAtivar.isChecked(), self.ui.cBoxFuncionarioCadastrar.isChecked(), self.ui.cBoxFuncionarioCancelar.isChecked(), self.ui.cBoxFuncionarioDeletar.isChecked(), self.ui.cBoxFuncionarioEditar.isChecked()),
                      ('3', self.ui.cBoxFornecedorAtivar.isChecked(), self.ui.cBoxFornecedorCadastro.isChecked(), self.ui.cBoxFornecedorCancelar.isChecked(), self.ui.cBoxFornecedorDeletar.isChecked(), self.ui.cBoxFornecedorEditar.isChecked()),
                      ('4', self.ui.cBoxClienteAtivar.isChecked(), self.ui.cBoxClienteCadastro.isChecked(), self.ui.cBoxClienteCancelar.isChecked(), self.ui.cBoxClienteDeletar.isChecked(), self.ui.cBoxClienteEditar.isChecked()),
                      ('5', self.ui.cBoxUsuPermAtivar.isChecked(), self.ui.cBoxUsuPermCadastro.isChecked(), self.ui.cBoxUsuPermCancelar.isChecked(), self.ui.cBoxUsuPermDeletar.isChecked(), self.ui.cBoxUsuPermEditar.isChecked()),
                      ('6', self.ui.cBoxMotoristaAtivar.isChecked(), self.ui.cBoxMotoristaCadastro.isChecked(), self.ui.cBoxMotoristaCancelar.isChecked(), self.ui.cBoxMotoristaDeletar.isChecked(), self.ui.cBoxMotoristaEditar.isChecked()),
                      ('7', self.ui.cheBoxEntrdaFuncionarioAtivar.isChecked(), self.ui.cheBoxEntrdaFuncionarioCadastro.isChecked(), self.ui.cheBoxEntrdaFuncionarioCancelar.isChecked(), None, None),
                      ('8', self.ui.cBoxNotaFiscalAtivar.isChecked(), self.ui.cBoxNotaFiscalCadastro.isChecked(), self.ui.cBoxNotaFiscalCancelar.isChecked(), self.ui.cBoxNotaFiscalDeletar.isChecked(), self.ui.cBoxNotaFiscalEditar.isChecked()),
                      ('9', self.ui.cheBoxEntradaVeiculosCarregamentoAtivar.isChecked(), self.ui.cheBoxEntradaVeiculosCarregamentoCadastro.isChecked(), self.ui.cheBoxEntradaVeiculosCarregamentoCancelar.isChecked(), None, None),
                      ('10', self.ui.cheBoxEntradaVeiculosDescarregamentoAtivar.isChecked(), self.ui.cheBoxEntradaVeiculosDescarregamentoCadastro.isChecked(), self.ui.cheBoxEntradaVeiculosDescarregamentoCancelar.isChecked(), None, None),
                      ('11', self.ui.cBoxRelatorioAtivar.isChecked(), self.ui.cBoxRelatorioGerarCsv.isChecked(), self.ui.cBoxRelatorioGerarHtml.isChecked(), None, None),
                      ('12', self.ui.cheBoxSaidaFuncionarioAtivar.isChecked(), self.ui.cheBoxSaidaFuncionarioCadastro.isChecked(), self.ui.cheBoxSaidaFuncionarioCancelar.isChecked(), None, None),
                      ('13', self.ui.cheBoxSaidaVeiculosDescarregamentoAtivar.isChecked(), self.ui.cheBoxSaidaVeiculosDescarregamentoCadastro.isChecked(), self.ui.cheBoxSaidaVeiculosDescarregamentoCancelar.isChecked(), None, None),
                      ('14', self.ui.cheBoxSaidaVeiculosCarregamentoAtivar.isChecked(), self.ui.cheBoxSaidaVeiculosCarregamentoCadastro.isChecked(), self.ui.cheBoxSaidaVeiculosCarregamentoCancelar.isChecked(), None, None),
                      ('15', self.ui.cBoxPessoaJuridicaAtivar.isChecked(), self.ui.cBoxPessoaJuridicaCadastro.isChecked(), self.ui.cBoxPessoaJuridicaCancelar.isChecked(), self.ui.cBoxPessoaJuridicaDeletar.isChecked(), self.ui.cBoxPessoaJuridicaEditar.isChecked()),
                      ('16', self.ui.cBoxPessoaFisica.isChecked(), self.ui.cBoxPessoaFisicaCadastro.isChecked(), self.ui.cBoxPessoaFisicaCancelar.isChecked(), self.ui.cBoxPessoaFisicaDeletar.isChecked(), self.ui.cBoxPessoaFisicaEditar.isChecked())]

        for lis in permissoes:
            idFormulario = lis[0]

            if lis[1] == True:
                ativo = 1
            else:
                ativo = 0

            if lis[2] == True:
                cadastro = 1
            else:
                cadastro = 0

            if lis[3] == True:
                cancela = 1
            else:
                cancela = 0

            if lis[4] == True:
                deleta = 1
            else:
                deleta = 0

            if lis[5] == True:
                edita = 1
            else:
                edita = 0

            permi = usuDao.pesquisarPermissoes(idFormulario, ativo, cadastro, cancela, deleta, edita)

            if permi != '':
                usuDao.cadatrarPermissao(idFormulario, ativo, cadastro, cancela, deleta, edita)
                idPer = usuDao.ultimoRegistro()
                usuDao.cadatrarPermissaoUsuario(idPer, self.idUsuario)
            else:
                usuDao.cadatrarPermissaoUsuario(permi, self.idUsuario)
