import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from telas.frmCadastroFuncionario import Ui_frmCadastroFuncionario

class CadastroFuncionario(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmCadastroFuncionario()
        self.ui.setupUi(self)
