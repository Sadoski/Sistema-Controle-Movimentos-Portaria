import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from telas.frmCadastroUsuarios import Ui_frmCadastroUsuarios

class CadastroEmpresa(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmCadastroUsuarios()
        self.ui.setupUi(self)
