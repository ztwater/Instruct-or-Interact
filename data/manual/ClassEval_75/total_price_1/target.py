class ShoppingCart:
    def total_price(self) -> float:
        """
        Calculate the total price of all items in the shopping list, which is the quantity of each item multiplied by the price
        :return:float, the total price of all items in the shopping list
        """
        total = 0
        for item in self.items.values():
            quantity = item['quantity']
            price = item['price']
            total += quantity * price
        return total