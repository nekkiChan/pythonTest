import psycopg2

from models.DatabaseConnectorModel import DatabaseConnectorModel

class UsersModel(DatabaseConnectorModel):
    def create_table(self):
        if self.cursor is None:
            # データベースに接続
            self.connect()

        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(30) NOT NULL,
                    status VARCHAR(10) DEFAULT 'active'
                );
            """)
            self.connection.commit()
            print("Users table created successfully.")
        except psycopg2.Error as e:
            self.connection.rollback()
            print("Error creating users table:", e)

    def select_users(self):
        try:
            self.cursor.execute("SELECT * FROM users;")
            rows = self.cursor.fetchall()
            return rows
        except psycopg2.Error as e:
            print("Error selecting users:", e)
            
    def update_users(self, data_list):
        self.update_data("users", data_list)