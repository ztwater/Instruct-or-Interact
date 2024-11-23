class DatabaseProcessor:
    def search_database(table_name, name):
        # Connect to the database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
    
        # Execute the query to search for rows with a matching name
        query = f"SELECT * FROM {table_name} WHERE name = ?"
        cursor.execute(query, (name,))
    
        # Fetch all the matching rows
        rows = cursor.fetchall()
    
        # Print the results
        for row in rows:
            print(row)
    
        # Close the database connection
        conn.close()