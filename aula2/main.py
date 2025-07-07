import pymysql

connection = pymysql.connect(
    host='localhost',
    user='usuario',
    password='senha',
    database='BD_ENV',
)
with connection:
    with connection.cursor() as cursor:
        #SQL
        print(cursor)



    cursor.close()