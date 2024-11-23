class MovieTicketDB:
    def insert_ticket(ticket_data):
        # Connect to the database
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
    
        # Insert the ticket into the "tickets" table
        c.execute("INSERT INTO tickets (ticket_number, description, status) VALUES (?, ?, ?)", ticket_data)
    
        # Commit the changes and close the connection
        conn.commit()
        conn.close()