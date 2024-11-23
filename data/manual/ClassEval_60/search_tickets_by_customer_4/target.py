class MovieTicketDB:
    def search_tickets_by_customer(self, customer_name):
        # Code to search for tickets in the "tickets" table by customer name
        self.cursor.execute("SELECT * FROM tickets WHERE customer_name = ?", (customer_name,))
        results = self.cursor.fetchall()
        return results