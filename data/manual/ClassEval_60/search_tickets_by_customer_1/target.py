class MovieTicketDB:
    def search_tickets_by_customer(self, customer_name):
        """
        Searches for tickets in the "tickets" table by customer name.
        :param customer_name: str, the name of the customer to search for.
        :return: list of tuples, the rows from the "tickets" table that match the search criteria.
        """
        query = '''
        SELECT *
        FROM tickets
        WHERE customer_name = ?
        '''
        self.cursor.execute(query, (customer_name,))
        result = self.cursor.fetchall()
        return result