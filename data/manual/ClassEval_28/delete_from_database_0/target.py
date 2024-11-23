class DatabaseProcessor:
    def delete_from_database(self, table_name, name):
        # Connect to the database
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
    
        # Delete rows with matching name from the specified table
        cursor.execute(f"DELETE FROM {table_name} WHERE name = ?", (name,))
    
        # Commit the changes and close the connection
        conn.commit()
        conn.close()