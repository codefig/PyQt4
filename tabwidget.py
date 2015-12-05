__author__ = '0code'

import mechanize
import urllib
import socket
import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *



class Window(QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent=None)

        self.paidCheckBox = QCheckBox()

        checkNumLabel = QLabel("Number Label")
        self.checkNumLineEdit = QLineEdit()

        bankLabel = QLabel("Bank")
        self.bankLineEdit = QLineEdit()

        accountNumLabel = QLabel("Account Label: ")
        self.accountNumLineEdit = QLineEdit()

        sortCodeLabel = QLabel("Sort Code")
        self.sortCodeLineEdit = QLineEdit()

        gridLayout = QGridLayout()
        self.buttonBox = QDialogButtonBox()


        tabWidget = QTabWidget()
        cashWidget = QWidget()
        cashLayout = QHBoxLayout()
        cashLayout.addWidget(self.paidCheckBox)
        cashWidget.setLayout(cashLayout)
        tabWidget.addTab(cashWidget, "Cas&h")


        checkWidget = QWidget()
        checkLayout = QGridLayout()
        checkLayout.addWidget(checkNumLabel, 0,0)
        checkLayout.addWidget(self.checkNumLineEdit,0, 1)
        checkLayout.addWidget(bankLabel,0, 2)
        checkLayout.addWidget(self.bankLineEdit,0 , 3)
        checkLayout.addWidget(accountNumLabel, 1, 0)
        checkLayout.addWidget(self.accountNumLineEdit, 1, 1)
        checkLayout.addWidget(sortCodeLabel,1, 2)
        checkLayout.addWidget(self.sortCodeLineEdit, 1, 3)
        checkWidget.setLayout(checkLayout)
        tabWidget.addTab(checkWidget, "Chec&k")



        #this was added by me

        cardWidget = QWidget()
        cardLayout = QGridLayout()

        cardLabel = QLabel("Card No: ")
        self.cardLineEdit = QLineEdit()
        cvvLabel = QLabel("CVV : ")
        self.cvvLineEdit = QLineEdit()
        pinLabel = QLabel("PIN: ")
        self.pinLineEdit = QLineEdit()

        self.proceedLabel = QPushButton("Check out ")

        cardLayout.addWidget(cardLabel, 0, 0)
        cardLayout.addWidget(self.cardLineEdit, 0, 1)
        cardLayout.addWidget(cvvLabel, 1, 0)
        cardLayout.addWidget(self.cvvLineEdit, 1,1)
        cardLayout.addWidget(pinLabel,2,0)
        cardLayout.addWidget(self.pinLineEdit, 2, 1)
        cardLayout.addWidget(self.proceedLabel,3, 1)
        cardWidget.setLayout(cardLayout)


        tabWidget.addTab(cardWidget, "Car&d")



        layout = QVBoxLayout()
        layout.addLayout(gridLayout)
        layout.addWidget(tabWidget)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)





app = QApplication(sys.argv)
window = Window()
window.show()
app.exec_()