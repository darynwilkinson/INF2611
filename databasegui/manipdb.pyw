import sys
import pymysql
import random
from databasegui import *
from PyQt4.QtGui import *

class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.addRowButton, QtCore.SIGNAL('clicked()'), self.addRow)
    
    def addRow(self):
        conn = pymysql.connect(host="localhost", user="root", passwd="root", db="shopping")
        cursor = conn.cursor()
        pid = random.randint(0,32000)
        pname = self.ui.addName.text()
        self.ui.addName.clear()
        qty = int(self.ui.addQuantity.text())
        self.ui.addQuantity.clear()
        price = int(self.ui.addPrice.text())
        self.ui.addPrice.clear()
        try:
            cursor.execute("""
            INSERT INTO products (prod_id, prod_name, quantity, price)
            VALUES (%d, '%s', %d, %f)
            """ %(pid, pname, qty, price))
            conn.commit()
        except pymysql.Error:
            print("Error in inserting to products table")
            conn.rollback()
        try:
            cursor.execute("SELECT * FROM products")
            rows = cursor.fetchall()
            self.ui.tableWidget.clear()
            self.ui.tableWidget.setRowCount(len(rows))
            for i in range(0,len(rows)):
                for j in range(0,3):
                    anitem = QTableWidgetItem(rows[i][j])
                    self.ui.tableWidget.setItem(i, j, anitem)
                    print (anitem)
        except:
            print("Error creating table")
        cursor.close()
        conn.close()

if __name__=="__main__":
     app = QtGui.QApplication(sys.argv)
     myapp = MyForm()
     myapp.show()
     sys.exit(app.exec())