class BookManagementDB:
    def add_book(self, title, author):
        """
        Adds a book to the database with the specified title and author, 
        setting its availability to 1 as free to borrow.
        :param title: str, book title
        :param author: str, author name
        """
        # Code to add the book to the database goes here
        query = "INSERT INTO books (title, author, availability) VALUES (?, ?, ?)"
        values = (title, author, 1)
        self.cursor.execute(query, values)
        self.connection.commit()