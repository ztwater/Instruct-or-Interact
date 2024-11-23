class BookManagement:
    def remove_book(self, title, quantity):
        """
        Remove one or several books from inventory which is sorted by book title.
        Raise false while get invalid input.
        :param title: str, the book title
        :param quantity: int
        """
        if title in self.inventory and self.inventory[title] >= quantity:
            self.inventory[title] -= quantity
            return True
        else:
            return False    