class MovieTicketDB:
    def insert_ticket(self, movie_name, theater_name, seat_number, customer_name):
        """
        Inserts a new ticket into the "tickets" table.
        :param movie_name: str, the name of the movie.
        :param theater_name: str, the name of the theater.
        :param seat_number: str, the seat number.
        :param customer_name: str, the name of the customer.
        :return: None
        """
        # Insert the ticket into the "tickets" table
        self.cursor.execute("INSERT INTO tickets (movie_name, theater_name, seat_number, customer_name) VALUES (?, ?, ?, ?)",
                            (movie_name, theater_name, seat_number, customer_name))
    
        # Commit the changes and close the connection
        self.connection.commit()