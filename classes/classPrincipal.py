import sys
import time
import datetime
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from classes.classCadPessoaFisica import CadastroPessoaFisica
from classes.classCarreSaida import CarregamentoSaida
from classes.classCadPessoaJuridica import CadastroPessoaJuridica
from classes.classRelatorio import Relatorio
from classes.classUsuarioPermissao import UsuarioPermissao
from telas.frmMainHouse import Ui_frmMainHouse
from .classEmpresa import Empresa
from .classCadFuncionarios import CadastroFuncionario
from .classCadFornecedor import CadastroFornecedores
from .classCadCliente import CadastroClientes
from .classCadMotorista import CadastroMotoristas
from .classNotasFiscal import CadastroNotaFiscal
from .classSaidaFuncionario import SaidaFuncionario
from .classEntradaFuncionario import EntradaFuncionarios
from .classCarreEntrada import CarregamentoEntrada
from .classDescaEntrada import DescaEntrada
from .classDescaSaida import DescaSaida
from .classSobre import Sobre
from .classEmail import Email


class Principal(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_frmMainHouse()
        self.ui.setupUi(self)


        self.ui.menuSair.triggered.connect(self._sair)
        self.ui.menuLogout.triggered.connect(self._trocarUsuario)
        self.ui.menuCadPesFisica.triggered.connect(self._cadastroPessoaFisica)
        self.ui.menuCadPesJuridica.triggered.connect(self._cadastroPessoaJurisdica)
        self.ui.subMenuCadastroEmpresa.triggered.connect(self._cadastroEmpresa)
        self.ui.subMenuCadastroFuncionarios.triggered.connect(self._cadastroFuncionario)
        self.ui.menuCadUsuario.triggered.connect(self._cadastroUsuarioPermissao)
        self.ui.subMenuCadastroFornecedor.triggered.connect(self._cadastroFornecedor)
        self.ui.subMenuCadastroClintes.triggered.connect(self._cadastroClintes)
        self.ui.subMenuCadastroMotoristas.triggered.connect(self._cadastroMotoristas)
        self.ui.subMenuEntradaNotasTeca.triggered.connect(self._entradaNotasTeca)
        self.ui.entSaiFuncSubMenuEntrada.triggered.connect(self._entradaFuncionrio)
        self.ui.menuCarregEntrada.triggered.connect(self._entradaCarregamento)
        self.ui.menuCarregSaida.triggered.connect(self._saidaCarregamento)
        self.ui.menuDescaEntrada.triggered.connect(self._entradaDescarregamento)
        self.ui.menuDescaSaida.triggered.connect(self._saidaDescarregamento)
        self.ui.subMenuSobre.triggered.connect(self._sobre)
        self.ui.subMenuRelatorios.triggered.connect(self._relatorio)

    def status(self, nome):
        self.label = QtGui.QLabel("Bem-Vindo " + nome)
        self.label.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label.setMinimumSize(self.label.sizeHint())
        self.ui.statusbar.addPermanentWidget(self.label, 1)
        self.time = QtGui.QLabel()
        self.time.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        self.ui.statusbar.addPermanentWidget(self.time)

    def hora(self):
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.displayTime)
        self.timer.start()

    def displayTime(self):
        self.ui.statusbar.addPermanentWidget(self.time.setText(QtCore.QDateTime.currentDateTime().toString()))

    def _trocarUsuario(self):
        try:
            _fromUtf8 = QtCore.QString.fromUtf8
        except AttributeError:
            def _fromUtf8(s):
                return s
        self.msgBox = QtGui.QMessageBox()
        self.msgBox.setWindowTitle("Mensagem")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/question.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.msgBox.setWindowIcon(icon)
        self.msgBox.setIconPixmap(QtGui.QPixmap(_fromUtf8("./imagens/icon-question.png")))
        self.msgBox.setText("Você tem certeza que deseja trocar de usuário?")
        btnSim = QtGui.QPushButton('Sim')
        self.msgBox.addButton(btnSim, QtGui.QMessageBox.YesRole)
        btnSim.clicked.connect(self._logout)
        btnNao = QtGui.QPushButton('Não')
        self.msgBox.addButton(btnNao, QtGui.QMessageBox.YesRole)
        btnNao.clicked.connect(self.closeMesagem)
        btnNao.setFocus()
        self.msgBox.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.msgBox.exec_()

    def _logout(self):
            self.msgBox.close()
            self.ui.statusbar.removeWidget(self.label)
            self.ui.statusbar.removeWidget(self.time)
            self.close()
            from classes.classLogin import Login
            _login = Login()
            _login.show()
            _login.exec_()

    def _sair(self):
        try:
            _fromUtf8 = QtCore.QString.fromUtf8
        except AttributeError:
            def _fromUtf8(s):
                return s
        self.msgBox = QtGui.QMessageBox()
        self.msgBox.setWindowTitle("Mensagem")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/question.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.msgBox.setWindowIcon(icon)
        self.msgBox.setIconPixmap(QtGui.QPixmap(_fromUtf8("./imagens/icon-question.png")))
        self.msgBox.setText("Deseja sair do Programa?")
        btnSim = QtGui.QPushButton('Sim')
        self.msgBox.addButton(btnSim, QtGui.QMessageBox.YesRole)
        btnSim.clicked.connect(self.fechar)
        btnNao = QtGui.QPushButton('Não')
        self.msgBox.addButton(btnNao, QtGui.QMessageBox.YesRole)
        btnNao.clicked.connect(self.closeMesagem)
        btnNao.setFocus()
        self.msgBox.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.msgBox.exec_()

    def fechar(self):
        sys.exit(0)

    def closeMesagem(self):
        self.msgBox.close()

    def closeTrocaUsuario(self):
        self.dialogTrocaUsuario.close()

    def _cadastroPessoaFisica(self):
        _fisica = CadastroPessoaFisica()
        _fisica.show()
        _fisica.exec_()

    def _cadastroPessoaJurisdica(self):
        _juridica = CadastroPessoaJuridica()
        _juridica.show()
        _juridica.exec_()

    def _cadastroEmpresa(self):
        _empresa = Empresa()
        _empresa.show()
        _empresa.exec_()

    def _cadastroFuncionario(self):
        _funcionario = CadastroFuncionario()
        _funcionario.show()
        _funcionario.exec_()

    def _cadastroUsuarioPermissao(self):
        _usuario = UsuarioPermissao()
        _usuario.show()
        _usuario.exec_()

    def _cadastroFornecedor(self):
        _fornecedor = CadastroFornecedores()
        _fornecedor.show()
        _fornecedor.exec_()

    def _cadastroClintes(self):
        _cintes = CadastroClientes()
        _cintes.show()
        _cintes.exec_()

    def _cadastroMotoristas(self):
        _motoristas = CadastroMotoristas()
        _motoristas.show()
        _motoristas.exec_()

    def _entradaNotasTeca(self):
        _notas = CadastroNotaFiscal()
        _notas.show()
        _notas.exec_()

    def _entradaFuncionrio(self):
        _entFun = EntradaFuncionarios()
        _entFun.show()
        _entFun.exec_()

    def _saidaFuncionrio(self):
        _entFun = SaidaFuncionario()
        _entFun.show()
        _entFun.exec_()

    def _entradaCarregamento(self):
        _entCarre = CarregamentoEntrada()
        _entCarre.show()
        _entCarre.exec_()

    def _saidaCarregamento(self):
        _saiCarre = CarregamentoSaida()
        _saiCarre.show()
        _saiCarre.exec_()

    def _entradaDescarregamento(self):
        _entDesca = DescaEntrada()
        _entDesca.show()
        _entDesca.exec_()

    def _saidaDescarregamento(self):
        _saiDesca = DescaSaida()
        _saiDesca.show()
        _saiDesca.exec_()

    def _sobre(self):
        _sobre = Sobre()
        _sobre.show()
        _sobre.exec_()

    def _email(self):
        _email = Email()
        _email.show()
        _email.exec_()

    def _relatorio(self):
        _relatorio = Relatorio()
        _relatorio.show()
        _relatorio.exec_()



    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.WindowStateChange:
            if self.windowState() & QtCore.Qt.WindowMaximized:
                a = self.centralWidget()
                print(a)
                b = self.geometry()
                print(b)
                vertcal = self.adjustSize()
                horizontal = self.adjustSize()
                imgVertical = self.ui.lblImagem.minimumWidth()
                imgHorizoltal = self.ui.lblImagem.minimumHeight()

            elif QtCore.QRect:

                pass
        QtGui.QWidget.changeEvent(self, event)

    '''
    def closeEvent(self, event):
        sair = QtGui.QMessageBox.question(QWidget(), 'Atenção', "Você tem certeza que deseja sair", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if sair == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    '''
