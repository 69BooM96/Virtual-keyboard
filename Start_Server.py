from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import socket
import os
import webbrowser

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(468, 615)
        MainWindow.setStyleSheet("background-color: rgb(12, 12, 12);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(400, 510, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(12, 12, 12);\n"
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
        self.pushButton_2.setStyleSheet("background-color: rgb(12, 12, 12);\n"
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
        self.label_3.setStyleSheet("background-color: rgb(12, 12, 12);\n"
"color: rgb(255, 255, 255);\n"
"border: 5px solid rgb(80, 162, 61);\n"
"border-radius: 25;")
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 0, 101, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(12, 12, 12);\n"
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
        self.pushButton_4.setStyleSheet("background-color: rgb(12, 12, 12);\n"
"color: rgb(255, 255, 255);\n"
"border: 4px solid rgb(80, 162, 61);\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(210, 0, 101, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(12, 12, 12);\n"
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
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(150, 440, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(12, 12, 12);\n"
"color: rgb(255, 255, 255);\n"
"border: 7px solid rgb(80, 162, 61);\n"
"border-radius: 30;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(200, 483, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_2.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label_3.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.label_4.raise_()
        self.pushButton_6.raise_()
        self.label_5.raise_()
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
        self.pushButton_6.setText(_translate("MainWindow", "Phone version"))
        self.label_5.setText(_translate("MainWindow", "Necessarily!"))

    def add_functions(self):
        self.pushButton.clicked.connect(lambda: self.I_L(self.pushButton.text()))
        self.pushButton_2.clicked.connect(lambda: self.K_L(self.pushButton_2.text()))
        self.pushButton_3.clicked.connect(lambda: self.Github(self.pushButton_3.text()))
        self.pushButton_4.clicked.connect(lambda: self.Support(self.pushButton_4.text()))
        self.pushButton_5.clicked.connect(lambda: self.L_L(self.pushButton_5.text()))
        self.pushButton_6.clicked.connect(lambda: self.P_V(self.pushButton_6.text()))




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
        msg.setText("Info:KL_Menu V.0.1.1 Server")
        msg.setIcon(QMessageBox.Warning)

        msg.exec_()

    def P_V(self, V):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        print(s.getsockname()[0])
        file = open("Green.py", "w", encoding="utf-8")
        file.write("from PyQt5 import QtCore, QtGui, QtWidgets\nimport socket\n\nfrom PyQt5.QtWidgets import QVBoxLayout, QButtonGroup, QPushButton\n\nclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\nclient.connect(('")
        file = open("Green.py", "a", encoding="utf-8")
        file.write("".join(s.getsockname()[0]))
        file = open("Green.py", "a", encoding="utf-8")
        file.write("', 7842))")
        file = open("Green - копия.py", encoding="utf-8")
        sf1 = file.read()
        print(sf1)
        file = open("Green.py", "a", encoding="utf-8")
        file.write("".join(sf1))

        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        file = open("Blue.py", "w", encoding="utf-8")
        file.write("from PyQt5 import QtCore, QtGui, QtWidgets\nimport socket\n\nfrom PyQt5.QtWidgets import QVBoxLayout, QButtonGroup, QPushButton\n\nclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\nclient.connect(('")
        file = open("Blue.py", "a", encoding="utf-8")
        file.write("".join(s.getsockname()[0]))
        file = open("Blue.py", "a", encoding="utf-8")
        file.write("', 7842))")
        file = open("Blue - копия.py", encoding="utf-8")
        sf2 = file.read()
        print(sf2)
        file = open("Blue.py", "a", encoding="utf-8")
        file.write("".join(sf2))

        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        file = open("red.py", "w", encoding="utf-8")
        file.write("from PyQt5 import QtCore, QtGui, QtWidgets\nimport socket\n\nfrom PyQt5.QtWidgets import QVBoxLayout, QButtonGroup, QPushButton\n\nclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\nclient.connect(('")
        file = open("red.py", "a", encoding="utf-8")
        file.write("".join(s.getsockname()[0]))
        file = open("red.py", "a", encoding="utf-8")
        file.write("', 7842))")
        file = open("red - копия.py", encoding="utf-8")
        sf3 = file.read()
        print(sf3)
        file = open("red.py", "a", encoding="utf-8")
        file.write("".join(sf3))

        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        file = open("orange.py", "w", encoding="utf-8")
        file.write("from PyQt5 import QtCore, QtGui, QtWidgets\nimport socket\n\nfrom PyQt5.QtWidgets import QVBoxLayout, QButtonGroup, QPushButton\n\nclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\nclient.connect(('")
        file = open("orange.py", "a", encoding="utf-8")
        file.write("".join(s.getsockname()[0]))
        file = open("orange.py", "a", encoding="utf-8")
        file.write("', 7842))")
        file = open("orange - копия.py", encoding="utf-8")
        sf4 = file.read()
        print(sf4)
        file = open("orange.py", "a", encoding="utf-8")
        file.write("".join(sf4))

        file.close()

        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        msg = QMessageBox()
        msg.setWindowTitle("Info")
        msg.setText("File successfully created on desktop!")
        msg.setIcon(QMessageBox.Warning)

        msg.exec_()

        file = open("red.py", encoding="utf-8")
        sg1 = file.read()

        file = open("orange.py", encoding="utf-8")
        sg2 = file.read()

        file = open("Green.py", encoding="utf-8")
        sg3 = file.read()

        file = open("Blue.py", encoding="utf-8")
        sg4 = file.read()

        file = open("Start_K.py", encoding="utf-8")
        sr = file.read()

        path = "C:/Users/студент.BestLaptop-ПК/Desktop"
        projectname = "Phone version"

        fullPath = os.path.join(path, projectname)
        if not os.path.exists(fullPath):
            os.mkdir(fullPath)
            file = open("C:/Users/студент.BestLaptop-ПК/Desktop/Phone version/Blue.py", "a",
                        encoding="utf-8")
            file.write("".join(sg4))

            file = open("C:/Users/студент.BestLaptop-ПК/Desktop/Phone version/Green.py", "a",
                        encoding="utf-8")
            file.write("".join(sg3))

            file = open("C:/Users/студент.BestLaptop-ПК/Desktop/Phone version/orange.py", "a",
                        encoding="utf-8")
            file.write("".join(sg2))

            file = open("C:/Users/студент.BestLaptop-ПК/Desktop/Phone version/red.py", "a",
                        encoding="utf-8")
            file.write("".join(sg1))
            file.close()







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
