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
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS users ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'name VARCHAR(50) NOT NULL, '
            'age INT NOT NULL, '
            'PRIMARY KEY (id)'
            ') '
        )
        # CUIDADO: isso limpa a tabela
        cursor.execute('TRUNCATE TABLE users')
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            'INSERT INTO users '
            '(name, age) VALUES (%(name)s, %(age)s) '
        )
        data = {
            "name": "Larissa",
            "age": "20"
        }
        result = cursor.execute(sql, data)
    connection.commit()


