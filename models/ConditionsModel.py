import psycopg2

from models.DatabaseConnectorModel import DatabaseConnectorModel

class ConditionsModel(DatabaseConnectorModel):
    def create_table(self):
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS conditions (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(30) NOT NULL,
                    item_id INTEGER REFERENCES items(id),
                    level INTEGER NOT NULL,
                    color VARCHAR(6) DEFAULT '000000',
                    status VARCHAR(10) DEFAULT 'active'
                );
            """)
            self.connection.commit()
            print("Conditions table created successfully.")
        except psycopg2.Error as e:
            self.connection.rollback()
            print("Error creating conditions table:", e)

    def select_conditions(self):
        try:
            self.cursor.execute("SELECT * FROM conditions;")
            rows = self.cursor.fetchall()
            return rows
        except psycopg2.Error as e:
            print("Error selecting conditions:", e)
            
    def update_conditions(self, data_list):
        self.update_data("conditions", data_list)