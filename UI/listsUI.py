# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lists.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(800, 650)
        Form.setStyleSheet("background: #D2C7DE;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Icons/Vaneshik_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 20, 81, 41))
        self.pushButton.setStyleSheet("background: #E5E5E5;\n"
                                      "border: 1px solid #000000;\n"
                                      "border-radius: 20px;")
        self.pushButton.setObjectName("pushButton")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(11, 170, 778, 450))
        self.scrollArea.setStyleSheet("background: #E5E5E5;\n"
                                      "border: 1px solid #000000;\n"
                                      "border-radius: 20px;")
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        # self.scrollAreaWidgetContents = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 679, 439))
        # self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        # self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.favour_butn = QtWidgets.QPushButton(Form)
        self.favour_butn.setGeometry(QtCore.QRect(40, 80, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Exo 2.0")
        font.setPointSize(10)
        self.favour_butn.setFont(font)
        self.favour_butn.setStyleSheet("background: #C4C4C4;\n"
                                       "border: 1px solid #000000;\n"
                                       "border-radius: 20px;")
        self.favour_butn.setObjectName("favour_butn")
        self.viewed_butn = QtWidgets.QPushButton(Form)
        self.viewed_butn.setGeometry(QtCore.QRect(230, 80, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Exo 2.0")
        font.setPointSize(10)
        self.viewed_butn.setFont(font)
        self.viewed_butn.setStyleSheet("background: #C4C4C4;\n"
                                       "border: 1px solid #000000;\n"
                                       "border-radius: 20px;")
        self.viewed_butn.setObjectName("viewed_butn")
        self.quited_butn = QtWidgets.QPushButton(Form)
        self.quited_butn.setGeometry(QtCore.QRect(410, 80, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Exo 2.0")
        font.setPointSize(10)
        self.quited_butn.setFont(font)
        self.quited_butn.setStyleSheet("background: #C4C4C4;\n"
                                       "border: 1px solid #000000;\n"
                                       "border-radius: 20px;")
        self.quited_butn.setObjectName("quited_butn")
        self.future_butn = QtWidgets.QPushButton(Form)
        self.future_butn.setGeometry(QtCore.QRect(590, 80, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Exo 2.0")
        font.setPointSize(10)
        self.future_butn.setFont(font)
        self.future_butn.setStyleSheet("background: #C4C4C4;\n"
                                       "border: 1px solid #000000;\n"
                                       "border-radius: 20px;")
        self.future_butn.setObjectName("future_butn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Списки"))
        self.pushButton.setText(_translate("Form", "← "))
        self.favour_butn.setText(_translate("Form", "Избранные"))
        self.viewed_butn.setText(_translate("Form", "Просмотренные"))
        self.quited_butn.setText(_translate("Form", "Брошенные"))
        self.future_butn.setText(_translate("Form", "Буду смотреть"))
