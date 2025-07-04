import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CUIDADO: fazendo delete sem where
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)

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
cursor.execute(
f'INSERT INTO {TABLE_NAME} (id, name, weigth) '
 'VALUES (NULL, "Matheus Ileck Farias", 64)'   
) # Inserir um valor na base de dados

connection.commit()


cursor.close()
connection.close()