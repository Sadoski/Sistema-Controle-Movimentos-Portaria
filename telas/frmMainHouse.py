# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmMainHouse.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui
from imagens import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_frmMainHouse(object):
    def setupUi(self, frmMainHouse):
        frmMainHouse.setObjectName(_fromUtf8("frmMainHouse"))
        frmMainHouse.setWindowModality(QtCore.Qt.WindowModal)
        frmMainHouse.resize(1016, 703)
        frmMainHouse.setMinimumSize(QtCore.QSize(1016, 703))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(10)
        frmMainHouse.setFont(font)

        self.centralwidget = QtGui.QWidget(frmMainHouse)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lblControlePortaria = QtGui.QLabel(self.centralwidget)
        self.lblControlePortaria.setGeometry(QtCore.QRect(130, 6, 727, 58))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.lblControlePortaria.setFont(font)
        self.lblControlePortaria.setObjectName(_fromUtf8("lblControlePortaria"))

        self.lblImagem = QtGui.QLabel(self.centralwidget)
        self.lblImagem.setGeometry(QtCore.QRect(10, 110, 1000, 521))
        self.lblImagem.setText(_fromUtf8(""))
        self.lblImagem.setPixmap(QtGui.QPixmap(_fromUtf8(".\imagens\controle movimentos portaria.png")))
        self.lblImagem.setObjectName(_fromUtf8("lblImagem"))

        #frmMainHouse.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(frmMainHouse)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1016, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))

        self.menuSistema = QtGui.QMenu(self.menubar)
        self.menuSistema.setObjectName(_fromUtf8("menuSistema"))

        self.menuCadastros = QtGui.QMenu(self.menubar)
        self.menuCadastros.setObjectName(_fromUtf8("menuCadastros"))

        self.menuConsultas = QtGui.QMenu(self.menubar)
        self.menuConsultas.setObjectName(_fromUtf8("menuConsultas"))

        self.subMenuConsultasEntradasSaidas = QtGui.QMenu(self.menuConsultas)
        self.subMenuConsultasEntradasSaidas.setObjectName(_fromUtf8("subMenuConsultasEntradasSaidas"))

        self.consEntSaidSubMenuCarregamento = QtGui.QMenu(self.subMenuConsultasEntradasSaidas)
        self.consEntSaidSubMenuCarregamento.setObjectName(_fromUtf8("consEntSaidSubMenuCarregamento"))

        self.consEntSaidSubMenuDescarregamento = QtGui.QMenu(self.subMenuConsultasEntradasSaidas)
        self.consEntSaidSubMenuDescarregamento.setObjectName(_fromUtf8("consEntSaidSubMenuDescarregamento"))

        self.consEntSaidSubMenuVeiculosLeves = QtGui.QMenu(self.subMenuConsultasEntradasSaidas)
        self.consEntSaidSubMenuVeiculosLeves.setObjectName(_fromUtf8("consEntSaidSubMenuVeiculosLeves"))

        self.consEntSaidSubMenuCaminhoes = QtGui.QMenu(self.subMenuConsultasEntradasSaidas)
        self.consEntSaidSubMenuCaminhoes.setObjectName(_fromUtf8("consEntSaidSubMenuCaminhoes"))

        self.menuMovimentoPortaria = QtGui.QMenu(self.menubar)
        self.menuMovimentoPortaria.setObjectName(_fromUtf8("menuMovimentoPortaria"))

        self.subMenuDescarregamento = QtGui.QMenu(self.menuMovimentoPortaria)
        self.subMenuDescarregamento.setObjectName(_fromUtf8("subMenuDescarregamento"))

        self.menuDescaTECA = QtGui.QMenu(self.subMenuDescarregamento)
        self.menuDescaTECA.setObjectName(_fromUtf8("menuDescaTECA"))
        self.menuDescaCavacoPoSerragem = QtGui.QMenu(self.subMenuDescarregamento)
        self.menuDescaCavacoPoSerragem.setObjectName(_fromUtf8("menuDescaCavacoPoSerragem"))

        self.menuOutros = QtGui.QMenu(self.subMenuDescarregamento)
        self.menuOutros.setObjectName(_fromUtf8("menuOutros"))

        self.subMenuCarregamentos = QtGui.QMenu(self.menuMovimentoPortaria)
        self.subMenuCarregamentos.setObjectName(_fromUtf8("subMenuCarregamentos"))

        self.menuCarregMadeira = QtGui.QMenu(self.subMenuCarregamentos)
        self.menuCarregMadeira.setObjectName(_fromUtf8("menuCarregMadeira"))

        self.menuCarregCavacoPoSerragem = QtGui.QMenu(self.subMenuCarregamentos)
        self.menuCarregCavacoPoSerragem.setObjectName(_fromUtf8("menuCarregCavacoPoSerragem"))

        self.submMenuEntradaSaidaVeiculosLeves = QtGui.QMenu(self.menuMovimentoPortaria)
        self.submMenuEntradaSaidaVeiculosLeves.setObjectName(_fromUtf8("submMenuEntradaSaidaVeiculosLeves"))

        self.entSaiVeicLevSubMenuVeiculosEmpresa = QtGui.QMenu(self.submMenuEntradaSaidaVeiculosLeves)
        self.entSaiVeicLevSubMenuVeiculosEmpresa.setObjectName(_fromUtf8("entSaiVeicLevSubMenuVeiculosEmpresa"))

        self.entSaiVeicLevSubmenuVeiculosTerceiros = QtGui.QMenu(self.submMenuEntradaSaidaVeiculosLeves)
        self.entSaiVeicLevSubmenuVeiculosTerceiros.setObjectName(_fromUtf8("entSaiVeicLevSubmenuVeiculosTerceiros"))

        self.subMenuEntradaSaidaCaminhoes = QtGui.QMenu(self.menuMovimentoPortaria)
        self.subMenuEntradaSaidaCaminhoes.setObjectName(_fromUtf8("subMenuEntradaSaidaCaminhoes"))

        self.entSaiCamiSubMenuCaminhoesEmpresa = QtGui.QMenu(self.subMenuEntradaSaidaCaminhoes)
        self.entSaiCamiSubMenuCaminhoesEmpresa.setObjectName(_fromUtf8("entSaiCamiSubMenuCaminhoesEmpresa"))

        self.entSaiCamiSubMenuCaminhoesTerceiros = QtGui.QMenu(self.subMenuEntradaSaidaCaminhoes)
        self.entSaiCamiSubMenuCaminhoesTerceiros.setObjectName(_fromUtf8("entSaiCamiSubMenuCaminhoesTerceiros"))

        self.subMenuEntradaSaidaMaquinas = QtGui.QMenu(self.menuMovimentoPortaria)
        self.subMenuEntradaSaidaMaquinas.setObjectName(_fromUtf8("subMenuEntradaSaidaMaquinas"))

        self.subMenuEntradaSaidaFuncionario = QtGui.QMenu(self.menuMovimentoPortaria)
        self.subMenuEntradaSaidaFuncionario.setObjectName(_fromUtf8("subMenuEntradaSaidaFuncionario"))

        self.menuRelatorios = QtGui.QMenu(self.menubar)
        self.menuRelatorios.setObjectName(_fromUtf8("menuRelatorios"))

        self.menuAjuda = QtGui.QMenu(self.menubar)
        self.menuAjuda.setObjectName(_fromUtf8("menuAjuda"))

        frmMainHouse.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(frmMainHouse)
        self.statusbar.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        self.statusbar.setFont(font)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))

        frmMainHouse.setStatusBar(self.statusbar)
        self.subMenuCadastroEmpresa = QtGui.QAction(frmMainHouse)
        #self.subMenuCadastroEmpresa.setEnabled(False)
        self.subMenuCadastroEmpresa.setObjectName(_fromUtf8("subMenuCadastroEmpresa"))

        self.subMenuCadastroFuncionarios = QtGui.QAction(frmMainHouse)
        self.subMenuCadastroFuncionarios.setObjectName(_fromUtf8("subMenuCadastroFuncionarios"))

        self.subMenuCadastroFornecedor = QtGui.QAction(frmMainHouse)
        self.subMenuCadastroFornecedor.setObjectName(_fromUtf8("subMenuCadastroFornecedor"))

        self.subMenuCadastroClintes = QtGui.QAction(frmMainHouse)
        self.subMenuCadastroClintes.setObjectName(_fromUtf8("subMenuCadastroClintes"))

        self.veicEmpSubMenuEntrada = QtGui.QAction(frmMainHouse)
        self.veicEmpSubMenuEntrada.setObjectName(_fromUtf8("veicEmpSubMenuEntrada"))

        self.veicEmpSaida = QtGui.QAction(frmMainHouse)
        self.veicEmpSaida.setObjectName(_fromUtf8("veicEmpSaida"))

        self.veiTerSubMenuEntrada = QtGui.QAction(frmMainHouse)
        self.veiTerSubMenuEntrada.setObjectName(_fromUtf8("veiTerSubMenuEntrada"))

        self.veicTerSubMenuSaida = QtGui.QAction(frmMainHouse)
        self.veicTerSubMenuSaida.setObjectName(_fromUtf8("veicTerSubMenuSaida"))

        self.camiEmpSubMenuEntrada = QtGui.QAction(frmMainHouse)
        self.camiEmpSubMenuEntrada.setObjectName(_fromUtf8("camiEmpSubMenuEntrada"))

        self.camiEmpSubMenuSaida = QtGui.QAction(frmMainHouse)
        self.camiEmpSubMenuSaida.setObjectName(_fromUtf8("camiEmpSubMenuSaida"))

        self.camiTerSubMenuEntrada = QtGui.QAction(frmMainHouse)
        self.camiTerSubMenuEntrada.setObjectName(_fromUtf8("camiTerSubMenuEntrada"))

        self.camiTerSubMenuSaida = QtGui.QAction(frmMainHouse)
        self.camiTerSubMenuSaida.setObjectName(_fromUtf8("camiTerSubMenuSaida"))

        self.entSadMaquiSubMenuEntrada = QtGui.QAction(frmMainHouse)
        self.entSadMaquiSubMenuEntrada.setObjectName(_fromUtf8("entSadMaquiSubMenuEntrada"))

        self.entSadMaquiSubMenuSaida = QtGui.QAction(frmMainHouse)
        self.entSadMaquiSubMenuSaida.setObjectName(_fromUtf8("entSadMaquiSubMenuSaida"))

        self.menuSair = QtGui.QAction(frmMainHouse)
        self.menuSair.setObjectName(_fromUtf8("menuSair"))

        self.subMenuSobre = QtGui.QAction(frmMainHouse)
        self.subMenuSobre.setObjectName(_fromUtf8("subMenuSobre"))

        self.subMenuRelatorios = QtGui.QAction(frmMainHouse)
        self.subMenuRelatorios.setEnabled(False)
        self.subMenuRelatorios.setObjectName(_fromUtf8("subMenuRelatorios"))

        self.subMenuGraficos = QtGui.QAction(frmMainHouse)
        self.subMenuGraficos.setEnabled(False)
        self.subMenuGraficos.setObjectName(_fromUtf8("subMenuGraficos"))

        self.subMenuConsultasEmpresas = QtGui.QAction(frmMainHouse)
        self.subMenuConsultasEmpresas.setEnabled(True)
        self.subMenuConsultasEmpresas.setObjectName(_fromUtf8("subMenuConsultasEmpresas"))

        self.subMenuConsultasFornecedores = QtGui.QAction(frmMainHouse)
        self.subMenuConsultasFornecedores.setObjectName(_fromUtf8("subMenuConsultasFornecedores"))

        self.subMenuConsultasFuncionarios = QtGui.QAction(frmMainHouse)
        self.subMenuConsultasFuncionarios.setObjectName(_fromUtf8("subMenuConsultasFuncionarios"))

        self.subMenuConsultasClientes = QtGui.QAction(frmMainHouse)
        self.subMenuConsultasClientes.setObjectName(_fromUtf8("subMenuConsultasClientes"))

        self.subMenuConsultasMotoristas = QtGui.QAction(frmMainHouse)
        self.subMenuConsultasMotoristas.setObjectName(_fromUtf8("subMenuConsultasMotoristas"))

        self.subMenuCadastroMotoristas = QtGui.QAction(frmMainHouse)
        self.subMenuCadastroMotoristas.setObjectName(_fromUtf8("subMenuCadastroMotoristas"))

        self.subMenuEntradaNotasTeca = QtGui.QAction(frmMainHouse)
        self.subMenuEntradaNotasTeca.setObjectName(_fromUtf8("subMenuEntradaNotasTeca"))

        self.subMenuConsultasNotas = QtGui.QAction(frmMainHouse)
        self.subMenuConsultasNotas.setObjectName(_fromUtf8("subMenuConsultasNotas"))

        self.entSaiFuncSubMenuEntrada = QtGui.QAction(frmMainHouse)
        self.entSaiFuncSubMenuEntrada.setObjectName(_fromUtf8("entSaiFuncSubMenuEntrada"))

        self.entSaiFuncSubMenuSaida = QtGui.QAction(frmMainHouse)
        self.entSaiFuncSubMenuSaida.setObjectName(_fromUtf8("entSaiFuncSubMenuSaida"))

        self.consEntSaidSubMenuMaquinas = QtGui.QAction(frmMainHouse)
        self.consEntSaidSubMenuMaquinas.setObjectName(_fromUtf8("consEntSaidSubMenuMaquinas"))

        self.carreConsSubMenuMadeira = QtGui.QAction(frmMainHouse)
        self.carreConsSubMenuMadeira.setObjectName(_fromUtf8("carreConsSubMenuMadeira"))

        self.carreConsSubMenuCavacoSerragem = QtGui.QAction(frmMainHouse)
        self.carreConsSubMenuCavacoSerragem.setObjectName(_fromUtf8("carreConsSubMenuCavacoSerragem"))

        self.descaConsSubMenuTeca = QtGui.QAction(frmMainHouse)
        self.descaConsSubMenuTeca.setObjectName(_fromUtf8("descaConsSubMenuTeca"))

        self.descaConsSubMenuCavacoSerragem = QtGui.QAction(frmMainHouse)
        self.descaConsSubMenuCavacoSerragem.setObjectName(_fromUtf8("descaConsSubMenuCavacoSerragem"))

        self.descaConsSubMenuOutros = QtGui.QAction(frmMainHouse)
        self.descaConsSubMenuOutros.setObjectName(_fromUtf8("descaConsSubMenuOutros"))

        self.veiLevConsSubMenuEmpresa = QtGui.QAction(frmMainHouse)
        self.veiLevConsSubMenuEmpresa.setObjectName(_fromUtf8("veiLevConsSubMenuEmpresa"))

        self.veiLevConsSubMenuTerceiros = QtGui.QAction(frmMainHouse)
        self.veiLevConsSubMenuTerceiros.setObjectName(_fromUtf8("veiLevConsSubMenuTerceiros"))

        self.camiConsSubMenuEmpresa = QtGui.QAction(frmMainHouse)
        self.camiConsSubMenuEmpresa.setObjectName(_fromUtf8("camiConsSubMenuEmpresa"))

        self.camiConsSubMenuTerceiros = QtGui.QAction(frmMainHouse)
        self.camiConsSubMenuTerceiros.setObjectName(_fromUtf8("camiConsSubMenuTerceiros"))

        self.consEntSaidSubMenuFuncionarios = QtGui.QAction(frmMainHouse)
        self.consEntSaidSubMenuFuncionarios.setObjectName(_fromUtf8("consEntSaidSubMenuFuncionarios"))

        self.consEntSaidSubMenuNotas = QtGui.QAction(frmMainHouse)
        self.consEntSaidSubMenuNotas.setObjectName(_fromUtf8("consEntSaidSubMenuNotas"))

        self.carreMadeiraEntrada = QtGui.QAction(frmMainHouse)
        self.carreMadeiraEntrada.setObjectName(_fromUtf8("carreMadeiraEntrada"))

        self.carreMadeiraSaida = QtGui.QAction(frmMainHouse)
        self.carreMadeiraSaida.setObjectName(_fromUtf8("carreMadeiraSaida"))

        self.carreCavacoPoSerragemEntrada = QtGui.QAction(frmMainHouse)
        self.carreCavacoPoSerragemEntrada.setObjectName(_fromUtf8("carreCavacoPoSerragemEntrada"))

        self.carreCavacoPoSerragemSaida = QtGui.QAction(frmMainHouse)
        self.carreCavacoPoSerragemSaida.setObjectName(_fromUtf8("carreCavacoPoSerragemSaida"))

        self.descTecaEntrada = QtGui.QAction(frmMainHouse)
        self.descTecaEntrada.setObjectName(_fromUtf8("descTecaEntrada"))

        self.descTecaSaida = QtGui.QAction(frmMainHouse)
        self.descTecaSaida.setObjectName(_fromUtf8("descTecaSaida"))

        self.descCavacoPoSerragemEntrada = QtGui.QAction(frmMainHouse)
        self.descCavacoPoSerragemEntrada.setObjectName(_fromUtf8("descCavacoPoSerragemEntrada"))

        self.descCavacoPoSerragemSaida = QtGui.QAction(frmMainHouse)
        self.descCavacoPoSerragemSaida.setObjectName(_fromUtf8("descCavacoPoSerragemSaida"))

        self.menuDescaOutrEntrada = QtGui.QAction(frmMainHouse)
        self.menuDescaOutrEntrada.setObjectName(_fromUtf8("menuDescaOutrEntrada"))

        self.menuDescaOutrSaida = QtGui.QAction(frmMainHouse)
        self.menuDescaOutrSaida.setObjectName(_fromUtf8("menuDescaOutrSaida"))

        self.menuSistema.addAction(self.menuSair)
        self.menuCadastros.addAction(self.subMenuCadastroEmpresa)
        self.menuCadastros.addAction(self.subMenuCadastroFuncionarios)
        self.menuCadastros.addAction(self.subMenuCadastroFornecedor)
        self.menuCadastros.addAction(self.subMenuCadastroClintes)
        self.menuCadastros.addAction(self.subMenuCadastroMotoristas)
        self.menuCadastros.addSeparator()
        self.menuCadastros.addAction(self.subMenuEntradaNotasTeca)
        self.consEntSaidSubMenuCarregamento.addAction(self.carreConsSubMenuMadeira)
        self.consEntSaidSubMenuCarregamento.addAction(self.carreConsSubMenuCavacoSerragem)
        self.consEntSaidSubMenuDescarregamento.addAction(self.descaConsSubMenuTeca)
        self.consEntSaidSubMenuDescarregamento.addAction(self.descaConsSubMenuCavacoSerragem)
        self.consEntSaidSubMenuDescarregamento.addAction(self.descaConsSubMenuOutros)
        self.consEntSaidSubMenuVeiculosLeves.addAction(self.veiLevConsSubMenuEmpresa)
        self.consEntSaidSubMenuVeiculosLeves.addAction(self.veiLevConsSubMenuTerceiros)
        self.consEntSaidSubMenuCaminhoes.addAction(self.camiConsSubMenuEmpresa)
        self.consEntSaidSubMenuCaminhoes.addAction(self.camiConsSubMenuTerceiros)
        self.subMenuConsultasEntradasSaidas.addAction(self.consEntSaidSubMenuCarregamento.menuAction())
        self.subMenuConsultasEntradasSaidas.addAction(self.consEntSaidSubMenuDescarregamento.menuAction())
        self.subMenuConsultasEntradasSaidas.addAction(self.consEntSaidSubMenuVeiculosLeves.menuAction())
        self.subMenuConsultasEntradasSaidas.addAction(self.consEntSaidSubMenuCaminhoes.menuAction())
        self.subMenuConsultasEntradasSaidas.addAction(self.consEntSaidSubMenuMaquinas)
        self.subMenuConsultasEntradasSaidas.addSeparator()
        self.subMenuConsultasEntradasSaidas.addAction(self.consEntSaidSubMenuNotas)
        self.subMenuConsultasEntradasSaidas.addAction(self.consEntSaidSubMenuFuncionarios)
        self.menuConsultas.addAction(self.subMenuConsultasEmpresas)
        self.menuConsultas.addAction(self.subMenuConsultasFuncionarios)
        self.menuConsultas.addAction(self.subMenuConsultasFornecedores)
        self.menuConsultas.addAction(self.subMenuConsultasClientes)
        self.menuConsultas.addAction(self.subMenuConsultasMotoristas)
        self.menuConsultas.addSeparator()
        self.menuConsultas.addAction(self.subMenuConsultasNotas)
        self.menuConsultas.addSeparator()
        self.menuConsultas.addAction(self.subMenuConsultasEntradasSaidas.menuAction())
        self.menuDescaTECA.addAction(self.descTecaEntrada)
        self.menuDescaTECA.addAction(self.descTecaSaida)
        self.menuDescaCavacoPoSerragem.addAction(self.descCavacoPoSerragemEntrada)
        self.menuDescaCavacoPoSerragem.addAction(self.descCavacoPoSerragemSaida)
        self.menuOutros.addAction(self.menuDescaOutrEntrada)
        self.menuOutros.addAction(self.menuDescaOutrSaida)
        self.subMenuDescarregamento.addAction(self.menuDescaTECA.menuAction())
        self.subMenuDescarregamento.addAction(self.menuDescaCavacoPoSerragem.menuAction())
        self.subMenuDescarregamento.addAction(self.menuOutros.menuAction())
        self.menuCarregMadeira.addAction(self.carreMadeiraEntrada)
        self.menuCarregMadeira.addAction(self.carreMadeiraSaida)
        self.menuCarregCavacoPoSerragem.addAction(self.carreCavacoPoSerragemEntrada)
        self.menuCarregCavacoPoSerragem.addAction(self.carreCavacoPoSerragemSaida)
        self.subMenuCarregamentos.addAction(self.menuCarregMadeira.menuAction())
        self.subMenuCarregamentos.addAction(self.menuCarregCavacoPoSerragem.menuAction())
        self.entSaiVeicLevSubMenuVeiculosEmpresa.addAction(self.veicEmpSubMenuEntrada)
        self.entSaiVeicLevSubMenuVeiculosEmpresa.addAction(self.veicEmpSaida)
        self.entSaiVeicLevSubmenuVeiculosTerceiros.addAction(self.veiTerSubMenuEntrada)
        self.entSaiVeicLevSubmenuVeiculosTerceiros.addAction(self.veicTerSubMenuSaida)
        self.submMenuEntradaSaidaVeiculosLeves.addAction(self.entSaiVeicLevSubMenuVeiculosEmpresa.menuAction())
        self.submMenuEntradaSaidaVeiculosLeves.addAction(self.entSaiVeicLevSubmenuVeiculosTerceiros.menuAction())
        self.entSaiCamiSubMenuCaminhoesEmpresa.addAction(self.camiEmpSubMenuEntrada)
        self.entSaiCamiSubMenuCaminhoesEmpresa.addAction(self.camiEmpSubMenuSaida)
        self.entSaiCamiSubMenuCaminhoesTerceiros.addAction(self.camiTerSubMenuEntrada)
        self.entSaiCamiSubMenuCaminhoesTerceiros.addAction(self.camiTerSubMenuSaida)
        self.subMenuEntradaSaidaCaminhoes.addAction(self.entSaiCamiSubMenuCaminhoesEmpresa.menuAction())
        self.subMenuEntradaSaidaCaminhoes.addAction(self.entSaiCamiSubMenuCaminhoesTerceiros.menuAction())
        self.subMenuEntradaSaidaMaquinas.addAction(self.entSadMaquiSubMenuEntrada)
        self.subMenuEntradaSaidaMaquinas.addAction(self.entSadMaquiSubMenuSaida)
        self.subMenuEntradaSaidaFuncionario.addAction(self.entSaiFuncSubMenuEntrada)
        self.subMenuEntradaSaidaFuncionario.addAction(self.entSaiFuncSubMenuSaida)
        self.menuMovimentoPortaria.addAction(self.subMenuCarregamentos.menuAction())
        self.menuMovimentoPortaria.addAction(self.subMenuDescarregamento.menuAction())
        self.menuMovimentoPortaria.addAction(self.submMenuEntradaSaidaVeiculosLeves.menuAction())
        self.menuMovimentoPortaria.addAction(self.subMenuEntradaSaidaCaminhoes.menuAction())
        self.menuMovimentoPortaria.addAction(self.subMenuEntradaSaidaMaquinas.menuAction())
        self.menuMovimentoPortaria.addSeparator()
        self.menuMovimentoPortaria.addAction(self.subMenuEntradaSaidaFuncionario.menuAction())
        self.menuRelatorios.addAction(self.subMenuRelatorios)
        self.menuRelatorios.addAction(self.subMenuGraficos)
        self.menuAjuda.addAction(self.subMenuSobre)
        self.menubar.addAction(self.menuSistema.menuAction())
        self.menubar.addAction(self.menuCadastros.menuAction())
        self.menubar.addAction(self.menuConsultas.menuAction())
        self.menubar.addAction(self.menuMovimentoPortaria.menuAction())
        self.menubar.addAction(self.menuRelatorios.menuAction())
        self.menubar.addAction(self.menuAjuda.menuAction())

        self.retranslateUi(frmMainHouse)
        QtCore.QMetaObject.connectSlotsByName(frmMainHouse)

    def retranslateUi(self, frmMainHouse):
        frmMainHouse.setWindowTitle(_translate("frmMainHouse", "Sistema Controle Movimentos Portaria", None))
        frmMainHouse.setWhatsThis(_translate("frmMainHouse", "Tela Principal do Sistema Controle Portaria", None))
        self.lblControlePortaria.setText(_translate("frmMainHouse", "Controle Movimentos Portaria", None))
        self.menuSistema.setTitle(_translate("frmMainHouse", "Sistema", None))
        self.menuCadastros.setTitle(_translate("frmMainHouse", "Cadastros", None))
        self.menuConsultas.setTitle(_translate("frmMainHouse", "Consultas", None))
        self.subMenuConsultasEntradasSaidas.setTitle(_translate("frmMainHouse", "Entradas e Saidas", None))
        self.consEntSaidSubMenuCarregamento.setTitle(_translate("frmMainHouse", "Carregamento", None))
        self.consEntSaidSubMenuDescarregamento.setTitle(_translate("frmMainHouse", "Descarregamento", None))
        self.consEntSaidSubMenuVeiculosLeves.setTitle(_translate("frmMainHouse", "Veiculos Leves", None))
        self.consEntSaidSubMenuCaminhoes.setTitle(_translate("frmMainHouse", "Caminhões", None))
        self.menuMovimentoPortaria.setTitle(_translate("frmMainHouse", "Movimentos", None))
        self.subMenuDescarregamento.setTitle(_translate("frmMainHouse", "Descarregamento", None))
        self.menuDescaTECA.setTitle(_translate("frmMainHouse", "TECA", None))
        self.menuDescaCavacoPoSerragem.setTitle(_translate("frmMainHouse", "Cavaco / Pó Serragem", None))
        self.menuOutros.setTitle(_translate("frmMainHouse", "Outros", None))
        self.subMenuCarregamentos.setTitle(_translate("frmMainHouse", "Carregamentos", None))
        self.menuCarregMadeira.setTitle(_translate("frmMainHouse", "Madeira", None))
        self.menuCarregCavacoPoSerragem.setTitle(_translate("frmMainHouse", "Cavaco /Pó Serragem", None))
        self.submMenuEntradaSaidaVeiculosLeves.setTitle(_translate("frmMainHouse", "Entrada e Saida Veiculos Leves", None))
        self.entSaiVeicLevSubMenuVeiculosEmpresa.setTitle(_translate("frmMainHouse", "Veiculos Empresa", None))
        self.entSaiVeicLevSubmenuVeiculosTerceiros.setTitle(_translate("frmMainHouse", "Veiculos Terceiros", None))
        self.subMenuEntradaSaidaCaminhoes.setTitle(_translate("frmMainHouse", "Entrada e Saida Caminhões", None))
        self.entSaiCamiSubMenuCaminhoesEmpresa.setTitle(_translate("frmMainHouse", "Caminhão Empresa", None))
        self.entSaiCamiSubMenuCaminhoesTerceiros.setTitle(_translate("frmMainHouse", "Caminhão Terceiros", None))
        self.subMenuEntradaSaidaMaquinas.setTitle(_translate("frmMainHouse", "Entrada e Saida Maquinas", None))
        self.subMenuEntradaSaidaFuncionario.setTitle(_translate("frmMainHouse", "Entrada e Saida Funcionarios", None))
        self.menuRelatorios.setTitle(_translate("frmMainHouse", "Relatorios", None))
        self.menuAjuda.setTitle(_translate("frmMainHouse", "Ajuda", None))
        self.subMenuCadastroEmpresa.setText(_translate("frmMainHouse", "Empresa", None))
        self.subMenuCadastroFuncionarios.setText(_translate("frmMainHouse", "Funcionarios", None))
        self.subMenuCadastroFornecedor.setText(_translate("frmMainHouse", "Fornecedor", None))
        self.subMenuCadastroClintes.setText(_translate("frmMainHouse", "Clintes", None))
        self.veicEmpSubMenuEntrada.setText(_translate("frmMainHouse", "Entrada", None))
        self.veicEmpSaida.setText(_translate("frmMainHouse", "Saída", None))
        self.veiTerSubMenuEntrada.setText(_translate("frmMainHouse", "Entrada", None))
        self.veicTerSubMenuSaida.setText(_translate("frmMainHouse", "Saída", None))
        self.camiEmpSubMenuEntrada.setText(_translate("frmMainHouse", "Entrada", None))
        self.camiEmpSubMenuSaida.setText(_translate("frmMainHouse", "Saída", None))
        self.camiTerSubMenuEntrada.setText(_translate("frmMainHouse", "Entrada", None))
        self.camiTerSubMenuSaida.setText(_translate("frmMainHouse", "Saida", None))
        self.entSadMaquiSubMenuEntrada.setText(_translate("frmMainHouse", "Entrada", None))
        self.entSadMaquiSubMenuSaida.setText(_translate("frmMainHouse", "Saída", None))
        self.menuSair.setText(_translate("frmMainHouse", "Sair", None))
        self.subMenuSobre.setText(_translate("frmMainHouse", "Sobre", None))
        self.subMenuRelatorios.setText(_translate("frmMainHouse", "Relatorios", None))
        self.subMenuGraficos.setText(_translate("frmMainHouse", "Graficos", None))
        self.subMenuConsultasEmpresas.setText(_translate("frmMainHouse", "Empresas", None))
        self.subMenuConsultasFornecedores.setText(_translate("frmMainHouse", "Fornecedores", None))
        self.subMenuConsultasFuncionarios.setText(_translate("frmMainHouse", "Funcionarios", None))
        self.subMenuConsultasClientes.setText(_translate("frmMainHouse", "Clientes", None))
        self.subMenuConsultasMotoristas.setText(_translate("frmMainHouse", "Motoristas", None))
        self.subMenuCadastroMotoristas.setText(_translate("frmMainHouse", "Motoristas", None))
        self.subMenuEntradaNotasTeca.setText(_translate("frmMainHouse", "Entrada de Notas", None))
        self.subMenuConsultasNotas.setText(_translate("frmMainHouse", "Notas", None))
        self.entSaiFuncSubMenuEntrada.setText(_translate("frmMainHouse", "Entrada", None))
        self.entSaiFuncSubMenuSaida.setText(_translate("frmMainHouse", "Saída", None))
        self.consEntSaidSubMenuMaquinas.setText(_translate("frmMainHouse", "Maquinas", None))
        self.carreConsSubMenuMadeira.setText(_translate("frmMainHouse", "Madeira", None))
        self.carreConsSubMenuCavacoSerragem.setText(_translate("frmMainHouse", "Cavaco / Pó Serragem", None))
        self.descaConsSubMenuTeca.setText(_translate("frmMainHouse", "Teca", None))
        self.descaConsSubMenuCavacoSerragem.setText(_translate("frmMainHouse", "Cavaco / Pó Serragem", None))
        self.descaConsSubMenuOutros.setText(_translate("frmMainHouse", "Outros", None))
        self.veiLevConsSubMenuEmpresa.setText(_translate("frmMainHouse", "Empresa", None))
        self.veiLevConsSubMenuTerceiros.setText(_translate("frmMainHouse", "Terceiros", None))
        self.camiConsSubMenuEmpresa.setText(_translate("frmMainHouse", "Empresa", None))
        self.camiConsSubMenuTerceiros.setText(_translate("frmMainHouse", "Terceiros", None))
        self.consEntSaidSubMenuFuncionarios.setText(_translate("frmMainHouse", "Funcionarios", None))
        self.consEntSaidSubMenuNotas.setText(_translate("frmMainHouse", "Notas", None))
        self.carreMadeiraEntrada.setText(_translate("frmMainHouse", "Entrada", None))
        self.carreMadeiraSaida.setText(_translate("frmMainHouse", "Saída", None))
        self.carreCavacoPoSerragemEntrada.setText(_translate("frmMainHouse", "Entrada", None))
        self.carreCavacoPoSerragemSaida.setText(_translate("frmMainHouse", "Saída", None))
        self.descTecaEntrada.setText(_translate("frmMainHouse", "Entrada", None))
        self.descTecaSaida.setText(_translate("frmMainHouse", "Saída", None))
        self.descCavacoPoSerragemEntrada.setText(_translate("frmMainHouse", "Entrada", None))
        self.descCavacoPoSerragemSaida.setText(_translate("frmMainHouse", "Saída", None))
        self.menuDescaOutrEntrada.setText(_translate("frmMainHouse", "Entrada", None))
        self.menuDescaOutrSaida.setText(_translate("frmMainHouse", "Saída", None))

