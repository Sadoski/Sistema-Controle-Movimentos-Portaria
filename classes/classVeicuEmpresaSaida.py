import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from telas.frmSaidaVeiculosEmpresa import Ui_frmSaidaVeiculosEmpresa

class CadastroEmpresa(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmSaidaVeiculosEmpresa()
        self.ui.setupUi(self)
