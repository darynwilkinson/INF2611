import sys
import pymysql

conn = pymysql.connect(host="localhost", user="root", passwd="root", db="shopping")
cursor = conn.cursor()
try:
    cursor.execute("""
    create table products(prod_id smallint NOT NULL,
    prod_name char(50),
    quantity smallint,
    price float)
    """)
except pymysql.Error:
    print("Error in creating products table")
    sys.exit(1)
cursor.close()
conn.close()