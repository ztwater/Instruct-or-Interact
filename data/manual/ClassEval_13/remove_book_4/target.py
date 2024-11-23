class BookManagement:
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