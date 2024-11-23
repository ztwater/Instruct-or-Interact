class BookManagementDB:
    def borrow_book(self, book_id):
        """
        Marks a book as borrowed in the database based on the given book ID.
        :param book_id: int
        """
        # Update the book status to "borrowed" based on the given book ID
        query = "UPDATE books SET status = 'borrowed' WHERE id = ?"
        self.cursor.execute(query, (book_id,))
        self.connection.commit()
    
        # Optionally, return a success message or any other relevant information