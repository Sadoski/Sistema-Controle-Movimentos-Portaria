import sys
from PyQt4 import QtGui, QtCore
from classes.classPrincipal import Principal


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    principal = Principal()
    principal.show()
    sys.exit(app.exec_())


