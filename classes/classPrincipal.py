import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from telas.frmMainHouse import Ui_frmMainHouse
from .classEmpresa import Empresa
from .classCadFuncionarios import CadastroFuncionario
from .classCadFornecedor import CadastroFornecedores
from .classCadCliente import CadastroClientes
from .classCadMotorista import CadastroMotoristas
from .classNotasFiscal import CadastroEmpresa
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
        QtGui.QApplication.__init__(self)
        self.ui = Ui_frmMainHouse()
        self.ui.setupUi(self)
        self.app = QtGui.QApplication(sys.argv)

        self.ui.subMenuCadastroEmpresa.triggered.connect(self.__cadastroEmpresa)
        self.ui.subMenuCadastroFuncionarios.triggered.connect(self.__cadastroFuncionario)
        self.ui.subMenuCadastroFornecedor.triggered.connect(self.__cadastroFornecedor)
        self.ui.subMenuCadastroClintes.triggered.connect(self.__cadastroClintes)
        self.ui.subMenuCadastroMotoristas.triggered.connect(self.__cadastroMotoristas)
        self.ui.subMenuEntradaNotasTeca.triggered.connect(self.__entradaNotasTeca)
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
    def __sair(self):
        w = QWidget()
        result = QMessageBox.question(w, 'Menssagem', "Deseja sair do Programa", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            sys.exit(None)

    def __cadastroEmpresa(self):
        __empresa = Empresa()
        __empresa.show()
        __empresa.exec_()

    def __cadastroFuncionario(self):
        __funcionario = CadastroFuncionario()
        __funcionario.show()
        __funcionario.exec_()

    def __cadastroFornecedor(self):
        __fornecedor = CadastroFornecedores()
        __fornecedor.show()
        __fornecedor.exec_()

    def __cadastroClintes(self):
        __cintes = CadastroClientes()
        __cintes.show()
        __cintes.exec_()

    def __cadastroMotoristas(self):
        __motoristas = CadastroMotoristas()
        __motoristas.show()
        __motoristas.exec_()

    def __entradaNotasTeca(self):
        __notas = CadastroEmpresa()
        __notas.show()
        __notas.exec_()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    principal = Principal()
    principal.show()
    sys.exit(app.exec_())