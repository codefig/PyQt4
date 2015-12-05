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

        colorlist = ["Red", "Green", "Yellow", "Black"]
        colorLabel = QLabel("Color :")
        self.colorComboBox = QComboBox()
        self.colorComboBox.addItems(colorlist)
        seatsLabel = QLabel("Seats ")
        self.seatSpinBox = QSpinBox()


        self.stackedWidget = QStackedWidget() #declares the qstackwidget stuff

        carWidget = QWidget()
        carLayout = QGridLayout()
        carLayout.addWidget(colorLabel,0, 0)
        carLayout.addWidget(self.colorComboBox,0,1)
        carLayout.addWidget(seatsLabel,1,0)
        carLayout.addWidget(self.seatSpinBox,1,1)
        carWidget.setLayout(carLayout)

        self.stackedWidget.addWidget(carWidget)

        vehicleList = ["Van", "Car", "Lorry", "Truck"]

        vehicleLabel = QLabel("Vehicle: ")
        self.vehicleComboBox = QComboBox()
        self.vehicleComboBox.addItems(vehicleList)

        mileageLabel = QLabel("mileage: ")
        self.mileageLabel = QLabel("")

        topLayout = QHBoxLayout()
        topLayout.addWidget(vehicleLabel)
        topLayout.addWidget(self.vehicleComboBox)

        bottomLayout =QHBoxLayout()
        bottomLayout.addWidget(mileageLabel)
        bottomLayout.addWidget(self.mileageLabel)

        self.buttonBox = QDoubleSpinBox()

        self.weightSpinBox = QSpinBox()


        self.connect(self.buttonBox, SIGNAL("accepted()"), self.accept)
        self.connect(self.buttonBox, SIGNAL("rejected()"), self.reject)
        self.connect(self.vehicleComboBox, SIGNAL("currentIndexChanged(QString)"), self.setWidgetStack)
        self.connect(self.weightSpinBox, SIGNAL("valueChanged(int"), self.weightChanged)

        layout = QVBoxLayout()
        layout.addLayout(topLayout)
        layout.addWidget(self.stackedWidget)
        layout.addLayout(bottomLayout)
        layout.addWidget(self.buttonBox)

        self.setLayout(layout)

    def setWidgetStack(self,text):
        if(text == "Car"):
            self.stackedWidget.setCurrentIndex(0)
            self.mileageLabel.setText("100 miles")
        else:
            self.stackedWidget.setCurrentIndex(1)
            self.weightChanged(self.weightSpinBox.value())

    def weightChanged(self, amount):
        self.mileageLabel.setText("%d miles " % (8000/ amount))



app = QApplication(sys.argv)
window = Window()
window.show()
app.exec_()