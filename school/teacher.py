from PyQt5 import QtCore, QtGui, QtWidgets
from starter import *

class Ui_TeacherWindow(object):

    def setupUi(self, TeacherWindow):

        TeacherWindow.setObjectName("TeacherWindow")
        TeacherWindow.resize(414, 526)
        self.centralwidget = QtWidgets.QWidget(TeacherWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.teacherlabel = QtWidgets.QLabel(self.centralwidget)
        self.teacherlabel.setGeometry(QtCore.QRect(120, 30, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.teacherlabel.setFont(font)
        self.teacherlabel.setObjectName("teacherlabel")
        name = getname()
        self.teacherlabel.setText(f"Hello {name}")

        self.tenterid = QtWidgets.QLineEdit(self.centralwidget)
        self.tenterid.setGeometry(QtCore.QRect(220, 115, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.tenterid.setFont(font)
        self.tenterid.setObjectName("tenterid")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 90, 181, 81))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.enterscore = QtWidgets.QLineEdit(self.centralwidget)
        self.enterscore.setGeometry(QtCore.QRect(220, 175, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.enterscore.setFont(font)
        self.enterscore.setText("")
        self.enterscore.setObjectName("enterscore")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 181, 81))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.tsubmit = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.tsub())
        self.tsubmit.setGeometry(QtCore.QRect(280, 230, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tsubmit.setFont(font)
        self.tsubmit.setObjectName("tsubmit")
    
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(46, 280, 321, 192))
        self.textBrowser.setObjectName("textBrowser")
        a = display()
        self.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
f"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">{a}</span></p></body></html>")


        TeacherWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TeacherWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 414, 26))
        self.menubar.setObjectName("menubar")
        TeacherWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TeacherWindow)
        self.statusbar.setObjectName("statusbar")
        TeacherWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TeacherWindow)
        QtCore.QMetaObject.connectSlotsByName(TeacherWindow)

    def tsub(self):
        username = self.tenterid.text()
        score = self.enterscore.text()
        tmaker(username, score)
        smaker(username, score)
        self.enterscore.setText("")
        self.tenterid.setText("")
        a = display()
        self.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
f"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">{a}</span></p></body></html>")


    def retranslateUi(self, TeacherWindow):
        _translate = QtCore.QCoreApplication.translate
        TeacherWindow.setWindowTitle(_translate("TeacherWindow", "MainWindow"))
        # self.teacherlabel.setText(_translate("TeacherWindow", "Hello"))
        self.label.setText(_translate("TeacherWindow", "Enter students ID"))
        self.label_3.setText(_translate("TeacherWindow", "Enter score"))
        self.tsubmit.setText(_translate("TeacherWindow", "SUBMIT"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TeacherWindow = QtWidgets.QMainWindow()
    ui = Ui_TeacherWindow()
    ui.setupUi(TeacherWindow)
    TeacherWindow.show()
    sys.exit(app.exec_())
