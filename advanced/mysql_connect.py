import pymysql

db = pymysql.connect(host="localhost", database="platform", user="root", password="root3306")
# 打开游标
cursor = db.cursor()

cursor.execute("show tables")
print(cursor)
print(cursor.fetchall())

cursor.execute("select * from sys_user")
for row in cursor.fetchall():
    print(row)
