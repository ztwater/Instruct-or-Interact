class ShoppingCart:
    def total_price(self) -> float:
        total = 0
        for item in self.items.values():
            quantity = item['quantity']
            price = item['price']
            total += quantity * price
        return total