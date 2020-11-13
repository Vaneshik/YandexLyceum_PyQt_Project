# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(506, 484)
        font = QtGui.QFont()
        font.setFamily("Exo 2.0 Extra Light")
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Icons/Vaneshik_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background: #D2C7DE;\n"
"border: 0px solid #000000;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 250, 250, 60))
        font = QtGui.QFont()
        font.setFamily("Exo 2.0 Extra Light")
        font.setPointSize(22)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background: #E5E5E5;\n"
"    border: 3px solid #000000;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background: #D7D7D7;\n"
"    border: 3px solid #000000;\n"
"    border-radius: 22px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 350, 250, 60))
        font = QtGui.QFont()
        font.setFamily("Exo 2.0 Extra Light")
        font.setPointSize(22)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    background: #E5E5E5;\n"
"    border: 3px solid #000000;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background: #D7D7D7;\n"
"    border: 3px solid #000000;\n"
"    border-radius: 22px;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 460, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Exo 2.0 Extra Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, -10, 521, 201))
        self.frame.setStyleSheet("background: #E6E6E6;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(150, 150, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Exo 2.0 Extra Light")
        font.setPointSize(28)
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setIndent(-1)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(140, 10, 261, 141))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../Icons/project_logo.png"))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AniChecker"))
        self.pushButton.setText(_translate("MainWindow", "Поиск"))
        self.pushButton_2.setText(_translate("MainWindow", "Списки"))
        self.label.setText(_translate("MainWindow", "@Vaneshik, 2020"))
        self.label_2.setText(_translate("MainWindow", "AniChecker"))
