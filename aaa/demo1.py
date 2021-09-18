# -*-codeing = utf-8 -*-
# @Time:2021/3/2 21:41
# @Author:吕尤
# @File:demo1.py
# @Software:PyCharm
import pymysql

conn=pymysql.connect(host='localhost',user='lvyou1',password='zdsgzczzkjgz1222',database='user_info')
cursor=conn.cursor()
sql="SELECT * FROM instructor2 WHERE NAME='Bawa' OR NAME='Lembr' OR NAME='Wieland';"
cursor.execute(sql)
retdat=cursor.fetchall()
for row in retdat:
    print(row)
print("----------------------------------------------------------")

sql="UPDATE instructor2 SET salary = salary-20000 WHERE NAME='Bawa' "
cursor.execute(sql)
sql=" UPDATE instructor2 SET salary = salary + 20000 WHERE NAME='Lembr'"
cursor.execute(sql)
sql="SELECT * FROM instructor2 WHERE NAME='Bawa' OR NAME='Lembr' OR NAME='Wieland';"
cursor.execute(sql)
retdat=cursor.fetchall()

temp=0
for row in retdat:
    if row[1]=="Bawa" and row[3]>0:
        temp=1
if temp==1:
    for row in retdat:
        print(row)
    sql="INSERT INTO mylog(title,result) values ('转账20000','success')"
    cursor.execute(sql)
else:
    sql = "UPDATE instructor2 SET salary = salary+20000 WHERE NAME='Bawa' "
    cursor.execute(sql)
    sql = " UPDATE instructor2 SET salary = salary - 20000 WHERE NAME='Lembr'"
    cursor.execute(sql)
    sql = "SELECT * FROM instructor2 WHERE NAME='Bawa' OR NAME='Lembr' OR NAME='Wieland';"
    cursor.execute(sql)
    retdat=cursor.fetchall()
    for row in retdat:
        print(row)
    sql = "INSERT INTO mylog(title,result) values ('转账20000','failed') "
    cursor.execute(sql)
print("----------------------------------------------------------")
print("日志结果：")
sql="select * from mylog"
cursor.execute(sql)
retdat=cursor.fetchall()
for row in retdat:
    print(row)

print("----------------------------------------------------------")

sql="UPDATE instructor2 SET salary = salary-100000 WHERE NAME='Bawa' "
cursor.execute(sql)
sql=" UPDATE instructor2 SET salary = salary + 100000 WHERE NAME='Lembr'"
cursor.execute(sql)
sql="SELECT * FROM instructor2 WHERE NAME='Bawa' OR NAME='Lembr' OR NAME='Wieland';"
cursor.execute(sql)
retdat=cursor.fetchall()

temp=0
for row in retdat:
    if row[1]=="Bawa" and row[3]>0:
        temp=1
if temp==1:
    for row in retdat:
        print(row)
    sql="INSERT INTO mylog(title,result) values ('转账100000','success')"
    cursor.execute(sql)
else:
    sql ="UPDATE instructor2 SET salary = salary + 100000 WHERE NAME='Bawa'"
    cursor.execute(sql)
    sql ="UPDATE instructor2 SET salary = salary - 100000 WHERE NAME='Lembr'"
    cursor.execute(sql)
    sql = "SELECT * FROM instructor2 WHERE NAME='Bawa' OR NAME='Lembr' OR NAME='Wieland';"
    cursor.execute(sql)
    retdat = cursor.fetchall()
    for row in retdat:
        print(row)
    sql = "INSERT INTO mylog(title,result) values ('转账100000','failed') "
    cursor.execute(sql)
print("----------------------------------------------------------")
print("日志结果：")
sql="select * from mylog"
cursor.execute(sql)
conn.rollback()
retdat=cursor.fetchall()
for row in retdat:
    print(row)
cursor.close()
conn.close()