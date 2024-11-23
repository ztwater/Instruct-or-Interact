class BookManagement:
    def view_book_quantity(self, title):
        """
        Get the quantity of a book.
        :param title: str, the title of the book.
        :return quantity: the quantity of this book title. return 0 when the title does not exist in self.inventory
        """
        if title in self.inventory:
            return self.inventory[title]
        else:
            return 0