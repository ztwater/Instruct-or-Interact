class ShoppingCart:
    def add_item(self, item, price, quantity=1):
        self.items[item] = {'price': price, 'quantity': quantity}