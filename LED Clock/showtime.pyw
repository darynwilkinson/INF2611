import sys
from disptime import *

class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.showlcd)
        timer.start(1000)
        self.showlcd()
    
    def showlcd(self):
        time = QtCore.QTime.currentTime()
        text = time.toString('hh:mm:ss')
        self.ui.lcdNumber.display(text)

if __name__=="__main__":
     app = QtGui.QApplication(sys.argv)
     myapp = MyForm()
     myapp.show()
     sys.exit(app.exec())