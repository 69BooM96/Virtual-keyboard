from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from time import sleep
import os
import socket
import webbrowser

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2030, 1010)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(12, 12, 12);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(470, 0, 211, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(12, 12, 12);\n"
"color: rgb(255, 255, 255);\n"
"border: 12px solid rgb(80, 162, 61);\n"
"border-radius: 25;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 230, 401, 251))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(12, 12, 12);\n"
"color: rgb(255, 255, 255);\n"
"border: 12px solid rgb(80, 162, 61);\n"
"border-radius: 125;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1510, 230, 401, 251))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(12, 12, 12);\n"
"color: rgb(255, 255, 255);\n"
"border: 12px solid rgb(80, 162, 61);\n"
"border-radius: 125;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1900, 840, 111, 111))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(12, 12, 12);\n"
"color: rgb(255, 255, 255);\n"
"border: 12px solid rgb(80, 162, 61);\n"
"border-radius: 55;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(1050, 230, 401, 251))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(12, 12, 12);\n"
"color: rgb(255, 255, 255);\n"
"border: 12px solid rgb(80, 162, 61);\n"
"border-radius: 125;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(590, 230, 401, 251))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(12, 12, 12);\n"
"color: rgb(255, 255, 255);\n"
"border: 12px solid rgb(80, 162, 61);\n"
"border-radius: 125;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(50, 0, 211, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(12, 12, 12);\n"
"color: rgb(255, 255, 255);\n"
"border: 12px solid rgb(80, 162, 61);\n"
"border-radius: 25;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(260, 0, 211, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(12, 12, 12);\n"
"color: rgb(255, 255, 255);\n"
"border: 12px solid rgb(80, 162, 61);\n"
"border-radius: 25;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, -110, 61, 1131))
        self.label.setStyleSheet("background-color: rgb(80, 162, 61);\n"
"color: rgb(255, 255, 255);\n"
"border: 12px solid rgb(80, 162, 61);\n"
"border-radius: 125;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-10, -70, 741, 131))
        self.label_2.setStyleSheet("background-color: rgb(80, 162, 61);\n"
"color: rgb(255, 255, 255);\n"
"border: 12px solid rgb(80, 162, 61);\n"
"border-radius: 35;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 860, 1801, 91))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(12, 12, 12);\n"
"color: rgb(255, 255, 255);\n"
"border: 12px solid rgb(80, 162, 61);\n"
"border-radius: 45;")
        self.label_3.setObjectName("label_3")
        self.label.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.label_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KL_Menu V.0.1.1"))
        self.pushButton.setText(_translate("MainWindow", "Local IP"))
        self.pushButton_2.setText(_translate("MainWindow", "Red"))
        self.pushButton_3.setText(_translate("MainWindow", "Orange"))
        self.pushButton_4.setText(_translate("MainWindow", "i"))
        self.pushButton_5.setText(_translate("MainWindow", "Blue"))
        self.pushButton_6.setText(_translate("MainWindow", "Green"))
        self.pushButton_7.setText(_translate("MainWindow", "Github"))
        self.pushButton_8.setText(_translate("MainWindow", "Support"))
        self.label_3.setText(_translate("MainWindow", "   V.0.1.1"))

    def add_functions(self):
        self.pushButton.clicked.connect(lambda: self.L_L(self.pushButton.text()))
        self.pushButton_2.clicked.connect(lambda: self.K_L(self.pushButton_2.text()))
        self.pushButton_3.clicked.connect(lambda: self.K_L2(self.pushButton_3.text()))
        self.pushButton_4.clicked.connect(lambda: self.info(self.pushButton_4.text()))
        self.pushButton_5.clicked.connect(lambda: self.K_L3(self.pushButton_5.text()))
        self.pushButton_6.clicked.connect(lambda: self.K_L4(self.pushButton_6.text()))
        self.pushButton_7.clicked.connect(lambda: self.Github(self.pushButton_7.text()))
        self.pushButton_8.clicked.connect(lambda: self.Support(self.pushButton_8.text()))

    def L_L(self, L):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        print(s.getsockname()[0])
        msg = QMessageBox()
        msg.setWindowTitle("Local IP")
        msg.setText(s.getsockname()[0])
        msg.setIcon(QMessageBox.Warning)

        msg.exec_()

    def Github(self, K):
        webbrowser.open("https://github.com/69BooM96")

    def Support(self, D):
        msg = QMessageBox()
        msg.setWindowTitle("Support")
        msg.setText("Sorry no support...")
        msg.setIcon(QMessageBox.Warning)

        msg.exec_()

    def K_L(self, F):
        msg = QMessageBox()
        msg.setWindowTitle("Warning!")
        msg.setText("Run the program on PC")
        msg.setIcon(QMessageBox.Warning)

        msg.exec_()

        os.startfile("/storage/emulated/0/Phone version/Program files/red.py")

    def K_L2(self, Z):
        msg = QMessageBox()
        msg.setWindowTitle("Warning!")
        msg.setText("Run the program on PC")
        msg.setIcon(QMessageBox.Warning)

        msg.exec_()

        os.startfile("Green.py.py")

    def K_L3(self, X):
        msg = QMessageBox()
        msg.setWindowTitle("Warning!")
        msg.setText("Run the program on PC")
        msg.setIcon(QMessageBox.Warning)

        msg.exec_()

        os.startfile("Blue.py")

    def K_L4(self, C):
        msg = QMessageBox()
        msg.setWindowTitle("Warning!")
        msg.setText("Run the program on PC")
        msg.setIcon(QMessageBox.Warning)

        msg.exec_()

        os.startfile("orange.py")

    def info(self, i):
        msg = QMessageBox()
        msg.setWindowTitle("info")
        msg.setText("KL_menu V.0.1.1 Client")
        msg.setIcon(QMessageBox.Warning)

        msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
