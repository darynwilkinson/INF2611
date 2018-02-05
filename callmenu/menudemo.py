# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menudemo.ui'
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
        MainWindow.resize(800, 526)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 100, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menu_View = QtGui.QMenu(self.menuFile)
        self.menu_View.setObjectName(_fromUtf8("menu_View"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionPage_Layout_Box = QtGui.QAction(MainWindow)
        self.actionPage_Layout_Box.setCheckable(True)
        self.actionPage_Layout_Box.setObjectName(_fromUtf8("actionPage_Layout_Box"))
        self.actionFormat_Box = QtGui.QAction(MainWindow)
        self.actionFormat_Box.setCheckable(True)
        self.actionFormat_Box.setObjectName(_fromUtf8("actionFormat_Box"))
        self.actionCut = QtGui.QAction(MainWindow)
        self.actionCut.setObjectName(_fromUtf8("actionCut"))
        self.actionCopy = QtGui.QAction(MainWindow)
        self.actionCopy.setObjectName(_fromUtf8("actionCopy"))
        self.menu_View.addAction(self.actionPage_Layout_Box)
        self.menu_View.addAction(self.actionFormat_Box)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menu_View.menuAction())
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "TextLabel", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menu_View.setTitle(_translate("MainWindow", "&View", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionOpen.setStatusTip(_translate("MainWindow", "Opening a file", None))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionPage_Layout_Box.setText(_translate("MainWindow", "Page Layout Box", None))
        self.actionPage_Layout_Box.setShortcut(_translate("MainWindow", "Shift+P", None))
        self.actionFormat_Box.setText(_translate("MainWindow", "Format Box", None))
        self.actionCut.setText(_translate("MainWindow", "Cut", None))
        self.actionCopy.setText(_translate("MainWindow", "Copy", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

