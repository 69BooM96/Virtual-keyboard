

print("Connected#")
client.send("\n#@Connected@#".encode("utf-8"))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2030, 1010)
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 350, 171, 181))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 5px solid rgb(237, 28, 36);\n"
"border-radius: 20;")
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1340, 680, 191, 181))
        font = QtGui.QFont()
        font.setPointSize(55)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 5px solid rgb(237, 28, 36);\n"
"border-radius: 20;\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 710, 171, 181))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 5px solid rgb(237, 28, 36);\n"
"border-radius: 20;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 530, 171, 181))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 5px solid rgb(237, 28, 36);\n"
"border-radius: 20;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(370, 530, 171, 181))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 5px solid rgb(237, 28, 36);\n"
"border-radius: 20;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(1830, 500, 111, 181))
        font = QtGui.QFont()
        font.setPointSize(55)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 5px solid rgb(237, 28, 36);\n"
"border-radius: 20;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(1530, 290, 191, 121))
        font = QtGui.QFont()
        font.setPointSize(55)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 5px solid rgb(237, 28, 36);\n"
"border-radius: 20;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(1630, 500, 91, 181))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 5px solid rgb(237, 28, 36);\n"
"border-radius: 20;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(1340, 320, 191, 181))
        font = QtGui.QFont()
        font.setPointSize(55)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 5px solid rgb(237, 28, 36);\n"
"border-radius: 20;")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(370, 350, 171, 181))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 5px solid rgb(237, 28, 36);\n"
"border-radius: 20;")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(1530, 770, 191, 121))
        font = QtGui.QFont()
        font.setPointSize(55)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 5px solid rgb(237, 28, 36);\n"
"border-radius: 20;")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(570, 680, 741, 191))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 7px solid rgb(237, 28, 36);\n"
"border-radius: 30;")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(1310, 500, 111, 181))
        font = QtGui.QFont()
        font.setPointSize(55)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 5px solid rgb(237, 28, 36);\n"
"border-radius: 20;")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(1720, 680, 191, 181))
        font = QtGui.QFont()
        font.setPointSize(55)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 5px solid rgb(237, 28, 36);\n"
"border-radius: 20;")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(1720, 320, 191, 181))
        font = QtGui.QFont()
        font.setPointSize(55)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 5px solid rgb(237, 28, 36);\n"
"border-radius: 20;")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(30, 350, 171, 181))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 5px solid rgb(237, 28, 36);\n"
"border-radius: 20;")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(130, 10, 111, 131))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(237, 28, 36);\n"
"border-radius: 10;")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(240, 10, 111, 131))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(237, 28, 36);\n"
"border-radius: 10;")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(350, 10, 111, 131))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(237, 28, 36);\n"
"border-radius: 10;")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(460, 10, 111, 131))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(237, 28, 36);\n"
"border-radius: 10;")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_21.setGeometry(QtCore.QRect(570, 10, 111, 131))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(237, 28, 36);\n"
"border-radius: 10;")
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_22.setGeometry(QtCore.QRect(680, 10, 111, 131))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(237, 28, 36);\n"
"border-radius: 10;")
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_23.setGeometry(QtCore.QRect(790, 10, 111, 131))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(237, 28, 36);\n"
"border-radius: 10;")
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_24.setGeometry(QtCore.QRect(900, 10, 111, 131))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(237, 28, 36);\n"
"border-radius: 10;")
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_25.setGeometry(QtCore.QRect(1010, 10, 111, 131))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_25.setFont(font)
        self.pushButton_25.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(237, 28, 36);\n"
"border-radius: 10;")
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_26 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_26.setGeometry(QtCore.QRect(1120, 10, 111, 131))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_26.setFont(font)
        self.pushButton_26.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(237, 28, 36);\n"
"border-radius: 10;")
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_27 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_27.setGeometry(QtCore.QRect(1230, 10, 111, 131))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_27.setFont(font)
        self.pushButton_27.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(237, 28, 36);\n"
"border-radius: 10;")
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_28 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_28.setGeometry(QtCore.QRect(1340, 10, 111, 131))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_28.setFont(font)
        self.pushButton_28.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(237, 28, 36);\n"
"border-radius: 10;")
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_29 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_29.setGeometry(QtCore.QRect(130, 140, 111, 131))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_29.setFont(font)
        self.pushButton_29.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(237, 28, 36);\n"
