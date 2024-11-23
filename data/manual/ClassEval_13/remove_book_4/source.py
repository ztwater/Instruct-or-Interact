class BookManagement:
    def remove_book(inventory, books):
        for book in books:
            inventory.remove(book)
        return inventory