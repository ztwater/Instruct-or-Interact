class BookManagementDB:
    def search_books(self):
        """
        Retrieves all books from the database and returns their information.
        :return books: list[tuple], the information of all books in database
        """
        self.cursor.execute("SELECT * FROM book")
        books = self.cursor.fetchall()
        return books