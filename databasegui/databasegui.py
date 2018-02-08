# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'databasegui.ui'
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
        Dialog.resize(454, 383)
        self.tableWidget = QtGui.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 431, 231))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.addRowButton = QtGui.QPushButton(Dialog)
        self.addRowButton.setGeometry(QtCore.QRect(90, 260, 75, 23))
        self.addRowButton.setObjectName(_fromUtf8("addRowButton"))
        self.deleteRowButton = QtGui.QPushButton(Dialog)
        self.deleteRowButton.setGeometry(QtCore.QRect(270, 260, 75, 23))
        self.deleteRowButton.setObjectName(_fromUtf8("deleteRowButton"))
        self.deletePid = QtGui.QLineEdit(Dialog)
        self.deletePid.setGeometry(QtCore.QRect(270, 290, 71, 20))
        self.deletePid.setText(_fromUtf8(""))
        self.deletePid.setObjectName(_fromUtf8("deletePid"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 290, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 320, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 350, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.addName = QtGui.QLineEdit(Dialog)
        self.addName.setGeometry(QtCore.QRect(90, 290, 113, 20))
        self.addName.setObjectName(_fromUtf8("addName"))
        self.addQuantity = QtGui.QLineEdit(Dialog)
        self.addQuantity.setGeometry(QtCore.QRect(90, 320, 113, 20))
        self.addQuantity.setObjectName(_fromUtf8("addQuantity"))
        self.addPrice = QtGui.QLineEdit(Dialog)
        self.addPrice.setGeometry(QtCore.QRect(90, 350, 113, 20))
        self.addPrice.setObjectName(_fromUtf8("addPrice"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(230, 290, 21, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.addRowButton.setText(_translate("Dialog", "Add Row", None))
        self.deleteRowButton.setText(_translate("Dialog", "Delete Row", None))
        self.label.setText(_translate("Dialog", "Name", None))
        self.label_2.setText(_translate("Dialog", "Quantity", None))
        self.label_3.setText(_translate("Dialog", "Price", None))
        self.label_4.setText(_translate("Dialog", "PID", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

