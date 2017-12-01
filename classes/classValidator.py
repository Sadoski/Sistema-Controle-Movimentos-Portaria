from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QIntValidator


class Validator(QtGui.QValidator):

    def validate(self, texto, pos):
        return QtGui.QValidator.Acceptable, texto.upper(), pos

