import sys
import os
import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import socket


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("KL_Menu V.0.1.1")
        MainWindow.setFixedSize(470, 600)
        MainWindow.setStyleSheet("background-color: rgb(22, 22, 22);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(400, 510, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 7px solid rgb(80, 162, 61);\n"
"border-radius: 30;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 80, 261, 261))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 12px solid rgb(80, 162, 61);\n"
"border-radius: 125;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 70, 261, 261))
        self.label.setStyleSheet("background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 12px solid rgb(104, 197, 80);\n"
"border-radius: 125;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 520, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 7px solid rgb(80, 162, 61);\n"
"border-radius: 25;")
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 0, 101, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 4px solid rgb(80, 162, 61);\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(110, 0, 101, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 4px solid rgb(80, 162, 61);\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(210, 0, 101, 31))
        self.pushButton_5.setStyleSheet("background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 4px solid rgb(80, 162, 61);\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-10, 0, 341, 31))
        self.label_2.setStyleSheet("background-color: rgb(80, 162, 61);\n"
"color: rgb(255, 255, 255);\n"
"border: 4px solid rgb(80, 162, 61);\n"
"border-radius: 15;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(-20, 30, 31, 571))
        self.label_4.setStyleSheet("background-color: rgb(80, 162, 61);\n"
"color: rgb(255, 255, 255);\n"
"border: 4px solid rgb(80, 162, 61);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_2.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label_3.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.label_4.raise_()
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
        self.pushButton.setText(_translate("MainWindow", "i"))
        self.pushButton_2.setText(_translate("MainWindow", "Start"))
        self.label_3.setText(_translate("MainWindow", "            V.0.1.1"))
        self.pushButton_3.setText(_translate("MainWindow", "Github"))
        self.pushButton_4.setText(_translate("MainWindow", "Support"))
        self.pushButton_5.setText(_translate("MainWindow", "Local IP"))

    def add_functions(self):
        self.pushButton.clicked.connect(lambda: self.I_L(self.pushButton.text()))
        self.pushButton_2.clicked.connect(lambda: self.K_L(self.pushButton_2.text()))
        self.pushButton_3.clicked.connect(lambda: self.Github(self.pushButton_3.text()))
        self.pushButton_4.clicked.connect(lambda: self.Support(self.pushButton_4.text()))
        self.pushButton_5.clicked.connect(lambda: self.L_L(self.pushButton_5.text()))



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
        webbrowser.open("https://github.com/69BooM96/Virtual-keyboard")

    def Support(self, D):
        msg = QMessageBox()
        msg.setWindowTitle("Support")
        msg.setText("No Support!")
        msg.setIcon(QMessageBox.Warning)

        msg.exec_()

    def K_L(self, F):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        print(s.getsockname()[0])
        file = open("Server.py", "w", encoding="utf-8")
        file.write("import os\nfrom time import sleep\nimport socket\nimport webbrowser\nimport pyautogui\nimport mouse\n\nserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\nserver.bind(('")
        file = open("Server.py", "a", encoding="utf-8")
        file.write("".join(s.getsockname()[0]))
        file = open("Server.py", "a", encoding="utf-8")
        file.write("', 7842))\nserver.listen(1)\nos.system('color 02')\nprint('Start...')\nprint('Waiting for connection...')\nprint('                  #Connected devices#')")
        file = open("Server - копия.py", encoding="utf-8")
        sf = file.read()
        print(sf)
        file = open("Server.py", "a", encoding="utf-8")
        file.write("".join(sf))
        file.close()
        os.startfile("Server.py")

    def I_L(self, H):
        msg = QMessageBox()
        msg.setWindowTitle("Info")
        msg.setText("Info:KL V.0.1.1")
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
