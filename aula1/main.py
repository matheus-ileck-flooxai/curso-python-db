import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CUIDADO: fazendo delete sem where
# cursor.execute(
    # f'DELETE FROM sqlite_sequence'
# )

# DELETE mais cuidadoso
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

# Cria a tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weigth REAL'
    ')'
)
connection.commit()

# Registrar valores nas colunas da tabela
#CUIDADO: sql injection
sql = (
f'INSERT INTO {TABLE_NAME} (name, weigth) '
 'VALUES (?, ?)'   
) 
cursor.execute(sql, ['Matheus teste', 4])

connection.commit()



if __name__ == '__main__':
    print(sql)


    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id = "3"'
    )
    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id = 1'
    )
    connection.commit()

    cursor.execute(
        f'SELECT * FROM {TABLE_NAME}'
    )

    cursor.execute(
        f'UPDATE {TABLE_NAME} '
        'SET name="QUALQUER", weigth=67.89 '
        'WHERE id = 2'
    )
    connection.commit()


    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight)

    cursor.close()
    connection.close()
