from PyQt5 import QtCore, QtGui, QtWidgets
from teacher import Ui_TeacherWindow
from student import Ui_StudentWindow
from starter import *

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(465, 313)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.school_label = QtWidgets.QLabel(self.centralwidget)
        self.school_label.setGeometry(QtCore.QRect(180, 20, 131, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.school_label.setFont(font)
        self.school_label.setObjectName("school_label")

        self.enterid = QtWidgets.QLineEdit(self.centralwidget)
        self.enterid.setGeometry(QtCore.QRect(270, 125, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.enterid.setFont(font)
        self.enterid.setObjectName("enterid")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 161, 81))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.idsubmit1 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.idsub())
        self.idsubmit1.setGeometry(QtCore.QRect(330, 240, 111, 31))
        self.idsubmit1.setObjectName("idsubmit1")

        self.enterid_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.enterid_2.setGeometry(QtCore.QRect(270, 185, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.enterid_2.setFont(font)
        self.enterid_2.setObjectName("enterid_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 160, 221, 81))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 465, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def idsub(self):
        a = self.enterid.text()
        b = self.enterid_2.text()
        self.enterid.setText("")
        self.enterid_2.setText("")
        a = getjob(a,b)
        if a=="s":
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_StudentWindow()
            self.ui.setupUi(self.window)
            self.window.show()
        elif a=="t":
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_TeacherWindow()
            self.ui.setupUi(self.window)
            self.window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.school_label.setText(_translate("MainWindow", "SCHOOL"))
        self.label_2.setText(_translate("MainWindow", "Enter your ID"))
        self.idsubmit1.setText(_translate("MainWindow", "SUBMIT"))
        self.label_3.setText(_translate("MainWindow", "Enter your password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
