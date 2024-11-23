class MovieTicketDB:
    def delete_ticket(self, ticket_id):
        """
        Deletes a ticket from the "tickets" table by ticket ID.
        :param ticket_id: int, the ID of the ticket to delete.
        :return: None
        """
        # Delete the ticket from the table
        self.cursor.execute("DELETE FROM tickets WHERE ticket_id = ?", (ticket_id,))
    
        # Commit the changes
        self.connection.commit()