__author__ = '0code'

from PyQt4.QtCore import *
from PyQt4.QtGui import  *
import PyQt4.QtNetwork
import sys


PORT = 4444

class BuildingServicesDlg(QPushButton):
    def __init__(self,parent=None):
        super(BuildingServicesDlg, self).__init__("&Close Server",parent)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.loadBookings()
        
        self.tcpServer = TcpServer(self)
        if not self.tcpServer.listen(QHostAddress("0.0.0.0"), PORT):
            QMessageBox.critical(self, "Building "
                                       "SErvicess SErver",
                                 QString("Failed to start server %1").arg(self.tcpServer.errorString()))
            self.close()
            return
        self.connect(self, SIGNAL("clicked()"), self.close)
