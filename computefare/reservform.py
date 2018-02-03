# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reservform.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        Dialog.setFont(font)
        self.calendarWidget = QtGui.QCalendarWidget(Dialog)
        self.calendarWidget.setGeometry(QtCore.QRect(110, 10, 280, 155))
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(5, 190, 91, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 240, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.spinBox = QtGui.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(110, 190, 41, 22))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(110, 230, 171, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(110, 270, 81, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.EnteredInfo = QtGui.QLabel(Dialog)
        self.EnteredInfo.setGeometry(QtCore.QRect(290, 190, 101, 61))
        self.EnteredInfo.setText(_fromUtf8(""))
        self.EnteredInfo.setObjectName(_fromUtf8("EnteredInfo"))
        self.FareInfo = QtGui.QLabel(Dialog)
        self.FareInfo.setGeometry(QtCore.QRect(200, 270, 46, 21))
        self.FareInfo.setText(_fromUtf8(""))
        self.FareInfo.setObjectName(_fromUtf8("FareInfo"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Reservation Form", None))
        self.label.setText(_translate("Dialog", "Date of Journey", None))
        self.label_2.setText(_translate("Dialog", "Number of Persons", None))
        self.label_3.setText(_translate("Dialog", "Class", None))
        self.comboBox.setItemText(0, _translate("Dialog", "First Class", None))
        self.comboBox.setItemText(1, _translate("Dialog", "Second Class", None))
        self.comboBox.setItemText(2, _translate("Dialog", "Business Class", None))
        self.comboBox.setItemText(3, _translate("Dialog", "Economic Class", None))
        self.pushButton.setText(_translate("Dialog", "Calculate Fare", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

