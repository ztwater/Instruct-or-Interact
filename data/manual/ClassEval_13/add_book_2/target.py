class BookManagement:
    def add_book(self, title, quantity=1):
        """
        Add one or several books to inventory which is sorted by book title.
        :param title: str, the book title
        :param quantity: int, default value is 1.
        """
        for _ in range(quantity):
            self.inventory[title] = self.inventory.get(title, 0) + 1
    
        sorted_inventory = sorted(self.inventory.items(), key=lambda x: x[0])
    
        self.inventory = {k: v for k, v in sorted_inventory}