class BookManagementDB:
    def borrow_book(self, book_id):
        """
        Marks a book as borrowed in the database based on the given book ID.
        :param book_id: int
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.borrow_book(1)
        """
        # Connect to the database
        self.connection = sqlite3.connect("test.db")
        self.cursor = self.connection.cursor()
        
        # Update the book status to "borrowed" based on the given book ID
        self.cursor.execute("UPDATE books SET status = 'borrowed' WHERE book_id=?", (book_id,))
        
        # Commit the changes to the database
        self.connection.commit()
        
        # Close the database connection
        self.connection.close()
        
        # Optionally, return a success message or any other relevant information
        return "The book with ID {} has been borrowed.".format(book_id)