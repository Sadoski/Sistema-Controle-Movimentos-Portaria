import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from telas.frmSaidaCaminhaoEmpresa import Ui_frmSaidaCaminhoaEmpresa


class SaidaCaminhaoEmpresa(QtGui.QDialog):

    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmSaidaCaminhoaEmpresa()
        self.ui.setupUi(self)
