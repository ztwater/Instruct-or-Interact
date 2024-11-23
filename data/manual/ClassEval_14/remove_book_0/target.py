class BookManagementDB:
    def remove_book(self, book_id):
        """
        Removes a book from the database based on the given book ID.
        :param book_id: int
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.remove_book(1)
        """
        query = "DELETE FROM book WHERE book_id = ?"
        self.cursor.execute(query, (book_id,))
        self.connection.commit()