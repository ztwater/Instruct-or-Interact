class Order:
    def calculate_total(self):
        """
        Calculate the total price of dishes that have been ordered. Multiply the count, price and sales.
        :return total: float, the final total price.
        >>> order = Order()
        >>> order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        >>> order.sales = {"dish1": 0.8}
        >>> order.add_dish({"dish": "dish1", "price": 10, "count": 4})
        True
        >>> order.calculate_total()
        32.0
        """
        total = 0
        for dish in self.selected_dishes:
            count = dish["count"]
            price = dish["price"]
            dish_name = dish["dish"]
            if dish_name in self.sales:
                sales = self.sales[dish_name]
            else:
                sales = 1
            total += count * price * sales
        return total
