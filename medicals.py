__author__ = '0code'


#this is a revamp of a java project i made for a student
#i am now trying to write the gui in python with PyQt also
# 2:54 AM 11/28/2015


from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys




class WelcomePage(QDialog):
    def __init__(self,parent=None):
        super(WelcomePage, self).__init__(parent)

        self.setWindowTitle("Diagnosis App !")
        self.setGeometry(300,300, 500, 500)



        self.ledit = QTextEdit()
        self.nextbtn = QPushButton("back")
        self.ledit.setReadOnly(True)

        text = "Welcome to Our Medical Diagnosis Application.. this app is going to help you" \
               "Malaria and Typhoid Basically by asking you a couple of questions while you answer" \
               "You can click the Next Button Below to start the Application Usage!"
        layout = QVBoxLayout()


        text = text.upper()
        self.ledit.setText(text)

        layout.addWidget(self.ledit)
        layout.addWidget(self.nextbtn)
        self.setObjectName("wpage")

        self.connect(self.nextbtn,SIGNAL("clicked()"), self.showNext)

        #initialising other pages
        self.setLayout(layout)

    def showNext(self):
        self.parent = QuestionsPage()
        self.hide()
        self.parent.show()







class QuestionsPage(QWidget):
    def __init__(self, parent=None):
        super(QuestionsPage, self).__init__(parent)

        self.questPane = QTextEdit()
        self.yesBtn = QPushButton("Yes")
        self.noBtn = QPushButton("No")
        self.nextBtn = QPushButton("Next")

        self.layout = QHBoxLayout()

        self.layout.addWidget(self.questPane)
        self.layout.addWidget(self.yesBtn)
        self.layout.addWidget(self.noBtn)
        self.layout.addWidget(self.nextBtn)

        self.connect(self.yesBtn, SIGNAL("clicked()"), self.showNext)
        self.setLayout(self.layout)

    def showNext(self):
        self.otherpage = WelcomePage()
        self.hide()
        self.otherpage.show()




app = QApplication(sys.argv)
wlcom = QuestionsPage()
wlcom.show()
app.exec_()
