import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from telas.frmSaidaVeiculosCarregamento import Ui_frmSaidaVeiculosCarregamento

class CadastroEmpresa(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmSaidaVeiculosCarregamento()
        self.ui.setupUi(self)
