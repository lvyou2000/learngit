import os
import pymysql

# conn=pymysql.connect(host='localhost',user='lvyou1',password='zdsgzczzkjgz1222',database='user_info')
# cursor=conn.cursor()
rootDir='D:\学习\数据库系统\dblabs\labs\sqlite-autoconf-3230100'
for (dirName, dirs, files) in os.walk(rootDir):
    temp=0
    for fileName in files:
        temp=temp+1
        parentFileName=os.path.basename(dirName)
    if temp<3:
        print(parentFileName)


# conn.commit()
# cursor.close()
# conn.close()



# import sys
# import pymysql
# try:
#     conn=pymysql.connect(host='localhost',user='lvyou1',password='zdsgzczzkjgz1222',database='user_info')
# except pymysql.connector.Error as e:
#     conn = None
#     print('connect fails!{}'.format(e))
# if None==conn:
#    sys.exit()
# cursor = conn.cursor()
# sql= 'SELECT name,dept_name,salary from instructor'
# try:
#     cursor.execute(sql)
#     retdat=cursor.fetchall()
#     for row in retdat:
#         print(row)
# except pymysql.connector.Error as e:
#     print('query error!{}'.format(e))
# finally:
#     cursor.close()
#     conn.close()
