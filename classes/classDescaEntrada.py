import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from telas.frmEntradaVeiculosDescarregamento import Ui_frmEntradaVeiculosDescarregamento

class DescaEntrada(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmEntradaVeiculosDescarregamento()
        self.ui.setupUi(self)
