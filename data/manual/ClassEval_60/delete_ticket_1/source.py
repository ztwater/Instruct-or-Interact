class MovieTicketDB:
    def delete_ticket(ticket_id):
        # Connect to the database
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
    
        # Delete the ticket from the table
        c.execute("DELETE FROM tickets WHERE ticket_id = ?", (ticket_id,))
    
        # Commit the changes and close the connection
        conn.commit()
        conn.close()