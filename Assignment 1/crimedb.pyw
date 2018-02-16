import sys
from crimeui import *
from PyQt4 import QtSql, QtGui
import pymysql

class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.ui.dateTimeEdit_2.setDateTime(QtCore.QDateTime.currentDateTime())
        QtCore.QObject.connect(self.ui.calendarWidget, QtCore.SIGNAL('selectionChanged()'), self.dispdate)
        QtCore.QObject.connect(self.ui.calendarWidget_2, QtCore.SIGNAL('selectionChanged()'), self.dispdate2)
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL('clicked()'), self.addRecord)
    
    def dispdate(self):
        self.ui.dateTimeEdit.setDate(self.ui.calendarWidget.selectedDate())
    
    def dispdate2(self):
        self.ui.dateTimeEdit_2.setDate(self.ui.calendarWidget_2.selectedDate())
    
    def addRecord(self):
        conn = pymysql.connect(host="localhost", user="root", passwd="root", db="crime")
        cursor = conn.cursor()
        typ = str(self.ui.comboBox.currentText())
        typ = cursor.execute("""
        SELECT type_id FROM type WHERE name='%s'
        """%(typ))
        typ = cursor.fetchone()[0]
        datetime = str(self.ui.dateTimeEdit.dateTime().toString())
        if self.ui.radioButton.isChecked():
            falsalm = 1
        else:
            falsalm = 0
        street = str(self.ui.streetnameEdit.text())
        strnum = int(self.ui.housenumberEdit.text())
        if self.ui.radioButton_3.isChecked():
            suscght = 1
        else:
            suscght = 0
        comment = self.ui.textEdit.toPlainText()
        area = str(self.ui.comboBox_4.currentText())
        area = cursor.execute("""
        SELECT area_id FROM area WHERE name='%s'
        """%(area))
        area = cursor.fetchone()[0]
        cursor.execute("""
        INSERT INTO event (type_id, time, false_alarm, loc_street, loc_num, suspect_caught, comments, area_id)
        VALUES (%d, '%s', %d, '%s', %d, %d, '%s', %d)
        """ %(typ, datetime, falsalm, street, strnum, suscght, comment, area))
        conn.commit()
        cursor.close()
        conn.close()
        self.ui.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.ui.streetnameEdit.clear()
        self.ui.housenumberEdit.clear()
        self.ui.textEdit.clear()

if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())