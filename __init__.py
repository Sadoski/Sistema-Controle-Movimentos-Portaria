import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from src.com.guavira.telas.frmMainHouse import Ui_frmMainHouse

class Principal(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_frmMainHouse()
        self.ui.setupUi(self)
        
app = QtGui.QApplication(sys.argv)
program = Principal()
program.show()
sys.exit(app.exec_())


    
