__author__ = '0code'
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class ClipBoard(QDialog):
    def __init__(self, parent=None):
        super(ClipBoard,self).__init__(parent)

        self.clipboard = QApplication.clipboard()
        self.clipboard.setText("Ive been clipped")

        #the upper text is meant for plain text

        #clipboard = QApplication.clipboard()
        #clipboard.setPixmap(QPixmap(os.path.join(os.path.dirname(__file__), "images/gvim.png")))

        #image data can be set on the clipboard by using SetImage() for QImages
        #or setPixmap() for pixmaps()

        self.label = QLabel("am still here")

        #retrieving data form the clipboard

        self.btn = QPushButton("click")
        self.connect(self.btn, SIGNAL("clicked()"), self.btnc)



        layout = QGridLayout()
        layout.addWidget(self.label, 0, 1)
        layout.addWidget(self.btn,1,0)

        self.setLayout(layout)

    def btnc(self):
        print("the text is : %s", self.clipboard.text())


app = QApplication(sys.argv)
ClipBoard = ClipBoard()
ClipBoard.show()
app.exec_()
