__author__ = '0code'


from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys


class Custom(QWidget):
    def __init__(self, parent=None):
        super(Custom,self).__init__(parent)

        self.zipcode = LabelledLineEdit("&Zipcode:")
        self.notes = LabelledTextEdit("&Notes:",parent=None)

        layout = QGridLayout()
        layout.addWidget(self.zipcode)
        layout.addWidget(self.notes)
        self.setLayout(layout)

class LabelledTextEdit(QWidget):
    def __init__(self,labelText=QString(), parent=None):
        super(LabelledTextEdit, self).__init__(parent)
        self.label = QLabel(labelText)
        self.textEdit = QTextEdit()
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.textEdit)
        self.setLayout(self.layout)

class LabelledLineEdit(QWidget):
    def __init__(self, labelText=QString(), position="LEFT", parent=None):
        super(LabelledLineEdit, self).__init__(parent)
        self.label = QLabel(labelText)
        self.lineEdit = QLineEdit()
        self.label.setBuddy(self.lineEdit)
        layout = QBoxLayout(QBoxLayout.LeftToRight if position == "LEFT" else  QBoxLayout.TopToBottom)
        layout.addWidget(self.label)
        layout.addWidget(self.lineEdit)
        self.setLayout(layout)




app = QApplication(sys.argv)
cs = Custom()
cs.show()
app.exec_()