import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from telas.frmEntradaVeiculosEmpresaTerceiro import Ui_frmEntradaVeiculosEmpresaTerceiros

class EntradaVeiculoEmpresaTerceiro(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmEntradaVeiculosEmpresaTerceiros()
        self.ui.setupUi(self)
