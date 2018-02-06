import sys
from mdidemo import *

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.mdiArea.addSubWindow(self.ui.subwindow)
        self.ui.mdiArea.addSubWindow(self.ui.subwindow_2)
        self.ui.mdiArea.tileSubWindows()
        QtCore.QObject.connect(self.ui.showNextButton, QtCore.SIGNAL('clicked()'), self.displayNext)
        QtCore.QObject.connect(self.ui.closeAllButton, QtCore.SIGNAL('clicked()'), self.closeAllSubWindows)
        QtCore.QObject.connect(self.ui.tabbedViewButton, QtCore.SIGNAL('cliciked()'), self.tabbedView)
    
    def displayNext(self):
        self.ui.mdiArea.activateNextSubWindow()
    
    def closeAllSubWindows(self):
        self.ui.mdiArea.closeAllSubWindows()
    
    def tabbedView(self):
        self.ui.mdiArea.setViewMode(1)

if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())