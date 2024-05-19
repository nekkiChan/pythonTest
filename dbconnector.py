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


# cur.execute('select * from users')
# cur.execute('select id as id, name as "名前", sex as "性別", age as "性別" from users')

def fetch_data():
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    cur = conn.cursor()
    cur.execute('select id as id, name as "名前", sex as "性別", age as "性別" from users')
    data = cur.fetchall()
    # cur.close()
    conn.close()
    return data

print(fetch_data())
