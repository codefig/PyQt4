__author__ = '0code'

import mechanize
import urllib
import socket
import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *


'''
    an example of the extension dialog which happens when
    u click the more button to show the more options
    which was hidden to the user '''


class Extension(QDialog):
    def __init__(self, parent=None):
        super(Extension, self).__init__(parent=None)
        self.setGeometry(500,500,300,300)
        self.setWindowTitle("Extension Dialog example ")

        findLabel = QLabel("find")
        findEdit = QLineEdit()
        morecheck = QCheckBox()

        uplayout = QVBoxLayout()
        uplayout.addWidget(findLabel)
        uplayout.addWidget(findEdit)
        uplayout.addWidget(morecheck)

        mainLayout = QVBoxLayout()

        hidelayout = QVBoxLayout()

        hidecheck = QCheckBox("hacking computers")
        hideprog  = QCheckBox("Python programming")

        hidelayout.addWidget(hidecheck)
        hidelayout.addWidget(hideprog)

        moreframe = QFrame()
        moreframe.setStyle(QFrame.StyledPanel | QFrame.Sunken)
        moreframe.setLayout(hidelayout)

        line = QFrame()
        line.setFrameStyle(QFrame.VLine | QFrame.Sunkrn)











app = QApplication(sys.argv)
window = Extension()
window.show()
app.exec_()