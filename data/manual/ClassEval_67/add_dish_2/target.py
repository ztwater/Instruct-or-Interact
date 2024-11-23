class Order:
    def add_dish(self, dish):
        """
        Check the self.menu and add into self.selected_dishes if the dish count is valid.
        And if the dish has successfully been added, change the count in self.menu.
        :param dish: dict, the information of dish. dish = {"dish": dish name, "count": count, price: price}
        :return: True if successfully added, or False otherwise.
        >>> order = Order()
        >>> order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        >>> order.add_dish({"dish": "dish1", "price": 10, "count": 3})
        True
        """
        for item in self.menu:
            if item["dish"] == dish["dish"]:
                count = item["count"]
                if count >= dish["count"]:
                    self.selected_dishes.append(dish)
                    self.menu.remove(item)
                    item["count"] -= dish["count"]
                    self.menu.append(item)
                    return True
        return False