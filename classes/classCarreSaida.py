import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from telas.frmSaidaVeiculosCarregamentos import Ui_frmSaidaVeiculosCarregamento

class CarregamentoSaida(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmSaidaVeiculosCarregamento()
        self.ui.setupUi(self)
