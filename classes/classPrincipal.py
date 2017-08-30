import sys
import time
import datetime
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from classes.classCarreSaida import CarregamentoSaida
from controller.getSetDadosUsuarios import DadosUsuario
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
from .classSobre import Sobre
'''
from classes.classConsulEmpresas import ConsultarEmpresas
from classes.classConsulFuncionarios import ConsultarFuncionarios
from classes.classConsulFornecedor import ConsultarFornecedor
from classes.classConsulClientes import ConsultarClientes
from classes.classConsulMotoristas import ConsultarMotoristas
from classes.classConsulNotas import ConsultarNotas
from classes.classConsulMadeira import ConsultarMadeira
from classes.classConsulCavacoSerragem import ConsultarCavacoSerragem
from classes.classConsulTeca import ConsultarTeca
from classes.classConsulCavacoSerragem import ConsultarCavacoSerragem
from classes.classConsulOutros import ConsultarOutros
from classes.classConsulVeicEmpresa import ConsultarVeicEmpresa
from classes.classConsulVeicTerceiros import ConsultarVeicTerceiros
from classes.classConsulCaminEmpresa import ConsultarCaminEmpresa
from classes.classConsulCaminTerceiros import ConsultarCaminTerceiros
from classes.classConsulMaquinas import ConsultarMaquinas
from classes.classConsulEntSaiFuncionarios import ConsultarEntSaiFuncionarios

from classes.classCarreMadeiraEntrada import CarreMadeiraEntrada
from classes.classCarreMadeiraSaida import CarreMadeiraSaida
from classes.classCarreCavacoPoSerragemEntrada import CarreCavacoPoSerragemEntrada
from classes.classCarreCavacoPoSerragemSaida import CarreCavacoPoSerragemSaida
from classes.classDescTecaEntrada import DescTecaEntrada
from classes.classDescTecaSaida import DescTecaSaida
from classes.classDescCavacoPoSerragemEntrada import DescCavacoPoSerragemEntrada
from classes.classDescCavacoPoSerragemSaida import DescCavacoPoSerragemSaida
from classes.classVeicEmpEntrada import VeicEmpEntrada
from classes.classVeicEmpSaida import VeicEmpSaida
from classes.classVeiTerEntrada import VeiTerEntrada
from classes.classVeiTerSaida import VeiTerSaida
from classes.classCamiEmpEntrada import CamiEmpEntrada
from classes.classCamiEmpSaida import CamiEmpSaida
from classes.classCamiTerEntrada import CamiTerEntrada
from classes.classCamiTerSaida import CamiTerSaida
from classes.classMaquinaEntrada import MaquinaEntrada
from classes.classMaquinaSaida import MaquinaSaida
from classes.classFuncionarioEntrada import FuncionarioEntrada
from classes.classFuncionarioSaida import FuncionarioSaida

from classes.classRelatorios import Relatorios
from classes.classGraficos import Graficos
'''



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
        self.ui.subMenuCadastroEmpresa.triggered.connect(self._cadastroEmpresa)
        self.ui.subMenuCadastroFuncionarios.triggered.connect(self._cadastroFuncionario)
        self.ui.subMenuCadastroFornecedor.triggered.connect(self._cadastroFornecedor)
        self.ui.subMenuCadastroClintes.triggered.connect(self._cadastroClintes)
        self.ui.subMenuCadastroMotoristas.triggered.connect(self._cadastroMotoristas)
        self.ui.subMenuEntradaNotasTeca.triggered.connect(self._entradaNotasTeca)
        self.ui.entSaiFuncSubMenuEntrada.triggered.connect(self._entradaFuncionrio)
        self.ui.entSaiFuncSubMenuSaida.triggered.connect(self._saidaFuncionrio)
        self.ui.menuCarregEntrada.triggered.connect(self._entradaCarregamento)
        self.ui.menuCarregSaida.triggered.connect(self._saidaCarregamento)
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

        #Menu Sobre
        self.ui.subMenuSobre.triggered.connect(self.__sobre)
        '''

    def status(self, nome):
        self.ui.statusbar.showMessage("Bem-Vindo "+nome)

    def displayTime(self):
        self.ui.statusbar.showMessage(QtCore.QDateTime.currentDateTime().toString())

    def _sair(self):
        w = QWidget()
        result = QMessageBox.question(w, 'Menssagem', "Deseja sair do Programa", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            sys.exit(0)

    def _cadastroEmpresa(self):
        _empresa = Empresa()
        _empresa.show()
        _empresa.exec_()

    def _cadastroFuncionario(self):
        _funcionario = CadastroFuncionario()
        _funcionario.show()
        _funcionario.exec_()

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

    def _sobre(self):
        _sobre = Sobre()
        _sobre.show()
        _sobre.exec_()

    def closeEvent(self, event):
        w = QWidget()
        sair = QtGui.QMessageBox.question(w, 'Atenção', "Você tem certeza que deseja sair", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if sair == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
