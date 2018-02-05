import sys
from menudemo import *

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect(self.ui.actionOpen, QtCore.SIGNAL('triggered()'), self.openmessage)
        self.connect(self.ui.actionPage_Layout_Box, QtCore.SIGNAL('triggered()'), self.layoutmessage)
    
    def openmessage(self):
        self.ui.label.setText('Opening a file')
    
    def layoutmessage(self):
        self.ui.label.setText('You selected Page Layout option')

if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())