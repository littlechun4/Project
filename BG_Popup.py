# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TimePopup.ui'
#
# Created: Sun Dec 15 02:57:37 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from datetime import datetime

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(527, 232)
        self.spinBox = QtGui.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(149, 20, 81, 41))
        self.spinBox.setMinimum(1970)
        self.spinBox.setMaximum(2090)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.spinBox_2 = QtGui.QSpinBox(Dialog)
        self.spinBox_2.setGeometry(QtCore.QRect(230, 20, 81, 41))
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(12)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.spinBox_3 = QtGui.QSpinBox(Dialog)
        self.spinBox_3.setGeometry(QtCore.QRect(310, 20, 81, 41))
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(31)
        self.spinBox_3.setObjectName(_fromUtf8("spinBox_3"))
        self.timeEdit = QtGui.QTimeEdit(Dialog)
        self.timeEdit.setGeometry(QtCore.QRect(397, 20, 121, 41))
        self.timeEdit.setObjectName(_fromUtf8("timeEdit"))
        self.timeEdit_2 = QtGui.QTimeEdit(Dialog)
        self.timeEdit_2.setGeometry(QtCore.QRect(397, 90, 121, 41))
        self.timeEdit_2.setObjectName(_fromUtf8("timeEdit_2"))
        self.spinBox_4 = QtGui.QSpinBox(Dialog)
        self.spinBox_4.setGeometry(QtCore.QRect(149, 90, 81, 41))
        self.spinBox_4.setMinimum(1970)
        self.spinBox_4.setMaximum(2090)
        self.spinBox_4.setObjectName(_fromUtf8("spinBox_4"))
        self.spinBox_5 = QtGui.QSpinBox(Dialog)
        self.spinBox_5.setGeometry(QtCore.QRect(230, 90, 81, 41))
        self.spinBox_5.setMinimum(1)
        self.spinBox_5.setMaximum(12)
        self.spinBox_5.setObjectName(_fromUtf8("spinBox_5"))
        self.spinBox_6 = QtGui.QSpinBox(Dialog)
        self.spinBox_6.setGeometry(QtCore.QRect(310, 90, 81, 41))
        self.spinBox_6.setMinimum(1)
        self.spinBox_6.setMaximum(31)
        self.spinBox_6.setObjectName(_fromUtf8("spinBox_6"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 101, 41))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 101, 41))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(310, 168, 178, 41))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.actionOK = QtGui.QAction(Dialog)
        self.actionOK.setObjectName(_fromUtf8("actionOK"))
        self.actionCancel = QtGui.QAction(Dialog)
        self.actionCancel.setObjectName(_fromUtf8("actionCancel"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt;\">시작 지점</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt;\">종료 지점</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOK.setText(QtGui.QApplication.translate("Dialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCancel.setText(QtGui.QApplication.translate("Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

    def data(self):
        start = {'year': self.spinBox.value(), 'month': self.spinBox_2.value(), 'day': self.spinBox_3.value(), 'time': self.timeEdit.time()}
        end = {'year': self.spinBox_4.value(), 'month': self.spinBox_5.value(), 'day': self.spinBox_6.value(), 'time': self.timeEdit_2.time()}
        return {'start': start, 'end': end}


class BGFill_Dialog(QtGui.QDialog):
    def __init__(self, start_timestamp):
        import sys
        self.Dialog = QtGui.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog)

        self.ui.pushButton.clicked.connect(lambda: QtGui.QDialog.accept(self.Dialog))
        self.ui.pushButton_2.clicked.connect(lambda: QtGui.QDialog.reject(self.Dialog))

        self.baseValue(start_timestamp)
        self.Dialog.show()

    def activate(self):
        if self.Dialog.exec_() == QtGui.QDialog.Accepted:
            vals = self.ui.data()
            return vals
        else:
            self.close()

    def baseValue(self, start_timestamp):
        time = datetime.fromtimestamp(start_timestamp / 1000)
        year = time.year
        month = time.month
        day = time.day
        hour = time.hour
        minute = time.minute

        self.ui.spinBox.setValue(year)
        self.ui.spinBox_4.setValue(year)

        self.ui.spinBox_2.setValue(month)
        self.ui.spinBox_5.setValue(month)

        self.ui.spinBox_3.setValue(day)
        self.ui.spinBox_6.setValue(day)

        time_edit = QtCore.QTime(hour, minute)
        self.ui.timeEdit.setTime(time_edit)
        self.ui.timeEdit_2.setTime(time_edit)
