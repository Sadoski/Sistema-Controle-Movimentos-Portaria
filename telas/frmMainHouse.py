# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmMainHouse.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/scmp.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmMainHouse.setWindowIcon(icon)
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
        self.lblImagem.setPixmap(QtGui.QPixmap(_fromUtf8("imagens/controlemovimentosportaria.png")))
        self.lblImagem.setObjectName(_fromUtf8("lblImagem"))

        frmMainHouse.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(frmMainHouse)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1016, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))

        self.menuSistema = QtGui.QMenu(self.menubar)
        self.menuSistema.setObjectName(_fromUtf8("menuSistema"))

        self.menuCadastros = QtGui.QMenu(self.menubar)
        self.menuCadastros.setObjectName(_fromUtf8("menuCadastros"))

        self.menuCadPesFisica = QtGui.QAction(frmMainHouse)
        self.menuCadPesFisica.setShortcut('Ctrl+F')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/pessoa_fisica.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuCadPesFisica.setIcon(icon)
        self.menuCadPesFisica.setObjectName(_fromUtf8("menuCadPesFisica"))

        self.menuCadPesJuridica = QtGui.QAction(frmMainHouse)
        self.menuCadPesJuridica.setShortcut('Ctrl+J')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/pessoa_juridica.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuCadPesJuridica.setIcon(icon)
        self.menuCadPesJuridica.setObjectName(_fromUtf8("menuCadPesJuridica"))

        self.menuCadUsuario = QtGui.QAction(frmMainHouse)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/tag_user_card.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuCadUsuario.setIcon(icon)
        self.menuCadUsuario.setObjectName(_fromUtf8("menuCadUsuario"))

        self.menuMovimentoPortaria = QtGui.QMenu(self.menubar)
        self.menuMovimentoPortaria.setObjectName(_fromUtf8("menuMovimentoPortaria"))

        self.subMenuDescarregamento = QtGui.QMenu(self.menuMovimentoPortaria)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/descarregamento.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.subMenuDescarregamento.setIcon(icon)
        self.subMenuDescarregamento.setObjectName(_fromUtf8("subMenuDescarregamento"))

        self.subMenuCarregamentos = QtGui.QMenu(self.menuMovimentoPortaria)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/carregamento.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.subMenuCarregamentos.setIcon(icon)
        self.subMenuCarregamentos.setObjectName(_fromUtf8("subMenuCarregamentos"))

        self.submMenuEntradaSaidaVeiculosLeves = QtGui.QMenu(self.menuMovimentoPortaria)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/carro.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.submMenuEntradaSaidaVeiculosLeves.setIcon(icon)
        self.submMenuEntradaSaidaVeiculosLeves.setObjectName(_fromUtf8("submMenuEntradaSaidaVeiculosLeves"))

        self.entSaiVeicLevSubMenuVeiculosEmpresa = QtGui.QMenu(self.submMenuEntradaSaidaVeiculosLeves)
        self.entSaiVeicLevSubMenuVeiculosEmpresa.setObjectName(_fromUtf8("entSaiVeicLevSubMenuVeiculosEmpresa"))

        self.entSaiVeicLevSubmenuVeiculosTerceiros = QtGui.QMenu(self.submMenuEntradaSaidaVeiculosLeves)
        self.entSaiVeicLevSubmenuVeiculosTerceiros.setObjectName(_fromUtf8("entSaiVeicLevSubmenuVeiculosTerceiros"))

        self.subMenuEntradaSaidaCaminhoes = QtGui.QMenu(self.menuMovimentoPortaria)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/caminhao.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.subMenuEntradaSaidaCaminhoes.setIcon(icon)
        self.subMenuEntradaSaidaCaminhoes.setObjectName(_fromUtf8("subMenuEntradaSaidaCaminhoes"))

        self.entSaiCamiSubMenuCaminhoesEmpresa = QtGui.QMenu(self.subMenuEntradaSaidaCaminhoes)
        self.entSaiCamiSubMenuCaminhoesEmpresa.setObjectName(_fromUtf8("entSaiCamiSubMenuCaminhoesEmpresa"))

        self.entSaiCamiSubMenuCaminhoesTerceiros = QtGui.QMenu(self.subMenuEntradaSaidaCaminhoes)
        self.entSaiCamiSubMenuCaminhoesTerceiros.setObjectName(_fromUtf8("entSaiCamiSubMenuCaminhoesTerceiros"))

        self.subMenuEntradaSaidaMaquinas = QtGui.QMenu(self.menuMovimentoPortaria)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/maquina.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.subMenuEntradaSaidaMaquinas.setIcon(icon)
        self.subMenuEntradaSaidaMaquinas.setObjectName(_fromUtf8("subMenuEntradaSaidaMaquinas"))

        self.subMenuEntradaSaidaFuncionario = QtGui.QMenu(self.menuMovimentoPortaria)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/funcionario-saida.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.subMenuEntradaSaidaFuncionario.setIcon(icon)
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
        self.subMenuCadastroEmpresa.setEnabled(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/company.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.subMenuCadastroEmpresa.setIcon(icon)
        self.subMenuCadastroEmpresa.setObjectName(_fromUtf8("subMenuCadastroEmpresa"))

        self.subMenuCadastroFuncionarios = QtGui.QAction(frmMainHouse)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/funcionario.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.subMenuCadastroFuncionarios.setIcon(icon)
        self.subMenuCadastroFuncionarios.setObjectName(_fromUtf8("subMenuCadastroFuncionarios"))

        self.subMenuCadastroFornecedor = QtGui.QAction(frmMainHouse)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/supplier.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.subMenuCadastroFornecedor.setIcon(icon)
        self.subMenuCadastroFornecedor.setObjectName(_fromUtf8("subMenuCadastroFornecedor"))

        self.subMenuCadastroClintes = QtGui.QAction(frmMainHouse)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/clientes.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.subMenuCadastroClintes.setIcon(icon)
        self.subMenuCadastroClintes.setObjectName(_fromUtf8("subMenuCadastroClintes"))

        self.veicEmpSubMenuEntrada = QtGui.QAction(frmMainHouse)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/seta-azul-direita.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.veicEmpSubMenuEntrada.setIcon(icon)
        self.veicEmpSubMenuEntrada.setObjectName(_fromUtf8("veicEmpSubMenuEntrada"))

        self.veicEmpSaida = QtGui.QAction(frmMainHouse)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/seta-vermelha-esquerda.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.veicEmpSaida.setIcon(icon)
        self.veicEmpSaida.setObjectName(_fromUtf8("veicEmpSaida"))

        self.veiTerSubMenuEntrada = QtGui.QAction(frmMainHouse)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/seta-azul-direita.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.veiTerSubMenuEntrada.setIcon(icon)
        self.veiTerSubMenuEntrada.setObjectName(_fromUtf8("veiTerSubMenuEntrada"))

        self.veicTerSubMenuSaida = QtGui.QAction(frmMainHouse)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/seta-vermelha-esquerda.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.veicTerSubMenuSaida.setIcon(icon)
        self.veicTerSubMenuSaida.setObjectName(_fromUtf8("veicTerSubMenuSaida"))

        self.camiEmpSubMenuEntrada = QtGui.QAction(frmMainHouse)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/seta-azul-direita.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.camiEmpSubMenuEntrada.setIcon(icon)
        self.camiEmpSubMenuEntrada.setObjectName(_fromUtf8("camiEmpSubMenuEntrada"))

        self.camiEmpSubMenuSaida = QtGui.QAction(frmMainHouse)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/seta-vermelha-esquerda.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.camiEmpSubMenuSaida.setIcon(icon)
        self.camiEmpSubMenuSaida.setObjectName(_fromUtf8("camiEmpSubMenuSaida"))

        self.camiTerSubMenuEntrada = QtGui.QAction(frmMainHouse)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/seta-azul-direita.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.camiTerSubMenuEntrada.setIcon(icon)
        self.camiTerSubMenuEntrada.setObjectName(_fromUtf8("camiTerSubMenuEntrada"))

        self.camiTerSubMenuSaida = QtGui.QAction(frmMainHouse)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/seta-vermelha-esquerda.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.camiTerSubMenuSaida.setIcon(icon)
        self.camiTerSubMenuSaida.setObjectName(_fromUtf8("camiTerSubMenuSaida"))

        self.entSadMaquiSubMenuEntrada = QtGui.QAction(frmMainHouse)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/seta-azul-direita.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.entSadMaquiSubMenuEntrada.setIcon(icon)
        self.entSadMaquiSubMenuEntrada.setObjectName(_fromUtf8("entSadMaquiSubMenuEntrada"))

        self.entSadMaquiSubMenuSaida = QtGui.QAction(frmMainHouse)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/seta-vermelha-esquerda.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.entSadMaquiSubMenuSaida.setIcon(icon)
        self.entSadMaquiSubMenuSaida.setObjectName(_fromUtf8("entSadMaquiSubMenuSaida"))

        self.menuSair = QtGui.QAction(frmMainHouse)
        self.menuSair.setShortcut('Ctrl+E')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/logout.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuSair.setIcon(icon)
        self.menuSair.setObjectName(_fromUtf8("menuSair"))

        self.subMenuSobre = QtGui.QAction(frmMainHouse)
        self.subMenuSobre.setShortcut('Ctrl+S')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/info-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.subMenuSobre.setIcon(icon)
        self.subMenuSobre.setObjectName(_fromUtf8("subMenuSobre"))

        self.subMenuRelatorios = QtGui.QAction(frmMainHouse)
        self.subMenuRelatorios.setShortcut('Ctrl+R')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/relatorio.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.subMenuRelatorios.setIcon(icon)
        self.subMenuRelatorios.setObjectName(_fromUtf8("subMenuRelatorios"))

        self.subMenuGraficos = QtGui.QAction(frmMainHouse)
        self.subMenuGraficos.setShortcut('Ctrl+G')
        self.subMenuGraficos.setEnabled(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/garfico_linha.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.subMenuGraficos.setIcon(icon)
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/motorista.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.subMenuCadastroMotoristas.setIcon(icon)
        self.subMenuCadastroMotoristas.setObjectName(_fromUtf8("subMenuCadastroMotoristas"))

        self.subMenuEntradaNotasTeca = QtGui.QAction(frmMainHouse)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/NF.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.subMenuEntradaNotasTeca.setIcon(icon)
        self.subMenuEntradaNotasTeca.setObjectName(_fromUtf8("subMenuEntradaNotasTeca"))

        self.subMenuConsultasNotas = QtGui.QAction(frmMainHouse)
        self.subMenuConsultasNotas.setObjectName(_fromUtf8("subMenuConsultasNotas"))

        self.entSaiFuncSubMenuEntrada = QtGui.QAction(frmMainHouse)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/seta-azul-direita.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.entSaiFuncSubMenuEntrada.setIcon(icon)
        self.entSaiFuncSubMenuEntrada.setObjectName(_fromUtf8("entSaiFuncSubMenuEntrada"))

        self.entSaiFuncSubMenuSaida = QtGui.QAction(frmMainHouse)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/seta-vermelha-esquerda.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.entSaiFuncSubMenuSaida.setIcon(icon)
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

        self.menuDescaEntrada = QtGui.QAction(frmMainHouse)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/seta-azul-direita.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuDescaEntrada.setIcon(icon)
        self.menuDescaEntrada.setObjectName(_fromUtf8("menuDescaEntrada"))

        self.menuDescaSaida = QtGui.QAction(frmMainHouse)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/seta-vermelha-esquerda.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuDescaSaida.setIcon(icon)
        self.menuDescaSaida.setObjectName(_fromUtf8("menuDescaSaida"))

        self.menuCarregEntrada = QtGui.QAction(frmMainHouse)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/seta-azul-direita.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuCarregEntrada.setIcon(icon)
        self.menuCarregEntrada.setObjectName(_fromUtf8("menuCarregEntrada"))

        self.menuCarregSaida = QtGui.QAction(frmMainHouse)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/seta-vermelha-esquerda.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuCarregSaida.setIcon(icon)
        self.menuCarregSaida.setObjectName(_fromUtf8("menuCarregSaida"))

        self.menuLogout = QtGui.QAction(frmMainHouse)
        self.menuLogout.setShortcut('Ctrl+T')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/peer_to_peer.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuLogout.setIcon(icon)
        self.menuLogout.setObjectName(_fromUtf8("menuLogout"))

        self.menuSistema.addAction(self.menuLogout)
        self.menuSistema.addSeparator()
        self.menuSistema.addAction(self.menuSair)
        self.menuCadastros.addAction(self.menuCadPesFisica)
        self.menuCadastros.addAction(self.menuCadPesJuridica)
        self.menuCadastros.addAction(self.subMenuCadastroEmpresa)
        self.menuCadastros.addAction(self.subMenuCadastroFuncionarios)
        self.menuCadastros.addAction(self.subMenuCadastroFornecedor)
        self.menuCadastros.addAction(self.subMenuCadastroClintes)
        self.menuCadastros.addAction(self.subMenuCadastroMotoristas)
        self.menuCadastros.addAction(self.menuCadUsuario)
        self.menuCadastros.addSeparator()
        self.menuCadastros.addAction(self.subMenuEntradaNotasTeca)
        self.subMenuDescarregamento.addAction(self.menuDescaEntrada)
        self.subMenuDescarregamento.addAction(self.menuDescaSaida)
        self.subMenuCarregamentos.addAction(self.menuCarregEntrada)
        self.subMenuCarregamentos.addAction(self.menuCarregSaida)
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
        self.menuCadPesFisica.setText(_translate("frmMainHouse", "Pessoa Física", None))
        self.menuCadPesJuridica.setText(_translate("frmMainHouse", "Pessoa Jurídica", None))
        self.menuCadUsuario.setText(_translate("frmMainHouse", "Usuario / Permissão", None))
        self.menuMovimentoPortaria.setTitle(_translate("frmMainHouse", "Movimentos", None))
        self.subMenuDescarregamento.setTitle(_translate("frmMainHouse", "Descarregamento", None))
        self.subMenuCarregamentos.setTitle(_translate("frmMainHouse", "Carregamentos", None))
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
        self.subMenuCadastroClintes.setText(_translate("frmMainHouse", "Clientes", None))
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
        self.menuDescaEntrada.setText(_translate("frmMainHouse", "Entrada", None))
        self.menuDescaSaida.setText(_translate("frmMainHouse", "Saida", None))
        self.menuCarregEntrada.setText(_translate("frmMainHouse", "Entrada", None))
        self.menuCarregSaida.setText(_translate("frmMainHouse", "Saida", None))
        self.menuLogout.setText(_translate("frmMainHouse", "Trocar Usuario", None))

