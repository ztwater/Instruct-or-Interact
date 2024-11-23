class DiscountStrategy:
    def total(self):
        """
        Calculate the total cost of items in the cart.
        :return: float, total cost of items
        """
        total_cost = 0
        for item in self.cart:
            total_cost += item['price']
        return total_cost