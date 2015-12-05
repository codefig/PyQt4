__author__ = '0code'
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys


class RomanSpinBox(QSpinBox):
    def __init__(self,parent=None):
        super(RomanSpinBox,self).__init__(parent)
        regex = QRegExp("r^M?M?M?(?:CM|CD|D?C?C?C?)(?:XC|XL|L?X?X?X?)(?:IX|IV|V?I?I?I?)$")
        regex.setCaseSensitivity(Qt.CaseSensitive)
        self.validator = QRegExpValidator(regex,self)
        self.setRange(1, 3999)
        self.connect(self.lineEdit(), SIGNAL("textEdited(QString)"),self.fixCase)

    def fixCase(self,text):
        self.lineEdit().setText(text.toUpper())


app =QApplication(sys.argv)
cmd = RomanSpinBox()
cmd.show()
app.exec_()