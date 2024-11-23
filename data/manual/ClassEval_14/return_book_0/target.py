class BookManagementDB:
    def return_book(self, book_id):
        """
        Marks a book as returned in the database based on the given book ID.
        :param book_id: int
        """
        query = "UPDATE books SET borrowed = 0 WHERE id = ?"
        self.cursor.execute(query, (book_id,))
        self.connection.commit()
        return "Book with ID {} has been marked as returned.".format(book_id)