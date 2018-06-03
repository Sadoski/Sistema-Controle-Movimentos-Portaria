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
        self.subMenuEntradaSaidaFuncionario.addAction(self.entSaiFuncSubMenuEntrada)
        self.subMenuEntradaSaidaFuncionario.addAction(self.entSaiFuncSubMenuSaida)
        self.menuMovimentoPortaria.addAction(self.subMenuCarregamentos.menuAction())
        self.menuMovimentoPortaria.addAction(self.subMenuDescarregamento.menuAction())
        self.menuMovimentoPortaria.addSeparator()
        self.menuMovimentoPortaria.addAction(self.subMenuEntradaSaidaFuncionario.menuAction())
        self.menuRelatorios.addAction(self.subMenuRelatorios)
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
        self.subMenuEntradaSaidaFuncionario.setTitle(_translate("frmMainHouse", "Entrada e Saida Funcionarios", None))
        self.menuRelatorios.setTitle(_translate("frmMainHouse", "Relatorios", None))
        self.menuAjuda.setTitle(_translate("frmMainHouse", "Ajuda", None))
        self.subMenuCadastroEmpresa.setText(_translate("frmMainHouse", "Empresa", None))
        self.subMenuCadastroFuncionarios.setText(_translate("frmMainHouse", "Funcionarios", None))
        self.subMenuCadastroFornecedor.setText(_translate("frmMainHouse", "Fornecedor", None))
        self.subMenuCadastroClintes.setText(_translate("frmMainHouse", "Clientes", None))
        self.menuSair.setText(_translate("frmMainHouse", "Sair", None))
        self.subMenuSobre.setText(_translate("frmMainHouse", "Sobre", None))
        self.subMenuRelatorios.setText(_translate("frmMainHouse", "Relatorios", None))
        self.subMenuCadastroMotoristas.setText(_translate("frmMainHouse", "Motoristas", None))
        self.subMenuEntradaNotasTeca.setText(_translate("frmMainHouse", "Entrada de Notas", None))
        self.subMenuConsultasNotas.setText(_translate("frmMainHouse", "Notas", None))
        self.entSaiFuncSubMenuEntrada.setText(_translate("frmMainHouse", "Entrada", None))
        self.entSaiFuncSubMenuSaida.setText(_translate("frmMainHouse", "Saida", None))
        self.menuDescaEntrada.setText(_translate("frmMainHouse", "Entrada", None))
        self.menuDescaSaida.setText(_translate("frmMainHouse", "Saida", None))
        self.menuCarregEntrada.setText(_translate("frmMainHouse", "Entrada", None))
        self.menuCarregSaida.setText(_translate("frmMainHouse", "Saida", None))
        self.menuLogout.setText(_translate("frmMainHouse", "Trocar Usuario", None))

