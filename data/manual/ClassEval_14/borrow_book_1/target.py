class BookManagementDB:
    def borrow_book(self, book_id):
        """
        Marks a book as borrowed in the database based on the given book ID.
        :param book_id: int
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.borrow_book(1)
        """
        # Update the book status to "borrowed" based on the given book ID
        self.cursor.execute("UPDATE books SET status = 'borrowed' WHERE id = ?", (book_id,))
    
        # Commit the changes to the database
        self.connection.commit()
    
        # Close the database connection
        self.connection.close()
    
        # Optionally, return a success message or any other relevant information
        return "Book with ID {} has been marked as borrowed.".format(book_id)