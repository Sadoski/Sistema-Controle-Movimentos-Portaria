import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from telas.frmSobre import Ui_frmSobre


class Sobre(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmSobre()
        self.ui.setupUi(self)

        self.ui.btnOk.clicked.connect(self.sair)

    def sair(self):
        self.close()
