# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mdidemo.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 564)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.mdiArea = QtGui.QMdiArea(self.centralwidget)
        self.mdiArea.setGeometry(QtCore.QRect(90, 10, 581, 411))
        self.mdiArea.setObjectName(_fromUtf8("mdiArea"))
        self.subwindow = QtGui.QWidget()
        self.subwindow.setObjectName(_fromUtf8("subwindow"))
        self.label = QtGui.QLabel(self.subwindow)
        self.label.setGeometry(QtCore.QRect(60, 90, 131, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.textEdit = QtGui.QTextEdit(self.subwindow)
        self.textEdit.setGeometry(QtCore.QRect(90, 140, 104, 71))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.subwindow_2 = QtGui.QWidget()
        self.subwindow_2.setObjectName(_fromUtf8("subwindow_2"))
        self.label_2 = QtGui.QLabel(self.subwindow_2)
        self.label_2.setGeometry(QtCore.QRect(90, 40, 141, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.showNextButton = QtGui.QPushButton(self.centralwidget)
        self.showNextButton.setGeometry(QtCore.QRect(150, 440, 75, 23))
        self.showNextButton.setObjectName(_fromUtf8("showNextButton"))
        self.showPreviousButton = QtGui.QPushButton(self.centralwidget)
        self.showPreviousButton.setGeometry(QtCore.QRect(340, 440, 81, 23))
        self.showPreviousButton.setObjectName(_fromUtf8("showPreviousButton"))
        self.closeAllButton = QtGui.QPushButton(self.centralwidget)
        self.closeAllButton.setGeometry(QtCore.QRect(520, 430, 75, 23))
        self.closeAllButton.setObjectName(_fromUtf8("closeAllButton"))
        self.cascadeButton = QtGui.QPushButton(self.centralwidget)
        self.cascadeButton.setGeometry(QtCore.QRect(130, 490, 75, 23))
        self.cascadeButton.setObjectName(_fromUtf8("cascadeButton"))
        self.tileButton = QtGui.QPushButton(self.centralwidget)
        self.tileButton.setGeometry(QtCore.QRect(270, 490, 75, 23))
        self.tileButton.setObjectName(_fromUtf8("tileButton"))
        self.SubWindowViewButton = QtGui.QPushButton(self.centralwidget)
        self.SubWindowViewButton.setGeometry(QtCore.QRect(420, 490, 91, 23))
        self.SubWindowViewButton.setObjectName(_fromUtf8("SubWindowViewButton"))
        self.tabbedViewButton = QtGui.QPushButton(self.centralwidget)
        self.tabbedViewButton.setGeometry(QtCore.QRect(570, 490, 75, 23))
        self.tabbedViewButton.setObjectName(_fromUtf8("tabbedViewButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuWindows = QtGui.QMenu(self.menubar)
        self.menuWindows.setObjectName(_fromUtf8("menuWindows"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionFirst_Window = QtGui.QAction(MainWindow)
        self.actionFirst_Window.setObjectName(_fromUtf8("actionFirst_Window"))
        self.actionSecond_Window = QtGui.QAction(MainWindow)
        self.actionSecond_Window.setObjectName(_fromUtf8("actionSecond_Window"))
        self.menuWindows.addAction(self.actionFirst_Window)
        self.menuWindows.addAction(self.actionSecond_Window)
        self.menubar.addAction(self.menuWindows.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.subwindow.setWindowTitle(_translate("MainWindow", "Subwindow", None))
        self.label.setText(_translate("MainWindow", "Enter your views here", None))
        self.subwindow_2.setWindowTitle(_translate("MainWindow", "Subwindow", None))
        self.label_2.setText(_translate("MainWindow", "This is a second sub window", None))
        self.showNextButton.setText(_translate("MainWindow", "Show Next", None))
        self.showPreviousButton.setText(_translate("MainWindow", "Show Previous", None))
        self.closeAllButton.setText(_translate("MainWindow", "Close All", None))
        self.cascadeButton.setText(_translate("MainWindow", "Cascade", None))
        self.tileButton.setText(_translate("MainWindow", "Tile", None))
        self.SubWindowViewButton.setText(_translate("MainWindow", "SubWindow View", None))
        self.tabbedViewButton.setText(_translate("MainWindow", "Tabbed View", None))
        self.menuWindows.setTitle(_translate("MainWindow", "Windows", None))
        self.actionFirst_Window.setText(_translate("MainWindow", "First Window", None))
        self.actionSecond_Window.setText(_translate("MainWindow", "Second Window", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

