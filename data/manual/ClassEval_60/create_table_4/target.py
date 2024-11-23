class MovieTicketDB:
    def create_table(self):
        """
        Creates a "tickets" table in the database if it does not exist already.
        Fields include ID of type int, movie name of type str, author name of type str, seat number of type str, and customer name of type str.
        :return: None
        """
        # Create the "tickets" table if it does not exist
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tickets
                             (ID INT, movie_name TEXT, author_name TEXT, seat_number TEXT, customer_name TEXT)''')
    
        # Commit the changes
        self.connection.commit()