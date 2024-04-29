import os
import psycopg2

class DatabaseConnectorModel:
    def __init__(self):
        self.connection = None
        self.cursor = None
        print("DatabaseConnectModel")
        
        # 環境変数からデータベース接続情報を取得
        self.dbname = os.environ.get('DB_NAME')
        self.user = os.environ.get('DB_USER')
        self.password = os.environ.get('DB_PASSWORD')
        self.host = os.environ.get('DB_HOST')
        self.port = os.environ.get('DB_PORT')
        
        self.connect()

        # データベースが存在しない場合にのみ作成する
        # if not self.check_database_exists():
        # self.create_database()

        self.disconnect()

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
            print("Connected to PostgreSQL!")
        except psycopg2.Error as e:
            print("Unable to connect to the database:", e)


    def disconnect(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Disconnected from PostgreSQL.")

    def check_database_exists(self):
        try:
            # データベースの存在を確認するクエリ
            self.cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s;", (self.dbname,))
            result = self.cursor.fetchone()
            return bool(result)
        except psycopg2.Error as e:
            print("Error checking database existence:", e)
            return False

    def create_database(self):
        try:
            # データベース作成のクエリを定義
            create_db_query = f"CREATE DATABASE {self.dbname};"

            # クエリを実行
            self.cursor.execute(create_db_query)
            self.connection.commit()

            print("Database created successfully.")
        except psycopg2.Error as e:
            self.connection.rollback()
            print("Error creating database:", e)

    def load_data_from_db(self):
        try:
            self.cursor.execute("SELECT name FROM your_table;")
            rows = self.cursor.fetchall()
            if rows:
                self.name = rows[-1][0]  # 最後の行の名前を取得
            else:
                self.name = ""
        except psycopg2.Error as e:
            print("Error loading data from the database:", e)

    def save_data_to_db(self):
        try:
            self.cursor.execute("INSERT INTO your_table (name) VALUES (%s);", (self.name,))
            self.connection.commit()
            print("Data saved to the database.")
        except psycopg2.Error as e:
            self.connection.rollback()
            print("Error saving data to the database:", e)

    def update_data(self, table_name, data_list):
        try:
            for data in data_list:
                columns = ', '.join(data.keys())
                placeholders = ', '.join(['%s'] * len(data))
                update_values = ', '.join([f"{key} = %s" for key in data.keys()])

                query = f"UPDATE {table_name} SET {update_values} WHERE id = %s;"
                values = list(data.values()) + [data['id']]

                self.cursor.execute(query, values)
            self.connection.commit()
            print("Data updated successfully.")
        except psycopg2.Error as e:
            self.connection.rollback()
            print("Error updating data:", e)
