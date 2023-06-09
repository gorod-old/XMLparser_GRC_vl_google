# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(839, 480)
        MainWindow.setMinimumSize(QtCore.QSize(0, 480))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 34))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMinimumSize(QtCore.QSize(780, 20))
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEditUrl = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditUrl.setMinimumSize(QtCore.QSize(610, 28))
        self.lineEditUrl.setText("")
        self.lineEditUrl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEditUrl.setObjectName("lineEditUrl")
        self.horizontalLayout_2.addWidget(self.lineEditUrl)
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setMinimumSize(QtCore.QSize(160, 0))
        self.clearButton.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout_2.addWidget(self.clearButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 3)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setMinimumSize(QtCore.QSize(780, 20))
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEditAppEmail = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditAppEmail.setMinimumSize(QtCore.QSize(610, 28))
        self.lineEditAppEmail.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEditAppEmail.setObjectName("lineEditAppEmail")
        self.horizontalLayout_3.addWidget(self.lineEditAppEmail)
        self.copyButton = QtWidgets.QPushButton(self.centralwidget)
        self.copyButton.setMinimumSize(QtCore.QSize(160, 0))
        self.copyButton.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.copyButton.setObjectName("copyButton")
        self.horizontalLayout_3.addWidget(self.copyButton)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 3)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setMinimumSize(QtCore.QSize(780, 20))
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEditTab1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditTab1.setMinimumSize(QtCore.QSize(200, 34))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEditTab1.setFont(font)
        self.lineEditTab1.setStyleSheet("background-color: rgb(255, 252, 210);")
        self.lineEditTab1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditTab1.setReadOnly(True)
        self.lineEditTab1.setObjectName("lineEditTab1")
        self.horizontalLayout_4.addWidget(self.lineEditTab1)
        self.lineEditTab1_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditTab1_2.setMinimumSize(QtCore.QSize(200, 34))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEditTab1_2.setFont(font)
        self.lineEditTab1_2.setStyleSheet("background-color: rgb(255, 252, 210);")
        self.lineEditTab1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditTab1_2.setReadOnly(True)
        self.lineEditTab1_2.setObjectName("lineEditTab1_2")
        self.horizontalLayout_4.addWidget(self.lineEditTab1_2)
        self.lineEditTab1_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditTab1_3.setMinimumSize(QtCore.QSize(200, 34))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEditTab1_3.setFont(font)
        self.lineEditTab1_3.setStyleSheet("background-color: rgb(255, 252, 210);")
        self.lineEditTab1_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditTab1_3.setReadOnly(True)
        self.lineEditTab1_3.setObjectName("lineEditTab1_3")
        self.horizontalLayout_4.addWidget(self.lineEditTab1_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEditDduInfo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditDduInfo.setMinimumSize(QtCore.QSize(200, 34))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.lineEditDduInfo.setFont(font)
        self.lineEditDduInfo.setStyleSheet("")
        self.lineEditDduInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditDduInfo.setReadOnly(True)
        self.lineEditDduInfo.setObjectName("lineEditDduInfo")
        self.horizontalLayout_5.addWidget(self.lineEditDduInfo)
        self.lineEditIpInfo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditIpInfo.setMinimumSize(QtCore.QSize(200, 34))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.lineEditIpInfo.setFont(font)
        self.lineEditIpInfo.setStyleSheet("")
        self.lineEditIpInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditIpInfo.setReadOnly(True)
        self.lineEditIpInfo.setObjectName("lineEditIpInfo")
        self.horizontalLayout_5.addWidget(self.lineEditIpInfo)
        self.lineEditUInfo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditUInfo.setMinimumSize(QtCore.QSize(200, 34))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.lineEditUInfo.setFont(font)
        self.lineEditUInfo.setStyleSheet("")
        self.lineEditUInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditUInfo.setReadOnly(True)
        self.lineEditUInfo.setObjectName("lineEditUInfo")
        self.horizontalLayout_5.addWidget(self.lineEditUInfo)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout, 6, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(20, 101, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 7, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setMinimumSize(QtCore.QSize(780, 20))
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 8, 0, 1, 3)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(0, 36))
        self.label_3.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.dateEdit_from = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_from.setMinimumSize(QtCore.QSize(160, 36))
        self.dateEdit_from.setMaximumSize(QtCore.QSize(160, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dateEdit_from.setFont(font)
        self.dateEdit_from.setObjectName("dateEdit_from")
        self.horizontalLayout.addWidget(self.dateEdit_from)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 36))
        self.label_4.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.dateEdit_to = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_to.setMinimumSize(QtCore.QSize(160, 36))
        self.dateEdit_to.setMaximumSize(QtCore.QSize(160, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dateEdit_to.setFont(font)
        self.dateEdit_to.setObjectName("dateEdit_to")
        self.horizontalLayout.addWidget(self.dateEdit_to)
        self.horizontalLayout_8.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(48, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setMinimumSize(QtCore.QSize(0, 36))
        self.label_9.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        self.lineEditStatus = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditStatus.setMinimumSize(QtCore.QSize(300, 28))
        self.lineEditStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditStatus.setReadOnly(True)
        self.lineEditStatus.setObjectName("lineEditStatus")
        self.horizontalLayout_6.addWidget(self.lineEditStatus)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_6)
        self.gridLayout.addLayout(self.horizontalLayout_8, 9, 0, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 10, 1, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lineEditFile = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditFile.setMinimumSize(QtCore.QSize(450, 28))
        self.lineEditFile.setMaximumSize(QtCore.QSize(550, 16777215))
        self.lineEditFile.setObjectName("lineEditFile")
        self.horizontalLayout_7.addWidget(self.lineEditFile)
        self.selectFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.selectFileButton.setMinimumSize(QtCore.QSize(160, 0))
        self.selectFileButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.selectFileButton.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.selectFileButton.setObjectName("selectFileButton")
        self.horizontalLayout_7.addWidget(self.selectFileButton)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_7)
        spacerItem3 = QtWidgets.QSpacerItem(30, 25, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setMinimumSize(QtCore.QSize(160, 0))
        self.startButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.startButton.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.startButton.setObjectName("startButton")
        self.horizontalLayout_9.addWidget(self.startButton)
        self.gridLayout.addLayout(self.horizontalLayout_9, 11, 0, 2, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Парсер данных из XML в таблицу Google"))
        self.label_5.setText(_translate("MainWindow", "Введите URL Google таблицы для вывода результатов:"))
        self.clearButton.setText(_translate("MainWindow", "очистить"))
        self.label_6.setText(_translate("MainWindow", "Добавьте в настройки доступа таблицы Email приложения с возможностью редактирования:"))
        self.lineEditAppEmail.setText(_translate("MainWindow", "gorod-old-service-account@python-bot-331309.iam.gserviceaccount.com"))
        self.copyButton.setText(_translate("MainWindow", "копировать"))
        self.label_8.setText(_translate("MainWindow", "Названия листов и результаты:"))
        self.lineEditTab1.setText(_translate("MainWindow", "дду"))
        self.lineEditTab1_2.setText(_translate("MainWindow", "ипотека"))
        self.lineEditTab1_3.setText(_translate("MainWindow", "уступки"))
        self.lineEditDduInfo.setText(_translate("MainWindow", "0"))
        self.lineEditIpInfo.setText(_translate("MainWindow", "0"))
        self.lineEditUInfo.setText(_translate("MainWindow", "0"))
        self.label_7.setText(_translate("MainWindow", "Настройте диапазон дат для извлечения информации"))
        self.label_3.setText(_translate("MainWindow", "Дата от:"))
        self.label_4.setText(_translate("MainWindow", "до"))
        self.label_9.setText(_translate("MainWindow", "статус:"))
        self.lineEditStatus.setText(_translate("MainWindow", "запущен"))
        self.selectFileButton.setText(_translate("MainWindow", "выберите файл"))
        self.startButton.setText(_translate("MainWindow", "Старт"))
