import sys
import time
import datetime
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from classes.classCadPessoaFisica import CadastroPessoaFisica
from classes.classCarreSaida import CarregamentoSaida
from classes.classEntraVeiEmpTer import EntradaVeiculoEmpresaTerceiro
from classes.classEntradaCaminhaoEmp import EntradaCaminhaoEmpresa
from classes.classEntradaVeiEmpresa import EntradaVeiEmpresa
from classes.classPesquisarNotaFiscal import PesquisarNotaFiscal
from classes.classCadPessoaJuridica import CadastroPessoaJuridica
from classes.classSaidaCaminhaoEmp import SaidaCaminhaoEmpresa
from classes.classSaidaVeiEmpTer import SaidaVeiEmpTer
from classes.classSaidaVeiEmpresa import SaidaVeiEmpresa
from classes.classUsuarioPermissao import UsuarioPermissao
from controller.getSetDadosUsuarios import DadosUsuario
from telas.frmMainHouse import Ui_frmMainHouse
from telas.frmMesagemSair import Ui_frmMensagemSair
from telas.frmMesagemTrocaUsuario import Ui_frmMensagemTrocaUsuario
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
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.displayTime)
        self.timer.start()

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
        self.ui.entSaiFuncSubMenuSaida.triggered.connect(self._saidaFuncionrio)
        self.ui.menuCarregEntrada.triggered.connect(self._entradaCarregamento)
        self.ui.menuCarregSaida.triggered.connect(self._saidaCarregamento)
        self.ui.menuDescaEntrada.triggered.connect(self._entradaDescarregamento)
        self.ui.menuDescaSaida.triggered.connect(self._saidaDescarregamento)
        self.ui.veiTerSubMenuEntrada.triggered.connect(self._entradaVeiEmpTer)
        self.ui.veicTerSubMenuSaida.triggered.connect(self._saidaVeiEmpTer)
        self.ui.veicEmpSubMenuEntrada.triggered.connect(self._entradaVeiEmpresa)
        self.ui.veicEmpSaida.triggered.connect(self._saidaVeiEmpresa)
        self.ui.camiEmpSubMenuEntrada.triggered.connect(self._entradaCaminEmp)
        self.ui.camiEmpSubMenuSaida.triggered.connect(self._saidaCaminEmp)
        self.ui.subMenuSobre.triggered.connect(self._sobre)
        '''
        #Menu Cosultas
        self.ui.subMenuConsultasEmpresas.triggered.connect(self.__consultasEmpresas)
        self.ui.subMenuConsultasFuncionarios.triggered.connect(self.__consultasFuncionarios)
        self.ui.subMenuConsultasFornecedores.triggered.connect(self.__consultasFornecedores)
        self.ui.subMenuConsultasClientes.triggered.connect(self.__consultasClientes)
        self.ui.subMenuConsultasMotoristas.triggered.connect(self.__consultasMotoristas)
        self.ui.subMenuConsultasNotas.triggered.connect(self.__consultasNotas)

        self.ui.carreConsSubMenuMadeira.triggered.connect(self.__consultasMadeira)
        self.ui.carreConsSubMenuCavacoSerragem.triggered.connect(self.__consultasCavacoSerragem)
        self.ui.descaConsSubMenuTeca.triggered.connect(self.__consultasTeca)
        self.ui.descaConsSubMenuCavacoSerragem.triggered.connect(self.__consultasCavacoSerragem)
        self.ui.descaConsSubMenuOutros.triggered.connect(self.__consultasOutros)
        self.ui.veiLevConsSubMenuEmpresa.triggered.connect(self.__consultasEmpresa)
        self.ui.veiLevConsSubMenuTerceiros.triggered.connect(self.__consultasTerceiros)
        self.ui.camiConsSubMenuEmpresa.triggered.connect(self.__consultasEmpresa)
        self.ui.camiConsSubMenuTerceiros.triggered.connect(self.__consultasTerceiros)
        self.ui.consEntSaidSubMenuMaquinas.triggered.connect(self.__consultasMaquinas)
        self.ui.consEntSaidSubMenuNotas.triggered.connect(self.__consultasNotas)
        self.ui.consEntSaidSubMenuFuncionarios.triggered.connect(self.__consultasFuncionarios)


        #Menu Movimentos
        self.ui.carreMadeiraEntrada.triggered.connect(self.__carreMadeiraEntrada)
        self.ui.carreMadeiraSaida.connect(self.__carreMadeiraSaida)

        self.ui.carreCavacoPoSerragemEntrada.triggered.connect(self.__carreCavacoPoSerragemEntrada)
        self.ui.carreCavacoPoSerragemSaida.connect(self.__carreCavacoPoSerragemSaida)

        self.ui.descTecaEntrada.triggered.connect(self.__descTecaEntrada)
        self.ui.descTecaSaida.connect(self.__descTecaSaida)

        self.ui.descCavacoPoSerragemEntrada.triggered.connect(self.__descCavacoPoSerragemEntrada)
        self.ui.descCavacoPoSerragemSaida.connect(self.__descCavacoPoSerragemSaida)

        self.ui.veicEmpSubMenuEntrada.triggered.connect(self.__veicEmpEntrada)
        self.ui.veicEmpSaida.connect(self.__veicEmpSaida)

        self.ui.veiTerSubMenuEntrada.triggered.connect(self.__veiTerEntrada)
        self.ui.veicTerSubMenuSaida.connect(self.__veicTerSaida)

        self.ui.camiEmpSubMenuEntrada.triggered.connect(self.__camiEmpSubEntrada)
        self.ui.camiEmpSubMenuSaida.connect(self.__camiEmpSaida)

        self.ui.camiTerSubMenuEntrada.triggered.connect(self.__camiTerEntrada)
        self.ui.camiTerSubMenuSaida.connect(self.__camiTerSaida)

        self.ui.entSadMaquiSubMenuEntrada.triggered.connect(self.__entSadMaquiEntrada)
        self.ui.entSadMaquiSubMenuSaida.connect(self.__entSadMaquiSaida)

        self.ui.entSaiFuncSubMenuEntrada.triggered.connect(self.__entSaiFuncEntrada)
        self.ui.entSaiFuncSubMenuSaida.connect(self.__entSaiFuncSaida)

        #Menu Relatorios
        self.ui.subMenuRelatorios.triggered.connect(self.__relatorios)
        self.ui.subMenuGraficos.connect(self.__graficos)
        '''

    def status(self, nome):
        self.ui.statusbar.showMessage("Bem-Vindo "+nome)

    def displayTime(self):
        self.ui.statusbar.showMessage(QtCore.QDateTime.currentDateTime().toString())

    def _sair(self):
        self.dialogMensagem = QDialog(self, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint
)
        self.__mesagem = Ui_frmMensagemSair()
        self.__mesagem.setupUi(self.dialogMensagem)

        self.__mesagem.btnSim.clicked.connect(self.fechar)
        self.__mesagem.btnNao.clicked.connect(self.closeMesagem)


        self.dialogMensagem.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.dialogMensagem.exec_()

    def fechar(self):
        sys.exit(0)

    def closeMesagem(self):
        self.dialogMensagem.close()

    def _trocarUsuario(self):
        self.dialogTrocaUsuario = QDialog(self, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint )
        self.__trocaUsuario = Ui_frmMensagemTrocaUsuario()
        self.__trocaUsuario.setupUi(self.dialogTrocaUsuario)

        self.__trocaUsuario.btnSim.clicked.connect(self._logout)
        self.__trocaUsuario.btnNao.clicked.connect(self.closeTrocaUsuario)


        self.dialogTrocaUsuario.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.dialogTrocaUsuario.exec_()

    def _logout(self):
            self.dialogTrocaUsuario.close()
            self.close()
            from classes.classLogin import Login
            _login = Login()
            _login.show()
            _login.exec_()

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

    def _entradaVeiEmpTer(self):
        _entrada = EntradaVeiculoEmpresaTerceiro()
        _entrada.show()
        _entrada.exec_()

    def _saidaVeiEmpTer(self):
        _saida = SaidaVeiEmpTer()
        _saida.show()
        _saida.exec_()

    def _entradaVeiEmpresa(self):
        _entrada = EntradaVeiEmpresa()
        _entrada.show()
        _entrada.exec_()

    def _saidaVeiEmpresa(self):
        _saida = SaidaVeiEmpresa()
        _saida.show()
        _saida.exec_()

    def _entradaCaminEmp(self):
        _entrada = EntradaCaminhaoEmpresa()
        _entrada.show()
        _entrada.exec_()

    def _saidaCaminEmp(self):
        _saida = SaidaCaminhaoEmpresa()
        _saida.show()
        _saida.exec_()

    def _sobre(self):
        _sobre = Sobre()
        _sobre.show()
        _sobre.exec_()

    def _email(self):
        _email = Email()
        _email.show()
        _email.exec_()
    '''
    def closeEvent(self, event):
        sair = QtGui.QMessageBox.question(QWidget(), 'Atenção', "Você tem certeza que deseja sair", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if sair == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    '''
