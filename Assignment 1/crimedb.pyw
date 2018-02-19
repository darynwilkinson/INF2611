import sys
from crimeui import *
from PyQt4 import QtSql, QtGui
import pymysql

class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_dialog()
        self.ui.setupUi(self)
        self.ui.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.ui.dateTimeEdit_2.setDateTime(QtCore.QDateTime.currentDateTime())
        QtCore.QObject.connect(self.ui.calendarWidget, QtCore.SIGNAL('selectionChanged()'), self.dispdate)
        QtCore.QObject.connect(self.ui.calendarWidget_2, QtCore.SIGNAL('selectionChanged()'), self.dispdate2)
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL('clicked()'), self.addRecord)
        QtCore.QObject.connect(self.ui.pushButton_2, QtCore.SIGNAL('clicked()'), self.updateRecord)
        QtCore.QObject.connect(self.ui.pushButton_3, QtCore.SIGNAL('clicked()'), self.searchRecords)
        QtCore.QObject.connect(self.ui.deleteButton, QtCore.SIGNAL('clicked()'), self.deleteRecord)
    
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
    
    def updateRecord(self):
        conn = pymysql.connect(host="localhost", user="root", passwd="root", db="crime")
        cursor = conn.cursor()
        typ = str(self.ui.comboBox_2.currentText())
        typ = cursor.execute("""
        SELECT type_id FROM type WHERE name='%s'
        """%(typ))
        typ = cursor.fetchone()[0]
        datetime = str(self.ui.dateTimeEdit_2.dateTime().toString())
        if self.ui.radioButton_5.isChecked():
            falsalm = 1
        else:
            falsalm = 0
        street = str(self.ui.streetnameEdit_2.text())
        strnum = int(self.ui.housenumberEdit_2.text())
        if self.ui.radioButton_7.isChecked():
            suscght = 1
        else:
            suscght = 0
        comment = self.ui.textEdit_2.toPlainText()
        area = str(self.ui.comboBox_5.currentText())
        area = cursor.execute("""
        SELECT area_id FROM area WHERE name='%s'
        """%(area))
        area = cursor.fetchone()[0]
        pid = int(self.ui.lineEdit_2.text())
        cursor.execute("""
        UPDATE event set type_id=%d, time='%s', false_alarm=%d, loc_street='%s', loc_num=%d, suspect_caught=%d, comments='%s', area_id=%d where event_id=%d
        """ %(typ, datetime, falsalm, street, strnum, suscght, comment, area, pid))
        conn.commit()
        cursor.close()
        conn.close()
        self.ui.dateTimeEdit_2.setDateTime(QtCore.QDateTime.currentDateTime())
        self.ui.streetnameEdit_2.clear()
        self.ui.housenumberEdit_2.clear()
        self.ui.textEdit_2.clear()
        self.ui.lineEdit_2.clear()
    
    def searchRecords(self):
        def createConnection():
            db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
            db.setHostName('localhost')
            db.setDatabaseName('crime')
            db.setUserName('root')
            db.setPassword('root')
            db.open()
            print (db.lastError().text())
            return True
        if not createConnection():
            sys.exit(1)
        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable("event")
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        filt = ""
        if self.ui.radioButton_9.isChecked():
            filt += "false_alarm=1 "
        elif self.ui.radioButton_10.isChecked():
            filt += "false_alarm=0 "
        if self.ui.radioButton_11.isChecked():
            if filt != "":
                filt += "AND "
            filt += "suspect_caught=1 "
        elif self.ui.radioButton_12.isChecked():
            if filt != "":
                filt += "AND "
            filt += "suspect_caught=0 "
        if self.ui.lineEdit.text() != "":
            if filt != "":
                filt += "AND "
            filt += "event_id=" + self.ui.lineEdit.text() + " "
        if self.ui.comboBox_3.currentText() != "":
            if filt != "":
                filt += "AND "
            conn = pymysql.connect(host="localhost", user="root", passwd="root", db="crime")
            cursor = conn.cursor()
            typ = str(self.ui.comboBox_3.currentText())
            typ = cursor.execute("""
            SELECT type_id FROM type WHERE name='%s'
            """%(typ))
            typ = cursor.fetchone()[0]
            cursor.close()
            conn.close()
            filt += "type_id=" + str(typ)
        print(filt) 
        self.model.setFilter(filt)
        self.model.select()
        self.ui.tableView.setModel(self.model)
    
    def deleteRecord(self):
        if str(self.ui.lineEdit_2.text()) != "":
            pid = int(self.ui.lineEdit_2.text())
            conn = pymysql.connect(host="localhost", user="root", passwd="root", db="crime")
            cursor = conn.cursor()
            cursor.execute("""
            DELETE from event WHERE event_id=%d
            """%(pid))
            conn.commit()
            cursor.close()
            conn.close()
            self.ui.lineEdit_2.clear()

if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())