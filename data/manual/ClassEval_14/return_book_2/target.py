class BookManagementDB:
    def return_book(self, book_id):
        """
        Marks a book as returned in the database based on the given book ID.
        :param book_id: int
        """
        sql = "UPDATE books SET is_returned = 1 WHERE book_id = ?"
        self.cursor.execute(sql, (book_id,))
        self.connection.commit()
        return "Book with ID {} has been marked as returned.".format(book_id)