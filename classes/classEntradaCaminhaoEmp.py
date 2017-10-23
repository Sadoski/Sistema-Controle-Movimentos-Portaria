import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from telas.frmEntradaCaminhaoEmpresa import Ui_frmEntradaCaminhoaEmpresa


class EntradaCaminhaoEmpresa(QtGui.QDialog):

    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmEntradaCaminhoaEmpresa()
        self.ui.setupUi(self)
