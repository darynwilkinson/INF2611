import sys
from dispcalendar import *
#import datetime

class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.calendarWidget, QtCore.SIGNAL('selectionChanged()'), self.dispdate)
        #self.ui.dateEdit.setDate(datetime.datetime.now() + datetime.timedelta(days = 1))
        self.ui.dateEdit.setDate(QtCore.QDate.currentDate().addDays(1))
    
    def dispdate(self):
        self.ui.dateEdit.setDate(self.ui.calendarWidget.selectedDate())

if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())