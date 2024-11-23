### Method Description:
    def search_books(self):
        """
        Retrieves all books from the database and returns their information.
        :return books: list[tuple], the information of all books in database
        >>> book_db.search_books()
        [(1, 'book1', 'author', 1)]
        """

### Solution Code:
    def search_books(self):
        self.cursor.execute('''
            SELECT * FROM books
        ''')
        books = self.cursor.fetchall()
        return books

### Source Code:
    def search_books():
        # Code to retrieve books from the database
        # ...
        
        # Code to format and return book information
        # ...
        
        return book_information

### Predicted Code:
    def search_books(self):
        """
        Retrieves all books from the database and returns their information.
        :return books: list[tuple], the information of all books in database
        """
        self.cursor.execute("SELECT * FROM book")
        books = self.cursor.fetchall()
        return books

### Adaptation:
Total number: 5
### Raw Output:
```
def search_books(self):
    """
    Retrieves all books from the database and returns their information.
    :return books: list[tuple], the information of all books in database
    """
    self.cursor.execute("SELECT * FROM book")
    books = self.cursor.fetchall()
    return books
```

### Test Code:
class BookManagementDBTestSearchBooks(unittest.TestCase):
    def setUp(self):
        self.db_name = "test.db"
        self.db = BookManagementDB(self.db_name)
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        # Add some books for testing search
        self.db.add_book("Book 1", "Author 1")
        self.db.add_book("Book 2", "Author 2")
        self.db.add_book("Book 3", "Author 3")

    def test_search_books(self):
        books = self.db.search_books()

        # Ensure that all books were retrieved
        self.assertEqual(len(books), 3)

        # Ensure that the correct book information is retrieved
        self.assertEqual(books[0][1], "Book 1")
        self.assertEqual(books[1][2], "Author 2")
        self.assertEqual(books[2][3], 1)

    def tearDown(self):
        self.db.connection.close()
        self.connection.close()
        # remove the test database file
        os.remove(self.db_name)

### Test Output:
# 1 errors, 1 failures in 1 runs.
# errors:
#     NameError:
#         test_search_books: name 'os' is not defined
# failures:
#     AssertionError:
#         test_search_books: 0 != 3


### Dependencies:
# lib_dependencies: 
# field_dependencies: self.cursor
# method_dependencies: 


