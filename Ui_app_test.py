# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_app_test.ui'
#
# Created: Fri Oct 11 10:28:36 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from a2 import ope
# from app_test import app_test
from a3 import epo

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_app(QtGui.QWidget):
    def setupUi(self, app_test):
        app_test.setObjectName(_fromUtf8("Test"))
        app_test.resize(553, 396)
        self.frame = QtGui.QFrame(app_test)
        self.frame.setGeometry(QtCore.QRect(90, 60, 331, 191))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayoutWidget = QtGui.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(90, 100, 160, 80))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pButtonMul = QtGui.QPushButton(self.gridLayoutWidget)
        self.pButtonMul.setObjectName(_fromUtf8("pButtonMul"))
        self.gridLayout.addWidget(self.pButtonMul, 1, 0, 1, 1)
        self.pButtonAdd = QtGui.QPushButton(self.gridLayoutWidget)
        self.pButtonAdd.setObjectName(_fromUtf8("pButtonAdd"))
        self.gridLayout.addWidget(self.pButtonAdd, 0, 0, 1, 1)
        self.pButtonDiv = QtGui.QPushButton(self.gridLayoutWidget)
        self.pButtonDiv.setObjectName(_fromUtf8("pButtonDiv"))
        self.gridLayout.addWidget(self.pButtonDiv, 1, 1, 1, 1)
        self.pButtonSou = QtGui.QPushButton(self.gridLayoutWidget)
        self.pButtonSou.setObjectName(_fromUtf8("pButtonSou"))
        self.gridLayout.addWidget(self.pButtonSou, 0, 1, 1, 1)
        self.widget = QtGui.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(10, 20, 304, 22))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lEX = QtGui.QLineEdit(self.widget)
        self.lEX.setObjectName(_fromUtf8("lEX"))
        self.horizontalLayout.addWidget(self.lEX)
        self.label_2 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.lEY = QtGui.QLineEdit(self.widget)
        self.lEY.setObjectName(_fromUtf8("lEY"))
        self.horizontalLayout.addWidget(self.lEY)
        self.label_3= QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("result"))
        self.horizontalLayout.addWidget(self.label_3)

        self.retranslateUi(app_test)
        #€QtCore.QMetaObject.connectSlotsByName(app_test)
        # QtCore.QObject.connect(self.pButtonMul ,ope.addi)
        self.connect(self.pButtonAdd, QtCore.SIGNAL("clicked()"), app_test.addi)
        self.connect(self.pButtonSou, QtCore.SIGNAL("clicked()"), app_test.sou)
        
    def retranslateUi(self, app_test):
        app_test.setWindowTitle(_translate("app_test", "app_test", None))
        self.pButtonMul.setText(_translate("app_test", "*", None))
        self.pButtonAdd.setText(_translate("app_test", "+", None))
        self.pButtonDiv.setText(_translate("app_test", "/", None))
        self.pButtonSou.setText(_translate("app_test", "-", None))
        self.label.setText(_translate("app_test", "x :", None))
        self.label_2.setText(_translate("app_test", "Y :", None))
        
