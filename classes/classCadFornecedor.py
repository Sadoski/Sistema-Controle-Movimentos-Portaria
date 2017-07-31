import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from telas.frmCadastroFornecedor import Ui_frmCadastroFornecedor

class CadastroFornecedores(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmCadastroFornecedor()
        self.ui.setupUi(self)
