__author__ = '0code'



from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys




class DragnDrop(QWidget):
    def __init__(self,parent=None):
        super(DragnDrop, self).__init__(parent)

        #listwidget = QListWidget()
        #listwidget.setAcceptDrops(True)
        #listwidget.setDragEnabled(True)
        #
        #
        #iconListWidget = QListWidget()
        #iconListWidget.setAcceptDrops(True)
        #iconListWidget.setDragEnabled(True)
        #iconListWidget.setViewMode(QListWidget.IconMode)


        layout = QGridLayout()

        self.chats = []

        self.list = Mylist()
        layout.addWidget(self.list, 0, 1)
        self.line = DropLineEdit()

        mybutton  = QPushButton("Send")
        mybutton.animateClick(5000)

        layout.addWidget(self.line, 1,1 )
        layout.addWidget(mybutton, 1, 2)
        self.connect(mybutton, SIGNAL("clicked()"), self.putchat)
        self.setLayout(layout)

    def putchat(self):
        self.curtext = self.line.text()
        print(self.curtext)
        if not self.curtext.isEmpty():
           self.chats.append(str(self.curtext))
           self.list.addItem(self.curtext)
           print(self.chats)
        self.line.setText("")

class Mylist(QListWidget):
    def __init__(self, parent=None):
        super(Mylist, self).__init__(parent)
        self.setDragEnabled(True)
        self.setAcceptDrops(True)

    def focusInEvent(self,event):
        print(event.type())





class DropLineEdit(QLineEdit):
    def __init(self, parent=None):
        super(DropLineEdit,self).__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat("application/x-icon-and-text"):
            event.accept()
        else:
            event.ignore()
    def dragMoveEvent(self, event):
        if event.mimeData().hasFormat("application/x-icon-and-text"):
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()
    def dropEvent(self, event):
        if event.mimeData().hasFormat("application/x-icon-and-text"):
            data  = event.mimeData().data("application/x-icon-and-text")
            stream = QDataStream(data, QIODevice.ReadOnly)
            text = QString()
            stream >> text
            self.setText(text)
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()



app = QApplication(sys.argv)
d = DragnDrop()
d.show()
app.exec_()