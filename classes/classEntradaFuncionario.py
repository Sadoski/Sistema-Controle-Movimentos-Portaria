import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from telas.frmEntradaFuncionario import Ui_frmCadastroEntradaFuncionario

class EntradaFuncionario(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmCadastroEntradaFuncionario()
        self.ui.setupUi(self)