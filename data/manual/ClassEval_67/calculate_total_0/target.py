class Order:
    def calculate_total(self):
        """
        Calculate the total price of dishes that have been ordered. Multiply the count, price and sales.
        :return total: float, the final total price.
        """
        total = 0
        for dish in self.selected_dishes:
            count = dish['count']
            price = dish['price']
            sales = self.sales.get(dish['dish'], 1.0)
            total += count * price * sales
        return total