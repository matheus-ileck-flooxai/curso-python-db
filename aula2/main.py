import pymysql
import dotenv
import os
from typing import cast

CURRENT_CURSOR = pymysql.cursors.SSDictCursor

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    cursorclass=CURRENT_CURSOR,
)

with connection:
  
    with connection.cursor() as cursor:
        cursor = cast(CURRENT_CURSOR, cursor)

        sql = (
            f'UPDATE users '
            'SET name=%s, age=%s '
            'WHERE id=%s'
        )

        cursor.execute(sql, ('caique', 19, 1))

        cursor.execute(f'SELECT * FROM users ')
        print('For 1: ')

        for row in cursor.fetchall_unbuffered():
            print(row)

            
        print()
        print('For 2: ')
        for row in cursor.fetchall_unbuffered():
            print(row)
    connection.commit()


