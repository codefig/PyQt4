__author__ = '0code'


from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import functools


PageSize = (612, 792)
PointSize = 10

MagicNumber = 0x70616765
FileVersion =1
Dirty = False


class GraphicsView(QGraphicsView):
    def __init__(self,parent=None):
        super(GraphicsView, self).__init__(parent)
        self.setDragMode(QGraphicsView.RubberBandDrag)
        self.setRenderHint(QPainter.Antialiasing)
        self.setRenderHint(QPainter.TextAntialiasing)

    def wheelEvent(self, event):
        factor = 1.41 ** (-event.delta() / 240.0)
        self.scale(factor, factor)

class MainForm(QDialog):
    def __init__(self,parent=None):
        super(MainForm, self).__init__(parent)

        self.filename = QString()
        self.copiedItem = QByteArray()
        self.pasteOffset = 5
        self.prevPoint = QPoint()
        self.addOffset = 5
        self.borders = []

        self.printer = QPrinter(QPrinter.HighResolution)
        self.printer.setPageSize(QPrinter.Letter)

        self.view = GraphicsView()
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0,0, PageSize[0], PageSize[1])
        self.addBorders()
        self.view.setScene(self.scene)

    def addBorders(self):
        self.borders = []
        rect = QRect(0,0, PageSize[0], PageSize[1])
        self.borders.append(self.scene.addRect(rect, Qt.yellow))
        margin = 5.25 * PointSize
        self.borders.append(self.scene.addRect(rect.adjusted(margin, margin, -margin, -margin)), Qt.yellow)



