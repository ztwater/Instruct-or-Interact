class BookManagement:
    def remove_book(self, title, quantity):
        """
        Remove one or several books from inventory which is sorted by book title.
        Raise false while get invalid input.
        :param title: str, the book title
        :param quantity: int
        """
        books_to_remove = []
        for book in self.inventory:
            if book["title"] == title and book["quantity"] >= quantity:
                books_to_remove.append(book)
                book["quantity"] -= quantity
                if book["quantity"] == 0:
                    self.inventory.remove(book)
                return self.inventory
        return False