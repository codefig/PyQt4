__author__ = '0code'

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys


class FractionSlide(QWidget):
    XMARGIN = 12.0
    YMARGIN  = 5.0
    WSTRING = "999"

    def __init__(self, numerator=0, denominator=0, parent=None):
        super(FractionSlide, self).__init__(parent)
        self.__numerator = numerator
        self.__denominator = denominator
        self.setFocusPolicy(Qt.WheelFocus)
        self.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)

    def decimal(self):
        return self.__numerator /float(self.__denominator)

    def fraction(self):
        return self.__numerator, self.__denominator

    def setFraction(self, numerator, denominator=None):
        if denominator is not None:
            if 3 <= denominator <= 60:
                self.__denominator  = denominator
            else:
                raise ValueError, "denominator out of range"
            if 0 <= numerator <= self.__denominator:
                self.__numerator = numerator
            else:
                raise ValueError, "numerator out of range"
            self.update()
            self.updateGeometry()
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.moveSlider(event.x())
            event.accept()
        else:
            QWidget.mousePressEvent(self, event)

    def moveSlider(self):
        span = self.width() - (FractionSlide.XMARGIN * 2)
        offset = span - x + FractionSlide.XMARGIN
        numerator = int(round(self.__denominator * (1.0 - (offset /span))))
        numerator = max(0, min(numerator, self.__denominator))
        if numerator != self.__numerator:
            self.__numerator = numerator
            self.emit(SIGNAL("valueChanged(int, int)"),self.__numerator, self.__denominator)
            self.update()
