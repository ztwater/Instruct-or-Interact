class BookManagementDB:
    def add_book(self, title, author):
        """
        Adds a book to the database with the specified title and author, 
        setting its availability to 1 as free to borrow.
        :param title: str, book title
        :param author: str, author name
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.create_table()
        >>> book_db.add_book('book1', 'author')
        """
        query = "INSERT INTO books (title, author, availability) VALUES (?, ?, 1)"
        self.cursor.execute(query, (title, author))
        self.connection.commit()