import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from telas.frmEntradaNotasRomaneios import Ui_frmEntradaNotaRomaneios

class CadastroEmpresa(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmEntradaNotaRomaneios()
        self.ui.setupUi(self)

        self.unidadeMedida()

    def unidadeMedida(self):
        lista = ["UN", "KM", "HM", "DAM", "M", "DM", "CM", "MM", "KM²", "HM²", "DAM²", "M²", "DM²", "CM²", "MM²", "KM³", "HM³", "DAM³", "M³", "DM³", "CM³", "MM³", "T", "KG", "HG", "DAG", "G", "DG", "CG", "MG", "KL", "HL", "DAL", "L", "DL", "CL", "ML"]
        for i in lista:
            self.ui.txtUn.addItem(i)