import pymysql
conn=pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='pythontest'
)
cursor=conn.cursor()
print(conn)