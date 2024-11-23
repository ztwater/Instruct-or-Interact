class VendingMachine:
    def display_items(self):
        """
        Displays the products in the vending machine.
        :return: If the vending machine is empty, returns False, otherwise, returns a list of the products in the vending machine, list.
        """
        if not self.inventory:
            return False
        else:
            displayed_items = []
            for item, details in self.inventory.items():
                price = details['price']
                quantity = details['quantity']
                item_info = f"{item} - ${price} [{quantity}]"
                displayed_items.append(item_info)
            return displayed_items