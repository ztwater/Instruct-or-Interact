class BookManagement:
    def add_book(self, title, quantity=1):
        """
        Add one or several books to inventory which is sorted by book title.
        :param title: str, the book title
        :param quantity: int, default value is 1.
        """
        for _ in range(quantity):
            self.inventory.append({'title': title})
        self.inventory.sort(key=lambda x: x['title'])