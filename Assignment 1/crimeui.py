# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Assignment 1\crimeui.ui'
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

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName(_fromUtf8("dialog"))
        dialog.resize(444, 554)
        self.tabWidget = QtGui.QTabWidget(dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 441, 551))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayoutWidget = QtGui.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 431, 521))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.comboBox = QtGui.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBox)
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label)
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.calendarWidget = QtGui.QCalendarWidget(self.verticalLayoutWidget)
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.calendarWidget)
        self.dateTimeEdit = QtGui.QDateTimeEdit(self.verticalLayoutWidget)
        self.dateTimeEdit.setObjectName(_fromUtf8("dateTimeEdit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.dateTimeEdit)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.falsealarmLayout = QtGui.QVBoxLayout()
        self.falsealarmLayout.setObjectName(_fromUtf8("falsealarmLayout"))
        self.radioButton = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.buttonGroup = QtGui.QButtonGroup(dialog)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.radioButton)
        self.falsealarmLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.buttonGroup.addButton(self.radioButton_2)
        self.falsealarmLayout.addWidget(self.radioButton_2)
        self.horizontalLayout.addLayout(self.falsealarmLayout)
        self.formLayout.setLayout(3, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_8)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.radioButton_3 = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.buttonGroup_2 = QtGui.QButtonGroup(dialog)
        self.buttonGroup_2.setObjectName(_fromUtf8("buttonGroup_2"))
        self.buttonGroup_2.addButton(self.radioButton_3)
        self.verticalLayout.addWidget(self.radioButton_3)
        self.radioButton_4 = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.buttonGroup_2.addButton(self.radioButton_4)
        self.verticalLayout.addWidget(self.radioButton_4)
        self.formLayout.setLayout(6, QtGui.QFormLayout.FieldRole, self.verticalLayout)
        self.streetnameEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.streetnameEdit.setObjectName(_fromUtf8("streetnameEdit"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.streetnameEdit)
        self.housenumberEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.housenumberEdit.setObjectName(_fromUtf8("housenumberEdit"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.housenumberEdit)
        self.textEdit = QtGui.QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.textEdit)
        self.label_22 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_22)
        self.comboBox_4 = QtGui.QComboBox(self.verticalLayoutWidget)
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.comboBox_4)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_3.addWidget(self.pushButton)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.tab_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 431, 527))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_9 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_9)
        self.comboBox_2 = QtGui.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.setItemText(0, _fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboBox_2)
        self.label_10 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_10)
        self.label_11 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_11)
        self.label_12 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_12.setText(_fromUtf8(""))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_12)
        self.calendarWidget_2 = QtGui.QCalendarWidget(self.verticalLayoutWidget_2)
        self.calendarWidget_2.setObjectName(_fromUtf8("calendarWidget_2"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.calendarWidget_2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.falsealarmLayout_2 = QtGui.QVBoxLayout()
        self.falsealarmLayout_2.setObjectName(_fromUtf8("falsealarmLayout_2"))
        self.radioButton_5 = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_5.setObjectName(_fromUtf8("radioButton_5"))
        self.buttonGroup_3 = QtGui.QButtonGroup(dialog)
        self.buttonGroup_3.setObjectName(_fromUtf8("buttonGroup_3"))
        self.buttonGroup_3.addButton(self.radioButton_5)
        self.falsealarmLayout_2.addWidget(self.radioButton_5)
        self.radioButton_6 = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_6.setObjectName(_fromUtf8("radioButton_6"))
        self.buttonGroup_3.addButton(self.radioButton_6)
        self.falsealarmLayout_2.addWidget(self.radioButton_6)
        self.horizontalLayout_2.addLayout(self.falsealarmLayout_2)
        self.formLayout_2.setLayout(4, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_13 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_13)
        self.label_14 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_14)
        self.label_15 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_15)
        self.label_16 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.formLayout_2.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_16)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.radioButton_7 = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_7.setObjectName(_fromUtf8("radioButton_7"))
        self.buttonGroup_4 = QtGui.QButtonGroup(dialog)
        self.buttonGroup_4.setObjectName(_fromUtf8("buttonGroup_4"))
        self.buttonGroup_4.addButton(self.radioButton_7)
        self.verticalLayout_2.addWidget(self.radioButton_7)
        self.radioButton_8 = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_8.setObjectName(_fromUtf8("radioButton_8"))
        self.buttonGroup_4.addButton(self.radioButton_8)
        self.verticalLayout_2.addWidget(self.radioButton_8)
        self.formLayout_2.setLayout(7, QtGui.QFormLayout.FieldRole, self.verticalLayout_2)
        self.streetnameEdit_2 = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.streetnameEdit_2.setObjectName(_fromUtf8("streetnameEdit_2"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.streetnameEdit_2)
        self.housenumberEdit_2 = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.housenumberEdit_2.setObjectName(_fromUtf8("housenumberEdit_2"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.FieldRole, self.housenumberEdit_2)
        self.textEdit_2 = QtGui.QTextEdit(self.verticalLayoutWidget_2)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.formLayout_2.setWidget(8, QtGui.QFormLayout.FieldRole, self.textEdit_2)
        self.label_19 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_19)
        self.label_23 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.formLayout_2.setWidget(9, QtGui.QFormLayout.LabelRole, self.label_23)
        self.comboBox_5 = QtGui.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.setItemText(0, _fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.formLayout_2.setWidget(9, QtGui.QFormLayout.FieldRole, self.comboBox_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.lineEdit_2 = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_6.addWidget(self.lineEdit_2)
        self.deleteButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.horizontalLayout_6.addWidget(self.deleteButton)
        self.formLayout_2.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.dateTimeEdit_2 = QtGui.QDateTimeEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateTimeEdit_2.sizePolicy().hasHeightForWidth())
        self.dateTimeEdit_2.setSizePolicy(sizePolicy)
        self.dateTimeEdit_2.setObjectName(_fromUtf8("dateTimeEdit_2"))
        self.horizontalLayout_5.addWidget(self.dateTimeEdit_2)
        self.formLayout_2.setLayout(3, QtGui.QFormLayout.FieldRole, self.horizontalLayout_5)
        self.verticalLayout_4.addLayout(self.formLayout_2)
        self.pushButton_2 = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout_4.addWidget(self.pushButton_2)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayoutWidget_6 = QtGui.QWidget(self.tab_3)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(1, 3, 431, 521))
        self.verticalLayoutWidget_6.setObjectName(_fromUtf8("verticalLayoutWidget_6"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.tableView = QtGui.QTableView(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.tableView.setFont(font)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.verticalLayout_8.addWidget(self.tableView)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_8.addItem(spacerItem)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_17 = QtGui.QLabel(self.verticalLayoutWidget_6)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_3.addWidget(self.label_17)
        self.lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.label_18 = QtGui.QLabel(self.verticalLayoutWidget_6)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.horizontalLayout_3.addWidget(self.label_18)
        self.comboBox_3 = QtGui.QComboBox(self.verticalLayoutWidget_6)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.setItemText(0, _fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.comboBox_3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        spacerItem1 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_7.addItem(spacerItem1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_20 = QtGui.QLabel(self.verticalLayoutWidget_6)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.horizontalLayout_4.addWidget(self.label_20)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.radioButton_9 = QtGui.QRadioButton(self.verticalLayoutWidget_6)
        self.radioButton_9.setObjectName(_fromUtf8("radioButton_9"))
        self.buttonGroup_5 = QtGui.QButtonGroup(dialog)
        self.buttonGroup_5.setObjectName(_fromUtf8("buttonGroup_5"))
        self.buttonGroup_5.addButton(self.radioButton_9)
        self.verticalLayout_5.addWidget(self.radioButton_9)
        self.radioButton_10 = QtGui.QRadioButton(self.verticalLayoutWidget_6)
        self.radioButton_10.setObjectName(_fromUtf8("radioButton_10"))
        self.buttonGroup_5.addButton(self.radioButton_10)
        self.verticalLayout_5.addWidget(self.radioButton_10)
        self.radioButton_13 = QtGui.QRadioButton(self.verticalLayoutWidget_6)
        self.radioButton_13.setObjectName(_fromUtf8("radioButton_13"))
        self.buttonGroup_5.addButton(self.radioButton_13)
        self.verticalLayout_5.addWidget(self.radioButton_13)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.label_21 = QtGui.QLabel(self.verticalLayoutWidget_6)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.horizontalLayout_4.addWidget(self.label_21)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.radioButton_11 = QtGui.QRadioButton(self.verticalLayoutWidget_6)
        self.radioButton_11.setObjectName(_fromUtf8("radioButton_11"))
        self.buttonGroup_6 = QtGui.QButtonGroup(dialog)
        self.buttonGroup_6.setObjectName(_fromUtf8("buttonGroup_6"))
        self.buttonGroup_6.addButton(self.radioButton_11)
        self.verticalLayout_6.addWidget(self.radioButton_11)
        self.radioButton_12 = QtGui.QRadioButton(self.verticalLayoutWidget_6)
        self.radioButton_12.setObjectName(_fromUtf8("radioButton_12"))
        self.buttonGroup_6.addButton(self.radioButton_12)
        self.verticalLayout_6.addWidget(self.radioButton_12)
        self.radioButton_14 = QtGui.QRadioButton(self.verticalLayoutWidget_6)
        self.radioButton_14.setObjectName(_fromUtf8("radioButton_14"))
        self.buttonGroup_6.addButton(self.radioButton_14)
        self.verticalLayout_6.addWidget(self.radioButton_14)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        spacerItem2 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_7.addItem(spacerItem2)
        self.pushButton_3 = QtGui.QPushButton(self.verticalLayoutWidget_6)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout_7.addWidget(self.pushButton_3)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))

        self.retranslateUi(dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(_translate("dialog", "Crimfo", None))
        self.label_2.setText(_translate("dialog", "Type", None))
        self.comboBox.setItemText(0, _translate("dialog", "car jacking", None))
        self.comboBox.setItemText(1, _translate("dialog", "car theft", None))
        self.comboBox.setItemText(2, _translate("dialog", "house breaking", None))
        self.comboBox.setItemText(3, _translate("dialog", "murder", None))
        self.comboBox.setItemText(4, _translate("dialog", "mugging", None))
        self.comboBox.setItemText(5, _translate("dialog", "rape", None))
        self.comboBox.setItemText(6, _translate("dialog", "domestic violence", None))
        self.comboBox.setItemText(7, _translate("dialog", "noise complaint", None))
        self.comboBox.setItemText(8, _translate("dialog", "other (please comment)", None))
        self.label_4.setText(_translate("dialog", "Time", None))
        self.label.setText(_translate("dialog", "False Alarm", None))
        self.radioButton.setText(_translate("dialog", "True", None))
        self.radioButton_2.setText(_translate("dialog", "False", None))
        self.label_5.setText(_translate("dialog", "Street Name", None))
        self.label_6.setText(_translate("dialog", "House Number", None))
        self.label_7.setText(_translate("dialog", "Suspect Caught", None))
        self.label_8.setText(_translate("dialog", "Comments", None))
        self.radioButton_3.setText(_translate("dialog", "True", None))
        self.radioButton_4.setText(_translate("dialog", "False", None))
        self.label_22.setText(_translate("dialog", "Area", None))
        self.comboBox_4.setItemText(0, _translate("dialog", "Rondebosch", None))
        self.comboBox_4.setItemText(1, _translate("dialog", "Claremont", None))
        self.comboBox_4.setItemText(2, _translate("dialog", "Newlands", None))
        self.pushButton.setText(_translate("dialog", "Add", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("dialog", "Add Event", None))
        self.label_9.setText(_translate("dialog", "Type", None))
        self.comboBox_2.setItemText(1, _translate("dialog", "car jacking", None))
        self.comboBox_2.setItemText(2, _translate("dialog", "car theft", None))
        self.comboBox_2.setItemText(3, _translate("dialog", "house breaking", None))
        self.comboBox_2.setItemText(4, _translate("dialog", "murder", None))
        self.comboBox_2.setItemText(5, _translate("dialog", "mugging", None))
        self.comboBox_2.setItemText(6, _translate("dialog", "rape", None))
        self.comboBox_2.setItemText(7, _translate("dialog", "domestic violence", None))
        self.comboBox_2.setItemText(8, _translate("dialog", "noise complaint", None))
        self.comboBox_2.setItemText(9, _translate("dialog", "other (please comment)", None))
        self.label_10.setText(_translate("dialog", "Time", None))
        self.label_11.setText(_translate("dialog", "False Alarm", None))
        self.radioButton_5.setText(_translate("dialog", "True", None))
        self.radioButton_6.setText(_translate("dialog", "False", None))
        self.label_13.setText(_translate("dialog", "Street Name", None))
        self.label_14.setText(_translate("dialog", "House Number", None))
        self.label_15.setText(_translate("dialog", "Suspect Caught", None))
        self.label_16.setText(_translate("dialog", "Comments", None))
        self.radioButton_7.setText(_translate("dialog", "True", None))
        self.radioButton_8.setText(_translate("dialog", "False", None))
        self.label_19.setText(_translate("dialog", "Event ID", None))
        self.label_23.setText(_translate("dialog", "Area", None))
        self.comboBox_5.setItemText(1, _translate("dialog", "Rondebosch", None))
        self.comboBox_5.setItemText(2, _translate("dialog", "Claremont", None))
        self.comboBox_5.setItemText(3, _translate("dialog", "Newlands", None))
        self.deleteButton.setText(_translate("dialog", "Delete", None))
        self.pushButton_2.setText(_translate("dialog", "Update", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("dialog", "Update Event", None))
        self.label_17.setText(_translate("dialog", "Event ID", None))
        self.label_18.setText(_translate("dialog", "type", None))
        self.comboBox_3.setItemText(1, _translate("dialog", "house breaking", None))
        self.comboBox_3.setItemText(2, _translate("dialog", "murder", None))
        self.comboBox_3.setItemText(3, _translate("dialog", "mugging", None))
        self.comboBox_3.setItemText(4, _translate("dialog", "rape", None))
        self.comboBox_3.setItemText(5, _translate("dialog", "car theft", None))
        self.comboBox_3.setItemText(6, _translate("dialog", "car jacking", None))
        self.comboBox_3.setItemText(7, _translate("dialog", "domestic violence", None))
        self.comboBox_3.setItemText(8, _translate("dialog", "noise complaint", None))
        self.comboBox_3.setItemText(9, _translate("dialog", "other", None))
        self.label_20.setText(_translate("dialog", "False Alarm", None))
        self.radioButton_9.setText(_translate("dialog", "True", None))
        self.radioButton_10.setText(_translate("dialog", "False", None))
        self.radioButton_13.setText(_translate("dialog", "All", None))
        self.label_21.setText(_translate("dialog", "Suspect Caught", None))
        self.radioButton_11.setText(_translate("dialog", "True", None))
        self.radioButton_12.setText(_translate("dialog", "False", None))
        self.radioButton_14.setText(_translate("dialog", "All", None))
        self.pushButton_3.setText(_translate("dialog", "Search", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("dialog", "Get Events", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dialog = QtGui.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())

