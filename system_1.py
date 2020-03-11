# -*- coding: cp936 -*-
import pymysql
connect = pymysql.connect(
    host="localhost",
    user="root",password="2020hx",
    database="datatest_1",)

def search():
    cursor = connect.cursor()
    search_sql = 'SELECT * FROM test_1 WHERE name = %s;'
    search_name = raw_input('search_name')
    cursor.execute(search_sql,[search_name])
    show=cursor.fetchall()
    print(show)
    cursor.close()
    connect.close()

def show():
    cursor = connect.cursor()
    show_sql = 'SELECT * FROM test_1 '
    cursor.execute(show_sql)
    show=cursor.fetchall()
    print(show)
    cursor.close()
    connect.close()

def insert():
    cursor = connect.cursor()
    insert_sql = 'INSERT INTO test_1 VALUES(%s,%s,%s);'
    p_id = input('id')
    p_name = raw_input('name')
    p_price = input('price')
    cursor.execute(insert_sql,[p_id,p_name,p_price])
    connect.commit()
    cursor.close()
    connect.close()

def update():
    cursor = connect.cursor()
    update_sql = 'UPDATE test_1 SET price=%s WHERE id = %s;'
    update_id = input('update_id')
    update_price = input('update_price')
    cursor.execute(update_sql,[update_price,update_id])
    connect.commit()
    cursor.close()
    connect.close()

def delete():
    cursor = connect.cursor()
    delete_sql = 'DELETE FROM test_1 WHERE id = %s;'
    delete_id = input('delete_id')
    cursor.execute(delete_sql,[delete_id])
    connect.commit()
    cursor.close()
    connect.close()

print('')
print('')
print('                          ��ӭʹ�òֿ����ϵͳ')
print('')
print('1 ����        '),
print('2 ɾ��      '),
print('3 �޸�   '),
print('4 ��ѯ     ')
print('')
print('99 �˳�    ')
print('')
i = input('               �밴�¶�Ӧ����ѡ��')
while 1 :
    if i == 1 :
        pass
    elif i== 2 :
        pass
    elif i == 3 :
        pass
    elif i == 4 :
        pass
    elif i == 99 :
        break
    else :
        pass
    i = input('               �밴�¶�Ӧ����ѡ��')
