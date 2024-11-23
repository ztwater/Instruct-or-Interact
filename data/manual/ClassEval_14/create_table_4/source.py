class BookManagementDB:
    def create_table():
        # Connect to the database
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
    
        # Create the book table if it doesn't exist
        c.execute('''
            CREATE TABLE IF NOT EXISTS book (
                id INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT,
                year INTEGER
            )
        ''')
    
        # Commit the changes and close the connection
        conn.commit()
        conn.close()