"border-radius: 10;")
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_30 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_30.setGeometry(QtCore.QRect(10, 10, 111, 131))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_30.setFont(font)
        self.pushButton_30.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 7px solid rgb(237, 28, 36);\n"
"border-radius: 10;")
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_31 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_31.setGeometry(QtCore.QRect(240, 140, 111, 131))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_31.setFont(font)
        self.pushButton_31.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(237, 28, 36);\n"
"border-radius: 10;\n"
"")
        self.pushButton_31.setObjectName("pushButton_31")
        self.pushButton_32 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_32.setGeometry(QtCore.QRect(350, 140, 111, 131))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_32.setFont(font)
        self.pushButton_32.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(237, 28, 36);\n"
"border-radius: 10;")
        self.pushButton_32.setObjectName("pushButton_32")
        self.pushButton_33 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_33.setGeometry(QtCore.QRect(460, 140, 111, 131))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_33.setFont(font)
        self.pushButton_33.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(237, 28, 36);\n"
"border-radius: 10;")
        self.pushButton_33.setObjectName("pushButton_33")
        self.pushButton_34 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_34.setGeometry(QtCore.QRect(570, 140, 111, 131))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_34.setFont(font)
        self.pushButton_34.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(237, 28, 36);\n"
"border-radius: 10;")
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_35 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_35.setGeometry(QtCore.QRect(680, 140, 111, 131))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_35.setFont(font)
        self.pushButton_35.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(237, 28, 36);\n"
"border-radius: 10;")
        self.pushButton_35.setObjectName("pushButton_35")
        self.pushButton_36 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_36.setGeometry(QtCore.QRect(790, 140, 111, 131))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_36.setFont(font)
        self.pushButton_36.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(237, 28, 36);\n"
"border-radius: 10;")
        self.pushButton_36.setObjectName("pushButton_36")
        self.pushButton_37 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_37.setGeometry(QtCore.QRect(900, 140, 111, 131))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_37.setFont(font)
        self.pushButton_37.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(237, 28, 36);\n"
"border-radius: 10;")
        self.pushButton_37.setObjectName("pushButton_37")
        self.pushButton_38 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_38.setGeometry(QtCore.QRect(1010, 140, 111, 131))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_38.setFont(font)
        self.pushButton_38.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(237, 28, 36);\n"
"border-radius: 10;")
        self.pushButton_38.setObjectName("pushButton_38")
        self.pushButton_39 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_39.setGeometry(QtCore.QRect(1120, 140, 111, 131))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_39.setFont(font)
        self.pushButton_39.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(237, 28, 36);\n"
"border-radius: 10;")
        self.pushButton_39.setObjectName("pushButton_39")
        self.pushButton_40 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_40.setGeometry(QtCore.QRect(1230, 140, 111, 131))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_40.setFont(font)
        self.pushButton_40.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(237, 28, 36);\n"
"border-radius: 10;")
        self.pushButton_40.setObjectName("pushButton_40")
        self.pushButton_41 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_41.setGeometry(QtCore.QRect(1340, 140, 111, 131))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_41.setFont(font)
        self.pushButton_41.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(237, 28, 36);\n"
"border-radius: 10;")
        self.pushButton_41.setObjectName("pushButton_41")
        self.pushButton_42 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_42.setGeometry(QtCore.QRect(1530, 500, 91, 181))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_42.setFont(font)
        self.pushButton_42.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 5px solid rgb(237, 28, 36);\n"
