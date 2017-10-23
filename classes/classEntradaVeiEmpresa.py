import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from telas.frmEntradaVeiculosEmpresa import Ui_frmEntradaVeiculosEmpresa


class EntradaVeiEmpresa(QtGui.QDialog):

    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmEntradaVeiculosEmpresa()
        self.ui.setupUi(self)