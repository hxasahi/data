# -*- coding: utf-8 -*-
import pymysql
connect = pymysql.connect(
    host="localhost",
    user="root",password="2020hx",
    database="datatest_1",)

cursor = connect.cursor()

update_sql = 'UPDATE test_1 SET price=%s WHERE id = %s;'

update_id = input('update_id')
update_price = input('update_price')

cursor.execute(update_sql,[update_price,update_id])

connect.commit()

cursor.close()
connect.close()
i = input()
