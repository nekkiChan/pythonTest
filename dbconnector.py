import psycopg2
import os

from dotenv import load_dotenv

# .envファイルの内容を読み込見込む
load_dotenv()


dbname = os.environ.get('DB_NAME')
user = os.environ.get('DB_USER')
password = os.environ.get('DB_PASSWORD')
host = os.environ.get('DB_HOST')
port = os.environ.get('DB_PORT')

conn = psycopg2.connect(
    dbname=dbname,
    user=user,
    password=password,
    host=host,
    port=port
)
cur = conn.cursor()

cur.execute('select * from users')
print(cur.fetchall())

cur.close()
conn.close()