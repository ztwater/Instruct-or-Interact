class DatabaseProcessor:
    def insert_into_database(table_name, data):
        # Connect to the database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
    
        # Insert data into the specified table
        cursor.execute(f"INSERT INTO {table_name} VALUES (?, ?, ?)", data)
    
        # Commit the changes and close the connection
        conn.commit()
        conn.close()