class ShoppingCart:
    def remove_item(self, item, quantity=1):
        """
        Subtract the specified quantity of item from the shopping list items
        :param item:string, Item to be subtracted in quantity
        :param quantity:int, Quantity to be subtracted
        :return:None
        >>> shoppingcart.add_item("apple", 1, 5)
        >>> shoppingcart.remove_item("apple", 3)
        self.items = {"apple":{"price":1, "quantity":2}}
        """
        if item in self.items:
            current_quantity = self.items[item]["quantity"]
            if current_quantity >= quantity:
                self.items[item]["quantity"] -= quantity
                print(f"Successfully removed {quantity} {item}(s) from the shopping list.")
            else:
                print(f"Error: There are only {current_quantity} {item}(s) in the shopping list.")
        else:
            print(f"Error: {item} is not in the shopping list.")