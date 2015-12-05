__author__ = '0code'


#this code has some fucking bugs ...i need to check on creating single document interface with pyqt

from __future__ import unicode_literals


from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys



'''creating single document interface requires subclass a window and making it handle
    all remaining stuffs itself '''

class MainWindow(QMainWindow):

    NextId = 1
    def __init__(self,filename=QString(), parent=None):
        super(MainWindow, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        MainWindow.Instances.add(self)

        '''the Instances static variable is used to keep track of instances in case
        of "save all ", quit->children too, and switching btw opend windows
        '''

        #in the app an instance window should be able to close itself on quiiting
        #dats the implication of using Qt.WA_DeleteOnclose


        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)

        fileSaveAllAction = self.createAction("Save A&ll", self.fileSaveAll, icon="filesave",tip="Save all files")

        fileCloseAction = self.createAction("&Close", self.close, QKeySequence.Close,"fileclose", "Close this editor")

        fileQuitAction = self.createAction("&Quit",self.fileQuit, "Ctrl+Q", "filequit", "close the application")
        editCopyAction = self.createAction("&Copy", self.editor.copy, QKeySequence.Copy, "editcopy", "copy to clipboard")

        self.windowMenu = self.menuBar().addAction("&Window")
        self.connect(self.windowMenu, SIGNAL("aboutToShow()"), self.updateWindowMenu)

        self.connect(self, SIGNAL("destroyed(QObject*)"), MainWindow.updateInstnces)

        self.filename = filename
        if self.filename.isEmpty():
            self.filename = QString("Unnamed-%d.txt" % MainWindow.NextId)
            MainWindow.NextId += 1
            self.editor.document().setModified(False)
            self.setWindowTitle("SDI TEXT eDITOR -%s", self.filename)
        else:
            self.loadFile()


    def closeEvent(self, *args, **kwargs):
        print("this is the close event")

    def loadFile(self):
        print("this is the loadfile function")

    def fileSave(self):
        print("this is the filesave")

    def fileSaveAs(self):
        print("this is the file save as")

    def fileNew(self):
        MainWindow().show()

    def fileOpen(self):
        filename = QFileDialog.getOpenFileName(self, "SDI TEXT editor -- Open File")
        if not filename.isEmpty():
            if not self.editor.document().isModified() and self.filename.startsWith("Unnamed"):
                self.filename = filename
                self.loadFile()
            else:
                MainWindow(filename).show()

    def fileSaveAll(self):
        count = 0
        for window in MainWindow.Instances:
            if isAlive(window) and window.editor.document().isModified():
                if window.fileSave():
                    count += 1
        self.statusBar().showMessage("Saved %d of % d files " %(count, len(MainWindow.Instances, 5000)))









app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()