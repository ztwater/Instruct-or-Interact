class DatabaseProcessor:
    def delete_from_database(self, table_name, name):
        """
        Delete rows from the specified table in the database with a matching name.
        :param table_name: str, the name of the table to delete rows from.
        :param name: str, the name to match for deletion.
        """
        # Connect to the database
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        # Delete rows with matching name from the specified table
        cursor.execute(f"DELETE FROM {table_name} WHERE name = ?", (name,))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()