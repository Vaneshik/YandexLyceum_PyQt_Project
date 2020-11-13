# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(800, 650)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Icons/Vaneshik_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background: #D2C7DE;")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 20, 70, 40))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border: 1px solid #000000;\n"
"border-radius: 20px;\n"
"background: #E5E5E5;")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(110, 20, 550, 60))
        font = QtGui.QFont()
        font.setFamily("Exo 2.0")
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setToolTipDuration(-1)
        self.lineEdit.setStyleSheet("background: #E5E5E5;\n"
"border: 1px solid #000000;\n"
"border-radius: 20px;")
        self.lineEdit.setMaxLength(27)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 20, 81, 61))
        self.pushButton_2.setStyleSheet("background:rgba(255, 255, 255, 0)\n"
"")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Icons/1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_2.setObjectName("pushButton_2")
#         self.frame = QtWidgets.QFrame(Form)
#         self.frame.setGeometry(QtCore.QRect(50, 100, 641, 131))
#         self.frame.setStyleSheet("background: #E5E5E5;\n"
# "border: 1px solid #000000;\n"
# "box-sizing: border-box;\n"
# "border-radius: 20px;")
#         self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.frame.setObjectName("frame")
#         self.comboBox = QtWidgets.QComboBox(self.frame)
#         self.comboBox.setGeometry(QtCore.QRect(10, 20, 271, 41))
#         font = QtGui.QFont()
#         font.setFamily("Exo 2.0 Extra Light")
#         font.setPointSize(14)
#         self.comboBox.setFont(font)
#         self.comboBox.setStyleSheet("QComboBox {\n"
# "background: #C4C4C4;\n"
# "border: 1px solid #BCBCBC;\n"
# "border-radius: 20px;\n"
# "}\n"
# "QComboBox::down-arrow {\n"
# "    color: white;\n"
# "}")
#         self.comboBox.setCurrentText("")
#         self.comboBox.setObjectName("comboBox")
#         self.comboBox.addItem("")
#         self.comboBox_3 = QtWidgets.QComboBox(self.frame)
#         self.comboBox_3.setGeometry(QtCore.QRect(10, 80, 271, 41))
#         font = QtGui.QFont()
#         font.setFamily("Exo 2.0 Extra Light")
#         font.setPointSize(14)
#         self.comboBox_3.setFont(font)
#         self.comboBox_3.setStyleSheet("QComboBox {\n"
# "background: #C4C4C4;\n"
# "border: 1px solid #BCBCBC;\n"
# "border-radius: 20px;\n"
# "}\n"
# "QComboBox::down-arrow {\n"
# "    color: white;\n"
# "}")
#         self.comboBox_3.setCurrentText("")
#         self.comboBox_3.setObjectName("comboBox_3")
#         self.comboBox_4 = QtWidgets.QComboBox(self.frame)
#         self.comboBox_4.setGeometry(QtCore.QRect(360, 80, 271, 41))
#         font = QtGui.QFont()
#         font.setFamily("Exo 2.0 Extra Light")
#         font.setPointSize(14)
#         self.comboBox_4.setFont(font)
#         self.comboBox_4.setStyleSheet("QComboBox {\n"
# "background: #C4C4C4;\n"
# "border: 1px solid #BCBCBC;\n"
# "border-radius: 20px;\n"
# "}\n"
# "QComboBox::down-arrow {\n"
# "    color: white;\n"
# "}")
#         self.comboBox_4.setCurrentText("")
#         self.comboBox_4.setObjectName("comboBox_4")
#         self.comboBox_2 = QtWidgets.QComboBox(self.frame)
#         self.comboBox_2.setGeometry(QtCore.QRect(360, 20, 271, 41))
#         font = QtGui.QFont()
#         font.setFamily("Exo 2.0 Extra Light")
#         font.setPointSize(14)
#         self.comboBox_2.setFont(font)
#         self.comboBox_2.setStyleSheet("QComboBox {\n"
# "background: #C4C4C4;\n"
# "border: 1px solid #BCBCBC;\n"
# "border-radius: 20px;\n"
# "}\n"
# "QComboBox::down-arrow {\n"
# "    color: white;\n"
# "}")
#         self.comboBox_2.setCurrentText("")
#         self.comboBox_2.setObjectName("comboBox_2")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(11, 150, 778, 450))
        self.scrollArea.setStyleSheet("background: #E5E5E5;\n"
"border: 1px solid #000000;\n"
"border-radius: 20px")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        # self.scrollAreaWidgetContents = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 669, 329))
        # self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        # self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.lineEdit.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        # self.frame.raise_()
        self.scrollArea.raise_()

        self.retranslateUi(Form)
        # self.comboBox.setCurrentIndex(-1)
        # self.comboBox_3.setCurrentIndex(-1)
        # self.comboBox_4.setCurrentIndex(-1)
        # self.comboBox_2.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Поиск"))
        self.pushButton.setText(_translate("Form", "←"))
        self.lineEdit.setText(_translate("Form", "Поиск аниме"))
