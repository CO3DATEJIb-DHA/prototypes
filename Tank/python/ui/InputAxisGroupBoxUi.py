# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InputAxisGroupBox.ui'
#
# Created: Mon Oct 27 18:56:59 2014
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_InputAxisGroupBox(object):
    def setupUi(self, InputAxisGroupBox):
        InputAxisGroupBox.setObjectName(_fromUtf8("InputAxisGroupBox"))
        InputAxisGroupBox.resize(430, 132)
        self.verticalLayout = QtGui.QVBoxLayout(InputAxisGroupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(InputAxisGroupBox)
        self.label.setMinimumSize(QtCore.QSize(40, 0))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.pbarInValue = QtGui.QProgressBar(InputAxisGroupBox)
        self.pbarInValue.setMinimum(-1000)
        self.pbarInValue.setMaximum(1000)
        self.pbarInValue.setProperty("value", 0)
        self.pbarInValue.setTextVisible(False)
        self.pbarInValue.setFormat(_fromUtf8(""))
        self.pbarInValue.setObjectName(_fromUtf8("pbarInValue"))
        self.horizontalLayout.addWidget(self.pbarInValue)
        self.labelInput = QtGui.QLabel(InputAxisGroupBox)
        self.labelInput.setMinimumSize(QtCore.QSize(40, 0))
        self.labelInput.setAlignment(QtCore.Qt.AlignCenter)
        self.labelInput.setObjectName(_fromUtf8("labelInput"))
        self.horizontalLayout.addWidget(self.labelInput)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtGui.QFrame(InputAxisGroupBox)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(InputAxisGroupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.sliderTrim = QtGui.QSlider(InputAxisGroupBox)
        self.sliderTrim.setMinimumSize(QtCore.QSize(100, 0))
        self.sliderTrim.setMinimum(-300)
        self.sliderTrim.setMaximum(300)
        self.sliderTrim.setOrientation(QtCore.Qt.Horizontal)
        self.sliderTrim.setTickPosition(QtGui.QSlider.NoTicks)
        self.sliderTrim.setObjectName(_fromUtf8("sliderTrim"))
        self.horizontalLayout_3.addWidget(self.sliderTrim)
        self.labelTrim = QtGui.QLabel(InputAxisGroupBox)
        self.labelTrim.setMinimumSize(QtCore.QSize(30, 0))
        self.labelTrim.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTrim.setObjectName(_fromUtf8("labelTrim"))
        self.horizontalLayout_3.addWidget(self.labelTrim)
        self.label_4 = QtGui.QLabel(InputAxisGroupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.sliderGamma = QtGui.QSlider(InputAxisGroupBox)
        self.sliderGamma.setMinimumSize(QtCore.QSize(100, 0))
        self.sliderGamma.setMinimum(-90)
        self.sliderGamma.setMaximum(90)
        self.sliderGamma.setOrientation(QtCore.Qt.Horizontal)
        self.sliderGamma.setObjectName(_fromUtf8("sliderGamma"))
        self.horizontalLayout_3.addWidget(self.sliderGamma)
        self.labelGamma = QtGui.QLabel(InputAxisGroupBox)
        self.labelGamma.setMinimumSize(QtCore.QSize(30, 0))
        self.labelGamma.setAlignment(QtCore.Qt.AlignCenter)
        self.labelGamma.setObjectName(_fromUtf8("labelGamma"))
        self.horizontalLayout_3.addWidget(self.labelGamma)
        self.checkInvert = QtGui.QCheckBox(InputAxisGroupBox)
        self.checkInvert.setObjectName(_fromUtf8("checkInvert"))
        self.horizontalLayout_3.addWidget(self.checkInvert)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line_2 = QtGui.QFrame(InputAxisGroupBox)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(InputAxisGroupBox)
        self.label_2.setMinimumSize(QtCore.QSize(40, 0))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.pbarOutValue = QtGui.QProgressBar(InputAxisGroupBox)
        self.pbarOutValue.setMinimum(-1000)
        self.pbarOutValue.setMaximum(1000)
        self.pbarOutValue.setProperty("value", 0)
        self.pbarOutValue.setTextVisible(False)
        self.pbarOutValue.setFormat(_fromUtf8(""))
        self.pbarOutValue.setObjectName(_fromUtf8("pbarOutValue"))
        self.horizontalLayout_2.addWidget(self.pbarOutValue)
        self.labelOutput = QtGui.QLabel(InputAxisGroupBox)
        self.labelOutput.setMinimumSize(QtCore.QSize(40, 0))
        self.labelOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.labelOutput.setObjectName(_fromUtf8("labelOutput"))
        self.horizontalLayout_2.addWidget(self.labelOutput)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(InputAxisGroupBox)
        QtCore.QMetaObject.connectSlotsByName(InputAxisGroupBox)

    def retranslateUi(self, InputAxisGroupBox):
        self.label.setText(_translate("InputAxisGroupBox", "Input:", None))
        self.labelInput.setText(_translate("InputAxisGroupBox", "0", None))
        self.label_3.setText(_translate("InputAxisGroupBox", "Trim:", None))
        self.labelTrim.setText(_translate("InputAxisGroupBox", "0", None))
        self.label_4.setText(_translate("InputAxisGroupBox", "Gamma:", None))
        self.labelGamma.setText(_translate("InputAxisGroupBox", "0", None))
        self.checkInvert.setText(_translate("InputAxisGroupBox", "Invert", None))
        self.label_2.setText(_translate("InputAxisGroupBox", "Output:", None))
        self.labelOutput.setText(_translate("InputAxisGroupBox", "0", None))

