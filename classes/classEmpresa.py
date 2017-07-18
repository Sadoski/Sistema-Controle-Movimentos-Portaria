import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from telas.frmCadastroEmpresa import Ui_frmCadastroEmpresa
app = QtGui.QApplication(sys.argv)

class Empresa(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_frmCadastroEmpresa()
        self.ui.setupUi(self)