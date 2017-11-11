import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from dao.usuarioDao import UsuarioDao
from telas.frmCadastroUsuarios import Ui_frmCadastroUsuarios


class UsuarioPermissao(QtGui.QDialog):

    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmCadastroUsuarios()
        self.ui.setupUi(self)

        # inicio botoes usuario
        self.ui.btnNovo.clicked.connect(self.ativarPesquisaUsuario)
        self.ui.btnCancelar.clicked.connect(self.cancelarUsuario)

        self.ui.btnCadPermiPesquisarFuncionario.clicked.connect(self.pesquisarFuncionario)

        self.ui.txtNomeFuncionarioUsuario.returnPressed.connect(self.pesquisarFuncionario)

        self.ui.tabFuncioariosUsuario.doubleClicked.connect(self.setarUsuario)
        # fim botoes usuario

        # inicio botoes permissão
        self.ui.btnPermissoesNovo.clicked.connect(self.ativarPesquisaPermissao)
        self.ui.btnPermissoesCancelar.clicked.connect(self.cancelarPermissao)

        self.ui.btnAvacarPg1.clicked.connect(self.avancarVoltarPg2)
        self.ui.btnAvacarPg2.clicked.connect(self.avancarVoltarPg3)
        self.ui.btnAvacarPg3.clicked.connect(self.avancarVoltarPg1)

        self.ui.btnVoltarPg1.clicked.connect(self.avancarVoltarPg3)
        self.ui.btnVoltarPg2.clicked.connect(self.avancarVoltarPg1)
        self.ui.btnVoltarPg3.clicked.connect(self.avancarVoltarPg2)


        self.ui.btnCadPermiPesquisar.clicked.connect(self.pesquisarUsuario)
        self.ui.txtNomeFuncionarioPermissoes.returnPressed.connect(self.pesquisarUsuario)

        self.ui.tabFuncioariosPermissoes.doubleClicked.connect(self.setarPermissao)
        # fim botoes permissão


    def avancarVoltarPg1(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def avancarVoltarPg2(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def avancarVoltarPg3(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def ativarPesquisaUsuario(self):
        self.ui.grbDadosPesquisaFuncionario.setEnabled(True)
        self.ui.txtNomeFuncionarioUsuario.setEnabled(True)
        self.ui.btnCadPermiPesquisarFuncionario.setEnabled(True)
        self.ui.tabFuncioariosUsuario.setEnabled(True)

        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(True)
        self.ui.btnCancelar.setEnabled(True)

    def ativarPesquisaPermissao(self):
        self.ui.grbDadosPesquisa.setEnabled(True)
        self.ui.txtNomeFuncionarioPermissoes.setEnabled(True)
        self.ui.btnCadPermiPesquisar.setEnabled(True)
        self.ui.tabFuncioariosPermissoes.setEnabled(True)

        self.ui.btnPermissoesNovo.setEnabled(False)
        self.ui.btnPermissoesSalvar.setEnabled(True)
        self.ui.btnPermissoesCancelar.setEnabled(True)

    def desativarPesquisaUsuario(self):
        self.ui.grbDadosPesquisaFuncionario.setEnabled(False)
        self.ui.txtNomeFuncionarioUsuario.setEnabled(False)
        self.ui.btnCadPermiPesquisarFuncionario.setEnabled(False)
        self.ui.tabFuncioariosUsuario.setEnabled(False)

        self.ui.btnNovo.setEnabled(True)
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(False)

    def desativarPesquisaPermissao(self):
        self.ui.grbDadosPesquisa.setEnabled(False)
        self.ui.txtNomeFuncionarioPermissoes.setEnabled(False)
        self.ui.btnCadPermiPesquisar.setEnabled(False)
        self.ui.tabFuncioariosPermissoes.setEnabled(False)

        self.ui.btnPermissoesNovo.setEnabled(True)
        self.ui.btnPermissoesSalvar.setEnabled(False)
        self.ui.btnPermissoesCancelar.setEnabled(False)

    def limparCamposPermicao(self):
        self.ui.txtNomeFuncionarioPermissoes.clear()
        self.ui.txtIdUsuario.clear()
        self.ui.txtNomeUsuario.clear()
        self.ui.txtNomFuncionarioPerm.clear()

    def limparCamposCheckBox(self):
        self.ui.cheBoxCadCargosAtivar.setChecked(False)
        self.ui.cheBoxCadCargosCadastro.setChecked(False)
        self.ui.cheBoxCadCargosCancelar.setChecked(False)
        self.ui.cheBoxCadCargosDeletar.setChecked(False)
        self.ui.cheBoxCadCargosEditar.setChecked(False)

        self.ui.cheBoxCadClienteAtivar.setChecked(False)
        self.ui.cheBoxCadClienteCadastro.setChecked(False)
        self.ui.cheBoxCadClienteCancelar.setChecked(False)
        self.ui.cheBoxCadClienteDeletar.setChecked(False)
        self.ui.cheBoxCadClienteEditar.setChecked(False)

        self.ui.cheBoxCadEmpresaAtivar.setChecked(False)
        self.ui.cheBoxCadEmpresaCadastro.setChecked(False)
        self.ui.cheBoxCadEmpresaCancelar.setChecked(False)
        self.ui.cheBoxCadEmpresaDeletar.setChecked(False)
        self.ui.cheBoxCadEmpresaEditar.setChecked(False)

        self.ui.cheBoxCadFornecedorAtivar.setChecked(False)
        self.ui.cheBoxCadFornecedorCadastro.setChecked(False)
        self.ui.cheBoxCadFornecedorCancelar.setChecked(False)
        self.ui.cheBoxCadFornecedorDeletar.setChecked(False)
        self.ui.cheBoxCadFornecedorEditar.setChecked(False)

        self.ui.cheBoxCadFuncionarioAtivar.setChecked(False)
        self.ui.cheBoxCadFuncionarioCadastro.setChecked(False)
        self.ui.cheBoxCadFuncionarioCancelar.setChecked(False)
        self.ui.cheBoxCadFuncionarioDeletar.setChecked(False)
        self.ui.cheBoxCadFuncionarioEditar.setChecked(False)

        self.ui.cheBoxCadMotoristaAtivar.setChecked(False)
        self.ui.cheBoxCadMotoristaCadastro.setChecked(False)
        self.ui.cheBoxCadMotoristaCancelar.setChecked(False)
        self.ui.cheBoxCadMotoristaDeletar.setChecked(False)
        self.ui.cheBoxCadMotoristaEditar.setChecked(False)

        self.ui.cheBoxCadPermissaoAtivar.setChecked(False)
        self.ui.cheBoxCadPermissaoCadastrar.setChecked(False)
        self.ui.cheBoxCadPermissaoCancelar.setChecked(False)
        self.ui.cheBoxCadPermissaodDeletar.setChecked(False)
        self.ui.cheBoxCadpermissaoEditar.setChecked(False)

        self.ui.cheBoxCadSetoresAtivar.setChecked(False)
        self.ui.cheBoxCadSetoresCadastro.setChecked(False)
        self.ui.cheBoxCadSetoresCancelar.setChecked(False)
        self.ui.cheBoxCadSetoresDeletar.setChecked(False)
        self.ui.cheBoxCadSetoresEditar.setChecked(False)

        self.ui.cheBoxCadUsuarioAtivar.setChecked(False)
        self.ui.cheBoxCadUsuarioCadastro.setChecked(False)
        self.ui.cheBoxCadUsuarioCancelar.setChecked(False)
        self.ui.cheBoxCadUsuarioDeletar.setChecked(False)
        self.ui.cheBoxCadUsuarioEditar.setChecked(False)

        self.ui.cheBoxEntradaCamEmpAtivar.setChecked(False)
        self.ui.cheBoxEntradaCamEmpCadastro.setChecked(False)
        self.ui.cheBoxEntradaCamEmpCancelar.setChecked(False)
        self.ui.cheBoxEntradaCamEmpDeletar.setChecked(False)
        self.ui.cheBoxEntradaCamEmpEditar.setChecked(False)

        self.ui.cheBoxEntradaCamTerAtivar.setChecked(False)
        self.ui.cheBoxEntradaCamTerCadastro.setChecked(False)
        self.ui.cheBoxEntradaCamTerCancelar.setChecked(False)
        self.ui.cheBoxEntradaCamTerDeletar.setChecked(False)
        self.ui.cheBoxEntradaCamTerEditar.setChecked(False)

        self.ui.cheBoxEntradaNotaFiscalAtivar.setChecked(False)
        self.ui.cheBoxEntradaNotaFiscalCadastro.setChecked(False)
        self.ui.cheBoxEntradaNotaFiscalCancelar.setChecked(False)
        self.ui.cheBoxEntradaNotaFiscalDeletar.setChecked(False)
        self.ui.cheBoxEntradaNotaFiscalEditar.setChecked(False)

        self.ui.cheBoxEntradaVeiculosCarregamentoAtivar.setChecked(False)
        self.ui.cheBoxEntradaVeiculosCarregamentoCadastro.setChecked(False)
        self.ui.cheBoxEntradaVeiculosCarregamentoCancelar.setChecked(False)
        self.ui.cheBoxEntradaVeiculosCarregamentoDeletar.setChecked(False)
        self.ui.cheBoxEntradaVeiculosCarregamentoEditar.setChecked(False)

        self.ui.cheBoxEntradaVeiculosDescarregamentoAtivar.setChecked(False)
        self.ui.cheBoxEntradaVeiculosDescarregamentoCadastro.setChecked(False)
        self.ui.cheBoxEntradaVeiculosDescarregamentoCancelar.setChecked(False)
        self.ui.cheBoxEntradaVeiculosDescarregamentoDeletar.setChecked(False)
        self.ui.cheBoxEntradaVeiculosDescarregamentoEditar.setChecked(False)

        self.ui.cheBoxEntradaVeiEmpAtivar.setChecked(False)
        self.ui.cheBoxEntradaVeiEmpCadastro.setChecked(False)
        self.ui.cheBoxEntradaVeiEmpCancelar.setChecked(False)
        self.ui.cheBoxEntradaVeiEmpDeletar.setChecked(False)
        self.ui.cheBoxEntradaVeiEmpEditar.setChecked(False)

        self.ui.cheBoxEntradaVeiTerAtivar.setChecked(False)
        self.ui.cheBoxEntradaVeiTerCadastro.setChecked(False)
        self.ui.cheBoxEntradaVeiTerCancelar.setChecked(False)
        self.ui.cheBoxEntradaVeiTerDeletar.setChecked(False)
        self.ui.cheBoxEntradaVeiTerEditar.setChecked(False)

        self.ui.cheBoxEntrdaFuncionarioAtivar.setChecked(False)
        self.ui.cheBoxEntrdaFuncionarioCadastro.setChecked(False)
        self.ui.cheBoxEntrdaFuncionarioCancelar.setChecked(False)
        self.ui.cheBoxEntrdaFuncionarioDeletar.setChecked(False)
        self.ui.cheBoxEntrdaFuncionarioEditar.setChecked(False)

        self.ui.cheBoxEntrdaMaquinaAtivar.setChecked(False)
        self.ui.cheBoxEntrdaMaquinaCadastro.setChecked(False)
        self.ui.cheBoxEntrdaMaquinaCancelar.setChecked(False)
        self.ui.cheBoxEntrdaMaquinaDeletar.setChecked(False)
        self.ui.cheBoxEntrdaMaquinaEditar.setChecked(False)

        self.ui.cheBoxGraficosAtivar.setChecked(False)
        self.ui.cheBoxGraficosGerar.setChecked(False)
        self.ui.cheBoxGraficosImprimir.setChecked(False)
        self.ui.cheBoxGraficosVisualizar.setChecked(False)

        self.ui.cheBoxRelacaoAtivar.setChecked(False)
        self.ui.cheBoxRelacaoCadastrar.setChecked(False)
        self.ui.cheBoxRelacaoDeletar.setChecked(False)
        self.ui.cheBoxRelacaoEditar.setChecked(False)
        self.ui.cheBoxRelacaooCancelar.setChecked(False)

        self.ui.cheBoxRelatorioAtivar.setChecked(False)
        self.ui.cheBoxRelatorioGerar.setChecked(False)
        self.ui.cheBoxRelatorioImprimir.setChecked(False)
        self.ui.cheBoxRelatorioVisualizar.setChecked(False)

        self.ui.cheBoxSaidaCamEmpAtivar.setChecked(False)
        self.ui.cheBoxSaidaCamEmpCadastro.setChecked(False)
        self.ui.cheBoxSaidaCamEmpCancelar.setChecked(False)
        self.ui.cheBoxSaidaCamEmpDeletar.setChecked(False)
        self.ui.cheBoxSaidaCamEmpEditar.setChecked(False)

        self.ui.cheBoxSaidaCamTerAtivar.setChecked(False)
        self.ui.cheBoxSaidaCamTerCadastro.setChecked(False)
        self.ui.cheBoxSaidaCamTerCancelar.setChecked(False)
        self.ui.cheBoxSaidaCamTerDeletar.setChecked(False)
        self.ui.cheBoxSaidaCamTerEditar.setChecked(False)

        self.ui.cheBoxSaidaFuncionarioAtivar.setChecked(False)
        self.ui.cheBoxSaidaFuncionarioCadastro.setChecked(False)
        self.ui.cheBoxSaidaFuncionarioCancelar.setChecked(False)
        self.ui.cheBoxSaidaFuncionarioDeletar.setChecked(False)
        self.ui.cheBoxSaidaFuncionarioEditar.setChecked(False)

        self.ui.cheBoxSaidaMaquinaAtivar.setChecked(False)
        self.ui.cheBoxSaidaMaquinaCadastro.setChecked(False)
        self.ui.cheBoxSaidaMaquinaCancelar.setChecked(False)
        self.ui.cheBoxSaidaMaquinaDeletar.setChecked(False)
        self.ui.cheBoxSaidaMaquinaEditar.setChecked(False)

        self.ui.cheBoxSaidaVeiculosCarregamentoAtivar.setChecked(False)
        self.ui.cheBoxSaidaVeiculosCarregamentoCadastro.setChecked(False)
        self.ui.cheBoxSaidaVeiculosCarregamentoCancelar.setChecked(False)
        self.ui.cheBoxSaidaVeiculosCarregamentoDeletar.setChecked(False)
        self.ui.cheBoxSaidaVeiculosCarregamentoEditar.setChecked(False)

        self.ui.cheBoxSaidaVeiculosDescarregamentoAtivar.setChecked(False)
        self.ui.cheBoxSaidaVeiculosDescarregamentoCadastro.setChecked(False)
        self.ui.cheBoxSaidaVeiculosDescarregamentoCancelar.setChecked(False)
        self.ui.cheBoxSaidaVeiculosDescarregamentoDeletar.setChecked(False)
        self.ui.cheBoxSaidaVeiculosDescarregamentoEditar.setChecked(False)

        self.ui.cheBoxSaidaVeiEmpAtivar.setChecked(False)
        self.ui.cheBoxSaidaVeiEmpCadastro.setChecked(False)
        self.ui.cheBoxSaidaVeiEmpCancelar.setChecked(False)
        self.ui.cheBoxSaidaVeiEmpDeletar.setChecked(False)
        self.ui.cheBoxSaidaVeiEmpEditar.setChecked(False)

        self.ui.cheBoxSaidaVeiTerAtivar.setChecked(False)
        self.ui.cheBoxSaidaVeiTerCadastro.setChecked(False)
        self.ui.cheBoxSaidaVeiTerCancelar.setChecked(False)
        self.ui.cheBoxSaidaVeiTerDeletar.setChecked(False)
        self.ui.cheBoxSaidaVeiTerEditar.setChecked(False)


    def cancelarPermissao(self):
        result = QMessageBox.question(QWidget(), 'Menssagem', "Deseja realmente cancelar a operação",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            self.desativarPesquisaPermissao()
            self.limparCamposPermicao()
            self.deletarTabelaPermissao()
            self.limparCamposCheckBox()
            self.ui.stackedWidget.setEnabled(False)

    def limparCamposUsuario(self):
        self.ui.txtNomeFuncionarioUsuario.clear()
        self.ui.txtidFuncionario.clear()
        self.ui.txtNomeFuncionario.clear()
        self.ui.txtCargo.clear()
        self.ui.txtSetor.clear()
        self.ui.txtLoginFuncionario.clear()
        self.ui.txtSenhaFuncionario.clear()

    def cancelarUsuario(self):
        result = QMessageBox.question(QWidget(), 'Menssagem', "Deseja realmente cancelar a operação", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            self.desativarPesquisaUsuario()
            self.limparCamposUsuario()
            self.deletarTabelaUsuario()

    def pesquisarFuncionario(self):
        usu = UsuarioDao()
        if self.ui.radBtnCodigoFun.isChecked():
            result = usu.pesquisarFuncionarioCod(self.ui.txtNomeFuncionarioUsuario.text())
            self.tabUsuario(result)
        elif self.ui.radBtnNomeFun.isChecked():
            result = usu.pesquisarFuncionarioNome(self.ui.txtNomeFuncionarioUsuario.text())
            self.tabUsuario(result)
        elif self.ui.radBtnCpf.isChecked():
            result = usu.pesquisarFuncionarioCpf(self.ui.txtNomeFuncionarioUsuario.text())
            self.tabUsuario(result)
        else:
            QMessageBox.warning(self, 'ATENÇÃO', "Selecione o dados de pesquisa desejado para realiza e pesquisa!")


    def tabUsuario(self, _pesquisar):
        qtde_registros = len(_pesquisar)
        self.ui.tabFuncioariosUsuario.setRowCount(qtde_registros)

        linha = 0
        for pesqui in _pesquisar:
            # capturando os dados da tupla

            codigo = pesqui[0]
            nome = pesqui[1]
            setor = pesqui[2]
            cargo = pesqui[3]
            login = pesqui[4]
            senha = pesqui[5]

            # preenchendo o grid de pesquisa
            self.ui.tabFuncioariosUsuario.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
            self.ui.tabFuncioariosUsuario.setItem(linha, 1, QtGui.QTableWidgetItem(str(nome)))
            self.ui.tabFuncioariosUsuario.setItem(linha, 2, QtGui.QTableWidgetItem(str(setor)))
            self.ui.tabFuncioariosUsuario.setItem(linha, 3, QtGui.QTableWidgetItem(str(cargo)))
            self.ui.tabFuncioariosUsuario.setItem(linha, 4, QtGui.QTableWidgetItem(str(login)))
            self.ui.tabFuncioariosUsuario.setItem(linha, 5, QtGui.QTableWidgetItem(str(senha)))

    def setarCamposUsuario(self):

        itens = []
        for item in self.ui.tabFuncioariosUsuario.selectedItems():
            itens.append(item.text())
        if len(itens) == 6:
            self.ui.txtidFuncionario.setText(str(itens[0]))
            self.ui.txtNomeFuncionario.setText(str(itens[1]))
            self.ui.txtSetor.setText(str(itens[2]))
            self.ui.txtCargo.setText(str(itens[3]))

    def setarUsuario(self):
        if self.ui.txtidFuncionario.text() == "" and self.ui.txtNomeFuncionario.text() == "" and self.ui.txtCargo.text() == "" and self.ui.txtSetor.text() == "" and self.ui.txtLoginFuncionario.text() == "" and self.ui.txtSenhaFuncionario.text() == "":
            self.setarCamposUsuario()

    def deletarTabelaUsuario(self):
        for i in reversed(range(self.ui.tabFuncioariosUsuario.rowCount())):
            self.ui.tabFuncioariosUsuario.removeRow(i)

    def pesquisarUsuario(self):
        usu = UsuarioDao()
        if self.ui.radBtnCodigoUsuario.isChecked():
            result = usu.pesquisarUsuarioCod(self.ui.txtNomeFuncionarioPermissoes.text())
            self.tabPermissao(result)
        elif self.ui.radBtnUsuario.isChecked():
            result = usu.pesquisarUsuarioNome(self.ui.txtNomeFuncionarioPermissoes.text())
            self.tabPermissao(result)
        elif self.ui.radBtnNomeFunPer.isChecked():
            result = usu.pesquisarUsuarioNomeFun(self.ui.txtNomeFuncionarioPermissoes.text())
            self.tabPermissao(result)
        else:
            QMessageBox.warning(self, 'ATENÇÃO', "Selecione o dados de pesquisa desejado para realiza e pesquisa!")

    def tabPermissao(self, _pesquisar):
        qtde_registros = len(_pesquisar)
        self.ui.tabFuncioariosPermissoes.setRowCount(qtde_registros)

        linha = 0
        for pesqui in _pesquisar:
            # capturando os dados da tupla

            codigo = pesqui[0]
            usuario = pesqui[1]
            nome = pesqui[2]
            setor = pesqui[3]
            cargo = pesqui[4]

            # preenchendo o grid de pesquisa
            self.ui.tabFuncioariosPermissoes.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
            self.ui.tabFuncioariosPermissoes.setItem(linha, 1, QtGui.QTableWidgetItem(str(usuario)))
            self.ui.tabFuncioariosPermissoes.setItem(linha, 2, QtGui.QTableWidgetItem(str(nome)))
            self.ui.tabFuncioariosPermissoes.setItem(linha, 3, QtGui.QTableWidgetItem(str(setor)))
            self.ui.tabFuncioariosPermissoes.setItem(linha, 4, QtGui.QTableWidgetItem(str(cargo)))

    def setarCamposPermissao(self):

        itens = []
        for item in self.ui.tabFuncioariosPermissoes.selectedItems():
            itens.append(item.text())
        if len(itens) == 5:
            self.ui.txtIdUsuario.setText(str(itens[0]))
            self.ui.txtNomeUsuario.setText(str(itens[1]))
            self.ui.txtNomFuncionarioPerm.setText(str(itens[2]))

    def setarPermissao(self):
        if self.ui.txtIdUsuario.text() == "" and self.ui.txtNomeUsuario.text() == "" and self.ui.txtNomFuncionarioPerm.text() == "":
            self.setarCamposPermissao()
            self.ui.stackedWidget.setEnabled(True)

    def deletarTabelaPermissao(self):
        for i in reversed(range(self.ui.tabFuncioariosPermissoes.rowCount())):
            self.ui.tabFuncioariosPermissoes.removeRow(i)