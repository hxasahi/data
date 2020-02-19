
import pymysql
import pandas 
conn = pymysql.connect(
    host="localhost",
    user="root",password="2020hx",
    database="ceshi",
    use_unicode=True, charset="utf8")

show_sql = 'SELECT * FROM ceshi_2 '

cursor = conn.cursor()
cursor.execute(show_sql)
show=cursor.fetchall()

print(show)
cursor.close()
conn.close()
i = input()
