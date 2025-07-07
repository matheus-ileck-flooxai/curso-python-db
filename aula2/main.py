import pymysql
import dotenv
import os


dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
)

with connection:
  
    with connection.cursor() as cursor:

        sql = (
            f'UPDATE users '
            'SET name=%s, age=%s '
            'WHERE id=%s'
        )

        cursor.execute(sql, ('caique', 19, 1))

        cursor.execute(f'SELECT * FROM users ')

        data = cursor.fetchall()
        
        for row in data:
            print(row)

        cursor.execute(
            'SELECT id from users ORDER BY id DESC LIMIT 1'
        )
        lastIdFromSelect = cursor.fetchone()
        print('rowcount', cursor.rowcount)
        print('lastrowid', cursor.lastrowid)
        print('lastrowid na mão', lastIdFromSelect)

        cursor.scroll(0, 'absolute')
        print('rownumber', cursor.rownumber)

      
    connection.commit()


