class DatabaseProcessor:
    def insert_into_database(self, table_name, data):
        """
        Insert data into the specified table in the database.
        :param table_name: str, the name of the table to insert data into.
        :param data: list, a list of dictionaries where each dictionary represents a row of data.
        """
        # Connect to the database
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        # Insert data into the specified table
        for row in data:
            values = tuple(row.values())
            placeholders = ', '.join(['?'] * len(row))
            query = f"INSERT INTO {table_name} VALUES ({placeholders})"
            cursor.execute(query, values)

        # Commit the changes and close the connection
        conn.commit()
        conn.close()
