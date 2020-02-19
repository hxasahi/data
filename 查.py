# -*- coding: utf-8 -*-
import pymysql
connect = pymysql.connect(
    host="localhost",
    user="root",password="2020hx",
    database="datatest_1",)

cursor = connect.cursor()

#查 sql
show_sql = 'SELECT * FROM test_1 '
cursor.execute(show_sql)
show=cursor.fetchall()
print(show)
cursor.scroll(1, mode="absolute")
cursor.close()
connect.close()
