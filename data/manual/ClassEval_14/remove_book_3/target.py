class BookManagementDB:
    def remove_book(self, book_id):
        """
        Removes a book from the database based on the given book ID.
        :param book_id: int
        """
        self.cursor.execute("DELETE FROM books WHERE book_id = ?", (book_id,))
        self.connection.commit()