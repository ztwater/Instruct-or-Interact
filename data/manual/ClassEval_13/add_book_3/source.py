class BookManagement:
    def add_book(inventory, *books):
        for book in books:
            inventory.append(book)
        inventory.sort(key=lambda x: x['title'])