class DatabaseProcessor:
    def search_database(self, table_name, name):
        # Connect to the database
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
    
        # Execute the query to search for rows with a matching name
        query = f"SELECT * FROM {table_name} WHERE name = ?"
        cursor.execute(query, (name,))
    
        # Fetch all the matching rows
        rows = cursor.fetchall()
    
        # Close the database connection
        conn.close()
        
        # Return the matching rows, if any; otherwise, return None
        if rows:
            return rows
        else:
            return None