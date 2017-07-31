import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from telas.frmSaidaVeiculosTerceiros import Ui_frmSaidaVeiculosTerceiros

class CadastroEmpresa(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmSaidaVeiculosTerceiros()
        self.ui.setupUi(self)
