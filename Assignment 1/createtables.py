import pymysql
import sys

conn = pymysql.connect(host="localhost", user="root", passwd="root")
cursor = conn.cursor()

#Create crime database
try:
    cursor.execute('create database crime')
except pymysql.Error:
    print("Error creating crime database")
    sys.exit(1)

#Create area table
try:
    cursor.execute("""
    create table crime.area (area_id int NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT,
    name char(50) NOT NULL UNIQUE)
    """)
except pymysql.Error:
    print("Error creating area table")
    sys.exit(1)

#Add areas to area table
areas = ["Newlands", "Claremont", "Rondebosch"]
for area in areas:
    try:
        cursor.execute("""
        INSERT INTO crime.area (name)
        VALUES ('%s')
        """ %(area))
        conn.commit()
    except:
        conn.rollback()
        exit(1)

#Create type table
try:
    cursor.execute("""
    create table crime.type (type_id int NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT,
    name char(50) NOT NULL UNIQUE)
    """)
except pymysql.Error:
    print("Error creating type table")
    sys.exit(1)

#Add types to type table
types = ["house breaking", "murder", "mugging", "rape", "car theft", "car jacking", "domestic vioence", "noise complaint", "other"]
for typ in types:
    try:
        cursor.execute("""
        INSERT INTO crime.type (name)
        VALUES ('%s')
        """ %(typ))
        conn.commit()
    except:
        conn.rollback()
        exit(1)

#Create event table
try:
    cursor.execute("""
    create table crime.event (event_id int NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT,
    type_id int NOT NULL,
    time char(100) NOT NULL,
    false_alarm boolean,
    loc_street char(50) NOT NULL,
    loc_num smallint NOT NULL,
    suspect_caught boolean,
    comments char(100),
    area_id int NOT NULL,
    FOREIGN KEY (type_id) REFERENCES type(type_id) ON DELETE CASCADE,
    FOREIGN KEY (area_id) REFERENCES area(area_id) ON DELETE CASCADE)
    """)
except pymysql.Error:
    print("Error creating event table")
    sys.exit(1)

conn.commit()
cursor.close()
conn.close()