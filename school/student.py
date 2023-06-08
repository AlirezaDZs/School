from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import messagebox
import sys
from starter import *

class Ui_StudentWindow(object):

    def setupUi(self, StudentWindow):

        StudentWindow.setObjectName("StudentWindow")
        StudentWindow.resize(257, 377)
        self.centralwidget = QtWidgets.QWidget(StudentWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 241, 321))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.label11 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label11.setAlignment(QtCore.Qt.AlignCenter)
        self.label11.setFont(font)
        self.label11.setObjectName("label11")

        self.gridLayout.addWidget(self.label11, 1, 0, 1, 1)
        self.label21 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label21.setAlignment(QtCore.Qt.AlignCenter)
        self.label21.setFont(font)
        self.label21.setObjectName("label21")

        self.gridLayout.addWidget(self.label21, 2, 0, 1, 1)
        self.label31 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label31.setAlignment(QtCore.Qt.AlignCenter)
        self.label31.setFont(font)
        self.label31.setObjectName("label31")

        self.gridLayout.addWidget(self.label31, 3, 0, 1, 1)
        self.label22 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label22.setAlignment(QtCore.Qt.AlignCenter)
        self.label22.setFont(font)
        self.label22.setObjectName("label22")

        self.gridLayout.addWidget(self.label22, 2, 1, 1, 1)
        self.label12 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label12.setAlignment(QtCore.Qt.AlignCenter)
        self.label12.setFont(font)
        self.label12.setObjectName("label12")

        self.gridLayout.addWidget(self.label12, 1, 1, 1, 1)
        self.label32 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label32.setAlignment(QtCore.Qt.AlignCenter)
        self.label32.setFont(font)
        self.label32.setObjectName("label32")

        self.gridLayout.addWidget(self.label32, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        StudentWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StudentWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 257, 26))
        self.menubar.setObjectName("menubar")
        StudentWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(StudentWindow)
        self.statusbar.setObjectName("statusbar")
        StudentWindow.setStatusBar(self.statusbar)

        self.retranslateUi(StudentWindow)
        QtCore.QMetaObject.connectSlotsByName(StudentWindow)

        name = getname()
        self.label.setText(f"Hello {name}")
        try:
            f = open(f"{name}.txt","r")
            f3 = f.read()
            f.close()
            f3 = ppp(f3)
            for i in range(0,len(f3),2):
                if f3[i]=="math":
                    self.label12.setText(f"{f3[i+1]}")
                elif f3[i]=="phy":
                    self.label32.setText(f"{f3[i+1]}")
                elif f3[i]=="chem":
                    self.label22.setText(f"{f3[i+1]}")
        except FileNotFoundError:
            messagebox.showinfo(title="SORRY!",message="No score is given yet!")
            sys.exit()



    def retranslateUi(self, StudentWindow):
        _translate = QtCore.QCoreApplication.translate
        StudentWindow.setWindowTitle(_translate("StudentWindow", "MainWindow"))
        self.label11.setText(_translate("StudentWindow", "Math"))
        self.label21.setText(_translate("StudentWindow", "Chemistry"))
        self.label31.setText(_translate("StudentWindow", "Physics"))
        self.label22.setText(_translate("StudentWindow", "No score yet"))
        self.label12.setText(_translate("StudentWindow", "No score yet"))
        self.label32.setText(_translate("StudentWindow", "No score yet"))
        self.label.setText(_translate("StudentWindow", "Hello"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    StudentWindow = QtWidgets.QMainWindow()
    ui = Ui_StudentWindow()
    ui.setupUi(StudentWindow)
    StudentWindow.show()
    sys.exit(app.exec_())
