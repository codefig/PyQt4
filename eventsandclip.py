__author__ = '0code'

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class Widget(QWidget):
    def __init__(self,parent=None):
        super(Widget, self).__init__(parent)

        self.justDoubleClicked = False
        self.key  = QString()
        self.text = QString()
        self.message = QString()

    def paintEvent(self, event):
        text = self.text
        i = text.indexOf("\n\n")
        if i>= 0:
            text = text.left(i)
        if not self.key.isEmpty():
            text += "\n\n You pressed: %s " % self.key
        painter = QPainter(self)
        painter.setRenderHint(QPainter.TextAntialiasing)
        painter.drawText(self.rect(), Qt.AlignCenter, text)
        if self.message:
            painter.drawText(self.rect(), Qt.AlignBottom|Qt.AlignCenter, self.message)
            QTimer.singleShot(5000, self.message.clear)
            QTimer.singleShot(5000, self.update)

    def resizeEvent(self, event):
        self.text = QString("REsizied to QSize (%d , %d)" %(event.size().width, event.size.height()))
        self.update()

    def keyPressEvent(self, event):
        self.key = QString()
        if event.key() == Qt.key_Home:
            self.key = "Home"
        elif event.key() == Qt.key_End:
            self.key = "End"
        elif event.key() == Qt.Key_PageUp:
            if event.modifiers() & Qt.ControlModifier:
                self.key = "Ctrl&PageUp"
            else:
                self.key = "PageUp"
        elif event.key() == Qt.key_PageDown:
            if event.modifiers & Qt.ControlModifier:
                self.key = "Ctrl+PageDown"
            else:
                self.key = "PageDown"
        elif Qt.key_A <= event.key() <= Qt.key_Z:
            if event.modifiers() & Qt.ShiftModifier:
                self.key = "Shift+"
            self.key += event.text()
        if self.key:
            self.key = QString(self.key)
            self.update()
        else:
            QWidget.keyPressEvent(self,event)

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        oneAction = menu.addAction("&One")
        twoAction = menu.addAction("&Two")
        self.connect(oneAction, SIGNAL("triggered()"), self.one)
        self.connect(twoAction, SIGNAL("triggered()"), self.two)
        if not self.message:
            menu.addSeparator()
            threeAction  = menu.addAction("Thre&e")
            self.connect(threeAction, SIGNAL("triggered()"), self.three)
            menu.exec_(event.globalPos())

    def mouseDoubleClickEvent(self, QMouseEvent):
        self.justDoubleClicked = True
        self.text = QString("Double-clicked")
        self.update()

    def mouseReleaseEvent(self, QMouseEvent):
        if self.justDoubleClicked:
            self.justDoubleClicked = False
        else:
            self.setMouseTracking(not self.hasMouseTracking())
            if self.hasMouseTracking():
                self.text = QString("Mouse tracking is on \n Try moving the mouse \n"
                                    "Single click to switch it off")
            else:
                self.text = QString("mouse tracking is off\n"
                                    "Single click to switch it on")
            self.update()
    def mouseMoveEvent(self, event):
        if not self.justDoubleClicked:
            globalPos = self.mapToGlobal(event.pos())
            self.text = QString("the mouse is at QPOINT(%d, %d)in widget cords ")
            self.update()
    def event(self, event):
        if event.type() == QEvent.KeyPress and event.key() == Qt.Key_Tab:
            self.key = QString("Tab captured in event()")
            self.update()
            return True
        return QWidget.event(self,event)





