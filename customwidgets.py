__author__ = '0code'



from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys


class CustomDlg(QDialog):
    def __init__(self, parent=None):
        super(CustomDlg, self).__init__(parent)

        self.setWindowTitle("Add Contact")


        fnameLabel = QLabel("Forename: ")
        snameLabel = QLabel("Surname: ")
        catLabel = QLabel("Category: ")
        compLabel = QLabel("Company: ")
        addLabel = QLabel("Address: ")
        phoneLabel = QLabel("Phone: ")
        mobileLabel = QLabel("Mobile: ")
        faxLabel = QLabel("Fax: ")
        emailLabel = QLabel("Email: ")


        self.fnameEdit = QLineEdit()
        self.snameEdit = QLineEdit()
        self.compnameEdit = QLineEdit()
        self.addEdit = QLineEdit()
        self.phoneEdit = QLineEdit()
        self.mobileEdit = QLineEdit()
        self.faxEdit = QLineEdit()
        self.emailEdit = QLineEdit()
        self.emailEdit.setObjectName("emailE")

        self.busbox = QComboBox()
        self.buslist = ["Business", "Marketing", "Technology"]
        self.busbox.addItems(self.buslist)

        layout = QGridLayout()
        layout.addWidget(fnameLabel, 0,0)
        layout.addWidget(self.fnameEdit, 0,1)
        layout.addWidget(snameLabel, 0,2)
        layout.addWidget(self.snameEdit, 0,3)
        layout.addWidget(catLabel, 1,0)
        layout.addWidget(self.busbox, 1,1)
        layout.addWidget(compLabel, 1,2)
        layout.addWidget(self.compnameEdit, 1,3)
        layout.addWidget(addLabel, 2,0)
        layout.addWidget(self.addEdit, 2,1)
        layout.addWidget(phoneLabel, 3,0)
        layout.addWidget(self.phoneEdit, 3,1)
        layout.addWidget(mobileLabel, 3,2)
        layout.addWidget(self.mobileEdit, 3,3)
        layout.addWidget(emailLabel, 4, 0)
        layout.addWidget(self.emailEdit,4,1 )


        self.btnBox = QDialogButtonBox()
        layout.addWidget(self.btnBox)

        self.lineedits = (self.fnameEdit, self.snameEdit, self.compnameEdit, self.phoneEdit)
        for lineEdits in self.lineedits:
            lineEdits.setProperty("mandatory", QVariant(True))
            self.connect(lineEdits, SIGNAL("textEdited(QString)"), self.updateUi)

            #using stuffs like that of the css/html selector
            # emailu = QlineEdit()
            #emailu.setObjectName("emailUser")
            #use e.g widget#objectname example QLineEdit#emailUser
            #another kind of selector
            # u know QcomboBox has an arrow at the right side
            #then use the selector : QCOmbobox::drop-down in the Stylesheet
            #also QCheckBox:checked

        Stylesheet = """
            QDialog{background-color:#34495e;}
            QComboBox {color:darkblue;}
            QComboBox::drop-down{ background-color:#fff;color:#1abc9c}
            QLabel {color:#fff;}
            QLineEdit[mandatory="true"]{
            background-color: rgb(255, 255, 127);
            color:darkblue;
            }
            QLineEdit#emailE{
             background-color:green;
             color:red;}
            """
        self.setStyleSheet(Stylesheet)



        self.setLayout(layout)
    def updateUi(self):
        mandatory = self.compnameEdit.property("mandatory").toBool()
        if self.busbox.currentText() == "Business":
            if not mandatory:
                self.compnameEdit.setProperty("mandatory", QVariant(True))
            elif mandatory: self.compnameEdit.setProperty("mandatory", QVariant(False))
            if mandatory != self.compnameEdit.property("mandatory").toBool():

                self.setStyleSheet(CustomDlg.Stylesheet)
            enable = True
            for lineEdit in self.lineedits:
                if lineEdit.property("mandatory").toBool() and lineEdit.text().isEmpty():
                    enable = False
                    break
            self.btnBox.button(QDialogButtonBox.Ok).setEnabled(enable)






app = QApplication(sys.argv)
cs = CustomDlg()
cs.show()
app.exec_()