"border-radius: 20;")
        self.pushButton_42.setObjectName("pushButton_42")
        self.pushButton_43 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_43.setGeometry(QtCore.QRect(1480, 10, 251, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_43.setFont(font)
        self.pushButton_43.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 6px solid rgb(237, 28, 36);\n"
"border-radius: 20;")
        self.pushButton_43.setObjectName("pushButton_43")
        self.pushButton_44 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_44.setGeometry(QtCore.QRect(1480, 150, 251, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_44.setFont(font)
        self.pushButton_44.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 6px solid rgb(237, 28, 36);\n"
"border-radius: 20;")
        self.pushButton_44.setObjectName("pushButton_44")
        self.pushButton_45 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_45.setGeometry(QtCore.QRect(1740, 10, 261, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_45.setFont(font)
        self.pushButton_45.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 6px solid rgb(237, 28, 36);\n"
"border-radius: 20;")
        self.pushButton_45.setObjectName("pushButton_45")
        self.pushButton_46 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_46.setGeometry(QtCore.QRect(1740, 150, 261, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_46.setFont(font)
        self.pushButton_46.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 6px solid rgb(237, 28, 36);\n"
"border-radius: 20;")
        self.pushButton_46.setObjectName("pushButton_46")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-30, 900, 2091, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 8px solid rgb(237, 28, 36);\n"
"border-radius: 30;")
        self.label.setObjectName("label")
        self.pushButton_47 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_47.setGeometry(QtCore.QRect(200, 530, 171, 181))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_47.setFont(font)
        self.pushButton_47.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 5px solid rgb(237, 28, 36);\n"
"border-radius: 20;\n"
"")
        self.pushButton_47.setObjectName("pushButton_47")
        self.pushButton_48 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_48.setGeometry(QtCore.QRect(30, 710, 171, 181))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_48.setFont(font)
        self.pushButton_48.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 5px solid rgb(237, 28, 36);\n"
"border-radius: 20;")
        self.pushButton_48.setObjectName("pushButton_48")
        self.pushButton_49 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_49.setGeometry(QtCore.QRect(370, 710, 171, 181))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_49.setFont(font)
        self.pushButton_49.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 5px solid rgb(237, 28, 36);\n"
"border-radius: 20;")
        self.pushButton_49.setObjectName("pushButton_49")
        self.pushButton_50 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_50.setGeometry(QtCore.QRect(1420, 500, 111, 181))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_50.setFont(font)
        self.pushButton_50.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 5px solid rgb(237, 28, 36);\n"
"border-radius: 20;")
        self.pushButton_50.setObjectName("pushButton_50")
        self.pushButton_51 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_51.setGeometry(QtCore.QRect(1720, 500, 111, 181))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_51.setFont(font)
        self.pushButton_51.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 5px solid rgb(237, 28, 36);\n"
