# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Coding\Python\DesuraTools\ui\progressbar.ui'
#
# Created: Mon Nov 11 23:44:24 2013
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ProgressBar(object):
    def setupUi(self, ProgressBar):
        ProgressBar.setObjectName("ProgressBar")
        ProgressBar.resize(259, 111)
        ProgressBar.setAutoFillBackground(True)
        ProgressBar.setStyleSheet("")
        self.gridLayout = QtGui.QGridLayout(ProgressBar)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtGui.QFrame(ProgressBar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtGui.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(-1, 0, 0, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.progressBar = QtGui.QProgressBar(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setAutoFillBackground(True)
        self.progressBar.setStyleSheet("")
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)
        self.frame_2 = QtGui.QFrame(ProgressBar)
        self.frame_2.setStyleSheet("background:#fff;")
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_3.setContentsMargins(-1, 9, -1, 9)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textLabel = QtGui.QLabel(self.frame_2)
        self.textLabel.setObjectName("textLabel")
        self.verticalLayout.addWidget(self.textLabel)
        self.infoTextLabel = QtGui.QLabel(self.frame_2)
        self.infoTextLabel.setObjectName("infoTextLabel")
        self.verticalLayout.addWidget(self.infoTextLabel)
        self.accountLabel = QtGui.QLabel(self.frame_2)
        self.accountLabel.setObjectName("accountLabel")
        self.verticalLayout.addWidget(self.accountLabel)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.iconLabel = QtGui.QLabel(self.frame_2)
        self.iconLabel.setMaximumSize(QtCore.QSize(32, 32))
        self.iconLabel.setObjectName("iconLabel")
        self.gridLayout_3.addWidget(self.iconLabel, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)

        self.retranslateUi(ProgressBar)
        QtCore.QMetaObject.connectSlotsByName(ProgressBar)

    def retranslateUi(self, ProgressBar):
        ProgressBar.setWindowTitle(QtGui.QApplication.translate("ProgressBar", "Loading...", None, QtGui.QApplication.UnicodeUTF8))
        self.progressBar.setFormat(QtGui.QApplication.translate("ProgressBar", "%p%", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel.setText(QtGui.QApplication.translate("ProgressBar", "Please wait..", None, QtGui.QApplication.UnicodeUTF8))
        self.infoTextLabel.setText(QtGui.QApplication.translate("ProgressBar", "DesuraTools is loading owned games", None, QtGui.QApplication.UnicodeUTF8))
        self.accountLabel.setText(QtGui.QApplication.translate("ProgressBar", "for account _account_", None, QtGui.QApplication.UnicodeUTF8))
        self.iconLabel.setText(QtGui.QApplication.translate("ProgressBar", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

