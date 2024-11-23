class ShoppingCart:
    def remove_item(self, item, quantity=1):
        if item in self.items:
            current_quantity = self.items[item]["quantity"]
            if current_quantity >= quantity:
                self.items[item]["quantity"] -= quantity
                print(f"Successfully removed {quantity} {item}(s) from the shopping list.")
            else:
                print(f"Error: There are only {current_quantity} {item}(s) in the shopping list.")
        else:
            print(f"Error: {item} is not in the shopping list.")