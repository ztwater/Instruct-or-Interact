class DatabaseProcessor:
    def delete_from_database(self, table_name, name):
        """
        Delete rows from the specified table in the database with a matching name.
        :param table_name: str, the name of the table to delete rows from.
        :param name: str, the name to match for deletion.
        >>> db.delete_from_database('user', 'John')
        """
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        cursor.execute(f"DELETE FROM {table_name} WHERE name = ?", (name,))

        conn.commit()
        conn.close()