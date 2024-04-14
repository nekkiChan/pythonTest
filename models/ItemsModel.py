import psycopg2

from models.DatabaseConnectorModel import DatabaseConnectorModel

class ItemsModel(DatabaseConnectorModel):
    def create_table(self):
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS items (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(30) NOT NULL,
                    status VARCHAR(10) DEFAULT 'active'
                );
            """)
            self.connection.commit()
            print("Items table created successfully.")
        except psycopg2.Error as e:
            self.connection.rollback()
            print("Error creating items table:", e)

    def select_items(self):
        try:
            self.cursor.execute("SELECT * FROM items;")
            rows = self.cursor.fetchall()
            return rows
        except psycopg2.Error as e:
            print("Error selecting items:", e)

    def update_items(self, data_list):
        self.update_data("items", data_list)
