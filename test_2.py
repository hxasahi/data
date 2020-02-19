# -*- coding: utf-8 -*-
import pymysql
connect = pymysql.connect(
    host="localhost",
    user="root",password="2020hx",
    database="datatest_1",)

cursor = connect.cursor()

#查 sql
#show_sql = 'SELECT * FROM test_1 '

#search_sql = 'SELECT * FROM test_1 WHERE name LIKE %%s%;'

#增 sql
insert_sql = 'INSERT INTO test_1 VALUES(%s,%s,%s);'

#增 实现

p_id = input('id')

p_name = raw_input('name')

p_price = input('price')

cursor.execute(insert_sql,[p_id,p_name,p_price])

#cursor.execute(show_sql)
connect.commit()

'''show=cursor.fetchall()
print(show)    '''
cursor.close()
connect.close()
i = input()
