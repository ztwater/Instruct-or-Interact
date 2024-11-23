class MovieTicketDB:
    def create_table():
        # Connect to the database
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        
        # Create the "tickets" table if it does not exist
        c.execute('''CREATE TABLE IF NOT EXISTS tickets
                     (ID INT, movie_name TEXT, author_name TEXT, seat_number TEXT, customer_name TEXT)''')
        
        # Commit the changes and close the connection
        conn.commit()
        conn.close()