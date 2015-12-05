__author__ = '0code'



from PyQt4.QtGui import *
from PyQt4.QtCore import  *
from PyQt4.QtNetwork import *
import sys

PORT = 4444
SIZEOF_UINT16 =0


class BuildingServicesClient(QWidget):
    """
        this is the class of the client
    """
    def __init__(self,parent=None):
        super(BuildingServicesClient, self).__init__(parent)

        layout = QGridLayout()
        roomLabel  = QLabel("Room: ")
        self.roomEdit = QLineEdit()

        dateLabel = QLabel("Date: ")
        self.dateEdit = QDateEdit()

        self.responseLabel = QLabel("Response: ")
        self.responseEdit = QLineEdit()

        self.bookBtn = QPushButton("&Book")
        self.unbookBtn = QPushButton("&Unbook")
        self.quitBtn = QPushButton("&Quit")

        buttonLayout = QGridLayout()
        buttonLayout.addWidget(self.bookBtn,0, 1)
        buttonLayout.addWidget(self.unbookBtn, 0, 2)
        buttonLayout.addWidget(self.quitBtn, 0, 3)

        layout.addWidget(roomLabel, 0, 0)
        layout.addWidget(self.roomEdit, 0,1)
        layout.addWidget(dateLabel, 0 ,2)
        layout.addWidget(self.dateEdit,0,3)
        layout.addWidget(self.responseLabel,1,0)
        layout.addWidget(self.responseEdit, 1,1)
        layout.addLayout(buttonLayout,2,1)
        self.setWindowTitle("Building Services")
        self.setLayout(layout)

        self.socket = QTcpSocket()
        self.nextBlockSize = 0
        self.request = None

        self.connect(self.socket, SIGNAL("connected()"), self.sendRequest)
        self.connect(self.socket, SIGNAL("readyRead()"), self.readResponse)
        self.connect(self.socket, SIGNAL("diconnected()"), self.serverHasStopped)
        self.connect(self.socket, SIGNAL("error(QAbstractSocket::SocketError)"),self.serverHasError)

        self.connect(self.roomEdit, SIGNAL("textEdited(QString)"), self.updateUi)
        self.connect(self.dateEdit, SIGNAL("dateChanged(QDate)"), self.updateUi)
        self.connect(self.bookBtn, SIGNAL("clicked()"), self.book)
        self.connect(self.unbookBtn, SIGNAL("clicked()"), self.unBook)
        self.connect(self.quitBtn, SIGNAL("clicked()"), self.close)

    def updateUi(self):
        enabled = False
        if not self.roomEdit.text().isEmpty() and self.dateEdit.date() > QDate.currentDate():
            enabled = True
        if self.request is not None:
            enabled = False
        self.bookBtn.setEnabled(enabled)
        self.unbookBtn.setEnabled(enabled)

    def closeEvent(self, event):
        self.socket.close()
        event.accept()

    def book(self):
        self.issueRequest(QString("BOOK"), self.roomEdit.text(), self.dateEdit.date())
    def unBook(self):
        self.issueRequest(QString("UNBOOK"),self.roomEdit.text(), self.dateEdit.date())

    def issueRequest(self, action, room, date):
        self.request = QByteArray()
        stream = QDataStream(self.request, QIODevice.WriteOnly)
        stream.setVersion(QDataStream.Qt_4_2)
        stream.writeUInt16(0) #make it contain the initial value of 0
        stream << action << room << date #write into the stream
        stream.device().seek(0) #move writiing position to 0 beginning
        stream.writeUInt16(self.request.size() - SIZEOF_UINT16)
        self.updateUi()
        if self.socket.isOpen():
            self.socket.close()
        self.responseLabel.setText("Connecting to server ...")
        self.socket.connectToHost("localhost",PORT)

    def sendRequest(self):
        self.responseLabel.setText("Sending request...")
        self.nextBlockSize = 0
        self.socket.write(self.request)
        self.request = None

    def readResponse(self):
        stream = QDataStream(self.socket)
        stream.setVersion(QDataStream.Qt_4_2)

        while True:
            if self.nextBlockSize == 0:
                if self.socket.bytesAvailable() < SIZEOF_UINT16:
                    break
                self.nextBlockSize = stream.readUInt16()
            if self.socket.bytesAvailable() < self.nextBlockSize:
                break
            action = QString()
            room = QString()
            date = QDate()
            stream >> action >> room
            if action != "ERROR":
                stream >> date
            if action == "ERROR":
                msg = QString("Error : %1").arg(room)
            elif action == "BOOK":
                msg = QString("Booked room %1 for %2").arg(room).arg(date.toString(Qt.ISODate))
            elif action == "UNBOOK":
                msg = QString("Unbooked room %1 for %2").arg(room).arg(date.stoString(Qt.ISODate))
            self.responseLabel.setText(msg)
            self.updateUi()
            self.nextBlockSize = 0
    def serverHasStopped(self):
        self.responseLabel.setText("Error: connection closed by server")
        self.socket.close()

    def serverHasError(self, error):
        self.responseLabel.setText(QString("Error: %1").arg(self.socket.errorString()))
        self.socket.close()

app = QApplication(sys.argv)
window = BuildingServicesClient()
window.show()
app.exec_()