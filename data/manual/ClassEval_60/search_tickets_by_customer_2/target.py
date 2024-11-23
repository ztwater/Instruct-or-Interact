class MovieTicketDB:
    def search_tickets_by_customer(self, customer_name):
        """
        Searches for tickets in the "tickets" table by customer name.
        :param customer_name: str, the name of the customer to search for.
        :return: list of tuples, the rows from the "tickets" table that match the search criteria.
        >>> ticket_db = MovieTicketDB("ticket_database.db")
        >>> ticket_db.create_table()
        >>> ticket_db.insert_ticket("Movie A", "Theater 1", "A1", "John Doe")
        >>> result = ticket_db.search_tickets_by_customer("John Doe")
        len(result) = 1
        """
        # SQL query to search for tickets by customer name
        query = "SELECT * FROM tickets WHERE customer_name = ?"
        
        # Execute the query and fetch the results
        self.cursor.execute(query, (customer_name,))
        results = self.cursor.fetchall()
        
        # Return the results
        return results