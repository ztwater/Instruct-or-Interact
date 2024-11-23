class ShoppingCart:
    def total_price(self) -> float:
        """
        Calculate the total price of all items in the shopping list, which is the quantity of each item multiplied by the price
        :return:float, the total price of all items in the shopping list
        """
        total = 0
        for item, details in self.items.items():
            quantity = details['quantity']
            price = details['price']
            total += quantity * price
        return total