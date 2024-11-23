### Method Description:
    def remove_book(self, title, quantity):
        """
        Remove one or several books from inventory which is sorted by book title.
        Raise false while get invalid input.
        :param title: str, the book title
        :param quantity: int
        """

### Solution Code:
    def remove_book(self, title, quantity):
        if title not in self.inventory or self.inventory[title] < quantity:
            raise False
        self.inventory[title] -= quantity
        if self.inventory[title] == 0:
            del (self.inventory[title])

### Source Code:
    def remove_book(inventory, books):
        for book in books:
            inventory.remove(book)
        return inventory

### Predicted Code:
    def remove_book(self, title, quantity):
        """
        Remove one or several books from inventory which is sorted by book title.
        Raise false while get invalid input.
        :param title: str, the book title
        :param quantity: int
        """
        for i in range(quantity):
            if title in self.inventory:
                if self.inventory[title] > 1:
                    self.inventory[title] -= 1
                else:
                    del self.inventory[title]
            else:
                return False
        return self.inventory

### Adaptation:
Total number: 20
### Raw Output:
```
class BookManagement:  
    """
    This is a class as managing books system, which supports to add and remove books from the inventory dict, view the inventory, and check the quantity of a specific book.
    """

    def __init__(self):
        """
        Initialize the inventory of Book Manager.
        """
        self.inventory = {}


    def add_book(self, title, quantity=1):
        pass

    def view_inventory(self):
        pass

    def view_book_quantity(self, title):
        pass

    def remove_book(self, title, quantity):
        """
        Remove one or several books from inventory which is sorted by book title.
        Raise false while get invalid input.
        :param title: str, the book title
        :param quantity: int
        """
        for i in range(quantity):
            if title in self.inventory:
                if self.inventory[title] > 1:
                    self.inventory[title] -= 1
                else:
                    del self.inventory[title]
            else:
                return False
        return self.inventory
```

### Test Code:
class BookManagementTestRemoveBook(unittest.TestCase):
    def setUp(self) -> None:
        self.bookManagement = BookManagement()
        self.bookManagement.add_book("book1", 2)
        self.bookManagement.add_book("book2")

    # remove all this title books
    def test_remove_book_1(self):
        self.bookManagement.remove_book("book1", 2)
        self.assertEqual(self.bookManagement.inventory, {"book2": 1})

    # remove part
    def test_remove_book_2(self):
        self.bookManagement.remove_book("book1", 1)
        self.assertEqual(self.bookManagement.inventory, {"book1": 1, "book2": 1})

    # remove the title that doesn't exist
    def test_remove_book_3(self):
        with self.assertRaises(Exception):
            self.bookManagement.remove_book("book3", 1)

    # invalid quantity
    def test_remove_book_4(self):
        with self.assertRaises(Exception):
            self.bookManagement.remove_book("book2", 2)

    def test_remove_book_5(self):
        with self.assertRaises(Exception):
            self.bookManagement.remove_book("book2", 5)

### Test Output:
# 0 errors, 3 failures in 5 runs.
# errors:
# failures:
#     AssertionError:
#         test_remove_book_3: Exception not raised
#         test_remove_book_4: Exception not raised
#         test_remove_book_5: Exception not raised


### Dependencies:
# lib_dependencies: 
# field_dependencies: self.inventory
# method_dependencies: 


