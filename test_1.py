# -*- coding: utf-8 -*-
import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",password="2020hx",
    database="ceshi",)

cursor = conn.cursor()

cursor.execute("""INSERT INTO ceshi_3 VALUES(3,'我',17);""")
conn.commit()
cursor.close()
conn.close()
