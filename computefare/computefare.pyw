import sys
from reservform import *

class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.classtypes = ['First Class', 'Second Class', 'Business Class', 'Economic Class']
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL('clicked()'), self.calcfare)
    
    def calcfare(self):
        self.ui.EnteredInfo.setText('Class: ' + self.ui.comboBox.currentText() + '\nNo. of Passengers: ' + str(self.ui.spinBox.value()) + '\nDate: ' + self.ui.calendarWidget.selectedDate().toString())
        fare = 0
        if self.ui.comboBox.currentText() == 'First Class':
            fare = 40
        elif self.ui.comboBox.currentText() == 'Second Class':
            fare = 30
        elif self.ui.comboBox.currentText() == 'Business Class':
            fare = 20
        else:
            fare = 10
        self.ui.FareInfo.setText('R ' + str(fare * self.ui.spinBox.value()))

if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())