"border-radius: 20;")
        self.pushButton_51.setObjectName("pushButton_51")
        self.pushButton_52 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_52.setGeometry(QtCore.QRect(1530, 410, 191, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_52.setFont(font)
        self.pushButton_52.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 5px solid rgb(237, 28, 36);\n"
"border-radius: 20;")
        self.pushButton_52.setObjectName("pushButton_52")
        self.pushButton_53 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_53.setGeometry(QtCore.QRect(1530, 680, 191, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_53.setFont(font)
        self.pushButton_53.setStyleSheet("background-color: rgb(1, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"border: 5px solid rgb(237, 28, 36);\n"
"border-radius: 20;")
        self.pushButton_53.setObjectName("pushButton_53")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "△"))
        self.pushButton_2.setText(_translate("MainWindow", "↙"))
        self.pushButton_3.setText(_translate("MainWindow", "▽"))
        self.pushButton_4.setText(_translate("MainWindow", "◁"))
        self.pushButton_5.setText(_translate("MainWindow", "▷"))
        self.pushButton_6.setText(_translate("MainWindow", "→"))
        self.pushButton_7.setText(_translate("MainWindow", "↑"))
        self.pushButton_8.setText(_translate("MainWindow", "PKM"))
        self.pushButton_9.setText(_translate("MainWindow", "↖"))
        self.pushButton_10.setText(_translate("MainWindow", "Enter"))
        self.pushButton_11.setText(_translate("MainWindow", "↓"))
        self.pushButton_12.setText(_translate("MainWindow", "Spase"))
        self.pushButton_13.setText(_translate("MainWindow", "←"))
        self.pushButton_14.setText(_translate("MainWindow", "↘"))
        self.pushButton_15.setText(_translate("MainWindow", "↗"))
        self.pushButton_16.setText(_translate("MainWindow", "Win"))
        self.pushButton_17.setText(_translate("MainWindow", "F1"))
        self.pushButton_18.setText(_translate("MainWindow", "F2"))
        self.pushButton_19.setText(_translate("MainWindow", "F3"))
        self.pushButton_20.setText(_translate("MainWindow", "F4"))
        self.pushButton_21.setText(_translate("MainWindow", "F5"))
        self.pushButton_22.setText(_translate("MainWindow", "F6"))
        self.pushButton_23.setText(_translate("MainWindow", "F7"))
        self.pushButton_24.setText(_translate("MainWindow", "F8"))
        self.pushButton_25.setText(_translate("MainWindow", "F9"))
        self.pushButton_26.setText(_translate("MainWindow", "F10"))
        self.pushButton_27.setText(_translate("MainWindow", "F11"))
        self.pushButton_28.setText(_translate("MainWindow", "F12"))
        self.pushButton_29.setText(_translate("MainWindow", "1"))
        self.pushButton_30.setText(_translate("MainWindow", "ESC"))
        self.pushButton_31.setText(_translate("MainWindow", "2"))
        self.pushButton_32.setText(_translate("MainWindow", "3"))
        self.pushButton_33.setText(_translate("MainWindow", "4"))
        self.pushButton_34.setText(_translate("MainWindow", "5"))
        self.pushButton_35.setText(_translate("MainWindow", "6"))
        self.pushButton_36.setText(_translate("MainWindow", "7"))
        self.pushButton_37.setText(_translate("MainWindow", "8"))
        self.pushButton_38.setText(_translate("MainWindow", "9"))
        self.pushButton_39.setText(_translate("MainWindow", "0"))
        self.pushButton_40.setText(_translate("MainWindow", "-"))
        self.pushButton_41.setText(_translate("MainWindow", "+"))
        self.pushButton_42.setText(_translate("MainWindow", "LKM"))
        self.pushButton_43.setText(_translate("MainWindow", "alt"))
        self.pushButton_44.setText(_translate("MainWindow", "caps lock"))
        self.pushButton_45.setText(_translate("MainWindow", "tab"))
        self.pushButton_46.setText(_translate("MainWindow", "ctrl"))
        self.label.setText(_translate("MainWindow", "         V.0.1.1"))
        self.pushButton_47.setText(_translate("MainWindow", "shift"))
        self.pushButton_48.setText(_translate("MainWindow", "shift+"))
        self.pushButton_49.setText(_translate("MainWindow", "shift-"))
        self.pushButton_50.setText(_translate("MainWindow", "l"))
        self.pushButton_51.setText(_translate("MainWindow", "R"))
        self.pushButton_52.setText(_translate("MainWindow", "up"))
        self.pushButton_53.setText(_translate("MainWindow", "down"))

    def add_functions(self):
        self.pushButton_39.clicked.connect(lambda: self.K_L(self.pushButton_39.text()))
        self.pushButton_2.clicked.connect(lambda: self.K_L(self.pushButton_2.text()))
        self.pushButton_3.clicked.connect(lambda: self.L_L(self.pushButton_3.text()))
        self.pushButton_4.clicked.connect(lambda: self.L_L(self.pushButton_4.text()))
        self.pushButton_5.clicked.connect(lambda: self.L_L(self.pushButton_5.text()))
        self.pushButton_6.clicked.connect(lambda: self.K_L(self.pushButton_6.text()))
        self.pushButton_7.clicked.connect(lambda: self.K_L(self.pushButton_7.text()))
        self.pushButton_8.clicked.connect(lambda: self.K_L(self.pushButton_8.text()))
        self.pushButton_9.clicked.connect(lambda: self.K_L(self.pushButton_9.text()))
        self.pushButton_10.clicked.connect(lambda: self.K_L(self.pushButton_10.text()))
        self.pushButton_11.clicked.connect(lambda: self.K_L(self.pushButton_11.text()))
        self.pushButton_12.clicked.connect(lambda: self.L_L(self.pushButton_12.text()))
        self.pushButton_13.clicked.connect(lambda: self.K_L(self.pushButton_13.text()))
        self.pushButton_14.clicked.connect(lambda: self.K_L(self.pushButton_14.text()))
        self.pushButton_15.clicked.connect(lambda: self.K_L(self.pushButton_15.text()))
        self.pushButton_16.clicked.connect(lambda: self.K_L(self.pushButton_16.text()))
        self.pushButton_17.clicked.connect(lambda: self.K_L(self.pushButton_17.text()))
        self.pushButton_18.clicked.connect(lambda: self.K_L(self.pushButton_18.text()))
        self.pushButton_19.clicked.connect(lambda: self.K_L(self.pushButton_19.text()))
        self.pushButton_20.clicked.connect(lambda: self.K_L(self.pushButton_20.text()))
        self.pushButton_21.clicked.connect(lambda: self.K_L(self.pushButton_21.text()))
        self.pushButton_22.clicked.connect(lambda: self.K_L(self.pushButton_22.text()))
        self.pushButton_23.clicked.connect(lambda: self.K_L(self.pushButton_23.text()))
        self.pushButton_24.clicked.connect(lambda: self.K_L(self.pushButton_24.text()))
        self.pushButton_25.clicked.connect(lambda: self.K_L(self.pushButton_25.text()))
        self.pushButton_26.clicked.connect(lambda: self.K_L(self.pushButton_26.text()))
        self.pushButton_27.clicked.connect(lambda: self.K_L(self.pushButton_27.text()))
        self.pushButton_28.clicked.connect(lambda: self.K_L(self.pushButton_28.text()))
        self.pushButton_29.clicked.connect(lambda: self.K_L(self.pushButton_29.text()))
        self.pushButton_30.clicked.connect(lambda: self.K_L(self.pushButton_30.text()))
        self.pushButton_31.clicked.connect(lambda: self.K_L(self.pushButton_31.text()))
        self.pushButton_32.clicked.connect(lambda: self.K_L(self.pushButton_32.text()))
        self.pushButton_33.clicked.connect(lambda: self.K_L(self.pushButton_33.text()))
        self.pushButton_34.clicked.connect(lambda: self.K_L(self.pushButton_34.text()))
        self.pushButton_35.clicked.connect(lambda: self.K_L(self.pushButton_35.text()))
        self.pushButton_36.clicked.connect(lambda: self.K_L(self.pushButton_36.text()))
        self.pushButton_37.clicked.connect(lambda: self.K_L(self.pushButton_37.text()))
        self.pushButton_38.clicked.connect(lambda: self.K_L(self.pushButton_38.text()))
        self.pushButton_40.clicked.connect(lambda: self.K_L(self.pushButton_40.text()))
        self.pushButton_41.clicked.connect(lambda: self.K_L(self.pushButton_41.text()))
        self.pushButton_42.clicked.connect(lambda: self.K_L(self.pushButton_42.text()))
        self.pushButton_43.clicked.connect(lambda: self.L_L(self.pushButton_43.text()))
        self.pushButton_44.clicked.connect(lambda: self.K_L(self.pushButton_44.text()))
        self.pushButton_45.clicked.connect(lambda: self.L_L(self.pushButton_45.text()))
        self.pushButton_46.clicked.connect(lambda: self.K_L(self.pushButton_46.text()))
        self.pushButton_47.clicked.connect(lambda: self.L_L(self.pushButton_47.text()))
        self.pushButton_48.clicked.connect(lambda: self.L_L(self.pushButton_48.text()))
        self.pushButton_49.clicked.connect(lambda: self.L_L(self.pushButton_49.text()))
        self.pushButton_50.clicked.connect(lambda: self.K_L(self.pushButton_50.text()))
        self.pushButton_51.clicked.connect(lambda: self.K_L(self.pushButton_51.text()))
        self.pushButton_52.clicked.connect(lambda: self.K_L(self.pushButton_52.text()))
        self.pushButton_53.clicked.connect(lambda: self.K_L(self.pushButton_53.text()))
        self.pushButton.clicked.connect(lambda: self.L_L(self.pushButton.text()))


    def K_L(self, k):
        client.send(k.encode("utf-8"))

    def L_L(self, y):
        self.buttonGroup = QButtonGroup(exclusive=False)
        self.pushButton_3.setCheckable(True)
        self.buttonGroup.addButton(self.pushButton_3)
        self.pushButton_4.setCheckable(True)
        self.buttonGroup.addButton(self.pushButton_4)
        self.pushButton_5.setCheckable(True)
        self.buttonGroup.addButton(self.pushButton_5)
        self.pushButton.setCheckable(True)
        self.buttonGroup.addButton(self.pushButton)
        self.pushButton_12.setCheckable(True)
        self.buttonGroup.addButton(self.pushButton_12)
        self.pushButton_45.setCheckable(True)
        self.buttonGroup.addButton(self.pushButton_45)
        self.pushButton_47.setCheckable(True)
        self.buttonGroup.addButton(self.pushButton_47)
        self.pushButton_48.setCheckable(True)
        self.buttonGroup.addButton(self.pushButton_48)
        self.pushButton_49.setCheckable(True)
        self.buttonGroup.addButton(self.pushButton_49)
        self.pushButton_43.setCheckable(True)
        self.buttonGroup.addButton(self.pushButton_43)
        self.buttonGroup.buttonClicked.connect(self.check_button)
    def check_button(self, btn):
        client.send(f"{btn.text()} - {btn.isChecked()}".encode("utf-8"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
