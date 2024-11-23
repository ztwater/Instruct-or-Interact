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
        for dish_in_menu in self.menu:
            if dish_in_menu["dish"] == dish["dish"]:
                if dish_in_menu["count"] >= dish["count"]:
                    self.selected_dishes.append(dish)
                    dish_in_menu["count"] -= dish["count"]
                    return True
        return False