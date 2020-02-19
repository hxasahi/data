# -*- coding: utf-8 -*-
import pymysql
connect = pymysql.connect(
    host="localhost",
    user="root",password="2020hx",
    database="datatest_1",)

cursor = connect.cursor()

delete_sql = 'DELETE FROM test_1 WHERE id = %s;'
delete_id = input('delete_id')
cursor.execute(delete_sql,[delete_id])

connect.commit()

cursor.close()
connect.close()
i = input()
