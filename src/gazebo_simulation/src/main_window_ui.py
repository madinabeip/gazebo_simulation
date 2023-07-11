# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 572)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.chasisImage = QtWidgets.QGraphicsView(self.centralwidget)
        self.chasisImage.setGeometry(QtCore.QRect(10, 10, 261, 211))
        self.chasisImage.setObjectName("chasisImage")
        self.armImage = QtWidgets.QGraphicsView(self.centralwidget)
        self.armImage.setGeometry(QtCore.QRect(270, 10, 261, 211))
        self.armImage.setObjectName("armImage")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 260, 191, 191))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.leftBtn = QtWidgets.QPushButton(self.frame)
        self.leftBtn.setGeometry(QtCore.QRect(10, 70, 51, 51))
        self.leftBtn.setObjectName("leftBtn")
        self.forwBtn = QtWidgets.QPushButton(self.frame)
        self.forwBtn.setGeometry(QtCore.QRect(70, 10, 51, 51))
        self.forwBtn.setObjectName("forwBtn")
        self.downBtn = QtWidgets.QPushButton(self.frame)
        self.downBtn.setGeometry(QtCore.QRect(70, 130, 51, 51))
        self.downBtn.setObjectName("downBtn")
        self.rightBtn = QtWidgets.QPushButton(self.frame)
        self.rightBtn.setGeometry(QtCore.QRect(130, 70, 51, 51))
        self.rightBtn.setObjectName("rightBtn")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(270, 260, 241, 181))
        self.widget.setObjectName("widget")
        self.armUpBtn = QtWidgets.QPushButton(self.widget)
        self.armUpBtn.setGeometry(QtCore.QRect(10, 40, 51, 51))
        self.armUpBtn.setObjectName("armUpBtn")
        self.armDownBtn = QtWidgets.QPushButton(self.widget)
        self.armDownBtn.setGeometry(QtCore.QRect(10, 110, 51, 51))
        self.armDownBtn.setObjectName("armDownBtn")
        self.openBtn = QtWidgets.QPushButton(self.widget)
        self.openBtn.setGeometry(QtCore.QRect(140, 40, 81, 51))
        self.openBtn.setObjectName("openBtn")
        self.closeBtn = QtWidgets.QPushButton(self.widget)
        self.closeBtn.setGeometry(QtCore.QRect(140, 110, 81, 51))
        self.closeBtn.setObjectName("closeBtn")
        self.arm2UpBtn = QtWidgets.QPushButton(self.widget)
        self.arm2UpBtn.setGeometry(QtCore.QRect(70, 40, 51, 51))
        self.arm2UpBtn.setObjectName("arm2UpBtn")
        self.arm2DownBtn = QtWidgets.QPushButton(self.widget)
        self.arm2DownBtn.setGeometry(QtCore.QRect(70, 110, 51, 51))
        self.arm2DownBtn.setObjectName("arm2DownBtn")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(20, 10, 41, 17))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(70, 10, 41, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(150, 10, 67, 17))
        self.label_5.setObjectName("label_5")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(20, 450, 511, 61))
        self.widget_2.setObjectName("widget_2")
        self.robotSlide = QtWidgets.QSlider(self.widget_2)
        self.robotSlide.setGeometry(QtCore.QRect(0, 30, 171, 31))
        self.robotSlide.setOrientation(QtCore.Qt.Horizontal)
        self.robotSlide.setObjectName("robotSlide")
        self.velNum = QtWidgets.QLCDNumber(self.widget_2)
        self.velNum.setGeometry(QtCore.QRect(180, 30, 51, 23))
        self.velNum.setObjectName("velNum")
        self.armSlide = QtWidgets.QSlider(self.widget_2)
        self.armSlide.setGeometry(QtCore.QRect(270, 30, 171, 31))
        self.armSlide.setOrientation(QtCore.Qt.Horizontal)
        self.armSlide.setObjectName("armSlide")
        self.armNum = QtWidgets.QLCDNumber(self.widget_2)
        self.armNum.setGeometry(QtCore.QRect(450, 30, 51, 23))
        self.armNum.setObjectName("armNum")
        self.label_1 = QtWidgets.QLabel(self.widget_2)
        self.label_1.setGeometry(QtCore.QRect(20, 10, 121, 17))
        self.label_1.setObjectName("label_1")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(300, 10, 101, 17))
        self.label_3.setObjectName("label_3")
        self.filteredArm = QtWidgets.QGraphicsView(self.centralwidget)
        self.filteredArm.setGeometry(QtCore.QRect(530, 10, 261, 211))
        self.filteredArm.setObjectName("filteredArm")
        self.graph = QtWidgets.QWidget(self.centralwidget)
        self.graph.setGeometry(QtCore.QRect(530, 270, 251, 181))
        self.graph.setObjectName("graph")
        self.velButton = QtWidgets.QPushButton(self.centralwidget)
        self.velButton.setGeometry(QtCore.QRect(560, 250, 191, 25))
        self.velButton.setObjectName("velButton")
        self.alert = QtWidgets.QLabel(self.centralwidget)
        self.alert.setGeometry(QtCore.QRect(620, 460, 70, 70))
        self.alert.setText("")
        self.alert.setObjectName("alert")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.leftBtn.setText(_translate("MainWindow", "Left"))
        self.forwBtn.setText(_translate("MainWindow", "Up"))
        self.downBtn.setText(_translate("MainWindow", "Down"))
        self.rightBtn.setText(_translate("MainWindow", "Right"))
        self.armUpBtn.setText(_translate("MainWindow", "Up"))
        self.armDownBtn.setText(_translate("MainWindow", "Down"))
        self.openBtn.setText(_translate("MainWindow", "Open"))
        self.closeBtn.setText(_translate("MainWindow", "Close"))
        self.arm2UpBtn.setText(_translate("MainWindow", "Up"))
        self.arm2DownBtn.setText(_translate("MainWindow", "Down"))
        self.label.setText(_translate("MainWindow", "Arm1"))
        self.label_4.setText(_translate("MainWindow", "Arm2"))
        self.label_5.setText(_translate("MainWindow", "Effector"))
        self.label_1.setText(_translate("MainWindow", "Robot velocity"))
        self.label_3.setText(_translate("MainWindow", "Arm velocity"))
        self.velButton.setText(_translate("MainWindow", "Show velocity graph"))
