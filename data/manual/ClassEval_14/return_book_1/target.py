class BookManagementDB:
    def return_book(self, book_id):
        """
        Marks a book as returned in the database based on the given book ID.
        :param book_id: int
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.return_book(1)
        """
        sql = "UPDATE books SET borrowed = 0 WHERE book_id = ?"
        self.cursor.execute(sql, (book_id,))
        self.connection.commit()
        return "Book with ID {} has been marked as returned.".format(book_id)