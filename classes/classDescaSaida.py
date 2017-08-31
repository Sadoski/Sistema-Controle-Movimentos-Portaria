import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from telas.frmSaidaVeiculoDescarregamento import Ui_frmSaidaVeiculoDescarregamento

class DescaSaida(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmSaidaVeiculoDescarregamento()
        self.ui.setupUi(self)
