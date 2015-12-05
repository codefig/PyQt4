__author__ = '0code'


from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys


class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow, self).__init__(parent=None)

        self.grouplist = QListWidget()
        self.messagelist = QListWidget()
        self.messageView = QTextBrowser()

        self.items = ['php',"python", "perl", "ruby"]
        self.itemsite = ['php.net', 'python.org', 'per.eu', 'ruby.com']

        self.grouplist.addItems(self.items)
        self.messagelist.addItems(self.itemsite)

        self.messageSplitter = QSplitter(Qt.Vertical)
        self.messageSplitter.addWidget(self.messagelist)
        self.messageSplitter.addWidget(self.messageView)

        self.mainSplitter = QSplitter(Qt.Horizontal)
        self.mainSplitter.addWidget(self.grouplist)
        self.mainSplitter.addWidget(self.messageSplitter)
        self.setCentralWidget(self.mainSplitter)

        ''' some users find splitters annoyng , becuae they can resize them only by using the mouse
        so we r gonna minimize this annoynace by saing and restoring the user's splitter sizes.
        this is helpful because the user can simply set the zsizes once, and from then onthe sizes they
        will be honored
            '''
        #
        settings = QSettings()
        size = settings.value("MainWindow/Size", QVariant(QSize(600,500))).toSize()
        self.resize(size)

        #position = settings.value("Mainwindow/Position", QVariant(QPoint(0,0))).toPoint()
        #self.move(position)
        #self.restoreState(settings.value("MainWindow/State").toByteArray())
        #self.messageSplitter.restoreState(settings.value("MessageSplitter").toByteArray())
        #self.mainSplitter.restoreState(settings.value("MainSplitter").toByteArray())


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()