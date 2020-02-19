# -*- coding: utf-8 -*-
import pymysql
connect = pymysql.connect(
    host="localhost",
    user="root",password="2020hx",
    database="datatest_1",)
cursor = connect.cursor()
search_sql = 'SELECT * FROM test_1 WHERE name = %s;'

search_name = raw_input('search_name')

cursor.execute(search_sql,[search_name])

show=cursor.fetchall()
print(show)
'''
cursor = connect.cursor()
cursor.scroll(1, mode='absolute')
print(cursor.fetchone())
'''
